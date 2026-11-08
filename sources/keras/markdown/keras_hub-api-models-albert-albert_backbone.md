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
 / [Albert](https://keras.io/keras_hub/api/models/albert/)
 / AlbertBackbone model

AlbertBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/albert/albert_backbone.py#L15)

### `AlbertBackbone` class

Copied!

`keras_hub.models.AlbertBackbone(     vocabulary_size,     num_layers,     num_heads,     embedding_dim,     hidden_dim,     intermediate_dim,     num_groups=1,     num_inner_repetitions=1,     dropout=0.0,     max_sequence_length=512,     num_segments=2,     dtype=None,     **kwargs )`

ALBERT encoder network.

This class implements a bi-directional Transformer-based encoder as described in ["ALBERT: A Lite BERT for Self-supervised Learning of Language Representations"](https://arxiv.org/abs/1909.11942)
. ALBERT is a more efficient variant of BERT, and uses parameter reduction techniques such as cross-layer parameter sharing and factorized embedding parameterization. This model class includes the embedding lookups and transformer layers, but not the masked language model or sentence order prediction heads.

The default constructor gives a fully customizable, randomly initialized ALBERT encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int, must be divisible by `num_groups`. The number of "virtual" layers, i.e., the total number of times the input sequence will be fed through the groups in one forward pass. The input will be routed to the correct group based on the layer index.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **embedding\_dim**: int. The size of the embeddings.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **num\_groups**: int. Number of groups, with each group having `num_inner_repetitions` number of `TransformerEncoder` layers.
*   **num\_inner\_repetitions**: int. Number of `TransformerEncoder` layers per group.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **num\_segments**: int. The number of types that the 'segment\_ids' input can take.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "segment_ids": np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]]),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Randomly initialized ALBERT encoder model = keras_hub.models.AlbertBackbone(     vocabulary_size=30000,     num_layers=12,     num_heads=12,     num_groups=1,     num_inner_repetitions=1,     embedding_dim=128,     hidden_dim=768,     intermediate_dim=3072,     max_sequence_length=12, ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`AlbertBackbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [albert\_base\_en\_uncased](https://www.kaggle.com/models/keras/albert/keras/albert_base_en_uncased/5) | 11.68M | 12-layer ALBERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [albert\_large\_en\_uncased](https://www.kaggle.com/models/keras/albert/keras/albert_large_en_uncased/3) | 17.68M | 24-layer ALBERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [albert\_extra\_large\_en\_uncased](https://www.kaggle.com/models/keras/albert/keras/albert_extra_large_en_uncased/3) | 58.72M | 24-layer ALBERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [albert\_extra\_extra\_large\_en\_uncased](https://www.kaggle.com/models/keras/albert/keras/albert_extra_extra_large_en_uncased/3) | 222.60M | 12-layer ALBERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.AlbertBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[AlbertBackbone model](https://keras.io/keras_hub/api/models/albert/albert_backbone/#albertbackbone-model)

[`AlbertBackbone` class](https://keras.io/keras_hub/api/models/albert/albert_backbone/#albertbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/albert/albert_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/albert/albert_backbone/#tokenembedding-property)