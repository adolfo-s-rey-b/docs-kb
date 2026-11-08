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
 / RetinaNetObjectDetectorPreprocessor layer

RetinaNetObjectDetectorPreprocessor layer
=========================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/retinanet/retinanet_object_detector_preprocessor.py#L11)

### `RetinaNetObjectDetectorPreprocessor` class

Copied!

`keras_hub.models.RetinaNetObjectDetectorPreprocessor(image_converter=None, **kwargs)`

Base class for object detector preprocessing layers.

`ObjectDetectorPreprocessor` tasks wraps a `keras_hub.layers.Preprocessor` to create a preprocessing layer for object detection tasks. It is intended to be paired with a `keras_hub.models.ImageObjectDetector` task.

All `ObjectDetectorPreprocessor` take three inputs, `x`, `y`, and `sample_weight`. `x`, the first input, should always be included. It can be an image or batch of images. See examples below. `y` and `sample_weight` are optional inputs that will be passed through unaltered. Usually, `y` will be the a dict of \`{"boxes": Tensor(batch\_size, num\_boxes, 4), "classes": (batch\_size, num\_boxes)}.

The layer will returns either `x`, an `(x, y)` tuple if labels were provided, or an `(x, y, sample_weight)` tuple if labels and sample weight were provided. `x` will be the input images after all model preprocessing has been applied.

All `ObjectDetectorPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for your model will be automatically instantiated.

**Arguments**

*   **image\_converter**: Preprocessing pipeline for images.

Examples.

Copied!

``preprocessor = keras_hub.models.ObjectDetectorPreprocessor.from_preset(     "retinanet_resnet50", )  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)</span>  ### `from_preset` method  ```python RetinaNetObjectDetectorPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )``

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [retinanet\_resnet50\_fpn\_v2\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_v2_coco/3) | 31.56M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution with FPN features created from P5 level. |
| [retinanet\_resnet50\_fpn\_coco](https://www.kaggle.com/models/keras/retinanet/keras/retinanet_resnet50_fpn_coco/4) | 34.12M | RetinaNet model with ResNet50 backbone fine-tuned on COCO in 800x800 resolution. |

**Guides and examples using `from_preset`**

*   [Object Detection Fine-tuning with KerasHub](https://keras.io/keras_hub/guides/object_detection_retinanet/)
    

* * *

### `image_converter` property

Copied!

`keras_hub.models.RetinaNetObjectDetectorPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[RetinaNetObjectDetectorPreprocessor layer](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector_preprocessor/#retinanetobjectdetectorpreprocessor-layer)

[`RetinaNetObjectDetectorPreprocessor` class](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector_preprocessor/#retinanetobjectdetectorpreprocessor-class)

[Load a preprocessor for Gemma generation.](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector_preprocessor/#load-a-preprocessor-for-gemma-generation)

[Load a preprocessor for Bert classification.](https://keras.io/keras_hub/api/models/retinanet/retinanet_object_detector_preprocessor/#load-a-preprocessor-for-bert-classification)