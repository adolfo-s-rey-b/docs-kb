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
 / ModernBertMaskedLM model

ModernBertMaskedLM model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_masked_lm.py#L13)

### `ModernBertMaskedLM` class

Copied!

`keras_hub.models.ModernBertMaskedLM(     backbone, preprocessor=None, dtype=None, **kwargs )`

ModernBERT Masked LM task model.

The Masked LM model provides a prediction head for the Masked Language Modeling task. It is composed of a [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
 and a prediction head which projects the backbone's hidden states back to the vocabulary space.

This model can be used for pre-training or fine-tuning on a specific corpus.

**Arguments**

*   **backbone**: A [`keras_hub.models.ModernBertBackbone`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone#modernbertbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.ModernBertMaskedLMPreprocessor`](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm_preprocessor#modernbertmaskedlmpreprocessor-class)
     instance or `None`. If `None`, this model will not handle input preprocessing automatically during `fit()`, `predict()`, or `evaluate()`.
*   **dtype**: string or `keras.DTypePolicy`. The precision policy used for the model's computations and weights. If `None`, defaults to the backbone's dtype policy.

**Examples**

Copied!

`import keras_hub import numpy as np  # Pre-trained backbone and preprocessor tokenizer = keras_hub.models.ModernBertTokenizer(     vocabulary="vocab.json",     merges="merges.txt", ) preprocessor = keras_hub.models.ModernBertMaskedLMPreprocessor(     tokenizer=tokenizer,     sequence_length=128, ) backbone = keras_hub.models.ModernBertBackbone(     vocabulary_size=50368,     hidden_dim=768,     intermediate_dim=1152,     num_layers=22,     num_heads=12, )  # Instantiate the MaskedLM task model masked_lm = keras_hub.models.ModernBertMaskedLM(     backbone=backbone,     preprocessor=preprocessor, )  # Predict on raw text strings raw_data = ["The quick brown fox [MASK] over the lazy dog."] predictions = masked_lm.predict(raw_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`ModernBertMaskedLM.from_preset(preset, load_weights=True, **kwargs)`

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

`keras_hub.models.ModernBertMaskedLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.ModernBertMaskedLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[ModernBertMaskedLM model](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm/#modernbertmaskedlm-model)

[`ModernBertMaskedLM` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm/#modernbertmaskedlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm/#preprocessor-property)