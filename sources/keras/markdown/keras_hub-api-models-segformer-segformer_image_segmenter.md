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
 / SegFormerImageSegmenter model

SegFormerImageSegmenter model
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/segformer/segformer_image_segmenter.py#L11)

### `SegFormerImageSegmenter` class

Copied!

`keras_hub.models.SegFormerImageSegmenter(     backbone, num_classes, preprocessor=None, **kwargs )`

A Keras model implementing SegFormer for semantic segmentation.

This class implements the segmentation head of the SegFormer architecture described in \[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers\] (https://arxiv.org/abs/2105.15203) and \[based on the TensorFlow implementation from DeepVision\] (https://github.com/DavidLandup0/deepvision/tree/main/deepvision/models/segmentation/segformer).

SegFormers are meant to be used with the MixTransformer (MiT) encoder family, and use a very lightweight all-MLP decoder head.

The MiT encoder uses a hierarchical transformer which outputs features at multiple scales, similar to that of the hierarchical outputs typically associated with CNNs.

**Arguments**

*   **image\_encoder**: [`keras.Model`](https://keras.io/api/models/model#model-class)
    . The backbone network for the model that is used as a feature extractor for the SegFormer encoder. It is _intended_ to be used only with the MiT backbone model ([`keras_hub.models.MiTBackbone`](https://keras.io/keras_hub/api/models/mit/mit_backbone#mitbackbone-class)
    ) which was created specifically for SegFormers. Alternatively, can be a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
     a model subclassing `keras_hub.models.FeaturePyramidBackbone`, or a [`keras.Model`](https://keras.io/api/models/model#model-class)
     that has a `pyramid_outputs` property which is a dictionary with keys "P2", "P3", "P4", and "P5" and layer names as values.
*   **num\_classes**: int, the number of classes for the detection model, including the background class.
*   **projection\_filters**: int, number of filters in the convolution layer projecting the concatenated features into a segmentation map. Defaults to 256\`.

**Example**

Using presets:

Copied!

`segmenter = keras_hub.models.SegFormerImageSegmenter.from_preset(     "segformer_b0_ade20k_512" )  images = np.random.rand(1, 512, 512, 3) segformer(images)`

Using the SegFormer backbone:

Copied!

`encoder = keras_hub.models.MiTBackbone.from_preset(     "mit_b0_ade20k_512" ) backbone = keras_hub.models.SegFormerBackbone(     image_encoder=encoder,     projection_filters=256, )`

Using the SegFormer backbone with a custom encoder:

Copied!

`images = np.ones(shape=(1, 96, 96, 3)) labels = np.zeros(shape=(1, 96, 96, 1))  encoder = keras_hub.models.MiTBackbone(     depths=[2, 2, 2, 2],     image_shape=(96, 96, 3),     hidden_dims=[32, 64, 160, 256],     num_layers=4,     blockwise_num_heads=[1, 2, 5, 8],     blockwise_sr_ratios=[8, 4, 2, 1],     max_drop_path_rate=0.1,     patch_sizes=[7, 3, 3, 3],     strides=[4, 2, 2, 2], )  backbone = keras_hub.models.SegFormerBackbone(     image_encoder=encoder,     projection_filters=256, ) segformer = keras_hub.models.SegFormerImageSegmenter(     backbone=backbone,     num_classes=4, ) segformer(images`

Using the segmentor class with a preset backbone:

Copied!

`image_encoder = keras_hub.models.MiTBackbone.from_preset(     "mit_b0_ade20k_512" ) backbone = keras_hub.models.SegFormerBackbone(     image_encoder=encoder,     projection_filters=256, ) segformer = keras_hub.models.SegFormerImageSegmenter(     backbone=backbone,     num_classes=4, )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`SegFormerImageSegmenter.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [segformer\_b0\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b0_ade20k_512/3) | 3.72M | SegFormer model with MiTB0 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b0\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b0_cityscapes_1024/3) | 3.72M | SegFormer model with MiTB0 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b1\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b1_ade20k_512/5) | 13.68M | SegFormer model with MiTB1 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b1\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b1_ade20k_512/1) | 13.68M | SegFormer model with MiTB1 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b2\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b2_ade20k_512/3) | 24.73M | SegFormer model with MiTB2 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b2\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b2_cityscapes_1024/3) | 24.73M | SegFormer model with MiTB2 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b3\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b3_ade20k_512/3) | 44.60M | SegFormer model with MiTB3 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b3\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b3_cityscapes_1024/3) | 44.60M | SegFormer model with MiTB3 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b4\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b4_ade20k_512/3) | 61.37M | SegFormer model with MiTB4 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b4\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b4_cityscapes_1024/3) | 61.37M | SegFormer model with MiTB4 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b5\_ade20k\_640](https://www.kaggle.com/models/keras/segformer/keras/segformer_b5_ade20k_640/3) | 81.97M | SegFormer model with MiTB5 backbone fine-tuned on ADE20k in 640x640 resolution. |
| [segformer\_b5\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b5_cityscapes_1024/3) | 81.97M | SegFormer model with MiTB5 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |

* * *

### `backbone` property

Copied!

`keras_hub.models.SegFormerImageSegmenter.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.SegFormerImageSegmenter.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[SegFormerImageSegmenter model](https://keras.io/keras_hub/api/models/segformer/segformer_image_segmenter/#segformerimagesegmenter-model)

[`SegFormerImageSegmenter` class](https://keras.io/keras_hub/api/models/segformer/segformer_image_segmenter/#segformerimagesegmenter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/segformer/segformer_image_segmenter/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/segformer/segformer_image_segmenter/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/segformer/segformer_image_segmenter/#preprocessor-property)