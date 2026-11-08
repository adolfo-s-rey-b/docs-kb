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
 / [DenseNet](https://keras.io/keras_hub/api/models/densenet/)
 / DensNetBackbone model

DensNetBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/densenet/densenet_backbone.py#L9)

### `DenseNetBackbone` class

Copied!

`keras_hub.models.DenseNetBackbone(     stackwise_num_repeats,     image_shape=(None, None, 3),     compression_ratio=0.5,     growth_rate=32,     **kwargs )`

Instantiates the DenseNet architecture.

This class implements a DenseNet backbone as described in [Densely Connected Convolutional Networks (CVPR 2017)](https://arxiv.org/abs/1608.06993)
.

**Arguments**

*   **stackwise\_num\_repeats**: list of ints, number of repeated convolutional blocks per dense block.
*   **image\_shape**: optional shape tuple, defaults to (None, None, 3).
*   **compression\_ratio**: float, compression rate at transition layers, defaults to 0.5.
*   **growth\_rate**: int, number of filters added by each dense block, defaults to 32

**Examples**

Copied!

`input_data = np.ones(shape=(8, 224, 224, 3))  # Pretrained backbone model = keras_hub.models.DenseNetBackbone.from_preset(     "densenet_121_imagenet" ) model(input_data)  # Randomly initialized backbone with a custom config model = keras_hub.models.DenseNetBackbone(     stackwise_num_repeats=[6, 12, 24, 16], ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DenseNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [densenet\_121\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_121_imagenet/3) | 7.04M | 121-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |
| [densenet\_169\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_169_imagenet/3) | 12.64M | 169-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |
| [densenet\_201\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_201_imagenet/3) | 18.32M | 201-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |

* * *

[DensNetBackbone model](https://keras.io/keras_hub/api/models/densenet/densenet_backbone/#densnetbackbone-model)

[`DenseNetBackbone` class](https://keras.io/keras_hub/api/models/densenet/densenet_backbone/#densenetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/densenet/densenet_backbone/#frompreset-method)