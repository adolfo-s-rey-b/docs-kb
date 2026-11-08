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
 / [VGG](https://keras.io/keras_hub/api/models/vgg/)
 / VGGBackbone model

VGGBackbone model
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/vgg/vgg_backbone.py#L8)

### `VGGBackbone` class

Copied!

`keras_hub.models.VGGBackbone(     stackwise_num_repeats, stackwise_num_filters, image_shape=(None, None, 3), **kwargs )`

This class represents Keras Backbone of VGG model.

This class implements a VGG backbone as described in [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)
(ICLR 2015).

**Arguments**

*   **stackwise\_num\_repeats**: list of ints, number of repeated convolutional blocks per VGG block. For VGG16 this is \[2, 2, 3, 3, 3\] and for VGG19 this is \[2, 2, 4, 4, 4\].
*   **stackwise\_num\_filters**: list of ints, filter size for convolutional blocks per VGG block. For both VGG16 and VGG19 this is \[ 64, 128, 256, 512, 512\].
*   **image\_shape**: tuple, optional shape tuple, defaults to (None, None, 3).

**Examples**

Copied!

`input_data = np.ones((2, 224, 224, 3), dtype="float32")  # Pretrained VGG backbone. model = keras_hub.models.VGGBackbone.from_preset("vgg_16_imagenet") model(input_data)  # Randomly initialized VGG backbone with a custom config. model = keras_hub.models.VGGBackbone(     stackwise_num_repeats = [2, 2, 3, 3, 3],     stackwise_num_filters = [64, 128, 256, 512, 512],     image_shape = (224, 224, 3), ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`VGGBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [vgg\_11\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_11_imagenet/3) | 9.22M | 11-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |
| [vgg\_13\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_13_imagenet/3) | 9.40M | 13-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |
| [vgg\_16\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_16_imagenet/3) | 14.71M | 16-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |
| [vgg\_19\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_19_imagenet/3) | 20.02M | 19-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |

* * *

[VGGBackbone model](https://keras.io/keras_hub/api/models/vgg/vgg_backbone/#vggbackbone-model)

[`VGGBackbone` class](https://keras.io/keras_hub/api/models/vgg/vgg_backbone/#vggbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/vgg/vgg_backbone/#frompreset-method)