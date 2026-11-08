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
 / [EmbeddingGemma2](https://keras.io/keras_hub/api/models/embedding_gemma2/)
 / EmbeddingGemma2TextEmbedder model

EmbeddingGemma2TextEmbedder model
=================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_text_embedder.py#L14)

### `EmbeddingGemma2TextEmbedder` class

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedder(     backbone, preprocessor=None, pooling_mode="mean", normalize=True, **kwargs )`

An end-to-end EmbeddingGemma2 model for generating sentence embeddings.

This model attaches a mean-pooling and L2 normalization head to an `EmbeddingGemma2Backbone` instance, mapping from the backbone outputs to fixed-size sentence embeddings suitable for semantic similarity, clustering, and retrieval tasks.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to raw inputs during `fit()`, `predict()`, and `evaluate()`. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **backbone**: An [`keras_hub.models.EmbeddingGemma2Backbone`](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone#embeddinggemma2backbone-class)
     instance.
*   **preprocessor**: An [`keras_hub.models.EmbeddingGemma2TextEmbedderPreprocessor`](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder_preprocessor#embeddinggemma2textembedderpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.
*   **pooling\_mode**: string. Kept for configuration compatibility with other embedders. Only `"mean"` is supported. Defaults to `"mean"`.
*   **normalize**: bool. Whether to L2 normalize the output embeddings. Defaults to `True`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`EmbeddingGemma2TextEmbedder.from_preset(preset, load_weights=True, **kwargs)`

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
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

### `backbone` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedder.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.EmbeddingGemma2TextEmbedder.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[EmbeddingGemma2TextEmbedder model](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder/#embeddinggemma2textembedder-model)

[`EmbeddingGemma2TextEmbedder` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder/#embeddinggemma2textembedder-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder/#preprocessor-property)