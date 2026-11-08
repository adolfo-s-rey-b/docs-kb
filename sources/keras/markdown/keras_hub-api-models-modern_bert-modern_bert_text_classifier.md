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
 / ModernBertTextClassifier model

ModernBertTextClassifier model
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_text_classifier.py#L13)

### `ModernBertTextClassifier` class

Copied!

`keras_hub.models.ModernBertTextClassifier(     backbone,     num_classes,     preprocessor=None,     activation=None,     hidden_dim=None,     dropout=0.0,     **kwargs )`

An end-to-end ModernBERT model for classification tasks.

This model attaches a classification head to a [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
 instance.

The representation of the first token is used as the sequence-level representation for classification.

**Arguments**

*   **backbone**: A [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
     instance.
*   **num\_classes**: int. Number of classes to predict.
*   **preprocessor**: A [`keras_hub.models.ModernBertTextClassifierPreprocessor`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier_preprocessor#modernberttextclassifierpreprocessor-class)
     or `None`. If `None`, inputs should already be preprocessed.
*   **activation**: Optional `str` or callable. The activation function applied to the output. Set `activation="softmax"` to return probabilities.
*   **hidden\_dim**: int. The size of the intermediate pooler layer. Defaults to the backbone hidden dimension.
*   **dropout**: float. Dropout probability applied to the pooled representation and classifier output.

**Examples**

Copied!

`import keras_hub import numpy as np  # Fine-tune from a preset. classifier = keras_hub.models.ModernBertTextClassifier.from_preset(     "modern_bert_base_en",     num_classes=2, ) classifier.fit(     x=["The quick brown fox jumped.", "Call me Ishmael."],     y=np.array([1, 0]),     batch_size=2, )  # Predict on new text. classifier.predict(["What an amazing movie!"])`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`ModernBertTextClassifier.from_preset(preset, load_weights=True, **kwargs)`

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

`keras_hub.models.ModernBertTextClassifier.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.ModernBertTextClassifier.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[ModernBertTextClassifier model](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier/#modernberttextclassifier-model)

[`ModernBertTextClassifier` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier/#modernberttextclassifier-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_text_classifier/#preprocessor-property)