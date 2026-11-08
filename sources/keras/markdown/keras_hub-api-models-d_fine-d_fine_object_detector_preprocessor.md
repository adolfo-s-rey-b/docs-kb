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
 / [D-FINE](https://keras.io/keras_hub/api/models/d_fine/)
 / DFineObjectDetectorPreprocessor layer

DFineObjectDetectorPreprocessor layer
=====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/d_fine/d_fine_object_detector_preprocessor.py#L11)

### `DFineObjectDetectorPreprocessor` class

Copied!

`keras_hub.models.DFineObjectDetectorPreprocessor(image_converter=None, **kwargs)`

Base class for object detector preprocessing layers.

`ObjectDetectorPreprocessor` tasks wraps a `keras_hub.layers.Preprocessor` to create a preprocessing layer for object detection tasks. It is intended to be paired with a `keras_hub.models.ImageObjectDetector` task.

All `ObjectDetectorPreprocessor` take three inputs, `x`, `y`, and `sample_weight`. `x`, the first input, should always be included. It can be an image or batch of images. See examples below. `y` and `sample_weight` are optional inputs that will be passed through unaltered. Usually, `y` will be the a dict of \`{"boxes": Tensor(batch\_size, num\_boxes, 4), "classes": (batch\_size, num\_boxes)}.

The layer will returns either `x`, an `(x, y)` tuple if labels were provided, or an `(x, y, sample_weight)` tuple if labels and sample weight were provided. `x` will be the input images after all model preprocessing has been applied.

All `ObjectDetectorPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for your model will be automatically instantiated.

**Arguments**

*   **image\_converter**: Preprocessing pipeline for images.

Examples.

Copied!

``preprocessor = keras_hub.models.ObjectDetectorPreprocessor.from_preset(     "retinanet_resnet50", )  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)</span>  ### `from_preset` method  ```python DFineObjectDetectorPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )``

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
| [dfine\_nano\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_nano_coco/1) | 3.79M | D-FINE Nano model, the smallest variant in the family, pretrained on the COCO dataset. Ideal for applications where computational resources are limited. |
| [dfine\_small\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_coco/1) | 10.33M | D-FINE Small model pretrained on the COCO dataset. Offers a balance between performance and computational efficiency. |
| [dfine\_small\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj2coco/1) | 10.33M | D-FINE Small model first pretrained on Objects365 and then fine-tuned on COCO, combining broad feature learning with benchmark-specific adaptation. |
| [dfine\_small\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj365/1) | 10.62M | D-FINE Small model pretrained on the large-scale Objects365 dataset, enhancing its ability to recognize a wider variety of objects. |
| [dfine\_medium\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_coco/1) | 19.62M | D-FINE Medium model pretrained on the COCO dataset. A solid baseline with strong performance for general-purpose object detection. |
| [dfine\_medium\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj2coco/1) | 19.62M | D-FINE Medium model using a two-stage training process: pretraining on Objects365 followed by fine-tuning on COCO. |
| [dfine\_medium\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj365/1) | 19.99M | D-FINE Medium model pretrained on the Objects365 dataset. Benefits from a larger and more diverse pretraining corpus. |
| [dfine\_large\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_coco/1) | 31.34M | D-FINE Large model pretrained on the COCO dataset. Provides high accuracy and is suitable for more demanding tasks. |
| [dfine\_large\_obj2coco\_e25](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj2coco_e25/1) | 31.34M | D-FINE Large model pretrained on Objects365 and then fine-tuned on COCO for 25 epochs. A high-performance model with specialized tuning. |
| [dfine\_large\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj365/1) | 31.86M | D-FINE Large model pretrained on the Objects365 dataset for improved generalization and performance on diverse object categories. |
| [dfine\_xlarge\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_coco/1) | 62.83M | D-FINE X-Large model, the largest COCO-pretrained variant, designed for state-of-the-art performance where accuracy is the top priority. |
| [dfine\_xlarge\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj2coco/1) | 62.83M | D-FINE X-Large model, pretrained on Objects365 and fine-tuned on COCO, representing the most powerful model in this series for COCO-style tasks. |
| [dfine\_xlarge\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj365/1) | 63.35M | D-FINE X-Large model pretrained on the Objects365 dataset, offering maximum performance by leveraging a vast number of object categories during pretraining. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.DFineObjectDetectorPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[DFineObjectDetectorPreprocessor layer](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector_preprocessor/#dfineobjectdetectorpreprocessor-layer)

[`DFineObjectDetectorPreprocessor` class](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector_preprocessor/#dfineobjectdetectorpreprocessor-class)

[Load a preprocessor for Gemma generation.](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector_preprocessor/#load-a-preprocessor-for-gemma-generation)

[Load a preprocessor for Bert classification.](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector_preprocessor/#load-a-preprocessor-for-bert-classification)