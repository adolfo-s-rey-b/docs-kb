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
 / [CSPNet](https://keras.io/keras_hub/api/models/cspnet/)
 / CSPNetBackbone model

CSPNetBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/cspnet/cspnet_backbone.py#L10)

### `CSPNetBackbone` class

Copied!

`keras_hub.models.CSPNetBackbone(     stem_filters,     stem_kernel_size,     stem_strides,     stackwise_depth,     stackwise_strides,     stackwise_num_filters,     block_type,     groups=1,     stage_type=None,     activation="leaky_relu",     output_strides=32,     bottle_ratio=[1.0],     block_ratio=[1.0],     expand_ratio=[1.0],     stem_padding="valid",     stem_pooling=None,     avg_down=False,     down_growth=False,     cross_linear=False,     image_shape=(None, None, 3),     data_format=None,     dtype=None,     **kwargs )`

This class represents Keras Backbone of CSPNet model.

This class implements a CSPNet backbone as described in [CSPNet: A New Backbone that can Enhance Learning Capability of CNN](https://arxiv.org/abs/1911.11929)
.

**Arguments**

*   **stem\_filters**: int or list of ints, filter size for the stem.
*   **stem\_kernel\_size**: int or tuple/list of 2 integers, kernel size for the stem.
*   **stem\_strides**: int or tuple/list of 2 integers, stride length of the convolution for the stem.
*   **stackwise\_num\_filters**: A list of ints, filter size for each block level in the model.
*   **stackwise\_strides**: int or tuple/list of ints, strides for each block level in the model.
*   **stackwise\_depth**: A list of ints, representing the depth (number of blocks) for each block level in the model.
*   **block\_type**: str. One of `"bottleneck_block"`, `"dark_block"`, or `"edge_block"`. Use `"dark_block"` for DarkNet blocks, `"edge_block"` for EdgeResidual / Fused-MBConv blocks.
*   **groups**: int, specifying the number of groups into which the input is split along the channel axis. Defaults to `1`.
*   **stage\_type**: str. One of `"csp"`, `"dark"`, or `"cs3"`. Use `"dark"` for DarkNet stages, `"csp"` for Cross Stage, and `"cs3"` for Cross Stage with only one transition conv. Defaults to `None`, which defaults to `"cs3"`.
*   **activation**: str. Activation function for the model.
*   **output\_strides**: int, output stride length of the backbone model. Must be one of `(8, 16, 32)`. Defaults to `32`.
*   **bottle\_ratio**: float or tuple/list of floats. The dimensionality of the intermediate bottleneck space (i.e., the number of output filters in the bottleneck convolution), calculated as `(filters * bottle_ratio)` and applied to:
    *   the first convolution of `"dark_block"` and `"edge_block"`
    *   the first two convolutions of `"bottleneck_block"` of each stage. Defaults to `1.0`.
*   **block\_ratio**: float or tuple/list of floats. Filter size for each block, calculated as `(stackwise_num_filters * block_ratio)` for each stage. Defaults to `1.0`.
*   **expand\_ratio**: float or tuple/list of floats. Filters ratio for `"csp"` and `"cs3"` stages at different levels. Defaults to `1.0`.
*   **stem\_padding**: str, padding value for the stem, either `"valid"` or `"same"`. Defaults to `"valid"`.
*   **stem\_pooling**: str, pooling value for the stem. Defaults to `None`.
*   **avg\_down**: bool, if `True`, `AveragePooling2D` is applied at the beginning of each stage when `strides == 2`. Defaults to `False`.
*   **down\_growth**: bool, grow downsample channels to output channels. Applies to Cross Stage only. Defaults to `False`.
*   **cross\_linear**: bool, if `True`, activation will not be applied after the expansion convolution. Applies to Cross Stage only. Defaults to `False`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **image\_shape**: tuple. The input shape without the batch size. Defaults to `(None, None, 3)`.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights.

**Examples**

Copied!

`input_data = np.ones(shape=(8, 224, 224, 3))  # Pretrained backbone model = keras_hub.models.CSPNetBackbone.from_preset(     "csp_darknet_53_ra_imagenet" ) model(input_data)  # Randomly initialized backbone with a custom config model = keras_hub.models.CSPNetBackbone(     stem_filters=32,     stem_kernel_size=3,     stem_strides=1,     stackwise_depth=[1, 2, 4],     stackwise_strides=[1, 2, 2],     stackwise_num_filters=[32, 64, 128],     block_type="dark, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`CSPNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [csp\_resnext\_50\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_resnext_50_ra_imagenet/1) | 20.57M | A CSP-ResNeXt (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |
| [csp\_resnet\_50\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_resnet_50_ra_imagenet/1) | 21.62M | A CSP-ResNet (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |
| [csp\_darknet\_53\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_darknet_53_ra_imagenet/2) | 27.64M | A CSP-DarkNet (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |
| [darknet\_53\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/darknet_53_imagenet/1) | 41.61M | A DarkNet image classification model pre-trained on theImageNet 1k dataset at a 256x256 resolution. |

* * *

[CSPNetBackbone model](https://keras.io/keras_hub/api/models/cspnet/cspnet_backbone/#cspnetbackbone-model)

[`CSPNetBackbone` class](https://keras.io/keras_hub/api/models/cspnet/cspnet_backbone/#cspnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/cspnet/cspnet_backbone/#frompreset-method)