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
 / [RetinaNet](https://keras.io/keras_hub/api/models/retinanet/)
 / RetinaNetBackbone model

RetinaNetBackbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/retinanet/retinanet_backbone.py#L9)

### `RetinaNetBackbone` class

Copied!

`keras_hub.models.RetinaNetBackbone(     image_encoder,     min_level,     max_level,     use_p5,     use_fpn_batch_norm=False,     image_shape=(None, None, 3),     data_format=None,     dtype=None,     **kwargs )`

RetinaNet Backbone.

Combines a CNN backbone (e.g., ResNet, MobileNet) with a feature pyramid network (FPN)to extract multi-scale features for object detection.

**Arguments**

*   **image\_encoder**: [`keras.Model`](https://keras.io/api/models/model#model-class)
    . The backbone model (e.g., ResNet50, MobileNetV2) used to extract features from the input image. It should have pyramid outputs (i.e., a dictionary mapping level names like `"P2"`, `"P3"`, etc. to their corresponding feature tensors).
*   **min\_level**: int. The minimum level of the feature pyramid (e.g., 3). This determines the coarsest level of features used.
*   **max\_level**: int. The maximum level of the feature pyramid (e.g., 7). This determines the finest level of features used.
*   **use\_p5**: bool. Determines the input source for creating coarser feature pyramid levels. If `True`, the output of the last backbone layer (typically `'P5'` in an FPN) is used as input to create higher-level feature maps (e.g., `'P6'`, `'P7'`) through additional convolutional layers. If `False`, the original `'P5'` feature map from the backbone is directly used as input for creating the coarser levels, bypassing any further processing of `'P5'` within the feature pyramid. Defaults to `False`.
*   **use\_fpn\_batch\_norm**: bool. Whether to use batch normalization in the feature pyramid network. Defaults to `False`.
*   **image\_shape**: tuple. tuple. The shape of the input image (H, W, C). The height and width can be `None` if they are variable.
*   **data\_format**: str. The data format of the input image (channels\_first or channels\_last).
*   **dtype**: str. The data type of the input image.
*   **\*\*kwargs**: Additional keyword arguments passed to the base class.

**Raises**

*   **ValueError**: If `min_level` is greater than `max_level`.
*   **ValueError**: If `backbone_max_level` is less than 5 and `max_level` is greater than or equal to 5.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`RetinaNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [retinanet\_resnet50\_fpn\_v2\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_v2_coco/3) | 31.56M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution with FPN features created from P5 level. |
| [retinanet\_resnet50\_fpn\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_coco/4) | 34.12M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution. |

* * *

[RetinaNetBackbone model](https://keras.io/keras_hub/api/models/retinanet/retinanet_backbone/#retinanetbackbone-model)

[`RetinaNetBackbone` class](https://keras.io/keras_hub/api/models/retinanet/retinanet_backbone/#retinanetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/retinanet/retinanet_backbone/#frompreset-method)