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
 / T5GemmaTokenizer

T5GemmaTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_tokenizer.py#L8)

### `T5GemmaTokenizer` class

Copied!

`keras_hub.tokenizers.T5GemmaTokenizer(proto, **kwargs)`

T5Gemma tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by T5Gemma models and provides a `from_preset()` method to automatically download a matching vocabulary for a T5Gemma preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`import io import tensorflow as tf import sentencepiece  # Unbatched input. tokenizer = keras_hub.models.T5GemmaTokenizer.from_preset(     "t5gemma_b_b_prefixlm_it" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. bytes_io = io.BytesIO() ds = tf.data.Dataset.from_tensor_slices(["The quick brown fox jumped."]) sentencepiece.SentencePieceTrainer.train(     sentence_iterator=ds.as_numpy_iterator(),     model_writer=bytes_io,     vocab_size=8,     model_type="WORD",     pad_id=0,     bos_id=1,     eos_id=2,     unk_id=3,     pad_piece="<pad>",     bos_piece="<bos>",     eos_piece="<eos>",     unk_piece="<unk>", ) tokenizer = keras_hub.models.T5GemmaTokenizer(     proto=bytes_io.getvalue(), ) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`T5GemmaTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

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

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_tokenizer.py#L8)

### `T5GemmaTokenizer` class

Copied!

`keras_hub.models.T5GemmaTokenizer(proto, **kwargs)`

T5Gemma tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by T5Gemma models and provides a `from_preset()` method to automatically download a matching vocabulary for a T5Gemma preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`import io import tensorflow as tf import sentencepiece  # Unbatched input. tokenizer = keras_hub.models.T5GemmaTokenizer.from_preset(     "t5gemma_b_b_prefixlm_it" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. bytes_io = io.BytesIO() ds = tf.data.Dataset.from_tensor_slices(["The quick brown fox jumped."]) sentencepiece.SentencePieceTrainer.train(     sentence_iterator=ds.as_numpy_iterator(),     model_writer=bytes_io,     vocab_size=8,     model_type="WORD",     pad_id=0,     bos_id=1,     eos_id=2,     unk_id=3,     pad_piece="<pad>",     bos_piece="<bos>",     eos_piece="<eos>",     unk_piece="<unk>", ) tokenizer = keras_hub.models.T5GemmaTokenizer(     proto=bytes_io.getvalue(), ) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`T5GemmaTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

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

[T5GemmaTokenizer](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer/#t5gemmatokenizer)

[`T5GemmaTokenizer` class](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer/#t5gemmatokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer/#frompreset-method)

[`T5GemmaTokenizer` class](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer/#t5gemmatokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_tokenizer/#frompreset-method)