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
 / [XLMRoberta](https://keras.io/keras_hub/api/models/xlm_roberta/)
 / XLMRobertaMaskedLM model

XLMRobertaMaskedLM model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/xlm_roberta/xlm_roberta_masked_lm.py#L17)

### `XLMRobertaMaskedLM` class

Copied!

`keras_hub.models.XLMRobertaMaskedLM(backbone, preprocessor=None, **kwargs)`

An end-to-end XLM-RoBERTa model for the masked language modeling task.

This model will train XLM-RoBERTa on a masked language modeling task. The model will predict labels for a number of masked tokens in the input data. For usage of this model with pre-trained weights, see the `from_preset()` method.

This model can optionally be configured with a `preprocessor` layer, in which case inputs can be raw string features during `fit()`, `predict()`, and `evaluate()`. Inputs will be tokenized and dynamically masked during training and evaluation. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/facebookresearch/fairseq)
.

**Arguments**

*   **backbone**: A [`keras_hub.models.XLMRobertaBackbone`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_backbone#xlmrobertabackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.XLMRobertaMaskedLMPreprocessor`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor#xlmrobertamaskedlmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Raw string inputs and pretrained backbone.

Copied!

`# Create a dataset with raw string features. Labels are inferred. features = ["The quick brown fox jumped.", "I forgot my homework."]  # Pretrained language model # on an MLM task. masked_lm = keras_hub.models.XLMRobertaMaskedLM.from_preset(     "xlm_roberta_base_multi", ) masked_lm.fit(x=features, batch_size=2)`

**Re-compile (e.g., with a new learning rate)**

.

masked\_lm.compile( loss=keras.losses.SparseCategoricalCrossentropy(from\_logits=True), optimizer=keras.optimizers.Adam(5e-5), jit\_compile=True, ) **Access backbone programmatically (e.g., to change `trainable`)**

.

masked\_lm.backbone.trainable = False **Fit again**

.

masked\_lm.fit(x=features, batch\_size=2)

Copied!

`Preprocessed integer data. ```python __Create a preprocessed dataset where 0 is the mask token__  .  features = {     "token_ids": np.array([[1, 2, 0, 4, 0, 6, 7, 8]] * 2),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1]] * 2),     "mask_positions": np.array([[2, 4]] * 2) } __Labels are the original masked values__  .  labels = [[3, 5]] * 2  masked_lm = keras_hub.models.XLMRobertaMaskedLM.from_preset(     "xlm_roberta_base_multi",     preprocessor=None, )  masked_lm.fit(x=features, y=labels, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`XLMRobertaMaskedLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [xlm\_roberta\_base\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_base_multi/3) | 277.45M | 12-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_base](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_base/1) | 277.45M | 12-layer multilingual E5 embedding model with 768-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [xlm\_roberta\_large\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_large_multi/3) | 558.84M | 24-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_large](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_large/1) | 558.84M | 24-layer multilingual E5 embedding model with 1024-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bge\_m3](https://www.kaggle.com/models/keras/bge/keras/bge_m3/1) | 566.70M | 568M-parameter multilingual text embedding model supporting 100+ languages with sequences up to 8192 tokens. Uses CLS token pooling with L2 normalization. Supports dense, sparse, and multi-vector (ColBERT-style) retrieval. From BAAI. |

* * *

### `backbone` property

Copied!

`keras_hub.models.XLMRobertaMaskedLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.XLMRobertaMaskedLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[XLMRobertaMaskedLM model](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm/#xlmrobertamaskedlm-model)

[`XLMRobertaMaskedLM` class](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm/#xlmrobertamaskedlm-class)

[Load a Gemma generative task.](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm/#load-a-gemma-generative-task)

[Load a Bert classification task.](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm/#load-a-bert-classification-task)