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
 / [Xception](https://keras.io/keras_hub/api/models/xception/)
 / XceptionBackbone model

XceptionBackbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/xception/xception_backbone.py#L10)

### `XceptionBackbone` class

Copied!

`keras_hub.models.XceptionBackbone(     stackwise_conv_filters,     stackwise_pooling,     image_shape=(None, None, 3),     data_format=None,     dtype=None,     **kwargs )`

Xception core network with hyperparameters.

This class implements a Xception backbone as described in [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)
.

Most users will want the pretrained presets available with this model. If you are creating a custom backbone, this model provides customizability through the `stackwise_conv_filters` and `stackwise_pooling` arguments. This backbone assumes the same basic structure as the original Xception mode: \* Residuals and pre-activation everywhere but the first and last block. \* Conv layers for the first block only, separable conv layers elsewhere.

**Arguments**

*   **stackwise\_conv\_filters**: list of list of ints. Each outermost list entry represents a block, and each innermost list entry a conv layer. The integer value specifies the number of filters for the conv layer.
*   **stackwise\_pooling**: list of bools. A list of booleans per block, where each entry is true if the block should includes a max pooling layer and false if it should not.
*   **image\_shape**: tuple. The input shape without the batch size. Defaults to `(None, None, 3)`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. If unspecified, the Keras default will be used.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights.

**Examples**

Copied!

`input_data = np.random.uniform(0, 1, size=(2, 224, 224, 3))  # Pretrained Xception backbone. model = keras_hub.models.Backbone.from_preset("xception_41_imagenet") model(input_data)  # Randomly initialized Xception backbone with a custom config. model = keras_hub.models.XceptionBackbone(     stackwise_conv_filters=[[32, 64], [64, 128], [256, 256]],     stackwise_pooling=[True, True, False], ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`XceptionBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [xception\_41\_imagenet](https://www.kaggle.com/models/keras/xception/keras/xception_41_imagenet/2) | 20.86M | 41-layer Xception model pre-trained on ImageNet 1k. |

* * *

[XceptionBackbone model](https://keras.io/keras_hub/api/models/xception/xception_backbone/#xceptionbackbone-model)

[`XceptionBackbone` class](https://keras.io/keras_hub/api/models/xception/xception_backbone/#xceptionbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/xception/xception_backbone/#frompreset-method)