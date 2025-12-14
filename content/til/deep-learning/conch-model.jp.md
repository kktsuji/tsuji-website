---
title: "CONCHモデルの詳細"
description: ""
date: 2025-05-20T09:00:00+09:00
lastmod:
draft: false
---

## 概要

- [CONtrastive learning from Captions for Histopathology (CONCH) model](https://arxiv.org/abs/2307.12914)の事前学習済みweightsは[こちら (Hugging Face)](https://huggingface.co/MahmoodLab/CONCH)で入手可能
- CONCHモデルのアーキテクチャは[Cntrastive Captioners (CoCa)](https://arxiv.org/abs/2205.01917)に基づいている
- CONCHモデルはimage-to-textおよびimage-text-alignmentタスクの機能を持つ（text-to-imageは不可）

## CONCHモデルの詳細を取得する方法

Google Colabで：

```python
!pip install git+https://github.com/Mahmoodlab/CONCH.git

from conch.open_clip_custom import create_model_from_pretrained

path_to_model = "checkpoints/conch/pytorch_model.bin"
model, preprocess = create_model_from_pretrained('conch_ViT-B-16', path_to_model)

print(model)
# モデルの出力についてはこのページの最後のセクションを参照
```

## CONCHモデルの詳細

このセクションはGitHub Copilotによって生成されました。

### CoCaモデルアーキテクチャの概要

CoCaモデルは、textとvisual（画像）データの両方を処理するように設計された**multimodal transformer**アーキテクチャです。いくつかの主要なコンポーネントで構成されています：

### 1. Text Encoder (`text`)

- **TextTransformer**
  - **token_embedding**: 入力tokenを埋め込む（語彙サイズ: 32,007、埋め込み次元: 768）
  - **transformer**: 12個の`ResidualAttentionBlock`のスタック、それぞれ以下を含む：
    - LayerNormレイヤー
    - MultiheadAttention（self-attention）
    - MLP（GELU activationを持つ2層feedforward）
    - Identityレイヤー（おそらくresidual scalingまたは将来の拡張用）
  - **ln_final**: 最終LayerNorm

### 2. Visual Encoder (`visual`)

- **VisualModel**
  - **trunk**: VisionTransformer
    - **PatchEmbed**: Conv2dレイヤーを使用して画像をパッチに変換（3入力チャネル、768出力、16x16パッチサイズ）
    - **blocks**: 12個のtransformer `Block`、それぞれ以下を含む：
      - LayerNorm
      - Attention（qkv projectionを持つself-attention）
      - MLP（GELUを持つ2層feedforward）
      - IdentityおよびDropoutレイヤー
    - **norm**: 最終LayerNorm
    - **fc_norm, head_drop, head**: 追加の正規化および出力レイヤー
  - **attn_pool_contrast**: contrastiveタスク用のattentional pooling（MultiheadAttentionとLayerNormを使用）
  - **ln_contrast**: contrastive出力用のLayerNorm
  - **head**: 出力head（空のSequential、おそらく拡張用）
  - **attn_pool_caption**: captioning用のattentional pooling（MultiheadAttentionとLayerNormを使用）
  - **ln_caption**: caption出力用のLayerNorm

### 3. Text Decoder (`text_decoder`)

- **MultimodalTransformer**
  - **resblocks**: 12個の`ResidualAttentionBlock`（encoderと同様、自己回帰decodingのため）
  - **cross_attn**: cross-attentionを持つ12個の`ResidualAttentionBlock`：
    - key/value入力用のLayerNormを含む（`ln_1_kv`）
    - decoderがvisual featuresにattendできるようにする
  - **ln_final**: 最終LayerNorm

### 主要なアーキテクチャ機能

- **ResidualAttentionBlock**: LayerNorm、MultiheadAttention、MLP、residual connectionsを持つコアtransformer block
- **MultiheadAttention**: self-attentionとcross-attentionの両方で全体的に使用
- **GELU Activation**: 非線形性のためすべてのMLPで使用
- **LayerNorm**: 安定性のためattentionとMLPの前後に適用
- **Attentional Poolers**: contrastiveおよびcaptioningタスクのfeature集約に使用

### 要約表

| コンポーネント    | レイヤー/ブロック  | 主な操作                  | 目的                             |
| ----------------- | ------------------ | ------------------------- | -------------------------------- |
| TextTransformer   | 12 Residual Blocks | Self-attention, MLP       | textのエンコード                 |
| VisionTransformer | 12 Blocks          | Self-attention, MLP       | 画像のエンコード                 |
| TextDecoder       | 12 Residual Blocks | Self/cross-attention, MLP | textのデコード、visionへのattend |
| Attn Poolers      | MultiheadAttention | Pooling, LayerNorm        | featureの集約                    |

### 使用法

- **Contrastive Learning**: textと画像の表現を整列（Clipのように）
- **Captioning**: decoder内のcross-attentionを介して画像を条件としたtextを生成
- Multimodal理解タスク

**要約すると：**
CoCaはmultimodal decoderを持つdual-encoder（text/image）transformerで、標準的なtransformerコンポーネントを全体的に使用して、contrastiveとgenerative（captioning）の両方のタスクをサポートします。

## モデルの出力

```python
CoCa(
  (text): TextTransformer(
    (token_embedding): Embedding(32007, 768)
    (transformer): Transformer(
      (resblocks): ModuleList(
        (0-11): 12 x ResidualAttentionBlock(
          (ln_1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
          (attn): MultiheadAttention(
            (out_proj): NonDynamicallyQuantizableLinear(in_features=768, out_features=768, bias=True)
          )
          (ls_1): Identity()
          (ln_2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
          (mlp): Sequential(
            (c_fc): Linear(in_features=768, out_features=3072, bias=True)
            (gelu): GELU(approximate='none')
            (c_proj): Linear(in_features=3072, out_features=768, bias=True)
          )
          (ls_2): Identity()
        )
      )
    )
    (ln_final): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
  )
  (visual): VisualModel(
    (trunk): VisionTransformer(
      (patch_embed): PatchEmbed(
        (proj): Conv2d(3, 768, kernel_size=(16, 16), stride=(16, 16))
        (norm): Identity()
      )
      (pos_drop): Dropout(p=0.0, inplace=False)
      (patch_drop): Identity()
      (norm_pre): Identity()
      (blocks): Sequential(
        (0): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (1): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (2): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (3): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (4): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (5): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (6): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (7): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (8): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (9): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (10): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
        (11): Block(
          (norm1): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (attn): Attention(
            (qkv): Linear(in_features=768, out_features=2304, bias=True)
            (q_norm): Identity()
            (k_norm): Identity()
            (attn_drop): Dropout(p=0.0, inplace=False)
            (proj): Linear(in_features=768, out_features=768, bias=True)
            (proj_drop): Dropout(p=0.0, inplace=False)
          )
          (ls1): Identity()
          (drop_path1): Identity()
          (norm2): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
          (mlp): Mlp(
            (fc1): Linear(in_features=768, out_features=3072, bias=True)
            (act): GELU(approximate='none')
            (drop1): Dropout(p=0.0, inplace=False)
            (norm): Identity()
            (fc2): Linear(in_features=3072, out_features=768, bias=True)
            (drop2): Dropout(p=0.0, inplace=False)
          )
          (ls2): Identity()
          (drop_path2): Identity()
        )
      )
      (norm): LayerNorm((768,), eps=1e-06, elementwise_affine=True)
      (fc_norm): Identity()
      (head_drop): Dropout(p=0.0, inplace=False)
      (head): Identity()
    )
    (attn_pool_contrast): AttentionalPooler(
      (attn): MultiheadAttention(
        (out_proj): NonDynamicallyQuantizableLinear(in_features=512, out_features=512, bias=True)
      )
      (ln_q): LayerNorm((512,), eps=1e-05, elementwise_affine=True)
      (ln_k): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
    )
    (ln_contrast): LayerNorm((512,), eps=1e-05, elementwise_affine=True)
    (head): Sequential()
    (attn_pool_caption): AttentionalPooler(
      (attn): MultiheadAttention(
        (out_proj): NonDynamicallyQuantizableLinear(in_features=768, out_features=768, bias=True)
      )
      (ln_q): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
      (ln_k): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
    )
    (ln_caption): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
  )
  (text_decoder): MultimodalTransformer(
    (resblocks): ModuleList(
      (0-11): 12 x ResidualAttentionBlock(
        (ln_1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        (attn): MultiheadAttention(
          (out_proj): NonDynamicallyQuantizableLinear(in_features=768, out_features=768, bias=True)
        )
        (ls_1): Identity()
        (ln_2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        (mlp): Sequential(
          (c_fc): Linear(in_features=768, out_features=3072, bias=True)
          (gelu): GELU(approximate='none')
          (c_proj): Linear(in_features=3072, out_features=768, bias=True)
        )
        (ls_2): Identity()
      )
    )
    (cross_attn): ModuleList(
      (0-11): 12 x ResidualAttentionBlock(
        (ln_1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        (attn): MultiheadAttention(
          (out_proj): NonDynamicallyQuantizableLinear(in_features=768, out_features=768, bias=True)
        )
        (ls_1): Identity()
        (ln_1_kv): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        (ln_2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        (mlp): Sequential(
          (c_fc): Linear(in_features=768, out_features=3072, bias=True)
          (gelu): GELU(approximate='none')
          (c_proj): Linear(in_features=3072, out_features=768, bias=True)
        )
        (ls_2): Identity()
      )
    )
    (ln_final): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
  )
)
```
