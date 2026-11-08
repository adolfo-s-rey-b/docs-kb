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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / TextEmbedderPreprocessor

TextEmbedderPreprocessor
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/text_embedder_preprocessor.py#L11)

### `TextEmbedderPreprocessor` class

Copied!

`keras_hub.models.TextEmbedderPreprocessor(     tokenizer, sequence_length=256, truncate="round_robin", **kwargs )`

Base class for text embedding preprocessing layers.

`TextEmbedderPreprocessor` tasks wrap a `keras_hub.tokenizer.Tokenizer` to create a preprocessing layer for text embedding tasks. It is intended to be paired with a [`keras_hub.models.TextEmbedder`](https://keras.io/keras_hub/api/base_classes/text_embedder#textembedder-class)
 task.

All `TextEmbedderPreprocessor` take inputs three ordered inputs, `x`, `y`, and `sample_weight`. `x`, the first input, should always be included. It can be a single string, a batch of strings, or a tuple of batches of string segments that should be combined into a single sequence. See examples below. `y` and `sample_weight` are optional inputs that will be passed through unaltered.

The layer will output either `x`, an `(x, y)` tuple if labels were provided, or an `(x, y, sample_weight)` tuple if labels and sample weight were provided. `x` will be a dictionary with tokenized input, the exact contents of the dictionary will depend on the model being used.

All `TextEmbedderPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for your model will be automatically instantiated.

**Examples**

Copied!

`preprocessor = keras_hub.models.TextEmbedderPreprocessor.from_preset(     "all_minilm_l6_v2_en",     sequence_length=256, # Optional. )  # Tokenize and pad/truncate a single sentence. x = "The quick brown fox jumped." x = preprocessor(x)  # Tokenize and pad/truncate a batch of sentences. x = ["The quick brown fox jumped.", "Call me Ishmael."] x = preprocessor(x)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`TextEmbedderPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

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
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |
| [gemma3\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_270m/3) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [gemma3\_instruct\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_270m/4) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only,instruction-tuned model designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [function\_gemma\_instruct\_270m](https://www.kaggle.com/models/keras/function-gemma/keras/function_gemma_instruct_270m/1) | 268.10M | A 270M Million parameter text-only model based on Gemma 3. This model is trained specifically for function calling improvements. |
| [harrier\_embedding\_oss\_270m](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_270m/1) | 268.10M | Microsoft harrier-oss-v1 270M multilingual text embedding model based on the Gemma3-270M architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 66.5 on Multilingual MTEB v2. |
| [embedding\_gemma3\_300m](https://www.kaggle.com/models/keras/embeddinggemma/keras/embedding_gemma3_300m/2) | 307.58M | Embedding-focused Gemma 3 model (300M parameters, 24 layers). |
| [gemma3\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b_text/2) | 3.88B | 4 billion parameter, 34-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b_text/3) | 3.88B | 4 billion parameter, 34-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_4b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_4b_it/1) | 4.30B | 4 billion parameter, 34-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is pre-trained for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_1.5\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_1.5_instruct_4b/1) | 4.30B | A 4 billion parameter,Instruct-tuned MedGemma 1.5 4B is an updated version of the Instruction-tuned MedGemma 4B model. |
| [gemma3\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_12b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_12b_it/1) | 12.19B | 12 billion parameter, 48-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [gemma3\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b_text/4) | 27.01B | 27 billion parameter, 62-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b_text/3) | 27.01B | 27 billion parameter, 62-layer, text-only instruction-tuned Gemma3 model. |
| [medgemma\_instruct\_27b\_text](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b_text/1) | 27.01B | A 27 billion parameter text-only model based on Gemma 3. This model is instruction-tuned (No images) for performance on medical text comprehension and is optimized for medical applications that involve a text generation component. |
| [gemma3\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_27b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_27b_it/1) | 27.43B | 27 billion parameter, 62-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_instruct\_27b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b/1) | 27.43B | A 27 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [modern\_bert\_base\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_base_en/1) | 149.01M | 22-layer ModernBERT Base encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [modern\_bert\_embed\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/modern_bert_embed_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Nomic AI (nomic-ai/modernbert-embed-base). Produces 768-dimensional, L2-normalized, mean-pooled embeddings for inputs of up to 8192 tokens. Prefix queries with 'search\_query: ' and documents with 'search\_document: '. |
| [gte\_modern\_bert\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/gte_modern_bert_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Alibaba-NLP (Alibaba-NLP/gte-modernbert-base). Produces 768-dimensional \[CLS\]-pooled embeddings that are not normalized, so compare them with cosine similarity. The model supports inputs of up to 8192 tokens. |
| [modern\_bert\_large\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_large_en/1) | 394.78M | 28-layer ModernBERT Large encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [all\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/all_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model. Maps sentences and paragraphs to 768-dimensional normalized vectors. Trained on 1B+ sentence pairs for semantic search, clustering, and similarity. |
| [nli\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/nli_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on natural language inference (NLI) data. Maps sentences to 768-dimensional dense vectors that are not normalized. Inputs are truncated to 75 tokens. |
| [paraphrase\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/paraphrase_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on paraphrase data. Maps sentences and paragraphs to 768-dimensional dense vectors that are not normalized, for paraphrase mining, clustering, and semantic search. |
| [qwen3\_embedding\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_0.6b_en/1) | 595.78M | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 1024. |
| [qwen3\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_0.6b_en/1) | 596.05M | 28-layer Qwen3 model with 596M parameters, optimized for efficiency and fast inference on resource-constrained devices. |
| [harrier\_embedding\_oss\_0.6b](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_0.6b/1) | 596.05M | Microsoft harrier-oss-v1 0.6B multilingual text embedding model based on the Qwen3-0.6B architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 69.0 on Multilingual MTEB v2. |
| [qwen3\_1.7b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_1.7b_en/1) | 1.72B | 28-layer Qwen3 model with 1.72B parameters, offering a good balance between performance and resource usage. |
| [qwen3\_embedding\_4b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_4b_en/1) | 4.02B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 2560. |
| [qwen3\_4b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_4b_en/1) | 4.02B | 36-layer Qwen3 model with 4.02B parameters, offering improved reasoning capabilities and better performance than smaller variants. |
| [qwen3\_embedding\_8b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_8b_en/1) | 8.19B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 4096. |
| [qwen3\_8b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_8b_en/1) | 8.19B | 36-layer Qwen3 model with 8.19B parameters, featuring enhanced reasoning, coding, and instruction-following capabilities. |
| [qwen3\_14b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_14b_en/1) | 14.77B | 40-layer Qwen3 model with 14.77B parameters, featuring advanced reasoning, coding, and multilingual capabilities. |
| [qwen3\_32b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_32b_en/1) | 32.76B | 64-layer Qwen3 model with 32.76B parameters, featuring state-of-the-art performance across reasoning, coding, and general language tasks. |
| [xlm\_roberta\_base\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_base_multi/3) | 277.45M | 12-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_base](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_base/1) | 277.45M | 12-layer multilingual E5 embedding model with 768-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [xlm\_roberta\_large\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_large_multi/3) | 558.84M | 24-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_large](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_large/1) | 558.84M | 24-layer multilingual E5 embedding model with 1024-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bge\_m3](https://www.kaggle.com/models/keras/bge/keras/bge_m3/1) | 566.70M | 568M-parameter multilingual text embedding model supporting 100+ languages with sequences up to 8192 tokens. Uses CLS token pooling with L2 normalization. Supports dense, sparse, and multi-vector (ColBERT-style) retrieval. From BAAI. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L254)

### `save_to_preset` method

Copied!

`TextEmbedderPreprocessor.save_to_preset(preset_dir)`

Save preprocessor to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.TextEmbedderPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[TextEmbedderPreprocessor](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#textembedderpreprocessor)

[`TextEmbedderPreprocessor` class](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#textembedderpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#frompreset-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#savetopreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#tokenizer-property)