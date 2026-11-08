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
 / ElectraBackbone model

ElectraBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/electra/electra_backbone.py#L15)

### `ElectraBackbone` class

Copied!

`keras_hub.models.ElectraBackbone(     vocab_size,     num_layers,     num_heads,     hidden_dim,     embedding_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     num_segments=2,     dtype=None,     **kwargs )`

A Electra encoder network.

This network implements a bidirectional Transformer-based encoder as described in ["Electra: Pre-training Text Encoders as Discriminators Rather Than Generators"](https://arxiv.org/abs/2003.10555)
. It includes the embedding lookups and transformer layers, but not the masked language model or classification task networks.

The default constructor gives a fully customizable, randomly initialized ELECTRA encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://huggingface.co/docs/transformers/model_doc/electra#overview)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **embedding\_dim**: int. The size of the token embeddings.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

`input_data = { "token_ids": np.ones(shape=(1, 12), dtype="int32"), "segment_ids": np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]]), "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pre-trained ELECTRA encoder. model = keras_hub.models.ElectraBackbone.from_preset(     "electra_base_discriminator_en" ) model(input_data)  # Randomly initialized Electra encoder backbone = keras_hub.models.ElectraBackbone(     vocabulary_size=1000,     num_layers=2,     num_heads=2,     hidden_dim=32,     intermediate_dim=64,     dropout=0.1,     max_sequence_length=512,     ) # Returns sequence and pooled outputs. sequence_output, pooled_output = backbone(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`ElectraBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [electra\_small\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_small_discriminator_uncased_en/2) | 13.55M | 12-layer small ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_small\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_small_generator_uncased_en/2) | 13.55M | 12-layer small ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_base\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_base_generator_uncased_en/2) | 33.58M | 12-layer base ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_large\_generator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_large_generator_uncased_en/2) | 51.07M | 24-layer large ELECTRA generator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_base\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_base_discriminator_uncased_en/2) | 109.48M | 12-layer base ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |
| [electra\_large\_discriminator\_uncased\_en](https://www.kaggle.com/models/keras/electra/keras/electra_large_discriminator_uncased_en/2) | 335.14M | 24-layer large ELECTRA discriminator model. All inputs are lowercased. Trained on English Wikipedia + BooksCorpus. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.ElectraBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[ElectraBackbone model](https://keras.io/keras_hub/api/models/electra/electra_backbone/#electrabackbone-model)

[`ElectraBackbone` class](https://keras.io/keras_hub/api/models/electra/electra_backbone/#electrabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/electra/electra_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/electra/electra_backbone/#tokenembedding-property)