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
 / [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
 / Mistral3VisionEncoder model

Mistral3VisionEncoder model
===========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral3/mistral3_vision_encoder.py#L761)

### `Mistral3VisionEncoder` class

Copied!

`keras_hub.models.Mistral3VisionEncoder(     image_size=1540,     patch_size=14,     num_channels=3,     hidden_dim=1024,     num_layers=24,     num_heads=16,     head_dim=64,     intermediate_dim=4096,     rope_theta=10000.0,     layer_norm_epsilon=1e-05,     activation="silu",     attention_dropout=0.0,     **kwargs )`

Vision encoder used by Mistral3.

This is not exposed as a standalone model. It is the vision tower consumed by the Mistral3 multimodal architecture.

`pixel_values` follows the Hugging Face Pixtral layout: `(num_images, num_channels, height, width)`.

When `image_sizes` is provided, each image is cropped to its effective image size after patchification, the resulting patch sequences are concatenated into a single sequence, and attention is restricted to patches belonging to the same image.

* * *

[Mistral3VisionEncoder model](https://keras.io/keras_hub/api/models/mistral3/mistral3_vision_encoder/#mistral3visionencoder-model)

[`Mistral3VisionEncoder` class](https://keras.io/keras_hub/api/models/mistral3/mistral3_vision_encoder/#mistral3visionencoder-class)