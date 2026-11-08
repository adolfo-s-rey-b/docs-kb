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
 / T5Gemma2Tokenizer

T5Gemma2Tokenizer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_tokenizer.py#L8)

### `T5Gemma2Tokenizer` class

Copied!

`keras_hub.tokenizers.T5Gemma2Tokenizer(proto, **kwargs)`

T5Gemma2 tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by T5Gemma2 models and provides a `from_preset()` method to automatically download a matching vocabulary for a T5Gemma2 preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto.

**Examples**

Copied!

`tokenizer = keras_hub.models.T5Gemma2Tokenizer.from_preset(     "t5gemma2_270m_270m" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`T5Gemma2Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_tokenizer.py#L8)

### `T5Gemma2Tokenizer` class

Copied!

`keras_hub.models.T5Gemma2Tokenizer(proto, **kwargs)`

T5Gemma2 tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by T5Gemma2 models and provides a `from_preset()` method to automatically download a matching vocabulary for a T5Gemma2 preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto.

**Examples**

Copied!

`tokenizer = keras_hub.models.T5Gemma2Tokenizer.from_preset(     "t5gemma2_270m_270m" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`T5Gemma2Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

[T5Gemma2Tokenizer](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer/#t5gemma2tokenizer)

[`T5Gemma2Tokenizer` class](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer/#t5gemma2tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer/#frompreset-method)

[`T5Gemma2Tokenizer` class](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer/#t5gemma2tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_tokenizer/#frompreset-method)