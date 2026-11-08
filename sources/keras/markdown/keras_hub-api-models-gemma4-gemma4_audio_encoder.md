None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [Gemma4](https://keras.io/keras_hub/api/models/gemma4/)
 / Gemma4AudioEncoder model

Gemma4AudioEncoder model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_audio_encoder.py#L1334)

### `Gemma4AudioEncoder` class

Copied!

`keras_hub.models.Gemma4AudioEncoder(     input_feat_size=128,     hidden_size=1024,     num_heads=8,     num_layers=12,     chunk_size=12,     context_left=13,     context_right=0,     logit_cap=50.0,     invalid_logit_value=-1000000000.0,     conv_kernel_size=5,     reduction_factor=1,     residual_weight=0.5,     gradient_clipping=10000000000.0,     sscp_conv_channels=(128, 32),     sscp_kernel_sizes=((3, 3), (3, 3)),     sscp_stride_sizes=((2, 2), (2, 2)),     output_proj_dims=1536,     output_dim=2048,     norm_eps=1e-06,     sscp_norm_eps=1e-06,     dtype=None,     **kwargs )`

Audio encoder for Gemma4 based on the Universal Speech Model (USM).

Encodes mel spectrograms into audio token embeddings projected into the language model's hidden space. The pipeline is:

1.  **SubSampleConvProjection**: two stacked Conv2D blocks that downsample time by 4× at 16ms hop rate, then a linear projection to `hidden_size`.
2.  **Conformer blocks** (`num_layers` of them): macaron-FFW → chunk attention with relative position bias → causal depthwise Conv1D → macaron-FFW → RMS norm.
3.  **Temporal striding** (if `reduction_factor > 1`): reduce sequence by taking every `reduction_factor`\-th token.
4.  **Output projection**: linear `hidden_size → output_proj_dims` followed by another linear `output_proj_dims → output_dim` (= text hidden size) and a parameter-free RMS norm.

Padded positions (indicated by `audio_mel_mask`) are zeroed out in the final output.

**Arguments**

*   **input\_feat\_size**: int. Number of mel filterbank channels. Defaults to `128`.
*   **hidden\_size**: int. Conformer hidden dimension. Defaults to `1024`.
*   **num\_heads**: int. Number of conformer attention heads. Defaults to `8`.
*   **num\_layers**: int. Number of Conformer blocks. Defaults to `12`.
*   **chunk\_size**: int. Block size for chunk-based attention. Defaults to `12`.
*   **context\_left**: int. Left attention context (inclusive). Defaults to `13`.
*   **context\_right**: int. Right attention context. Defaults to `0`.
*   **logit\_cap**: float. Soft-cap on attention logits. Defaults to `50.0`.
*   **invalid\_logit\_value**: float. Fill for masked logits. Defaults to `-1e9`.
*   **conv\_kernel\_size**: int. Depthwise conv kernel size. Defaults to `5`.
*   **reduction\_factor**: int. Temporal stride after the conformer stack. Defaults to `1`.
*   **residual\_weight**: float. Macaron FFW residual weight. Defaults to `0.5`.
*   **gradient\_clipping**: float. Clip value. Defaults to `1e10`.
*   **sscp\_conv\_channels**: tuple of two ints. Output channels per SSCP conv. Defaults to `(128, 32)`.
*   **sscp\_kernel\_sizes**: tuple of two `(kT, kF)` pairs. Defaults to `((3, 3), (3, 3))`.
*   **sscp\_stride\_sizes**: tuple of two `(sT, sF)` pairs. Defaults to `((2, 2), (2, 2))`.
*   **output\_proj\_dims**: int or `None`. Intermediate audio projection dimension (e.g. 1536). `None` skips this projection.
*   **output\_dim**: int. Final output dimension = text backbone hidden size.
*   **norm\_eps**: float. Epsilon for conformer RMS norms. Defaults to `1e-6`.
*   **sscp\_norm\_eps**: float. Epsilon for SSCP LayerNorm. Defaults to `1e-6`.
*   **dtype**: Compute dtype. Defaults to `None`.

* * *

[Gemma4AudioEncoder model](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_encoder/#gemma4audioencoder-model)

[`Gemma4AudioEncoder` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_encoder/#gemma4audioencoder-class)