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
 / [HGNetV2](https://keras.io/keras_hub/api/models/hgnetv2/)
 / HGNetV2Backbone model

HGNetV2Backbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/hgnetv2/hgnetv2_backbone.py#L10)

### `HGNetV2Backbone` class

Copied!

`keras_hub.models.HGNetV2Backbone(     depths,     embedding_size,     hidden_sizes,     stem_channels,     hidden_act,     use_learnable_affine_block,     stackwise_stage_filters,     apply_downsample,     use_lightweight_conv_block,     image_shape=(None, None, 3),     data_format=None,     out_features=None,     dtype=None,     **kwargs )`

This class represents a Keras Backbone of the HGNetV2 model.

This class implements an HGNetV2 backbone architecture, a convolutional neural network (CNN) optimized for GPU efficiency. HGNetV2 is frequently used as a lightweight CNN backbone in object detection pipelines like RT-DETR and YOLO variants, delivering strong performance on classification and detection tasks, with speed-ups and accuracy gains compared to larger CNN backbones.

**Arguments**

*   **depths**: list of ints, the number of blocks in each stage.
*   **embedding\_size**: int, the size of the embedding layer.
*   **hidden\_sizes**: list of ints, the sizes of the hidden layers.
*   **stem\_channels**: list of ints, the channels for the stem part.
*   **hidden\_act**: str, the activation function for hidden layers.
*   **use\_learnable\_affine\_block**: bool, whether to use learnable affine transformations.
*   **stackwise\_stage\_filters**: list of tuples, where each tuple contains configuration for a stage: (stage\_in\_channels, stage\_mid\_channels, stage\_out\_channels, stage\_num\_blocks, stage\_num\_of\_layers, stage\_kernel\_size).
    *   stage\_in\_channels: int, input channels for the stage
    *   stage\_mid\_channels: int, middle channels for the stage
    *   stage\_out\_channels: int, output channels for the stage
    *   stage\_num\_blocks: int, number of blocks in the stage
    *   stage\_num\_of\_layers: int, number of layers in each block
    *   stage\_kernel\_size: int, kernel size for the stage
*   **apply\_downsample**: list of bools, whether to downsample in each stage.
*   **use\_lightweight\_conv\_block**: list of bools, whether to use HGNetV2 lightweight convolutional blocks in each stage.
*   **image\_shape**: tuple, the shape of the input image without the batch size. Defaults to `(None, None, 3)`.
*   **data\_format**: `None` or str, the data format ('channels\_last' or 'channels\_first'). If not specified, defaults to the `image_data_format` value in your Keras config.
*   **out\_features**: list of str or `None`, the names of the output features to return. If `None`, returns all available features from all stages. Defaults to `None`.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`, the data type for computations and weights.

**Examples**

Copied!

`import numpy as np from keras_hub.src.models.hgnetv2.hgnetv2_backbone import HGNetV2Backbone input_data = np.ones(shape=(8, 224, 224, 3))  # Pretrained backbone. model = keras_hub.models.HGNetV2Backbone.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) model(input_data)  # Randomly initialized backbone with a custom config. model = HGNetV2Backbone(     depths=[1, 2, 4],     embedding_size=32,     hidden_sizes=[64, 128, 256],     stem_channels=[3, 16, 32],     hidden_act="relu",     use_learnable_affine_block=False,     stackwise_stage_filters=[         (32, 16, 64, 1, 1, 3),     # Stage 0         (64, 32, 128, 2, 1, 3),    # Stage 1         (128, 64, 256, 4, 1, 3),   # Stage 2     ],     apply_downsample=[False, True, True],     use_lightweight_conv_block=[False, False, False],     image_shape=(224, 224, 3), ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`HGNetV2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [hgnetv2\_b4\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b4_ssld_stage2_ft_in1k/1) | 13.60M | HGNetV2 B4 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |
| [hgnetv2\_b5\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage1_in22k_in1k/1) | 33.42M | HGNetV2 B5 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |
| [hgnetv2\_b5\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage2_ft_in1k/1) | 33.42M | HGNetV2 B5 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |
| [hgnetv2\_b6\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage1_in22k_in1k/1) | 69.18M | HGNetV2 B6 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |
| [hgnetv2\_b6\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage2_ft_in1k/1) | 69.18M | HGNetV2 B6 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |

* * *

[HGNetV2Backbone model](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_backbone/#hgnetv2backbone-model)

[`HGNetV2Backbone` class](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_backbone/#hgnetv2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_backbone/#frompreset-method)