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
 / [Segment Anything Model 3](https://keras.io/keras_hub/api/models/sam3/)
 / SAM3PromptableConceptImageSegmenterPreprocessor layer

SAM3PromptableConceptImageSegmenterPreprocessor layer
=====================================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/sam3/sam3_pc_image_segmenter_preprocessor.py#L20)

### `SAM3PromptableConceptImageSegmenterPreprocessor` class

Copied!

`keras_hub.models.SAM3PromptableConceptImageSegmenterPreprocessor(     tokenizer,     image_converter,     sequence_length=32,     add_start_token=True,     add_end_token=True,     point_pad_value=-10,     **kwargs )`

SAM3 Promptable Concept Image Segmenter preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.SAM3PromptableConceptImageSegmenter`](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter#sam3promptableconceptimagesegmenter-class)
.

**Arguments**

*   **tokenizer**: A `keras_hub.models.SAM3Tokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.SAM3ImageConverter`](https://keras.io/keras_hub/api/models/sam3/sam3_image_converter#sam3imageconverter-class)
     instance.
*   **sequence\_length**: The length of the packed token\_ids. Defaults to `32`.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Defaults to `True`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Defaults to `True`.
*   **point\_pad\_value**: int. The padding value for box prompts. Defaults to `-10`.

**Call arguments**

*   **x**: A dictionary with the following keys:
    *   images: A single image or a batch of images, of shape `(height, width, 3)` or `(batch_size, height, width, 3)`.
    *   prompts: (optional) A string or a batch of strings containing the text prompts. If not provided, a default prompt will be used.
    *   boxes: (optional) A tensor of shape `(num_boxes, 4)` or `(batch_size, num_boxes, 4)` containing box coordinates in `(x_min, y_min, x_max, y_max)` format. Coordinates should be in absolute pixel values. If not provided, no box prompts will be used. `-10` is used as the padding value.
    *   box\_labels: (optional) A tensor of shape `(num_boxes,)` or `(batch_size, num_boxes)` containing box labels. If not provided, no box labels will be used. `-10` is used as the padding value.

**Examples**

Copied!

``# Load the preprocessor from a preset. preprocessor = keras_hub.models.SAM3PromptableConceptImageSegmenterPreprocessor.from_preset(     "sam3_pcs" )  # Unbatched inputs, with one image and one text prompt. preprocessor(     {         "prompts": "ear",         "images": np.ones((896, 896, 3), dtype="float32")     } )  # Unbatched inputs, with one image and one box prompt. preprocessor(     {         "boxes": [[0, 0, 300, 300]],         "box_labels": [1],         "images": np.ones((896, 896, 3), dtype="float32")     } )  # Batched inputs, one image per text prompt. preprocessor(     {         "prompts": [             "ear",             "head"         ],         "images": [             np.ones((896, 896, 3), dtype="float32"),             np.ones((896, 896, 3), dtype="float32")         ]     } )  # Batched inputs, one image per box prompt. preprocessor(     {         "boxes": [             [[0, 0, 300, 300]],             [[50, 50, 100, 100]]         ],         "box_labels": [             [1],             [1]         ],         "images": [             np.ones((896, 896, 3), dtype="float32"),             np.ones((896, 896, 3), dtype="float32")         ]     } )  # Different number of box prompts in every sample. preprocessor(     {         "boxes": [             [[0, 0, 300, 300]],             [[50, 50, 100, 100], [150, 150, 200, 200]]         ],         "box_labels": [             [1],             [1, 1]         ],         "images": [             np.ones((896, 896, 3), dtype="float32"),             np.ones((896, 896, 3), dtype="float32")         ]     } )  # Apply preprocessing to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). inputs = {     "prompts": [         "ear",         "head",     ],     "images": np.ones((2, 896, 896, 3), dtype="float32") } ds = tf.data.Dataset.from_tensor_slices(inputs) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`SAM3PromptableConceptImageSegmenterPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [sam3\_pcs](https://www.kaggle.com/models/keras/sam3/keras/sam3_pcs/1) | 30.00M | 30 million parameter Promptable Concept Segmentation (PCS) SAM model. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.SAM3PromptableConceptImageSegmenterPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[SAM3PromptableConceptImageSegmenterPreprocessor layer](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter_preprocessor/#sam3promptableconceptimagesegmenterpreprocessor-layer)

[`SAM3PromptableConceptImageSegmenterPreprocessor` class](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter_preprocessor/#sam3promptableconceptimagesegmenterpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter_preprocessor/#frompreset-method)

[`image_converter` property](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter_preprocessor/#imageconverter-property)