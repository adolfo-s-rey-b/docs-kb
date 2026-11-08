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
 / [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
 / SmolVLM2VisionEncoder model

SmolVLM2VisionEncoder model
===========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_vision_encoder.py#L405)

### `SmolVLM2VisionEncoder` class

Copied!

`keras_hub.models.SmolVLM2VisionEncoder(     image_size,     patch_size,     hidden_dim,     intermediate_dim,     num_layers,     num_heads,     num_channels=3,     layer_norm_epsilon=1e-06,     attention_dropout=0.0,     dtype=None,     **kwargs )`

SmolVLM2 vision encoder (Idefics3-style SigLIP ViT).

A vision transformer that embeds images into patch features with a `Conv2D` patch embedding plus a learned, raster-order position embedding, followed by a stack of encoder blocks and a final LayerNorm. Inputs must already be square and match `image_size`; `SmolVLM2ImageConverter` is responsible for resizing and splitting images to that size.

**Arguments**

*   **image\_size**: int. Expected input image size (square).
*   **patch\_size**: int. Size of each image patch.
*   **hidden\_dim**: int. Dimensionality of the encoder.
*   **intermediate\_dim**: int. Inner dimensionality of the MLP.
*   **num\_layers**: int. Number of encoder blocks.
*   **num\_heads**: int. Number of attention heads.
*   **num\_channels**: int. Number of input channels. Defaults to `3`.
*   **layer\_norm\_epsilon**: float. Epsilon for LayerNorm. Defaults to `1e-6`.
*   **attention\_dropout**: float. Attention dropout rate. Defaults to `0.0`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`.

**Examples**

Copied!

`# Randomly initialized vision encoder. encoder = keras_hub.models.SmolVLM2VisionEncoder(     image_size=384,     patch_size=14,     hidden_dim=1152,     intermediate_dim=4304,     num_layers=27,     num_heads=16, ) images = np.random.rand(1, 384, 384, 3).astype("float32") output = encoder({"pixel_values": images}) # output.shape == (1, 729, 1152)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SmolVLM2VisionEncoder.from_preset(preset, load_weights=True, **kwargs)`

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

* * *

[SmolVLM2VisionEncoder model](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_vision_encoder/#smolvlm2visionencoder-model)

[`SmolVLM2VisionEncoder` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_vision_encoder/#smolvlm2visionencoder-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_vision_encoder/#frompreset-method)