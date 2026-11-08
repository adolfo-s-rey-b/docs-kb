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
 / [VideoPrism](https://keras.io/keras_hub/api/models/video_prism/)
 / VideoPrismBackbone model

VideoPrismBackbone model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/video_prism/video_prism_backbone.py#L30)

### `VideoPrismBackbone` class

Copied!

`keras_hub.models.VideoPrismBackbone(     num_frames,     patch_size,     hidden_dim,     intermediate_dim,     num_heads,     num_spatial_layers,     num_temporal_layers,     num_auxiliary_layers,     vocabulary_size=0,     num_text_layers=0,     dropout_rate=0.0,     attention_dropout_rate=0.0,     attention_logit_soft_cap=None,     layer_norm_epsilon=1e-06,     image_shape=(288, 288, 3),     data_format=None,     dtype=None,     **kwargs )`

VideoPrism backbone for video and multimodal understanding.

This backbone implements the VideoPrism architecture, a powerful video understanding model that uses a factorized encoder design. The model can operate in two modes:

1.  **Video-only mode** (`num_text_layers=0`): Contains only a video encoder that processes videos through spatial and temporal factorized encoding, outputting frame-level video features.
2.  **Multimodal mode** (`num_text_layers>0`): Includes both a video encoder and a CoCa-style text encoder, producing aligned video and text embeddings suitable for contrastive learning and vision-language tasks.

The video encoder uses a factorized design that separately processes spatial and temporal information for efficiency and scalability.

**Arguments**

*   **num\_frames**: int. The number of frames in the input video sequence.
*   **patch\_size**: int. The size of each square patch in the input image.
*   **hidden\_dim**: int. The dimensionality of the hidden representations throughout the model.
*   **intermediate\_dim**: int. The dimensionality of the intermediate layer in the feedforward MLP blocks.
*   **num\_heads**: int. The number of attention heads for each transformer.
*   **num\_spatial\_layers**: int. Number of transformer layers in the spatial encoder that processes within-frame information.
*   **num\_temporal\_layers**: int. Number of transformer layers in the temporal encoder that processes across-frame information.
*   **num\_auxiliary\_layers**: int. Number of additional transformer layers applied after the factorized video encoder. Only used when `num_text_layers > 0`.
*   **vocabulary\_size**: int. The size of the token vocabulary. Only required when `num_text_layers > 0`. Defaults to `0`.
*   **num\_text\_layers**: int. The number of transformer encoder layers for the text encoder. Set to `0` for video-only mode, or a positive value for multimodal mode with both video and text encoders. Defaults to `0`.
*   **dropout\_rate**: float. Dropout probability for the Transformer encoder. Defaults to `0.0`.
*   **attention\_dropout**: float. Dropout probability applied to the attention weights. Defaults to `0.0`.
*   **attention\_logit\_soft\_cap**: None or float. Soft cap for the attention logits. Defaults to `None`.
*   **image\_shape**: tuple of ints. The shape of each input frame as `(height, width, channels)`. For example, `(288, 288, 3)`.
*   **layer\_norm\_epsilon**: float. The epsilon for the layer normalization. Defaults to `1e-6`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Note that some operations, such as softmax and layer normalization, will always be performed in float32 precision regardless of dtype.

**Returns**

*   **When `num_text_layers=0` (video-only mode)**: A tensor of shape `(batch_size, num_frames, num_patches, hidden_dim)` containing the video features for each patch in each frame.
*   \_\_ When `num_text_layers>0` (multimodal mode)\_\_: A dictionary with two keys:
    *   `"vision_embeddings"`: A tensor of shape `(batch_size, hidden_dim)` containing the pooled and normalized video embeddings.
    *   `"text_embeddings"`: A tensor of shape `(batch_size, hidden_dim)` containing the normalized text embeddings from the final token.

**Example**

Copied!

`# Video-only mode backbone = keras_hub.models.VideoPrismBackbone.from_preset(     "videoprism_public_v1_base" ) # (batch_size, frames, H, W, C) pixel_values = np.random.rand(2, 16, 288, 288, 3) # (batch_size, num_frames, num_patches, hidden_dim) features = backbone.predict(pixel_values)  # Multimodal mode with text encoder token_ids = np.ones((2, 64), dtype="int32")  # (batch_size, seq_len) padding_mask = np.ones((2, 64), dtype="int32")  # (batch_size, seq_len) backbone = keras_hub.models.VideoPrismBackbone.from_preset(     "videoprism_lvt_public_v1_base" ) inputs = {     "pixel_values": pixel_values,     "token_ids": token_ids,     "padding_mask": padding_mask, } outputs = backbone.predict(inputs) outputs["vision_embeddings"]  # (batch_size, hidden_dim) outputs["text_embeddings"]  # (batch_size, hidden_dim)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`VideoPrismBackbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [videoprism\_public\_v1\_base](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_public_v1_base/1) | 114.00M | 114 million parameter, 12-layer ViT-B, 16-frame, 288x288 resolution, video-only encoder for spatiotemporal representation. |
| [videoprism\_lvt\_public\_v1\_base](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_lvt_public_v1_base/1) | 248.00M | 248 million parameter, 12-layer ViT-B video encoder + text encoder, 16-frame, 288x288 resolution, for multimodal video-language tasks. |
| [videoprism\_public\_v1\_large](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_public_v1_large/1) | 354.00M | 354 million parameter, 24-layer ViT-L, 16-frame, 288x288 resolution, video-only encoder for spatiotemporal representation. |
| [videoprism\_lvt\_public\_v1\_large](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_lvt_public_v1_large/1) | 580.00M | 580 million parameter, 24-layer ViT-L video encoder + text encoder, 16-frame, 288x288 resolution, for multimodal video-language tasks. |

* * *

[VideoPrismBackbone model](https://keras.io/keras_hub/api/models/video_prism/video_prism_backbone/#videoprismbackbone-model)

[`VideoPrismBackbone` class](https://keras.io/keras_hub/api/models/video_prism/video_prism_backbone/#videoprismbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/video_prism/video_prism_backbone/#frompreset-method)