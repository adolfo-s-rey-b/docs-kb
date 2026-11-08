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
 / [CLIP](https://keras.io/keras_hub/api/models/clip/)
 / CLIPPreprocessor

CLIPPreprocessor
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/clip/clip_preprocessor.py#L18)

### `CLIPPreprocessor` class

Copied!

`keras_hub.models.CLIPPreprocessor(     tokenizer,     image_converter=None,     sequence_length=77,     add_start_token=True,     add_end_token=True,     to_lower=True,     **kwargs )`

CLIP preprocessor.

This preprocessing layer will do 2 things:

This preprocessing layer is meant for use with [`keras_hub.models.CLIPBackbone`](https://keras.io/keras_hub/api/models/clip/clip_backbone#clipbackbone-class)
. By default, it will take in batches of strings and images, and return token ids and resized images.

**Arguments**

*   **tokenizer**: A `keras_hub.models.CLIPTokenizer` instance.
*   **image\_converter**: A `keras_hub.models.CLIPImageConverter` instance.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence.
*   **to\_lower**: bool. Whether to lower the inputs.

**Call arguments**

*   **x**: A dict with `"prompts"` and `"images"` keys, where `"prompts"` is [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings and `"images"` are the image tensors.
*   **y**: Label data. Should always be `None` since SigLIP doesn't need the label to calculate the loss.
*   **sample\_weight**: Label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.CLIPPreprocessor.from_preset(     "clip_vit_base_patch16" )  # Tokenize the sentence and preprocess the image. preprocessor(     {         "prompts": "The quick brown fox jumped.",         "images": np.ones(shape=(123, 123, 3)),     } )  # Tokenize a batch of sentences and preprocess a batch of images. preprocessor(     {         "prompts": ["The quick brown fox jumped.", "The fox slept."],         "images": np.ones(shape=(2, 123, 123, 3)),     } )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`CLIPPreprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

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
| [clip\_vit\_base\_patch16](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch16/3) | 149.62M | 150 million parameter, 12-layer for vision and 12-layer for text, patch size of 16, CLIP model. |
| [clip\_vit\_base\_patch32](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch32/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, CLIP model. |
| [clip\_vit\_b\_32\_laion2b\_s34b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_b_32_laion2b_s34b_b79k/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, Open CLIP model. |
| [clip\_vit\_large\_patch14](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14/3) | 427.62M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, CLIP model. |
| [clip\_vit\_large\_patch14\_336](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14_336/3) | 427.94M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, image size of 336, CLIP model. |
| [clip\_vit\_h\_14\_laion2b\_s32b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_h_14_laion2b_s32b_b79k/3) | 986.11M | 986 million parameter, 32-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_g\_14\_laion2b\_s12b\_b42k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_g_14_laion2b_s12b_b42k/3) | 1.37B | 1.4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_bigg\_14\_laion2b\_39b\_b160k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_bigg_14_laion2b_39b_b160k/3) | 2.54B | 2.5 billion parameter, 48-layer for vision and 32-layer for text, patch size of 14, Open CLIP model. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.CLIPPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[CLIPPreprocessor](https://keras.io/keras_hub/api/models/clip/clip_preprocessor/#clippreprocessor)

[`CLIPPreprocessor` class](https://keras.io/keras_hub/api/models/clip/clip_preprocessor/#clippreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/clip/clip_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/clip/clip_preprocessor/#tokenizer-property)