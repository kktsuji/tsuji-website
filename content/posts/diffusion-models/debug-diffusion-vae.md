---
title: "Debugging Latent Diffusion VAE Issues"
description: ""
date: 2025-10-29T07:00:00+09:00
lastmod:
math: true
draft: false
---

When working with latent diffusion models like Stable Diffusion, issues in the generated images can often be traced back to problems in the VAE (Variational Autoencoder) component. This script allows you to isolate and debug the VAE by encoding an input image to latent space and then decoding it back to pixel space. You can confirm whether the VAE is functioning correctly if the input and output images closely match.

`git clone https://gist.github.com/7fe430bc5640a2dafa9f9814f9c9b8d9.git`

or see below:

```python
import argparse
import os
from typing import Tuple, Optional

import numpy as np
import torch
from PIL import Image
from diffusers import AutoencoderKL


def pick_device_and_dtype() -> Tuple[torch.device, torch.dtype]:
    if torch.cuda.is_available():
        return torch.device("cuda"), torch.float16
    # If you're on Apple Silicon and want to use MPS, uncomment below:
    # if torch.backends.mps.is_available():
    #     return torch.device("mps"), torch.float16
    return torch.device("cpu"), torch.float32


def load_vae(repo_id: str, device: torch.device, dtype: torch.dtype, hf_token: Optional[str] = None) -> AutoencoderKL:
    vae = AutoencoderKL.from_pretrained(
        repo_id,
        subfolder="vae",
        torch_dtype=dtype,
        token=hf_token,  # If None, it will use cached creds or anonymous (will fail if auth is required)
    )
    vae.to(device)
    vae.eval()
    return vae


def ensure_multiple_of_8(size: Tuple[int, int]) -> Tuple[int, int]:
    w, h = size
    w8 = (w // 8) * 8
    h8 = (h // 8) * 8
    # Avoid zero
    w8 = max(8, w8)
    h8 = max(8, h8)
    return w8, h8


def image_to_tensor(
    img: Image.Image,
    target_size: Optional[Tuple[int, int]],
    device: torch.device,
    dtype: torch.dtype,
) -> torch.Tensor:
    """
    Convert PIL Image -> normalized tensor in [-1, 1], shape (1, 3, H, W).
    Resizes to target_size (W, H) if provided; otherwise, rounds down to multiples of 8.
    """
    img = img.convert("RGB")
    if target_size is None:
        # Make dimensions multiples of 8 (required for SD VAE)
        target_size = ensure_multiple_of_8(img.size)
    img = img.resize(target_size, Image.BICUBIC)

    np_img = np.array(img).astype(np.float32) / 255.0  # (H, W, 3) in [0, 1]
    torch_img = torch.from_numpy(np_img).permute(2, 0, 1).unsqueeze(0)  # (1, 3, H, W)
    torch_img = torch_img.to(device=device, dtype=dtype)
    torch_img = (torch_img * 2.0) - 1.0  # Normalize to [-1, 1]
    return torch_img


def encode_to_latents(vae: AutoencoderKL, tensor_img: torch.Tensor, sample: bool, seed: Optional[int] = None) -> torch.Tensor:
    """
    Encode image tensor in [-1, 1] to latent space.
    Returns latents scaled by vae.config.scaling_factor, shape (B, 4, H/8, W/8).
    """
    if seed is not None:
        g = torch.Generator(device=tensor_img.device).manual_seed(seed)
    else:
        g = None

    with torch.no_grad():
        posterior = vae.encode(tensor_img).latent_dist
        latents = posterior.sample(generator=g) if sample else posterior.mean
        latents = latents * vae.config.scaling_factor
    return latents


def decode_from_latents(vae: AutoencoderKL, latents: torch.Tensor) -> torch.Tensor:
    """
    Decode scaled latents back to image tensor in [-1, 1], shape (B, 3, H, W).
    """
    with torch.no_grad():
        scaled = latents / vae.config.scaling_factor
        decoded = vae.decode(scaled).sample
    return decoded


def tensor_to_image(tensor_img: torch.Tensor) -> Image.Image:
    """
    Convert tensor in [-1, 1] to PIL Image (uint8).
    Expects shape (1, 3, H, W) or (3, H, W).
    """
    if tensor_img.dim() == 4:
        tensor_img = tensor_img[0]
    tensor_img = (tensor_img / 2 + 0.5).clamp(0, 1)  # to [0, 1]
    np_img = (tensor_img.detach().cpu().permute(1, 2, 0).numpy() * 255).round().astype(np.uint8)
    return Image.fromarray(np_img)


def main():
    parser = argparse.ArgumentParser(description="VAE encode/decode with stable diffusion using diffusers.")
    parser.add_argument("--image", type=str, required=True, help="Path to input image.")
    parser.add_argument("--out", type=str, default="decoded.png", help="Path to save the decoded image.")
    parser.add_argument("--width", type=int, default=None, help="Target width (must be multiple of 8). If omitted, rounded down.")
    parser.add_argument("--height", type=int, default=None, help="Target height (must be multiple of 8). If omitted, rounded down.")
    parser.add_argument("--sample", action="store_true", help="Sample from posterior instead of using mean (stochastic).")
    parser.add_argument("--seed", type=int, default=None, help="Random seed used when --sample is set.")
    parser.add_argument("--repo", type=str, default="CompVis/stable-diffusion-v1-4", help="HF repo id for the model.")
    parser.add_argument("--hf_token_env", type=str, default="HF_TOKEN", help="Env var name for HF token if required.")
    args = parser.parse_args()

    device, dtype = pick_device_and_dtype()
    hf_token = os.environ.get(args.hf_token_env, None)

    # Load only the VAE from the SD v1-4 checkpoint
    vae = load_vae(args.repo, device=device, dtype=dtype, hf_token=hf_token)

    # Load and prepare image tensor
    pil_img = Image.open(args.image)
    target_size = None
    if args.width is not None and args.height is not None:
        if args.width % 8 != 0 or args.height % 8 != 0:
            raise ValueError("width and height must be multiples of 8.")
        target_size = (args.width, args.height)  # (W, H)
    tensor_img = image_to_tensor(pil_img, target_size, device=device, dtype=dtype)

    # Encode to latents
    latents = encode_to_latents(vae, tensor_img, sample=args.sample, seed=args.seed)
    print(f"Encoded latents shape: {tuple(latents.shape)} (scaled by {vae.config.scaling_factor})")

    # Decode back to image tensor
    decoded_tensor = decode_from_latents(vae, latents)
    print(f"Decoded tensor shape: {tuple(decoded_tensor.shape)} (value range ~[-1, 1])")

    # Convert to PIL and save
    decoded_img = tensor_to_image(decoded_tensor)
    decoded_img.save(args.out)
    print(f"Saved decoded image to: {args.out}")


if __name__ == "__main__":
    main()
```

Usage example:

```bash
python debug_diffusion_vae.py --image input.png --out out.png --width 512 --height 512 --sample --seed 42 --repo CompVis/stable-diffusion-v1-4
```
