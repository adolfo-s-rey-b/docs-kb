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
 / [Roberta](https://keras.io/keras_hub/api/models/roberta/)
 / RobertaTokenizer

RobertaTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/roberta/roberta_tokenizer.py#L6)

### `RobertaTokenizer` class

Copied!

`keras_hub.tokenizers.RobertaTokenizer(vocabulary=None, merges=None, **kwargs)`

A RoBERTa tokenizer using Byte-Pair Encoding subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by RoBERTa models and provides a `from_preset()` method to automatically download a matching vocabulary for a RoBERTa preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: A dictionary mapping tokens to integer ids, or file path to a json file containing the token to id mapping.
*   **merges**: A list of merge rules or a string file path, If passing a file path. the file should have one merge rule per line. Every merge rule contains merge entities separated by a space.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.RobertaTokenizer.from_preset(     "roberta_base_en", ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. # Note: 'Ġ' is space vocab = {"<s>": 0, "<pad>": 1, "</s>": 2, "<mask>": 3} vocab = {**vocab, "a": 4, "Ġquick": 5, "Ġfox": 6} merges = ["Ġ q", "u i", "c k", "ui ck", "Ġq uick"] merges += ["Ġ f", "o x", "Ġf ox"] tokenizer = keras_hub.models.RobertaTokenizer(     vocabulary=vocab,     merges=merges ) tokenizer(["a quick fox", "a fox quick"])`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`RobertaTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [roberta\_base\_en](https://www.kaggle.com/models/keras/roberta/keras/roberta_base_en/3) | 124.05M | 12-layer RoBERTa model where case is maintained.Trained on English Wikipedia, BooksCorpus, CommonCraw, and OpenWebText. |
| [roberta\_large\_en](https://www.kaggle.com/models/keras/roberta/keras/roberta_large_en/3) | 354.31M | 24-layer RoBERTa model where case is maintained.Trained on English Wikipedia, BooksCorpus, CommonCraw, and OpenWebText. |
| [xlm\_roberta\_base\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_base_multi/3) | 277.45M | 12-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_base](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_base/1) | 277.45M | 12-layer multilingual E5 embedding model with 768-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [xlm\_roberta\_large\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_large_multi/3) | 558.84M | 24-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_large](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_large/1) | 558.84M | 24-layer multilingual E5 embedding model with 1024-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bge\_m3](https://www.kaggle.com/models/keras/bge/keras/bge_m3/1) | 566.70M | 568M-parameter multilingual text embedding model supporting 100+ languages with sequences up to 8192 tokens. Uses CLS token pooling with L2 normalization. Supports dense, sparse, and multi-vector (ColBERT-style) retrieval. From BAAI. |

* * *

[RobertaTokenizer](https://keras.io/keras_hub/api/models/roberta/roberta_tokenizer/#robertatokenizer)

[`RobertaTokenizer` class](https://keras.io/keras_hub/api/models/roberta/roberta_tokenizer/#robertatokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/roberta/roberta_tokenizer/#frompreset-method)