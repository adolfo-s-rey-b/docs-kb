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
 / [SigLIP](https://keras.io/keras_hub/api/models/siglip/)
 / SigLIPPreprocessor

SigLIPPreprocessor
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/siglip/siglip_preprocessor.py#L20)

### `SigLIPPreprocessor` class

Copied!

`keras_hub.models.SigLIPPreprocessor(     tokenizer,     image_converter=None,     sequence_length=64,     add_start_token=False,     add_end_token=True,     canonicalize_text=True,     **kwargs )`

SigLIP preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.SigLIPBackbone`](https://keras.io/keras_hub/api/models/siglip/siglip_backbone#siglipbackbone-class)
. By default, it will take in batches of strings and images, and return token ids and resized images.

**Arguments**

*   **tokenizer**: A `keras_hub.models.SigLIPTokenizer` instance.
*   **image\_converter**: A `keras_hub.models.SigLIPImageConverter` instance.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Defaults to `False`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Defaults to `True`.
*   **canonicalize\_text**: If `True`, the input strings will be canonicalized (converted to lowercase, punctuation removed, and stripped).

**Call arguments**

*   **x**: A dict with `"prompts"` and `"images"` keys, where `"prompts"` is [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings and `"images"` are the image tensors.
*   **y**: Label data. Should always be `None` since SigLIP doesn't need the label to calculate the loss.
*   **sample\_weight**: Label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.SigLIPPreprocessor.from_preset(     "siglip_base_patch16_224" )  # Tokenize the sentence and preprocess the image. preprocessor(     {         "prompts": "The quick brown fox jumped.",         "images": np.ones(shape=(123, 123, 3)),     } )  # Tokenize a batch of sentences and preprocess a batch of images. preprocessor(     {         "prompts": ["The quick brown fox jumped.", "The fox slept."],         "images": np.ones(shape=(2, 123, 123, 3)),     } )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`SigLIPPreprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

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
| [siglip\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_224/1) | 203.16M | 200 million parameter, image size 224, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256/1) | 203.20M | 200 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_384/1) | 203.45M | 200 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_base\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_512/1) | 203.79M | 200 million parameter, image size 512, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256\_multilingual](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256_multilingual/1) | 370.63M | 370 million parameter, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_224/1) | 375.19M | 375 million parameter, patch size 16, image size 224, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_256/1) | 375.23M | 375 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch32\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch32_256/1) | 376.86M | 376 million parameter, patch size 32, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_384/1) | 376.86M | 376 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_256/1) | 652.15M | 652 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_384/1) | 652.48M | 652 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_224/1) | 877.36M | 877 million parameter, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_384/1) | 877.96M | 877 million parameter, image size 384, shape-optimized version, pre-trained on WebLi. |
| [medsiglip\_900m\_448](https://www.kaggle.com/models/keras/medsiglip/keras/medsiglip_900m_448/1) | 878.30M | A 900 million parameter variant of SigLIP trained to encode medical images and text into a common embedding space. MedSigLIP contains a vision encoder and a text encoder, and supports 448x448 image resolution with up to 64 text tokens. |
| [siglip2\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_256/1) | 881.53M | 881 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_384/1) | 881.86M | 881 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_512/1) | 882.31M | 882 million parameter, patch size 16, image size 512, pre-trained on WebLi. |
| [siglip\_so400m\_patch16\_256\_i18n](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch16_256_i18n/1) | 1.13B | 1.1 billion parameter, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_224/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_256/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_384/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_384/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 384, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_512/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 512, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_256/2) | 1.87B | 1.8 billion parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_384/1) | 1.87B | 1.8 billion parameter, patch size 16, image size 384, pre-trained on WebLi. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.SigLIPPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[SigLIPPreprocessor](https://keras.io/keras_hub/api/models/siglip/siglip_preprocessor/#siglippreprocessor)

[`SigLIPPreprocessor` class](https://keras.io/keras_hub/api/models/siglip/siglip_preprocessor/#siglippreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/siglip/siglip_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/siglip/siglip_preprocessor/#tokenizer-property)