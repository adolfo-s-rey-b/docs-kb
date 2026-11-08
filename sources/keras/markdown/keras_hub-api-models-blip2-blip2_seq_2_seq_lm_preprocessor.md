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
 / [Blip2](https://keras.io/keras_hub/api/models/blip2/)
 / BLIP2Seq2SeqLMPreprocessor layer

BLIP2Seq2SeqLMPreprocessor layer
================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/blip2/blip2_seq_2_seq_lm_preprocessor.py#L19)

### `BLIP2Seq2SeqLMPreprocessor` class

Copied!

`keras_hub.models.BLIP2Seq2SeqLMPreprocessor(     tokenizer,     image_converter=None,     encoder_sequence_length=512,     decoder_sequence_length=512,     **kwargs )`

Multimodal seq2seq preprocessor for the BLIP-2 Flan-T5 variant.

This preprocessing layer is meant for use with [`keras_hub.models.BLIP2Seq2SeqLM`](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm#blip2seq2seqlm-class)
, the encoder-decoder (Flan-T5) BLIP-2 task. Following the keras-hub seq2seq convention it takes a dictionary with `"encoder_text"` and (optionally) `"decoder_text"` keys, and additionally accepts an `"images"` key when an `image_converter` is configured.

The encoder text is fed to the T5 encoder (alongside the Q-Former visual soft-prompt produced by the backbone), and the decoder text is the teacher-forced target during training, or the decoder prompt during generation. It returns outputs in the standard `(x, y, sample_weight)` format, where `y` is the decoder sequence shifted one step left.

For use with generation, the layer also exposes `generate_preprocess()` and `generate_postprocess()`, which are called implicitly by `keras_hub.models.BLIP2Seq2SeqLM.generate()`.

**Arguments**

*   **tokenizer**: A `keras_hub.models.BLIP2FlanT5Tokenizer` instance.
*   **image\_converter**: A `keras_hub.models.BLIP2ImageConverter` instance, or `None`. If `None`, the preprocessor operates in text-only mode.
*   **encoder\_sequence\_length**: int. The length of the packed encoder inputs. Defaults to `512`.
*   **decoder\_sequence\_length**: int. The length of the packed decoder inputs. Defaults to `512`.

**Examples**

Copied!

`preprocessor = keras_hub.models.BLIP2Seq2SeqLMPreprocessor.from_preset(     "blip2_flan_t5_xl" )  # Image + text input. preprocessor({     "images": np.random.randint(0, 256, (2, 224, 224, 3)),     "encoder_text": ["a photo of a cat", "a photo of a dog"],     "decoder_text": ["a cat sitting", "a running dog"], })  # Prepare an image and prompt for generation. preprocessor.generate_preprocess({     "images": np.random.randint(0, 256, (224, 224, 3)),     "encoder_text": "a photo of", })`

**References**

*   [Li et al., 2023](https://arxiv.org/abs/2301.12597)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`BLIP2Seq2SeqLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.BLIP2Seq2SeqLMPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.BLIP2Seq2SeqLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[BLIP2Seq2SeqLMPreprocessor layer](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm_preprocessor/#blip2seq2seqlmpreprocessor-layer)

[`BLIP2Seq2SeqLMPreprocessor` class](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm_preprocessor/#blip2seq2seqlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm_preprocessor/#frompreset-method)

[`image_converter` property](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm_preprocessor/#imageconverter-property)

[`tokenizer` property](https://keras.io/keras_hub/api/models/blip2/blip2_seq_2_seq_lm_preprocessor/#tokenizer-property)