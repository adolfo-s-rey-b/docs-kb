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
 / [T5Gemma2](https://keras.io/keras_hub/api/models/t5gemma2/)
 / T5Gemma2Seq2SeqLMPreprocessor layer

T5Gemma2Seq2SeqLMPreprocessor layer
===================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor.py#L20)

### `T5Gemma2Seq2SeqLMPreprocessor` class

Copied!

`keras_hub.models.T5Gemma2Seq2SeqLMPreprocessor(     tokenizer,     encoder_sequence_length=512,     decoder_sequence_length=512,     image_converter=None,     image_size=None,     num_vision_tokens_per_image=None,     add_start_token=False,     add_end_token=True,     **kwargs )`

T5Gemma2 Seq2Seq LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.T5Gemma2Seq2SeqLM`](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm#t5gemma2seq2seqlm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.T5Gemma2Seq2SeqLM`](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm#t5gemma2seq2seqlm-class)
 instance, these methods will be called implicitly in `generate()`.

When an `image_converter` is provided, the preprocessor also supports multimodal inputs with images. Images are inserted into the encoder sequence as placeholder tokens that the backbone's vision encoder will replace with image embeddings.

**Arguments**

*   **tokenizer**: A [`keras_hub.models.T5Gemma2Tokenizer`](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer#t5gemma2tokenizer-class)
     instance.
*   **encoder\_sequence\_length**: The length of the packed encoder inputs.
*   **decoder\_sequence\_length**: The length of the packed decoder inputs.
*   **image\_converter**: A [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
     instance, or `None` for text-only. Defaults to `None`.
*   **add\_start\_token**: If `True`, prepend the start token. Defaults to `False`.
*   **add\_end\_token**: If `True`, append the end token. Defaults to `True`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`T5Gemma2Seq2SeqLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor.py#L232)

### `generate_preprocess` method

Copied!

`T5Gemma2Seq2SeqLMPreprocessor.generate_preprocess(     x, encoder_sequence_length=None, decoder_sequence_length=None, sequence_length=None )`

Convert input strings to integer token inputs for generation.

Similar to calling the layer for training, this method takes in a dict containing `"encoder_text"` and `"decoder_text"`, with strings or tensor strings for values, tokenizes and packs the input, and computes a padding mask masking all inputs not filled in with a padded value.

Unlike calling the layer for training, this method does not compute labels and will never append a tokenizer.end\_token\_id to the end of the decoder sequence (as generation is expected to continue at the end of the inputted decoder prompt).

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/seq_2_seq_lm_preprocessor.py#L209)

### `generate_postprocess` method

Copied!

`T5Gemma2Seq2SeqLMPreprocessor.generate_postprocess(x)`

Convert integer token output to strings for generation.

This method reverses `generate_preprocess()`, by first removing all padding and start/end tokens, and then converting the integer sequence back to a string.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.T5Gemma2Seq2SeqLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[T5Gemma2Seq2SeqLMPreprocessor layer](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#t5gemma2seq2seqlmpreprocessor-layer)

[`T5Gemma2Seq2SeqLMPreprocessor` class](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#t5gemma2seq2seqlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#frompreset-method)

[`generate_preprocess` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#generatepreprocess-method)

[`generate_postprocess` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#generatepostprocess-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor/#tokenizer-property)