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
 / Gemma4VisionEncoder model

Gemma4VisionEncoder model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_vision_encoder.py#L12)

### `Gemma4VisionEncoder` class

Copied!

`keras_hub.models.Gemma4VisionEncoder(     image_size,     patch_size,     num_heads,     hidden_dim,     num_layers,     intermediate_dim,     head_dim,     output_dim,     num_key_value_heads=None,     pool_size=3,     position_embedding_size=1024,     rope_max_wavelength=100.0,     layer_norm_epsilon=1e-06,     dropout=0,     use_clipped_linears=True,     standardize=False,     dtype=None,     **kwargs )`

Vision Transformer (ViT) encoder for Gemma4.

This encoder is architecturally different from the Gemma3 vision encoder. Rather than using a separate CLIP-style ViT, Gemma4 uses the same transformer block style as the text decoder (with 4 norms per block, Q/K/V normalization) with bidirectional (non-causal) attention.

Position information is encoded via two separate learnable position- embedding tables — one for the x-axis and one for the y-axis — whose outputs are added to the patch features. This 2D decomposed embedding can represent any image height and width independently.

After encoding, the patch sequence is spatially pooled down to a fixed `output_dim`\-wide representation and then projected into the text hidden dimension.

**Arguments**

*   **image\_size**: int. The height/width of the (square) image. Must be divisible by `patch_size * pool_size`.
*   **patch\_size**: int. Size of each square patch in pixels.
*   **num\_heads**: int. Number of attention heads in each vision transformer layer.
*   **hidden\_dim**: int. Hidden dimension of the vision transformer blocks.
*   **num\_layers**: int. Number of transformer layers in the vision encoder.
*   **intermediate\_dim**: int. Intermediate FFW dimension in each block.
*   **head\_dim**: int. Dimension of each attention head.
*   **output\_dim**: int. Dimension to project encoded patches to (should equal the text backbone's `hidden_dim`).
*   **num\_key\_value\_heads**: int. For grouped-query attention. Defaults to `num_heads` (MHA).
*   **pool\_size**: int. Spatial pooling factor applied after the transformer. The output sequence length equals `(image_size // patch_size // pool_size) ** 2`. Must evenly divide `image_size // patch_size`. Defaults to `3`.
*   **position\_embedding\_size**: int. Number of learnable entries in each (x or y) position embedding table. Should be at least `image_size // patch_size`. Defaults to `1024`.
*   **rope\_max\_wavelength**: float. Maximum wavelength used for rotary position embeddings inside vision transformer blocks. Defaults to `100.0`.
*   **layer\_norm\_epsilon**: float. Epsilon for layer normalisations. Defaults to `1e-6`.
*   **dropout**: float. Dropout probability. Defaults to `0`.
*   **use\_clipped\_linears**: bool. If `True`, use clipped linear activations in the vision feed-forward layers to match the reference implementation. Defaults to `True`.
*   **standardize**: bool. If `True`, standardize patch features before encoding. Defaults to `False`.
*   **dtype**: Compute dtype. Defaults to `None` (uses Keras global policy).

**Example**

Copied!

`import numpy as np  vision_encoder = keras_hub.models.Gemma4VisionEncoder(     image_size=768,     patch_size=16,     num_heads=12,     hidden_dim=768,     num_layers=12,     intermediate_dim=3072,     head_dim=64,     output_dim=2304,     pool_size=3, ) # pixel_values: (batch, num_images, num_patches, patch_dim) # For a 768x768 image with patch_size=16: num_patches=48*48=2304, # patch_dim=16*16*3=768. pixel_values = np.ones((1, 1, 2304, 768), dtype="float32") # pixel_position_ids: (batch, num_images, num_patches, 2) pixel_position_ids = np.zeros((1, 1, 2304, 2), dtype="int32") output = vision_encoder(     {"pixel_values": pixel_values, "pixel_position_ids": pixel_position_ids} ) # output.shape == (1, 1, 256, 2304) # (batch, num_images, pooled_patches, output_dim)`

* * *

[Gemma4VisionEncoder model](https://keras.io/keras_hub/api/models/gemma4/gemma4_vision_encoder/#gemma4visionencoder-model)

[`Gemma4VisionEncoder` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_vision_encoder/#gemma4visionencoder-class)