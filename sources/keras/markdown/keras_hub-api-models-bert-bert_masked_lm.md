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
 / BertMaskedLM model

BertMaskedLM model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bert/bert_masked_lm.py#L13)

### `BertMaskedLM` class

Copied!

`keras_hub.models.BertMaskedLM(backbone, preprocessor=None, **kwargs)`

An end-to-end BERT model for the masked language modeling task.

This model will train BERT on a masked language modeling task. The model will predict labels for a number of masked tokens in the input data. For usage of this model with pre-trained weights, see the `from_preset()` constructor.

This model can optionally be configured with a `preprocessor` layer, in which case inputs can be raw string features during `fit()`, `predict()`, and `evaluate()`. Inputs will be tokenized and dynamically masked during training and evaluation. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **backbone**: A [`keras_hub.models.BertBackbone`](https://keras.io/keras_hub/api/models/bert/bert_backbone#bertbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.BertMaskedLMPreprocessor`](https://keras.io/keras_hub/api/models/bert/bert_masked_lm_preprocessor#bertmaskedlmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Raw string data.

Copied!

``features = ["The quick brown fox jumped.", "I forgot my homework."]  # Pretrained language model. masked_lm = keras_hub.models.BertMaskedLM.from_preset(     "bert_base_en_uncased", ) masked_lm.fit(x=features, batch_size=2)  # Re-compile (e.g., with a new learning rate). masked_lm.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5),     jit_compile=True, ) # Access backbone programmatically (e.g., to change `trainable`). masked_lm.backbone.trainable = False # Fit again. masked_lm.fit(x=features, batch_size=2)``

Preprocessed integer data.

Copied!

`# Create preprocessed batch where 0 is the mask token. features = {     "token_ids": np.array([[1, 2, 0, 4, 0, 6, 7, 8]] * 2),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1]] * 2),     "mask_positions": np.array([[2, 4]] * 2),     "segment_ids": np.array([[0, 0, 0, 0, 0, 0, 0, 0]] * 2) } # Labels are the original masked values. labels = [[3, 5]] * 2  masked_lm = keras_hub.models.BertMaskedLM.from_preset(     "bert_base_en_uncased",     preprocessor=None, ) masked_lm.fit(x=features, y=labels, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`BertMaskedLM.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

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

*   [Data Parallel Training with KerasHub and tf.distribute](https://keras.io/examples/nlp/data_parallel_training_with_keras_hub/)
    

* * *

### `backbone` property

Copied!

`keras_hub.models.BertMaskedLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.BertMaskedLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[BertMaskedLM model](https://keras.io/keras_hub/api/models/bert/bert_masked_lm/#bertmaskedlm-model)

[`BertMaskedLM` class](https://keras.io/keras_hub/api/models/bert/bert_masked_lm/#bertmaskedlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bert/bert_masked_lm/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/bert/bert_masked_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/bert/bert_masked_lm/#preprocessor-property)