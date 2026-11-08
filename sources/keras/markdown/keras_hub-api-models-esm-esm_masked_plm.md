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
 / [ESM](https://keras.io/keras_hub/api/models/esm/)
 / ESMMaskedPLM model

ESMMaskedPLM model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/esm/esm_masked_plm.py#L13)

### `ESMMaskedPLM` class

Copied!

`keras_hub.models.ESMMaskedPLM(backbone, preprocessor=None, **kwargs)`

An end-to-end ESM2 model for the masked protein language modeling task.

This model will train ESM2 on a masked protein language modeling task. The model will predict labels for a number of masked tokens in the input data. For usage of this model with pre-trained weights, see the `from_preset()` method.

This model can optionally be configured with a `preprocessor` layer, in which case inputs can be raw string features during `fit()`, `predict()`, and `evaluate()`. Inputs will be tokenized and dynamically masked during training and evaluation. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **backbone**: A `keras_hub.models.ESM2Backbone` instance.
*   **preprocessor**: A `keras_hub.models.ESM2MaskedPLMPreprocessor` or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Raw string data.

Copied!

``features = ["The quick brown fox jumped.", "I forgot my homework."]  # Pretrained protein language model. masked_lm = keras_hub.models.ESM2MaskedPLM.from_preset(     "hf://facebook/esm2_t6_8M_UR50D", ) masked_lm.fit(x=features, batch_size=2)  # Re-compile (e.g., with a new learning rate). masked_lm.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5),     jit_compile=True, ) # Access backbone programmatically (e.g., to change `trainable`). masked_lm.backbone.trainable = False # Fit again. masked_lm.fit(x=features, batch_size=2)``

Preprocessed integer data.

Copied!

`# Create a preprocessed dataset where 0 is the mask token. features = {     "token_ids": np.array([[1, 2, 0, 4, 0, 6, 7, 8]] * 2),     "mask_positions": np.array([[2, 4]] * 2) } # Labels are the original masked values. labels = [[3, 5]] * 2  masked_lm = keras_hub.models.ESM2MaskedPLM.from_preset(     'hf://facebook/esm2_t6_8M_UR50D',     preprocessor=None, )  masked_lm.fit(x=features, y=labels, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`ESMMaskedPLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [esm2\_t6\_8M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t6_8M/1) | 7.41M | 6 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t12\_35M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t12_35M/1) | 33.27M | 12 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t30\_150M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t30_150M/1) | 147.73M | 30 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t33\_650M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t33_650M/1) | 649.40M | 33 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |

* * *

### `backbone` property

Copied!

`keras_hub.models.ESMMaskedPLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.ESMMaskedPLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[ESMMaskedPLM model](https://keras.io/keras_hub/api/models/esm/esm_masked_plm/#esmmaskedplm-model)

[`ESMMaskedPLM` class](https://keras.io/keras_hub/api/models/esm/esm_masked_plm/#esmmaskedplm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/esm/esm_masked_plm/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/esm/esm_masked_plm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/esm/esm_masked_plm/#preprocessor-property)