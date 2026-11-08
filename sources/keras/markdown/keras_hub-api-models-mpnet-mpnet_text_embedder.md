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
 / [MPNet](https://keras.io/keras_hub/api/models/mpnet/)
 / MPNetTextEmbedder model

MPNetTextEmbedder model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mpnet/mpnet_text_embedder.py#L11)

### `MPNetTextEmbedder` class

Copied!

`keras_hub.models.MPNetTextEmbedder(     backbone, preprocessor=None, pooling_mode="mean", normalize=True, **kwargs )`

An end-to-end MPNet model for generating sentence embeddings.

This model attaches a pooling head, optionally followed by L2 normalization, to a [`keras_hub.models.MPNetBackbone`](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone#mpnetbackbone-class)
 instance, mapping from the backbone outputs to fixed-size sentence embeddings suitable for semantic similarity, clustering, and retrieval tasks.

This is the architecture used by sentence-transformer models such as `all-mpnet-base-v2`. For usage of this model with pre-trained weights, use the `from_preset()` constructor.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to raw inputs during `fit()`, `predict()`, and `evaluate()`. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **backbone**: A [`keras_hub.models.MPNetBackbone`](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone#mpnetbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.MPNetTextEmbedderPreprocessor`](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder_preprocessor#mpnettextembedderpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.
*   **pooling\_mode**: str. The pooling strategy to use. One of `"mean"`, `"cls"`, or `"max"`. Defaults to `"mean"`.
    *   `"mean"`: Attention-mask-aware mean pooling over all tokens.
    *   `"cls"`: Use the `<s>` (CLS) token representation.
    *   `"max"`: Max pooling over all tokens.
*   **normalize**: bool. Whether to L2 normalize the output embeddings. Defaults to `True`.

**Examples**

Raw string data.

Copied!

`embedder = keras_hub.models.MPNetTextEmbedder.from_preset(     "all_mpnet_base_v2", )  # Semantic search. query = "Which planet is known as the Red Planet?" documents = [     "Mars is often referred to as the Red Planet.",     "Venus is often called Earth's twin.", ] q_emb = embedder.encode_text(query) d_embs = embedder.encode_documents(documents) sims = embedder.similarity(q_emb, d_embs) print("Best match:", documents[sims.argmax()])`

Preprocessed integer data.

Copied!

`features = {     "token_ids": np.ones(shape=(2, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]] * 2), }  embedder = keras_hub.models.MPNetTextEmbedder.from_preset(     "all_mpnet_base_v2",     preprocessor=None, ) embeddings = embedder.predict(features)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`MPNetTextEmbedder.from_preset(preset, load_weights=True, **kwargs)`

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
| [all\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/all_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model. Maps sentences and paragraphs to 768-dimensional normalized vectors. Trained on 1B+ sentence pairs for semantic search, clustering, and similarity. |
| [nli\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/nli_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on natural language inference (NLI) data. Maps sentences to 768-dimensional dense vectors that are not normalized. Inputs are truncated to 75 tokens. |
| [paraphrase\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/paraphrase_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on paraphrase data. Maps sentences and paragraphs to 768-dimensional dense vectors that are not normalized, for paraphrase mining, clustering, and semantic search. |

* * *

### `backbone` property

Copied!

`keras_hub.models.MPNetTextEmbedder.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.MPNetTextEmbedder.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[MPNetTextEmbedder model](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder/#mpnettextembedder-model)

[`MPNetTextEmbedder` class](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder/#mpnettextembedder-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder/#preprocessor-property)