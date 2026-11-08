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
 / [Segment Anything Model](https://keras.io/keras_hub/api/models/sam/)
 / SAMImageSegmenterPreprocessor layer

SAMImageSegmenterPreprocessor layer
===================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/sam/sam_image_segmenter_preprocessor.py#L12)

### `SAMImageSegmenterPreprocessor` class

Copied!

`keras_hub.models.SAMImageSegmenterPreprocessor(     image_converter=None, resize_output_mask=False, **kwargs )`

Base class for image segmentation preprocessing layers.

`ImageSegmenterPreprocessor` wraps a [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
 to create a preprocessing layer for image segmentation tasks. It is intended to be paired with a [`keras_hub.models.ImageSegmenter`](https://keras.io/keras_hub/api/base_classes/image_segmenter#imagesegmenter-class)
 task.

All `ImageSegmenterPreprocessor` instances take three inputs: `x`, `y`, and `sample_weight`.

*   `x`: The first input, should always be included. It can be an image or a batch of images.
*   `y`: (Optional) Usually the segmentation mask(s), if `resize_output_mask` is set to `True` this will be resized to input image shape else will be passed through unaltered.
*   `sample_weight`: (Optional) Will be passed through unaltered.
*   `resize_output_mask` bool: If set to `True` the output mask will be resized to the same size as the input image. Defaults to `False`.

The layer will output either `x`, an `(x, y)` tuple if labels were provided, or an `(x, y, sample_weight)` tuple if labels and sample weight were provided. `x` will be the input images after all model preprocessing has been applied.

All `ImageSegmenterPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for your model will be automatically instantiated.

Examples.

Copied!

``preprocessor = keras_hub.models.ImageSegmenterPreprocessor.from_preset(     "deeplabv3_resnet50", )  # Resize a single image for the model. x = np.ones((512, 512, 3)) x = preprocessor(x)  # Resize an image and its mask. x, y = np.ones((512, 512, 3)), np.zeros((512, 512, 1)) x, y = preprocessor(x, y)  # Resize a batch of images and masks. x, y = [np.ones((512, 512, 3)), np.zeros((512, 512, 3))],        [np.ones((512, 512, 1)), np.zeros((512, 512, 1))] x, y = preprocessor(x, y)  # Use a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). ds = tf.data.Dataset.from_tensor_slices((x, y)).batch(2) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`SAMImageSegmenterPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [sam\_base\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_base_sa1b/5) | 93.74M | The base SAM model trained on the SA1B dataset. |
| [sam\_huge\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_huge_sa1b/5) | 312.34M | The huge SAM model trained on the SA1B dataset. |
| [sam\_large\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_large_sa1b/5) | 641.09M | The large SAM model trained on the SA1B dataset. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.SAMImageSegmenterPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[SAMImageSegmenterPreprocessor layer](https://keras.io/keras_hub/api/models/sam/sam_image_segmenter_preprocessor/#samimagesegmenterpreprocessor-layer)

[`SAMImageSegmenterPreprocessor` class](https://keras.io/keras_hub/api/models/sam/sam_image_segmenter_preprocessor/#samimagesegmenterpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/sam/sam_image_segmenter_preprocessor/#frompreset-method)

[`image_converter` property](https://keras.io/keras_hub/api/models/sam/sam_image_segmenter_preprocessor/#imageconverter-property)