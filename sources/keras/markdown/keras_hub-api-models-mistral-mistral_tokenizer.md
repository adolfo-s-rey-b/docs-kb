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
 / [Mistral](https://keras.io/keras_hub/api/models/mistral/)
 / MistralTokenizer

MistralTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral/mistral_tokenizer.py#L23)

### `MistralTokenizer` class

Copied!

`keras_hub.tokenizers.MistralTokenizer(proto, **kwargs)`

Mistral tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by Mistral models and provides a `from_preset()` method to automatically download a matching vocabulary for a Mistral preset.

This tokenizer is used by SentencePiece-based Mistral presets. Presets that ship a Tekken (byte-level BPE) vocabulary, such as Magistral, use [`keras_hub.tokenizers.MistralTekkenTokenizer`](https://keras.io/keras_hub/api/models/mistral/mistral_tekken_tokenizer#mistraltekkentokenizer-class)
 instead.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.MistralTokenizer.from_preset(     "mistral_7b_en", ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

**Guides and examples using `MistralTokenizer`**

*   [Function Calling with KerasHub models](https://keras.io/keras_hub/guides/function_calling_with_keras_hub/)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MistralTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [mistral\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_7b_en/8) | 7.24B | Mistral 7B base model |
| [mistral\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_instruct_7b_en/8) | 7.24B | Mistral 7B instruct model |
| [mistral\_0.2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.2_instruct_7b_en/3) | 7.24B | Mistral 7B instruct version 0.2 model |
| [mistral\_0.3\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_7b_en/1) | 7.25B | Mistral 7B base version 0.3 model |
| [mistral\_0.3\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_instruct_7b_en/1) | 7.25B | Mistral 7B instruct version 0.3 model |
| [magistral\_small\_2506\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2506_en/1) | 23.57B | Magistral Small 2506 model |
| [magistral\_small\_2507\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2507_en/1) | 23.57B | Magistral Small 2507 model |

**Guides and examples using `from_preset`**

*   [Function Calling with KerasHub models](https://keras.io/keras_hub/guides/function_calling_with_keras_hub/)
    

* * *

[MistralTokenizer](https://keras.io/keras_hub/api/models/mistral/mistral_tokenizer/#mistraltokenizer)

[`MistralTokenizer` class](https://keras.io/keras_hub/api/models/mistral/mistral_tokenizer/#mistraltokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral/mistral_tokenizer/#frompreset-method)