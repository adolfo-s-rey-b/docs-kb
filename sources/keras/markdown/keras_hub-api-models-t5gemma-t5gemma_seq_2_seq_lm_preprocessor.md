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
 / [T5Gemma](https://keras.io/keras_hub/api/models/t5gemma/)
 / T5GemmaSeq2SeqLMPreprocessor layer

T5GemmaSeq2SeqLMPreprocessor layer
==================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor.py#L15)

### `T5GemmaSeq2SeqLMPreprocessor` class

Copied!

`keras_hub.models.T5GemmaSeq2SeqLMPreprocessor(     tokenizer,     encoder_sequence_length=512,     decoder_sequence_length=512,     add_start_token=False,     add_end_token=True,     **kwargs )`

T5Gemma Seq2Seq LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.T5GemmaSeq2SeqLM`](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm#t5gemmaseq2seqlm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.T5GemmaSeq2SeqLM`](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm#t5gemmaseq2seqlm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A [`keras_hub.models.T5GemmaTokenizer`](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer#t5gemmatokenizer-class)
     instance.
*   **encoder\_sequence\_length**: The length of the packed encoder inputs.
*   **decoder\_sequence\_length**: The length of the packed decoder inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. For T5Gemma models, this should be `False`. Defaults to `False`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. For T5Gemma models, this should be `True`. Defaults to `True`.

**Call arguments**

*   **x**: A dictionary with two keys, `"encoder_text"` and `"decoder_text"`. The values can be a string, a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or a list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **encoder\_sequence\_length**: Pass to override the configured `encoder_sequence_length` of the layer.
*   **decoder\_sequence\_length**: Pass to override the configured `decoder_sequence_length` of the layer.

**Examples**

Copied!

``import tensorflow as tf import numpy as np  # Load the preprocessor from a preset. preprocessor = keras_hub.models.T5GemmaSeq2SeqLMPreprocessor.from_preset(     "t5gemma_b_b_prefixlm_it" )  # For example usage, see the dictionary example below which provides # both encoder and decoder text. # Tokenize a batch of sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."]) # Tokenize a dictionary with separate encoder and decoder inputs. preprocessor({     "encoder_text": "The quick brown fox jumped.",     "decoder_text": "The fast fox." })  # Apply tokenization to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). encoder_features = tf.constant(["The quick brown fox.", "Call me Ishmael."]) decoder_features = tf.constant(["The fast fox.", "I am Ishmael."]) ds = tf.data.Dataset.from_tensor_slices(     {"encoder_text": encoder_features, "decoder_text": decoder_features} ) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Prepare tokens for generation. preprocessor.generate_preprocess({     "encoder_text": "The quick brown fox jumped.",     "decoder_text": "The fast fox." })  # Map generation outputs back to strings. preprocessor.generate_postprocess({     'decoder_token_ids': np.array([[2, 714, 4320, 8426, 25341, 1, 0, 0]]),     'decoder_padding_mask': np.array([[1, 1, 1, 1, 1, 1, 0, 0]]), })``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`T5GemmaSeq2SeqLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [t5gemma\_s\_s\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model. |
| [t5gemma\_s\_s\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model. |
| [t5gemma\_s\_s\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_s\_s\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model. |
| [t5gemma\_b\_b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model. |
| [t5gemma\_b\_b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model. |
| [t5gemma\_l\_l\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model. |
| [t5gemma\_l\_l\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model. |
| [t5gemma\_ml\_ml\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model. |
| [t5gemma\_ml\_ml\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model. |
| [t5gemma\_xl\_xl\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model. |
| [t5gemma\_xl\_xl\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_2b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_2b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_9b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_9b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor.py#L160)

### `generate_preprocess` method

Copied!

`T5GemmaSeq2SeqLMPreprocessor.generate_preprocess(     x, encoder_sequence_length=None, decoder_sequence_length=None, sequence_length=None )`

Convert input strings to integer token inputs for generation.

Similar to calling the layer for training, this method takes in a dict containing `"encoder_text"` and `"decoder_text"`, with strings or tensor strings for values, tokenizes and packs the input, and computes a padding mask masking all inputs not filled in with a padded value.

Unlike calling the layer for training, this method does not compute labels and will never append a tokenizer.end\_token\_id to the end of the decoder sequence (as generation is expected to continue at the end of the inputted decoder prompt).

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/seq_2_seq_lm_preprocessor.py#L209)

### `generate_postprocess` method

Copied!

`T5GemmaSeq2SeqLMPreprocessor.generate_postprocess(x)`

Convert integer token output to strings for generation.

This method reverses `generate_preprocess()`, by first removing all padding and start/end tokens, and then converting the integer sequence back to a string.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.T5GemmaSeq2SeqLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[T5GemmaSeq2SeqLMPreprocessor layer](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#t5gemmaseq2seqlmpreprocessor-layer)

[`T5GemmaSeq2SeqLMPreprocessor` class](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#t5gemmaseq2seqlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#frompreset-method)

[`generate_preprocess` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#generatepreprocess-method)

[`generate_postprocess` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#generatepostprocess-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor/#tokenizer-property)