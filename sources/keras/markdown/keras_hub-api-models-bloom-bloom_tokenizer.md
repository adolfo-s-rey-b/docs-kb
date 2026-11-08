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
 / [Bloom](https://keras.io/keras_hub/api/models/bloom/)
 / BloomTokenizer

BloomTokenizer
==============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bloom/bloom_tokenizer.py#L6)

### `BloomTokenizer` class

Copied!

`keras_hub.tokenizers.BloomTokenizer(vocabulary=None, merges=None, **kwargs)`

A BLOOM tokenizer using Byte-Pair Encoding subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by BLOOM models and provides a `from_preset()` method to automatically download a matching vocabulary for a BLOOM preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: string or dict, maps token to integer ids. If it is a string, it should be the file path to a json file.
*   **merges**: string or list, contains the merge rule. If it is a string, it should be the file path to merge rules. The merge rule file should have one merge rule per line. Every merge rule contains merge entities separated by a space.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.BloomTokenizer.from_preset("bloom_560m_multi") tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. vocab = {"<s>": 0, "</s>": 1, "<pad>": 2, "a": 3, "Ġquick": 4, "Ġfox": 5} merges = ["Ġ q", "u i", "c k", "ui ck", "Ġq uick"] merges += ["Ġ f", "o x", "Ġf ox"] tokenizer = keras_hub.models.BloomTokenizer(vocabulary=vocab, merges=merges) tokenizer("a quick fox.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`BloomTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [bloom\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_560m_multi/4) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_560m_multi/2) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. finetuned on crosslingual task mixture (xP3) dataset. |

* * *

[BloomTokenizer](https://keras.io/keras_hub/api/models/bloom/bloom_tokenizer/#bloomtokenizer)

[`BloomTokenizer` class](https://keras.io/keras_hub/api/models/bloom/bloom_tokenizer/#bloomtokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bloom/bloom_tokenizer/#frompreset-method)