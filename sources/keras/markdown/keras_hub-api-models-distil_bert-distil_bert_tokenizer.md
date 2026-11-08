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
 / [DistilBert](https://keras.io/keras_hub/api/models/distil_bert/)
 / DistilBertTokenizer

DistilBertTokenizer
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/distil_bert/distil_bert_tokenizer.py#L8)

### `DistilBertTokenizer` class

Copied!

`keras_hub.tokenizers.DistilBertTokenizer(vocabulary, lowercase=False, **kwargs)`

A DistilBERT tokenizer using WordPiece subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.WordPieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer#wordpiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by DistilBERT models and provides a `from_preset()` method to automatically download a matching vocabulary for a DistilBERT preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: A list of strings or a string filename path. If passing a list, each element of the list should be a single word piece token string. If passing a filename, the file should be a plain text file containing a single word piece token per line.
*   **lowercase**: If `True`, the input text will be first lowered before tokenization.
*   **special\_tokens\_in\_strings**: bool. A bool to indicate if the tokenizer should expect special tokens in input strings that should be tokenized and mapped correctly to their ids. Defaults to False.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.DistilBertTokenizer.from_preset(     "distil_bert_base_en_uncased", ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. vocab = ["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"] vocab += ["The", "quick", "brown", "fox", "jumped", "."] tokenizer = keras_hub.models.DistilBertTokenizer(vocabulary=vocab) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`DistilBertTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [distil\_bert\_base\_en](https://www.kaggle.com/models/keras/distil_bert/keras/distil_bert_base_en/3) | 65.19M | 6-layer DistilBERT model where case is maintained. Trained on English Wikipedia + BooksCorpus using BERT as the teacher model. |
| [distil\_bert\_base\_en\_uncased](https://www.kaggle.com/models/keras/distil_bert/keras/distil_bert_base_en_uncased/3) | 66.36M | 6-layer DistilBERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus using BERT as the teacher model. |
| [distil\_bert\_base\_multi](https://www.kaggle.com/models/keras/distil_bert/keras/distil_bert_base_multi/3) | 134.73M | 6-layer DistilBERT model where case is maintained. Trained on Wikipedias of 104 languages |

* * *

[DistilBertTokenizer](https://keras.io/keras_hub/api/models/distil_bert/distil_bert_tokenizer/#distilberttokenizer)

[`DistilBertTokenizer` class](https://keras.io/keras_hub/api/models/distil_bert/distil_bert_tokenizer/#distilberttokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/distil_bert/distil_bert_tokenizer/#frompreset-method)