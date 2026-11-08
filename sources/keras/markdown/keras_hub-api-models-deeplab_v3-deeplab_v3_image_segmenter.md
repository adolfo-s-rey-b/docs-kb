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
 / [DeepLabV3](https://keras.io/keras_hub/api/models/deeplab_v3/)
 / DeepLabV3ImageSegmenter model

DeepLabV3ImageSegmenter model
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/deeplab_v3/deeplab_v3_segmenter.py#L13)

### `DeepLabV3ImageSegmenter` class

Copied!

`keras_hub.models.DeepLabV3ImageSegmenter(     backbone, num_classes, activation=None, preprocessor=None, **kwargs )`

DeepLabV3 and DeeplabV3 and DeeplabV3Plus segmentation task.

**Arguments**

*   **backbone**: A `keras_hub.models.DeepLabV3` instance.
*   **num\_classes**: int. The number of classes for the detection model. Note that the `num_classes` contains the background class, and the classes from the data should be represented by integers with range `[0, num_classes]`.
*   **activation**: str or callable. The activation function to use on the `Dense` layer. Set `activation=None` to return the output logits. Defaults to `None`.
*   **preprocessor**: A [`keras_hub.models.DeepLabV3ImageSegmenterPreprocessor`](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter_preprocessor#deeplabv3imagesegmenterpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Example**

Load a DeepLabV3 preset with all the 21 class, pretrained segmentation head.

Copied!

`images = np.ones(shape=(1, 96, 96, 3)) labels = np.zeros(shape=(1, 96, 96, 2)) segmenter = keras_hub.models.DeepLabV3ImageSegmenter.from_preset(     "deeplab_v3_plus_resnet50_pascalvoc", ) segmenter.predict(images)`

Specify `num_classes` to load randomly initialized segmentation head.

Copied!

`segmenter = keras_hub.models.DeepLabV3ImageSegmenter.from_preset(     "deeplab_v3_plus_resnet50_pascalvoc",     num_classes=2, ) segmenter.preprocessor.image_size = (96, 96) segmenter.fit(images, labels, epochs=3) segmenter.predict(images)  # Trained 2 class segmentation.`

Load DeepLabv3+ presets a extension of DeepLabv3 by adding a simple yet effective decoder module to refine the segmentation results especially along object boundaries.

Copied!

`segmenter = keras_hub.models.DeepLabV3ImageSegmenter.from_preset(     "deeplabv3_plus_resnet50_pascalvoc", ) segmenter.predict(images)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`DeepLabV3ImageSegmenter.from_preset(preset, load_weights=True, **kwargs)`

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
| [deeplab\_v3\_plus\_resnet50\_pascalvoc](https://www.kaggle.com/models/keras/deeplabv3plus/keras/deeplab_v3_plus_resnet50_pascalvoc/4) | 39.19M | DeepLabV3+ model with ResNet50 as image encoder and trained on augmented Pascal VOC dataset by Semantic Boundaries Dataset(SBD) which is having categorical accuracy of 90.01 and 0.63 Mean IoU. |

**Guides and examples using `from_preset`**

*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
    

* * *

### `backbone` property

Copied!

`keras_hub.models.DeepLabV3ImageSegmenter.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.DeepLabV3ImageSegmenter.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[DeepLabV3ImageSegmenter model](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter/#deeplabv3imagesegmenter-model)

[`DeepLabV3ImageSegmenter` class](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter/#deeplabv3imagesegmenter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/deeplab_v3/deeplab_v3_image_segmenter/#preprocessor-property)