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
 / [DepthAnything](https://keras.io/keras_hub/api/models/depth_anything/)
 / DepthAnythingBackbone model

DepthAnythingBackbone model
===========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/depth_anything/depth_anything_backbone.py#L16)

### `DepthAnythingBackbone` class

Copied!

`keras_hub.models.DepthAnythingBackbone(     image_encoder,     reassemble_factors,     neck_hidden_dims,     fusion_hidden_dim,     head_hidden_dim,     head_in_index,     feature_keys=None,     data_format=None,     dtype=None,     **kwargs )`

DepthAnything core network with hyperparameters.

DepthAnything offers a powerful monocular depth estimation as described in [Depth Anything V2](https://arxiv.org/abs/2406.09414)
.

The default constructor gives a fully customizable, randomly initialized DepthAnything model with any number of layers, heads, and embedding dimensions by providing the DINOV2 as the `image_encoder`. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **image\_encoder**: The DINOV2 image encoder for encoding the input images.
*   **reassemble\_factors**: List of float. The reassemble factor for each feature map from the image encoder. The length of the list must be equal to the number of feature maps from the image encoder.
*   **neck\_hidden\_dims**: int. The size of the neck hidden state.
*   **fusion\_hidden\_dim**: int. The size of the fusion hidden state.
*   **head\_hidden\_dim**: int. The size of the neck hidden state.
*   **head\_in\_index**: int. The index to select the feature from the neck features as the input to the head.
*   **feature\_keys**: List of string. The keys to select the feature maps from the image encoder. If `None`, all feature maps from the image encoder will be used. Defaults to `None`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`# Pretrained DepthAnything model. input_data = {     "images": np.ones(shape=(1, 518, 518, 3), dtype="float32"), } model = keras_hub.models.DepthAnythingBackbone.from_preset(     "depth_anything_v2_small" ) model(input_data)  # Pretrained DepthAnything model with custom image shape. input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"), } model = keras_hub.models.DepthAnythingBackbone.from_preset(     "depth_anything_v2_small", image_shape=(224, 224, 3) ) model(input_data)  # Randomly initialized DepthAnything model with custom config. image_encoder = keras_hub.models.DINOV2Backbone(     patch_size=14,     num_layers=4,     hidden_dim=32,     num_heads=2,     intermediate_dim=128,     image_shape=(224, 224, 3),     position_embedding_shape=(518, 518), ) model = keras_hub.models.DepthAnythingBackbone(     image_encoder=image_encoder,     reassemble_factors=[4, 2, 1, 0.5],     neck_hidden_dims=[16, 32, 64, 128],     fusion_hidden_dim=128,     head_hidden_dim=16,     head_in_index=-1,     feature_keys=["Stage1", "Stage2", "Stage3", "Stage4"], ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DepthAnythingBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [depth\_anything\_v2\_small](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_small/1) | 25.31M | Small variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |
| [depth\_anything\_v2\_base](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_base/1) | 98.52M | Base variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |
| [depth\_anything\_v2\_large](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_large/1) | 336.72M | Large variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |

* * *

[DepthAnythingBackbone model](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_backbone/#depthanythingbackbone-model)

[`DepthAnythingBackbone` class](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_backbone/#depthanythingbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_backbone/#frompreset-method)