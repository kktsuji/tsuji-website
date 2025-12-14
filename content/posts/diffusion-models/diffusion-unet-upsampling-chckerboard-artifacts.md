---
title: "Checkerboard Artifacts Caused by UNet Upsampling in Diffusion Models"
description: ""
date: 2025-11-28T08:00:00+09:00
lastmod:
math: true
draft: false
---

When working with diffusion models, you might encounter checkerboard artifacts in the generated images. These artifacts can often be traced back to the upsampling methods used in the UNet architecture of the diffusion model.

A common cause of checkerboard artifacts is the use of transposed convolutions (also known as deconvolutions) for upsampling within the UNet. Transposed convolutions can introduce uneven overlap in the output pixels, leading to visible patterns that resemble a checkerboard.

To mitigate these artifacts, consider the following approaches:

1. **Use Alternative Upsampling Methods**: Replace transposed convolutions with other upsampling techniques such as nearest-neighbor upsampling followed by a standard convolution, or bilinear upsampling followed by a convolution. These methods tend to produce smoother results without introducing checkerboard patterns.
2. **Adjust Kernel Sizes and Strides**: If transposed convolutions must be used, carefully choose kernel sizes and strides to ensure even coverage of the output space. Avoid configurations that lead to uneven overlaps.
3. **Post-Processing Techniques**: Apply post-processing filters to smooth out any residual artifacts. Techniques such as Gaussian blurring or median filtering can help reduce the visibility of checkerboard patterns.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class UpsampleBlock(nn.Module):
    def __init__(self, in_channels, out_channels, method='nearest',
                 scale_factor=2, kernel_size=3, stride=2, padding=1):
        super(UpsampleBlock, self).__init__()
        self.method = method
        self.scale_factor = scale_factor

        if method in ['nearest', 'bilinear']:
            # Alternative upsampling: interpolation + convolution
            self.conv = nn.Conv2d(in_channels, out_channels,
                                 kernel_size=kernel_size,
                                 padding=kernel_size//2)
        elif method == 'transpose':
            # Transposed convolution with carefully chosen parameters to avoid artifacts
            # Default: kernel_size=4, stride=2, padding=1 ensures even coverage
            # This satisfies: output_size = (input_size - 1) * stride - 2 * padding + kernel_size
            # For 2x upsampling: output = 2 * input
            self.conv_transpose = nn.ConvTranspose2d(
                in_channels, out_channels,
                kernel_size=kernel_size if method == 'transpose' else 4,
                stride=stride,
                padding=padding
            )
        else:
            raise ValueError(f"Unsupported upsampling method: {method}")

    def forward(self, x):
        if self.method == 'nearest':
            x = F.interpolate(x, scale_factor=self.scale_factor, mode='nearest')
            x = self.conv(x)
        elif self.method == 'bilinear':
            x = F.interpolate(x, scale_factor=self.scale_factor, mode='bilinear', align_corners=False)
            x = self.conv(x)
        elif self.method == 'transpose':
            x = self.conv_transpose(x)
        return x
```
