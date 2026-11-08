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
 / [ModernBERT](https://keras.io/keras_hub/api/models/modern_bert/)
 / ModernBertTextEmbedderPreprocessor layer

ModernBertTextEmbedderPreprocessor layer
========================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_text_embedder_preprocessor.py#L13)

### `ModernBertTextEmbedderPreprocessor` class

Copied!

`keras_hub.models.ModernBertTextEmbedderPreprocessor(     tokenizer, sequence_length=256, truncate="round_robin", **kwargs )`

A ModernBERT preprocessing layer which tokenizes and packs inputs for sentence embedding.

This preprocessing layer will do three things:

1.  Tokenize any number of input segments using the `tokenizer`.
2.  Pack the inputs together using a [`keras_hub.layers.MultiSegmentPacker`](https://keras.io/keras_hub/api/preprocessing_layers/multi_segment_packer#multisegmentpacker-class)
     with the appropriate `"[CLS]"`, `"[SEP]"` and `"[PAD]"` tokens, i.e., adding a single `"[CLS]"` at the start of the entire sequence and a `"[SEP]"` at the end of each segment. This matches the Hugging Face ModernBERT template: `[CLS] A [SEP]` for single inputs and `[CLS] A [SEP] B [SEP]` for pairs.
3.  Construct a dictionary with keys `"token_ids"` and `"padding_mask"` that can be passed directly to a ModernBERT text embedder. ModernBERT has no segment embeddings, so no `"segment_ids"` are returned.

This layer can be used directly with [`tf.data.Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
 to preprocess string data in the `(x, y, sample_weight)` format used by [`keras.Model.fit`](https://keras.io/api/models/model_training_apis#fit-method)
.

**Arguments**

*   **tokenizer**: A `keras_hub.models.ModernBertTokenizer` instance.
*   **sequence\_length**: int. The length of the packed inputs. Defaults to `256`. When loading from a Hugging Face sentence-transformers checkpoint, this is overridden by the length sentence-transformers uses: `max_seq_length` from `sentence_bert_config.json` (e.g. `8192` for `nomic-ai/modernbert-embed-base`), or otherwise the model's maximum length (e.g. `8192` for `Alibaba-NLP/gte-modernbert-base`). Every input is padded to this length, so for faster inference on short texts, pass a smaller `sequence_length` to this class's `from_preset()` or set the `sequence_length` attribute after loading.
*   **truncate**: string. The algorithm to truncate a list of batched segments to fit within `sequence_length`. The value can be either `round_robin` or `waterfall`:
    *   `"round_robin"`: Available space is assigned one token at a time in a round-robin fashion to the inputs that still need some, until the limit is reached.
    *   `"waterfall"`: The allocation of the budget is done using a "waterfall" algorithm that allocates quota in a left-to-right manner and fills up the buckets until we run out of budget. It supports an arbitrary number of segments.

**Call arguments**

*   **x**: A tensor of single string sequences, or a tuple of multiple tensor sequences to be packed together. Inputs may be batched or unbatched. For single sequences, raw python inputs will be converted to tensors. For multiple sequences, pass tensors directly.
*   **y**: Any label data. Will be passed through unaltered.
*   **sample\_weight**: Any label weight data. Will be passed through unaltered.

**Examples**

Directly calling the layer on data.

Copied!

`preprocessor = (     keras_hub.models.ModernBertTextEmbedderPreprocessor.from_preset(         "hf://nomic-ai/modernbert-embed-base",         sequence_length=128,     ) )  # Tokenize and pack a single sentence. preprocessor("search_query: What is TSNE?")  # Tokenize a batch of single sentences. preprocessor([     "search_query: What is TSNE?",     "search_document: TSNE is a dimensionality reduction algorithm.", ])`

Mapping with [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

Copied!

`preprocessor = (     keras_hub.models.ModernBertTextEmbedderPreprocessor.from_preset(         "hf://nomic-ai/modernbert-embed-base",         sequence_length=128,     ) )  first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."])  # Map unlabeled single sentences. ds = tf.data.Dataset.from_tensor_slices(first) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`ModernBertTextEmbedderPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [modern\_bert\_base\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_base_en/1) | 149.01M | 22-layer ModernBERT Base encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [modern\_bert\_embed\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/modern_bert_embed_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Nomic AI (nomic-ai/modernbert-embed-base). Produces 768-dimensional, L2-normalized, mean-pooled embeddings for inputs of up to 8192 tokens. Prefix queries with 'search\_query: ' and documents with 'search\_document: '. |
| [gte\_modern\_bert\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/gte_modern_bert_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Alibaba-NLP (Alibaba-NLP/gte-modernbert-base). Produces 768-dimensional \[CLS\]-pooled embeddings that are not normalized, so compare them with cosine similarity. The model supports inputs of up to 8192 tokens. |
| [modern\_bert\_large\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_large_en/1) | 394.78M | 28-layer ModernBERT Large encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.ModernBertTextEmbedderPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[ModernBertTextEmbedderPreprocessor layer](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder_preprocessor/#modernberttextembedderpreprocessor-layer)

[`ModernBertTextEmbedderPreprocessor` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder_preprocessor/#modernberttextembedderpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder_preprocessor/#tokenizer-property)