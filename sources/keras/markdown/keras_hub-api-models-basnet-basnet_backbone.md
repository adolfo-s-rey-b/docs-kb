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
 / [BASNet](https://keras.io/keras_hub/api/models/basnet/)
 / BASNetBackbone model

BASNetBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/basnet/basnet_backbone.py#L10)

### `BASNetBackbone` class

Copied!

`keras_hub.models.BASNetBackbone(     image_encoder,     num_classes,     image_shape=(None, None, 3),     projection_filters=64,     prediction_heads=None,     refinement_head=None,     dtype=None,     **kwargs )`

BASNet architecture for semantic segmentation.

A Keras model implementing the BASNet architecture described in [BASNet: Boundary-Aware Segmentation Network for Mobile and Web Applications](https://arxiv.org/abs/2101.04704)
. BASNet uses a predict-refine architecture for highly accurate image segmentation.

**Arguments**

*   **image\_encoder**: A [`keras_hub.models.ResNetBackbone`](https://keras.io/keras_hub/api/models/resnet/resnet_backbone#resnetbackbone-class)
     instance. The backbone network for the model that is used as a feature extractor for BASNet prediction encoder. Currently supported backbones are ResNet18 and ResNet34. (Note: Do not specify `image_shape` within the backbone. Please provide these while initializing the 'BASNetBackbone' model)
*   **num\_classes**: int, the number of classes for the segmentation model.
*   **image\_shape**: optional shape tuple, defaults to (None, None, 3).
*   **projection\_filters**: int, number of filters in the convolution layer projecting low-level features from the `backbone`.
*   **prediction\_heads**: (Optional) List of `keras.layers.Layer` defining the prediction module head for the model. If not provided, a default head is created with a Conv2D layer followed by resizing.
*   **refinement\_head**: (Optional) a `keras.layers.Layer` defining the refinement module head for the model. If not provided, a default head is created with a Conv2D layer.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`BASNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [basnet\_duts](https://www.kaggle.com/models/keras/basnet/keras/basnet_duts) | 108.89M | BASNet model with a 34-layer ResNet backbone, pre-trained on the DUTS image dataset at a 288x288 resolution. Model training was performed by Hamid Ali (https://github.com/hamidriasat/BASNet). |

* * *

[BASNetBackbone model](https://keras.io/keras_hub/api/models/basnet/basnet_backbone/#basnetbackbone-model)

[`BASNetBackbone` class](https://keras.io/keras_hub/api/models/basnet/basnet_backbone/#basnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/basnet/basnet_backbone/#frompreset-method)