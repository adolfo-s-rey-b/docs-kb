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
 / RobertaBackbone model

RobertaBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/roberta/roberta_backbone.py#L15)

### `RobertaBackbone` class

Copied!

`keras_hub.models.RobertaBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     dtype=None,     **kwargs )`

A RoBERTa encoder network.

This network implements a bi-directional Transformer-based encoder as described in ["RoBERTa: A Robustly Optimized BERT Pretraining Approach"](https://arxiv.org/abs/1907.11692)
. It includes the embedding lookups and transformer layers, but does not include the masked language model head used during pretraining.

The default constructor gives a fully customizable, randomly initialized RoBERTa encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/facebookresearch/fairseq)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_sequence\_length**: int. The maximum sequence length this encoder can consume. The sequence length of the input must be less than `max_sequence_length` default value. This determines the variable shape for positional embeddings.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array(         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], shape=(1, 12)), }  # Pretrained RoBERTa encoder model = keras_hub.models.RobertaBackbone.from_preset("roberta_base_en") model(input_data)  # Randomly initialized RoBERTa model with custom config model = keras_hub.models.RobertaBackbone(     vocabulary_size=50265,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`RobertaBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [roberta\_base\_en](https://www.kaggle.com/models/keras/roberta/keras/roberta_base_en/3) | 124.05M | 12-layer RoBERTa model where case is maintained.Trained on English Wikipedia, BooksCorpus, CommonCraw, and OpenWebText. |
| [roberta\_large\_en](https://www.kaggle.com/models/keras/roberta/keras/roberta_large_en/3) | 354.31M | 24-layer RoBERTa model where case is maintained.Trained on English Wikipedia, BooksCorpus, CommonCraw, and OpenWebText. |
| [xlm\_roberta\_base\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_base_multi/3) | 277.45M | 12-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_base](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_base/1) | 277.45M | 12-layer multilingual E5 embedding model with 768-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [xlm\_roberta\_large\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_large_multi/3) | 558.84M | 24-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_large](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_large/1) | 558.84M | 24-layer multilingual E5 embedding model with 1024-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bge\_m3](https://www.kaggle.com/models/keras/bge/keras/bge_m3/1) | 566.70M | 568M-parameter multilingual text embedding model supporting 100+ languages with sequences up to 8192 tokens. Uses CLS token pooling with L2 normalization. Supports dense, sparse, and multi-vector (ColBERT-style) retrieval. From BAAI. |

**Guides and examples using `from_preset`**

*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)
    

* * *

### `token_embedding` property

Copied!

`keras_hub.models.RobertaBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[RobertaBackbone model](https://keras.io/keras_hub/api/models/roberta/roberta_backbone/#robertabackbone-model)

[`RobertaBackbone` class](https://keras.io/keras_hub/api/models/roberta/roberta_backbone/#robertabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/roberta/roberta_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/roberta/roberta_backbone/#tokenembedding-property)