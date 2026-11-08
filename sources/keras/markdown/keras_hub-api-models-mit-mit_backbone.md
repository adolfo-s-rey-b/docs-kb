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
 / [MiT](https://keras.io/keras_hub/api/models/mit/)
 / MiTBackbone model

MiTBackbone model
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mit/mit_backbone.py#L22)

### `MiTBackbone` class

Copied!

`keras_hub.models.MiTBackbone(     layerwise_depths,     num_layers,     layerwise_num_heads,     layerwise_sr_ratios,     max_drop_path_rate,     layerwise_patch_sizes,     layerwise_strides,     image_shape=(None, None, 3),     hidden_dims=None,     **kwargs )`

A backbone with feature pyramid outputs.

`FeaturePyramidBackbone` extends `Backbone` with a single `pyramid_outputs` property for accessing the feature pyramid outputs of the model. Subclassers should set the `pyramid_outputs` property during the model constructor.

**Example**

Copied!

`input_data = np.random.uniform(0, 256, size=(2, 224, 224, 3))  # Convert to feature pyramid output format using ResNet. backbone = ResNetBackbone.from_preset("resnet50") model = keras.Model(     inputs=backbone.inputs, outputs=backbone.pyramid_outputs ) model(input_data)  # A dict containing the keys ["P2", "P3", "P4", "P5"]`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MiTBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [mit\_b0\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b0_ade20k_512/4) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |
| [mit\_b0\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b0_cityscapes_1024/3) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |
| [mit\_b1\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b1_ade20k_512/4) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |
| [mit\_b1\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b1_cityscapes_1024/3) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |
| [mit\_b2\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b2_ade20k_512/4) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |
| [mit\_b2\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b2_cityscapes_1024/3) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |
| [mit\_b3\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b3_ade20k_512/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |
| [mit\_b3\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b3_cityscapes_1024/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |
| [mit\_b4\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b4_ade20k_512/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |
| [mit\_b4\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b4_cityscapes_1024/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |
| [mit\_b5\_ade20k\_640](https://www.kaggle.com/models/keras/mit/keras/mit_b5_ade20k_640/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |
| [mit\_b5\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b5_cityscapes_1024/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |

* * *

[MiTBackbone model](https://keras.io/keras_hub/api/models/mit/mit_backbone/#mitbackbone-model)

[`MiTBackbone` class](https://keras.io/keras_hub/api/models/mit/mit_backbone/#mitbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mit/mit_backbone/#frompreset-method)