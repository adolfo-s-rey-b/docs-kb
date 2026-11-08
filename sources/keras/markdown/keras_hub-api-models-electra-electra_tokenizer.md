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
 / [Electra](https://keras.io/keras_hub/api/models/electra/)
 / ElectraTokenizer

ElectraTokenizer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/electra/electra_tokenizer.py#L6)

### `ElectraTokenizer` class

Copied!

`keras_hub.tokenizers.ElectraTokenizer(vocabulary, lowercase=False, **kwargs)`

A ELECTRA tokenizer using WordPiece subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.WordPieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer#wordpiecetokenizer-class)
.

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

`# Custom Vocabulary. vocab = ["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"] vocab += ["The", "quick", "brown", "fox", "jumped", "."]  # Instantiate the tokenizer. tokenizer = keras_hub.models.ElectraTokenizer(vocabulary=vocab)  # Unbatched input. tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`ElectraTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [electra\_small\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_small_discriminator_uncased_en/2) | 13.55M | 12-layer small ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_small\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_small_generator_uncased_en/2) | 13.55M | 12-layer small ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_base\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_base_generator_uncased_en/2) | 33.58M | 12-layer base ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_large\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_large_generator_uncased_en/2) | 51.07M | 24-layer large ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_base\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_base_discriminator_uncased_en/2) | 109.48M | 12-layer base ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_large\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_large_discriminator_uncased_en/2) | 335.14M | 24-layer large ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |

* * *

[ElectraTokenizer](https://keras.io/keras_hub/api/models/electra/electra_tokenizer/#electratokenizer)

[`ElectraTokenizer` class](https://keras.io/keras_hub/api/models/electra/electra_tokenizer/#electratokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/electra/electra_tokenizer/#frompreset-method)