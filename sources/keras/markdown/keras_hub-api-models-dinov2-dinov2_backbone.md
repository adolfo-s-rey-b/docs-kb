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
 / [DINOV2](https://keras.io/keras_hub/api/models/dinov2/)
 / DINOV2Backbone model

DINOV2Backbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/dinov2/dinov2_backbone.py#L10)

### `DINOV2Backbone` class

Copied!

`keras_hub.models.DINOV2Backbone(     patch_size,     num_layers,     hidden_dim,     num_heads,     intermediate_dim,     layer_scale_init_value=1.0,     num_register_tokens=0,     use_mask_token=True,     use_swiglu_ffn=False,     dropout_rate=0.0,     drop_path_rate=0.0,     image_shape=(224, 224, 3),     position_embedding_shape=(518, 518, 3),     antialias_in_interpolation=False,     apply_layernorm=False,     data_format=None,     dtype=None,     name=None,     **kwargs )`

DINOV2 core network with hyperparameters.

DINOV2 offers a powerful, generalist visual backbone learned entirely from unlabeled images as described in [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193)

The default constructor gives a fully customizable, randomly initialized DINOV2 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Note that this backbone is a Feature Pyramid Backbone that can output intermediate feature maps from different stages of the model. See the example below for how to access these feature pyramid outputs.

Note that this backbone supports interpolation of the position embeddings to the input image shape. This is useful when the input image shape is different from the shape used to train the position embeddings. The `position_embedding_shape` argument is used to specify the original shape used to train the position embeddings.

**Arguments**

*   **patch\_size**: int. The size of each square patch in the input image.
*   **num\_layers**: int. The number of transformer layers.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **num\_heads**: int. The number of attention heads for each transformer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **layer\_scale\_init\_value**: float. The initial value for the layer scale in the transformer layers. Defaults to `1.0`.
*   **num\_register\_tokens**: int. The number of register tokens to use in the embedding layer. Defaults to `0`.
*   **use\_mask\_token**: bool. Whether to use a mask token in the embedding layer. Defaults to `True`.
*   **use\_swiglu\_ffn**: bool. Whether to use SwigLU activation in the MLP layers. Defaults to `False`.
*   **dropout\_rate**: float. The dropout rate to use. Defaults to `0.0`.
*   **drop\_path\_rate**: float. The drop path rate to use. Defaults to `0.0`.
*   **image\_shape**: tuple. The input shape without the batch size. Defaults to `(224, 224, 3)`.
*   **position\_embedding\_shape**: tuple. The original shape used to train the position embeddings. This is used to interpolate the position embeddings to the actual input shape. Defaults to `(518, 518)`.
*   **antialias\_in\_interpolation**: bool. Whether to use antialiasing in the interpolation of the position embeddings. Defaults to `False`.
*   **apply\_layernorm**: bool. Whether to apply layer normalization to the outputs of each stage in the feature pyramid. Defaults to `False`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`# Pretrained DINOV2 model. input_data = {     "images": np.ones(shape=(1, 518, 518, 3), dtype="float32"), } model = keras_hub.models.DINOV2Backbone.from_preset(     "dinov2_base" ) model(input_data)  # Pretrained DINOV2 model with custom image shape. input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"), } model = keras_hub.models.DINOV2Backbone.from_preset(     "dinov2_base", image_shape=(224, 224, 3) ) model(input_data)  # Randomly initialized DINOV2 model with custom config. model = keras_hub.models.DINOV2Backbone(     patch_size=14,     num_layers=2,     hidden_dim=32,     num_heads=2,     intermediate_dim=128,     image_shape=(224, 224, 3),     position_embedding_shape=(518, 518), ) model(input_data)  # Accessing feature pyramid outputs. backbone = keras_hub.models.DINOV2Backbone.from_preset(     "dinov2_base", image_shape=(224, 224, 3) ) model = keras.Model(     inputs=backbone.inputs,     outputs=backbone.pyramid_outputs, ) features = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DINOV2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [dinov2\_small](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_small/1) | 22.58M | Vision Transformer (small-sized model) trained using DINOv2. |
| [dinov2\_with\_registers\_small](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_with_registers_small/1) | 22.58M | Vision Transformer (small-sized model) trained using DINOv2, with registers. |
| [dinov2\_base](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_base/1) | 87.63M | Vision Transformer (base-sized model) trained using DINOv2. |
| [dinov2\_with\_registers\_base](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_with_registers_base/1) | 87.64M | Vision Transformer (base-sized model) trained using DINOv2, with registers. |
| [dinov2\_large](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_large/1) | 305.77M | Vision Transformer (large-sized model) trained using DINOv2. |
| [dinov2\_with\_registers\_large](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_with_registers_large/1) | 305.78M | Vision Transformer (large-sized model) trained using DINOv2, with registers. |
| [dinov2\_giant](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_giant/1) | 1.14B | Vision Transformer (giant-sized model) trained using DINOv2. |
| [dinov2\_with\_registers\_giant](https://www.kaggle.com/models/keras/dinov2/keras/dinov2_with_registers_giant/1) | 1.14B | Vision Transformer (giant-sized model) trained using DINOv2, with registers. |

* * *

[DINOV2Backbone model](https://keras.io/keras_hub/api/models/dinov2/dinov2_backbone/#dinov2backbone-model)

[`DINOV2Backbone` class](https://keras.io/keras_hub/api/models/dinov2/dinov2_backbone/#dinov2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/dinov2/dinov2_backbone/#frompreset-method)