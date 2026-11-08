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
 / [SegFormer](https://keras.io/keras_hub/api/models/segformer/)
 / SegFormerBackbone model

SegFormerBackbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/segformer/segformer_backbone.py#L7)

### `SegFormerBackbone` class

Copied!

`keras_hub.models.SegFormerBackbone(image_encoder, projection_filters, **kwargs)`

A Keras model implementing SegFormer for semantic segmentation.

This class implements the majority of the SegFormer architecture described in [SegFormer: Simple and Efficient Design for Semantic Segmentation](https://arxiv.org/abs/2105.15203)
 and based on the TensorFlow implementation [from DeepVision](https://github.com/DavidLandup0/deepvision/tree/main/deepvision/models/segmentation/segformer)
.

SegFormers are meant to be used with the MixTransformer (MiT) encoder family, and use a very lightweight all-MLP decoder head.

The MiT encoder uses a hierarchical transformer which outputs features at multiple scales, similar to that of the hierarchical outputs typically associated with CNNs.

**Arguments**

*   **image\_encoder**: [`keras.Model`](https://keras.io/api/models/model#model-class)
    . The backbone network for the model that is used as a feature extractor for the SegFormer encoder. Should be used with the MiT backbone model ([`keras_hub.models.MiTBackbone`](https://keras.io/keras_hub/api/models/mit/mit_backbone#mitbackbone-class)
    ) which was created specifically for SegFormers.
*   **num\_classes**: int, the number of classes for the detection model, including the background class.
*   **projection\_filters**: int, number of filters in the convolution layer projecting the concatenated features into a segmentation map. Defaults to 256\`.

**Example**

Using the class with a custom `backbone`:

Copied!

`import keras_hub  backbone = keras_hub.models.MiTBackbone(     image_shape=(224, 224, 3),     num_layers=4,     hidden_dims=[32, 64, 160, 256],     layerwise_depths=[2, 2, 2, 2],     layerwise_num_heads=[1, 2, 5, 8],     layerwise_sr_ratios=[8, 4, 2, 1],     layerwise_patch_sizes=[7, 3, 3, 3],     layerwise_strides=[4, 2, 2, 2],     max_drop_path_rate=0.1, )  segformer_backbone = keras_hub.models.SegFormerBackbone(     image_encoder=backbone, projection_filters=256)`

Using the class with a preset `backbone`:

Copied!

`import keras_hub  backbone = keras_hub.models.MiTBackbone.from_preset("mit_b0_ade20k_512") segformer_backbone = keras_hub.models.SegFormerBackbone(     image_encoder=backbone, projection_filters=256)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SegFormerBackbone.from_preset(preset, load_weights=True, **kwargs)`

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

[SegFormerBackbone model](https://keras.io/keras_hub/api/models/segformer/segformer_backbone/#segformerbackbone-model)

[`SegFormerBackbone` class](https://keras.io/keras_hub/api/models/segformer/segformer_backbone/#segformerbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/segformer/segformer_backbone/#frompreset-method)