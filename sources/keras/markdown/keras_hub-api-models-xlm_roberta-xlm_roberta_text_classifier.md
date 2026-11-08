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
 / XLMRobertaTextClassifier model

XLMRobertaTextClassifier model
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/xlm_roberta/xlm_roberta_text_classifier.py#L16)

### `XLMRobertaTextClassifier` class

Copied!

`keras_hub.models.XLMRobertaTextClassifier(     backbone,     num_classes,     preprocessor=None,     activation=None,     hidden_dim=None,     dropout=0.0,     **kwargs )`

An end-to-end XLM-RoBERTa model for classification tasks.

This model attaches a classification head to a `keras_hub.model.XLMRobertaBackbone` instance, mapping from the backbone outputs to logits suitable for a classification task. For usage of this model with pre-trained weights, see the `from_preset()` constructor.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to raw inputs during `fit()`, `predict()`, and `evaluate()`. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/facebookresearch/fairseq)
.

**Arguments**

*   **backbone**: A [`keras_hub.models.XLMRobertaBackbone`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_backbone#xlmrobertabackbone-class)
     instance.
*   **num\_classes**: int. Number of classes to predict.
*   **preprocessor**: A [`keras_hub.models.XLMRobertaTextClassifierPreprocessor`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier_preprocessor#xlmrobertatextclassifierpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.
*   **activation**: Optional `str` or callable. The activation function to use on the model outputs. Set `activation="softmax"` to return output probabilities. Defaults to `None`.
*   **hidden\_dim**: int. The size of the pooler layer.
*   **dropout**: float. The dropout probability value, applied to the pooled output, and after the first dense layer.

**Examples**

Raw string data.

Copied!

``features = ["The quick brown fox jumped.", "نسيت الواجب"] labels = [0, 3]  # Pretrained classifier. classifier = keras_hub.models.XLMRobertaTextClassifier.from_preset(     "xlm_roberta_base_multi",     num_classes=4, ) classifier.fit(x=features, y=labels, batch_size=2) classifier.predict(x=features, batch_size=2)  # Re-compile (e.g., with a new learning rate). classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5),     jit_compile=True, ) # Access backbone programmatically (e.g., to change `trainable`). classifier.backbone.trainable = False # Fit again. classifier.fit(x=features, y=labels, batch_size=2)``

Preprocessed integer data.

Copied!

`features = {     "token_ids": np.ones(shape=(2, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]] * 2), } labels = [0, 3]  # Pretrained classifier without preprocessing. classifier = keras_hub.models.XLMRobertaTextClassifier.from_preset(     "xlm_roberta_base_multi",     num_classes=4,     preprocessor=None, ) classifier.fit(x=features, y=labels, batch_size=2)`

Custom backbone and vocabulary.

Copied!

`features = ["The quick brown fox jumped.", "نسيت الواجب"] labels = [0, 3]  def train_sentencepiece(ds, vocab_size):     bytes_io = io.BytesIO()     sentencepiece.SentencePieceTrainer.train(         sentence_iterator=ds.as_numpy_iterator(),         model_writer=bytes_io,         vocab_size=vocab_size,         model_type="WORD",         unk_id=0,         bos_id=1,         eos_id=2,     )     return bytes_io.getvalue() ds = tf.data.Dataset.from_tensor_slices(     ["the quick brown fox", "the earth is round"] ) proto = train_sentencepiece(ds, vocab_size=10) tokenizer = keras_hub.models.XLMRobertaTokenizer(     proto=proto ) preprocessor = keras_hub.models.XLMRobertaTextClassifierPreprocessor(     tokenizer,     sequence_length=128, ) backbone = keras_hub.models.XLMRobertaBackbone(     vocabulary_size=250002,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) classifier = keras_hub.models.XLMRobertaTextClassifier(     backbone=backbone,     preprocessor=preprocessor,     num_classes=4, ) classifier.fit(x=features, y=labels, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`XLMRobertaTextClassifier.from_preset(preset, load_weights=True, **kwargs)`

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

`keras_hub.models.XLMRobertaTextClassifier.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.XLMRobertaTextClassifier.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[XLMRobertaTextClassifier model](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier/#xlmrobertatextclassifier-model)

[`XLMRobertaTextClassifier` class](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier/#xlmrobertatextclassifier-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_text_classifier/#preprocessor-property)