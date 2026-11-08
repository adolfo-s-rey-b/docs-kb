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
 / RetinaNetObjectDetector model

RetinaNetObjectDetector model
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/retinanet/retinanet_object_detector.py#L19)

### `RetinaNetObjectDetector` class

Copied!

`keras_hub.models.RetinaNetObjectDetector(     backbone,     num_classes,     bounding_box_format="yxyx",     anchor_generator=None,     label_encoder=None,     use_prediction_head_norm=False,     classification_head_prior_probability=0.01,     pre_logits_num_conv_layers=4,     preprocessor=None,     activation=None,     dtype=None,     prediction_decoder=None,     **kwargs )`

RetinaNet object detector model.

This class implements the RetinaNet object detection architecture. It consists of a feature extractor backbone, a feature pyramid network(FPN), and two prediction heads (for classification and bounding box regression).

**Arguments**

*   **backbone**: [`keras.Model`](https://keras.io/api/models/model#model-class)
    . A `keras.models.RetinaNetBackbone` class, defining the backbone network architecture. Provides feature maps for detection.
*   **anchor\_generator**: A `keras_hub.layers.AnchorGenerator` instance. Generates anchor boxes at different scales and aspect ratios across the image. If None, a default `AnchorGenerator` is created with the following parameters: - `bounding_box_format`: Same as the model's `bounding_box_format`. - `min_level`: The backbone's `min_level`. - `max_level`: The backbone's `max_level`. - `num_scales`: 3. - `aspect_ratios`: \[0.5, 1.0, 2.0\]. - `anchor_size`: 4.0. You can create a custom `AnchorGenerator` by instantiating the `keras_hub.layers.AnchorGenerator` class and passing the desired arguments.
*   **num\_classes**: int. The number of object classes to be detected.
*   **bounding\_box\_format**: str. Dataset bounding box format (e.g., "xyxy", "yxyx"). Defaults to `yxyx`.
*   **label\_encoder**: Optional. A `RetinaNetLabelEncoder` instance. Encodes ground truth boxes and classes into training targets. It matches ground truth boxes to anchors based on IoU and encodes box coordinates as offsets. If `None`, a default encoder is created. See the `RetinaNetLabelEncoder` class for details. If None, a default encoder is created with standard parameters. - `anchor_generator`: Same as the model's. - `bounding_box_format`: Same as the model's `bounding_box_format`. - `positive_threshold`: 0.5 - `negative_threshold`: 0.4 - `encoding_format`: "center\_xywh" - `box_variance`: \[1.0, 1.0, 1.0, 1.0\] - `background_class`: -1 - `ignore_class`: -2
*   **use\_prediction\_head\_norm**: bool. Whether to use Group Normalization after the convolution layers in the prediction heads. Defaults to `False`.
*   **classification\_head\_prior\_probability**: float. Prior probability for the classification head (used for focal loss). Defaults to 0.01.
*   **pre\_logits\_num\_conv\_layers**: int. The number of convolutional layers in the head before the logits layer. These convolutional layers are applied before the final linear layer (logits) that produces the output predictions (bounding box regressions, classification scores).
*   **preprocessor**: Optional. An instance of `RetinaNetObjectDetectorPreprocessor`or a custom preprocessor. Handles image preprocessing before feeding into the backbone.
*   **activation**: Optional. The activation function to be used in the classification head. If None, sigmoid is used.
*   **dtype**: Optional. The data type for the prediction heads. Defaults to the backbone's dtype policy.
*   **prediction\_decoder**: Optional. A `keras.layers.Layer` instance responsible for transforming RetinaNet predictions (box regressions and classifications) into final bounding boxes and classes with confidence scores. Defaults to a `NonMaxSuppression` instance.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`RetinaNetObjectDetector.from_preset(preset, load_weights=True, **kwargs)`

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
| [retinanet\_resnet50\_fpn\_v2\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_v2_coco/3) | 31.56M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution with FPN features created from P5 level. |
| [retinanet\_resnet50\_fpn\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_coco/4) | 34.12M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution. |

* * *

### `backbone` property

Copied!

`keras_hub.models.RetinaNetObjectDetector.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.RetinaNetObjectDetector.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[RetinaNetObjectDetector model](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector/#retinanetobjectdetector-model)

[`RetinaNetObjectDetector` class](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector/#retinanetobjectdetector-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector/#preprocessor-property)