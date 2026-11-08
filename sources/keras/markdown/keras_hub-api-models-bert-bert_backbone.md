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
 / [Bert](https://keras.io/keras_hub/api/models/bert/)
 / BertBackbone model

BertBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bert/bert_backbone.py#L15)

### `BertBackbone` class

Copied!

`keras_hub.models.BertBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     num_segments=2,     dtype=None,     **kwargs )`

A BERT encoder network.

This class implements a bi-directional Transformer-based encoder as described in ["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"](https://arxiv.org/abs/1810.04805)
. It includes the embedding lookups and transformer layers, but not the masked language model or next sentence prediction heads.

The default constructor gives a fully customizable, randomly initialized BERT encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden\_dim must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **num\_segments**: int. The number of types that the 'segment\_ids' input can take.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "segment_ids": np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]]),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained BERT encoder. model = keras_hub.models.BertBackbone.from_preset("bert_base_en_uncased") model(input_data)  # Randomly initialized BERT encoder with a custom config. model = keras_hub.models.BertBackbone(     vocabulary_size=30552,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`BertBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [bert\_tiny\_en\_uncased](https://www.kaggle.com/models/keras/bert/keras/bert_tiny_en_uncased/3) | 4.39M | 2-layer BERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [bert\_tiny\_en\_uncased\_sst2](https://www.kaggle.com/models/keras/bert/keras/bert_tiny_en_uncased_sst2/5) | 4.39M | The bert\_tiny\_en\_uncased backbone model fine-tuned on the SST-2 sentiment analysis dataset. |
| [paraphrase\_minilm\_l3\_v2\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/paraphrase_minilm_l3_v2_en/1) | 17.07M | 3-layer MiniLM model for paraphrase detection. Ultra-fast with 384-dimensional sentence embeddings. |
| [all\_minilm\_l6\_v2\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/all_minilm_l6_v2_en/1) | 22.71M | 6-layer MiniLM sentence embedding model. Maps sentences to 384-dimensional dense vectors. Trained on 1B+ sentence pairs for semantic similarity, search, and clustering. |
| [all\_minilm\_l6\_v1\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/all_minilm_l6_v1_en/1) | 22.71M | 6-layer MiniLM sentence embedding model (v1). Maps sentences to 384-dimensional dense vectors. |
| [paraphrase\_minilm\_l6\_v2\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/paraphrase_minilm_l6_v2_en/1) | 22.71M | 6-layer MiniLM model for paraphrase detection. Fast with 384-dimensional sentence embeddings. |
| [multi\_qa\_minilm\_l6\_cos\_v1\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/multi_qa_minilm_l6_cos_v1_en/1) | 22.71M | 6-layer MiniLM model for semantic search with cosine similarity. Trained on 215M QA pairs. |
| [multi\_qa\_minilm\_l6\_dot\_v1\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/multi_qa_minilm_l6_dot_v1_en/1) | 22.71M | 6-layer MiniLM model for semantic search with dot-product similarity. Trained on 215M QA pairs. |
| [msmarco\_minilm\_l6\_cos\_v5\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/msmarco_minilm_l6_cos_v5_en/1) | 22.71M | 6-layer MiniLM model for information retrieval with cosine similarity. Trained on MS MARCO passage ranking. |
| [bge\_small\_v1.5\_zh](https://www.kaggle.com/models/keras/bge/keras/bge_small_v1.5_zh/1) | 23.95M | 12-layer BGE small Chinese embedding model (v1.5). Maps sentences to 384-dimensional L2-normalized dense vectors. Optimized for dense retrieval on Chinese text. |
| [mxbai\_embed\_xsmall\_v1\_en](https://www.kaggle.com/models/keras/mxbai-embed/keras/mxbai_embed_xsmall_v1_en/1) | 24.09M | 6-layer BERT sentence embedding model by mixedbread-ai. Maps sentences to 384-dimensional dense vectors using mean pooling. Compact model for fast inference. |
| [bert\_small\_en\_uncased](https://www.kaggle.com/models/keras/bert/keras/bert_small_en_uncased/3) | 28.76M | 4-layer BERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [all\_minilm\_l12\_v2\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/all_minilm_l12_v2_en/1) | 33.36M | 12-layer MiniLM sentence embedding model. Maps sentences to 384-dimensional dense vectors. Higher accuracy than the L6 variant with moderate speed tradeoff. |
| [paraphrase\_minilm\_l12\_v2\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/paraphrase_minilm_l12_v2_en/1) | 33.36M | 12-layer MiniLM model for paraphrase detection with 384-dimensional sentence embeddings. |
| [msmarco\_minilm\_l12\_cos\_v5\_en](https://www.kaggle.com/models/keras/sentence-transformers/keras/msmarco_minilm_l12_cos_v5_en/1) | 33.36M | 12-layer MiniLM model for information retrieval with cosine similarity. Trained on MS MARCO passage ranking. |
| [bge\_small\_en](https://www.kaggle.com/models/keras/bge/keras/bge_small_en/1) | 33.36M | 12-layer BGE small English embedding model (v1). Maps sentences to 384-dimensional L2-normalized dense vectors. Optimized for dense retrieval and semantic similarity. |
| [bge\_small\_v1.5\_en](https://www.kaggle.com/models/keras/bge/keras/bge_small_v1.5_en/1) | 33.36M | 12-layer BGE small English embedding model (v1.5). Maps sentences to 384-dimensional L2-normalized dense vectors. Optimized for dense retrieval and semantic similarity. |
| [bert\_medium\_en\_uncased](https://www.kaggle.com/models/keras/bert/keras/bert_medium_en_uncased/3) | 41.37M | 8-layer BERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [bert\_base\_zh](https://www.kaggle.com/models/keras/bert/keras/bert_base_zh/3) | 102.27M | 12-layer BERT model. Trained on Chinese Wikipedia. |
| [bge\_base\_zh](https://www.kaggle.com/models/keras/bge/keras/bge_base_zh/1) | 102.27M | 12-layer BGE base Chinese embedding model (v1). Maps sentences to 768-dimensional L2-normalized dense vectors. Optimized for dense retrieval on Chinese text. |
| [bge\_base\_v1.5\_zh](https://www.kaggle.com/models/keras/bge/keras/bge_base_v1.5_zh/1) | 102.27M | 12-layer BGE base Chinese embedding model (v1.5). Maps sentences to 768-dimensional L2-normalized dense vectors. Optimized for dense retrieval on Chinese text. |
| [bert\_base\_en](https://www.kaggle.com/models/keras/bert/keras/bert_base_en/3) | 108.31M | 12-layer BERT model where case is maintained. Trained on English Wikipedia + BooksCorpus. |
| [bert\_base\_en\_uncased](https://www.kaggle.com/models/keras/bert/keras/bert_base_en_uncased/3) | 109.48M | 12-layer BERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [bge\_base\_en](https://www.kaggle.com/models/keras/bge/keras/bge_base_en/1) | 109.48M | 12-layer BGE base English embedding model (v1). Maps sentences to 768-dimensional L2-normalized dense vectors. Optimized for dense retrieval and semantic similarity. |
| [bge\_base\_v1.5\_en](https://www.kaggle.com/models/keras/bge/keras/bge_base_v1.5_en/1) | 109.48M | 12-layer BGE base English embedding model (v1.5). Maps sentences to 768-dimensional L2-normalized dense vectors. Optimized for dense retrieval and semantic similarity. |
| [bge\_llm\_embedder](https://www.kaggle.com/models/keras/bge/keras/bge_llm_embedder/1) | 109.48M | BGE-LLM-Embedder: 12-layer embedding model for retrieval-augmented language model applications. Maps text to 768-dimensional dense vectors and supports knowledge, memory, demonstration, and tool retrieval tasks. |
| [multilingual\_e5\_small](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_small/1) | 117.65M | 12-layer multilingual E5 embedding model with 384-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bert\_base\_multi](https://www.kaggle.com/models/keras/bert/keras/bert_base_multi/3) | 177.85M | 12-layer BERT model where case is maintained. Trained on trained on Wikipedias of 104 languages |
| [bge\_large\_zh](https://www.kaggle.com/models/keras/bge/keras/bge_large_zh/1) | 325.52M | 24-layer BGE large Chinese embedding model (v1). Maps sentences to 1024-dimensional L2-normalized dense vectors. Highest accuracy in the BGE Chinese v1 family. |
| [bge\_large\_v1.5\_zh](https://www.kaggle.com/models/keras/bge/keras/bge_large_v1.5_zh/1) | 325.52M | 24-layer BGE large Chinese embedding model (v1.5). Maps sentences to 1024-dimensional L2-normalized dense vectors. Highest accuracy in the BGE Chinese v1.5 family. |
| [bert\_large\_en](https://www.kaggle.com/models/keras/bert/keras/bert_large_en/3) | 333.58M | 24-layer BERT model where case is maintained. Trained on English Wikipedia + BooksCorpus. |
| [bert\_large\_en\_uncased](https://www.kaggle.com/models/keras/bert/keras/bert_large_en_uncased/3) | 335.14M | 24-layer BERT model where all input is lowercased. Trained on English Wikipedia + BooksCorpus. |
| [bge\_large\_en](https://www.kaggle.com/models/keras/bge/keras/bge_large_en/1) | 335.14M | 24-layer BGE large English embedding model (v1). Maps sentences to 1024-dimensional L2-normalized dense vectors. Highest accuracy in the BGE English v1 family. |
| [bge\_large\_v1.5\_en](https://www.kaggle.com/models/keras/bge/keras/bge_large_v1.5_en/1) | 335.14M | 24-layer BGE large English embedding model (v1.5). Maps sentences to 1024-dimensional L2-normalized dense vectors. Highest accuracy in the BGE English family. |
| [mxbai\_embed\_large\_v1\_en](https://www.kaggle.com/models/keras/mxbai-embed/keras/mxbai_embed_large_v1_en/1) | 335.14M | 24-layer BERT sentence embedding model by mixedbread-ai. Maps sentences to 1024-dimensional dense vectors using CLS pooling. Trained for semantic similarity, search, and clustering tasks. |
| [mxbai\_embed\_2d\_large\_v1\_en](https://www.kaggle.com/models/keras/mxbai-embed/keras/mxbai_embed_2d_large_v1_en/1) | 335.14M | 24-layer BERT sentence embedding model by mixedbread-ai with 2D Matryoshka representation learning. Maps sentences to 1024-dimensional dense vectors using CLS pooling. Supports flexible truncation of both layers and dimensions. |

**Guides and examples using `from_preset`**

*   [Multimodal entailment](https://keras.io/examples/nlp/multimodal_entailment/)
    

* * *

### `token_embedding` property

Copied!

`keras_hub.models.BertBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[BertBackbone model](https://keras.io/keras_hub/api/models/bert/bert_backbone/#bertbackbone-model)

[`BertBackbone` class](https://keras.io/keras_hub/api/models/bert/bert_backbone/#bertbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bert/bert_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/bert/bert_backbone/#tokenembedding-property)