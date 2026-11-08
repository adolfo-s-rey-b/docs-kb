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
 / ModernBertTextEmbedder model

ModernBertTextEmbedder model
============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_text_embedder.py#L13)

### `ModernBertTextEmbedder` class

Copied!

`keras_hub.models.ModernBertTextEmbedder(     backbone, preprocessor=None, pooling_mode="mean", normalize=True, **kwargs )`

An end-to-end ModernBERT model for generating sentence embeddings.

This model attaches a pooling and optional L2 normalization head to a [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
 instance, mapping from the backbone outputs to fixed-size sentence embeddings suitable for semantic similarity, clustering, and retrieval tasks.

This is the architecture used by ModernBERT-based sentence-transformer models such as `nomic-ai/modernbert-embed-base` (mean pooling with L2 normalization) and `Alibaba-NLP/gte-modernbert-base` (`[CLS]` pooling without normalization). When loading a Hugging Face sentence-transformers checkpoint with `from_preset()`, the pooling strategy, normalization, and sequence length are read from the checkpoint's sentence-transformers config files.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to raw inputs during `fit()`, `predict()`, and `evaluate()`. This is done by default when creating the model with `from_preset()`.

Task prefixes (prompts) are not added automatically. Some checkpoints expect them on their inputs, e.g. `nomic-ai/modernbert-embed-base` expects `"search_query: "` on queries and `"search_document: "` on documents. Prepend them to the input strings yourself, as the examples below do. Without them, the embeddings are silently worse.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **backbone**: A [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.ModernBertTextEmbedderPreprocessor`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder_preprocessor#modernberttextembedderpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.
*   **pooling\_mode**: str. The pooling strategy to use. One of `"mean"`, `"cls"`, or `"max"`. Defaults to `"mean"`.
    *   `"mean"`: Attention-mask-aware mean pooling over all tokens.
    *   `"cls"`: Use the `[CLS]` token representation.
    *   `"max"`: Max pooling over all tokens, ignoring padding.
*   **normalize**: bool. Whether to L2 normalize the output embeddings. Defaults to `True`.

**Examples**

Raw string data.

Copied!

``# Inputs are padded to the checkpoint's 8192-token limit by default. # Load the preprocessor with a shorter length for faster inference on # short texts. On an already loaded model, setting # `embedder.preprocessor.sequence_length = 512` works too. preprocessor = (     keras_hub.models.ModernBertTextEmbedderPreprocessor.from_preset(         "hf://nomic-ai/modernbert-embed-base",         sequence_length=512,     ) ) embedder = keras_hub.models.ModernBertTextEmbedder.from_preset(     "hf://nomic-ai/modernbert-embed-base",     preprocessor=preprocessor, )  # Semantic search. This checkpoint expects task prefixes, which are not # added for you. query = "search_query: Which planet is known as the Red Planet?" documents = [     "search_document: Mars is often referred to as the Red Planet.",     "search_document: Venus is often called Earth's twin.", ] q_emb = embedder.encode_text(query) d_embs = embedder.encode_documents(documents) sims = embedder.similarity(q_emb, d_embs) print("Best match:", documents[ops.convert_to_numpy(sims).argmax()])``

Preprocessed integer data.

Copied!

`features = {     "token_ids": np.ones(shape=(2, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]] * 2), }  embedder = keras_hub.models.ModernBertTextEmbedder.from_preset(     "hf://nomic-ai/modernbert-embed-base",     preprocessor=None, ) embeddings = embedder.predict(features)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`ModernBertTextEmbedder.from_preset(preset, load_weights=True, **kwargs)`

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
| [modern\_bert\_base\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_base_en/1) | 149.01M | 22-layer ModernBERT Base encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [modern\_bert\_embed\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/modern_bert_embed_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Nomic AI (nomic-ai/modernbert-embed-base). Produces 768-dimensional, L2-normalized, mean-pooled embeddings for inputs of up to 8192 tokens. Prefix queries with 'search\_query: ' and documents with 'search\_document: '. |
| [gte\_modern\_bert\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/gte_modern_bert_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Alibaba-NLP (Alibaba-NLP/gte-modernbert-base). Produces 768-dimensional \[CLS\]-pooled embeddings that are not normalized, so compare them with cosine similarity. The model supports inputs of up to 8192 tokens. |
| [modern\_bert\_large\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_large_en/1) | 394.78M | 28-layer ModernBERT Large encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |

* * *

### `backbone` property

Copied!

`keras_hub.models.ModernBertTextEmbedder.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.ModernBertTextEmbedder.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[ModernBertTextEmbedder model](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder/#modernberttextembedder-model)

[`ModernBertTextEmbedder` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder/#modernberttextembedder-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_embedder/#preprocessor-property)