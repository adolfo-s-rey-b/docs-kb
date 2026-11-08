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
 / [FNet](https://keras.io/keras_hub/api/models/f_net/)
 / FNetMaskedLM model

FNetMaskedLM model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/f_net/f_net_masked_lm.py#L13)

### `FNetMaskedLM` class

Copied!

`keras_hub.models.FNetMaskedLM(backbone, preprocessor=None, **kwargs)`

An end-to-end FNet model for the masked language modeling task.

This model will train FNet on a masked language modeling task. The model will predict labels for a number of masked tokens in the input data. For usage of this model with pre-trained weights, see the `from_preset()` constructor.

This model can optionally be configured with a `preprocessor` layer, in which case inputs can be raw string features during `fit()`, `predict()`, and `evaluate()`. Inputs will be tokenized and dynamically masked during training and evaluation. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **backbone**: A [`keras_hub.models.FNetBackbone`](https://keras.io/keras_hub/api/models/f_net/f_net_backbone#fnetbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.FNetMaskedLMPreprocessor`](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm_preprocessor#fnetmaskedlmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Raw string data.

Copied!

``features = ["The quick brown fox jumped.", "I forgot my homework."]  # Pretrained language model. masked_lm = keras_hub.models.FNetMaskedLM.from_preset(     "f_net_base_en", ) masked_lm.fit(x=features, batch_size=2)  # Re-compile (e.g., with a new learning rate). masked_lm.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5),     jit_compile=True, ) # Access backbone programmatically (e.g., to change `trainable`). masked_lm.backbone.trainable = False # Fit again. masked_lm.fit(x=features, batch_size=2)``

Preprocessed integer data.

Copied!

`# Create a preprocessed dataset where 0 is the mask token. features = {     "token_ids": np.array([[1, 2, 0, 4, 0, 6, 7, 8]] * 2),     "segment_ids": np.array([[0, 0, 0, 1, 1, 1, 0, 0]] * 2),     "mask_positions": np.array([[2, 4]] * 2) } # Labels are the original masked values. labels = [[3, 5]] * 2  masked_lm = keras_hub.models.FNetMaskedLM.from_preset(     "f_net_base_en",     preprocessor=None, ) masked_lm.fit(x=features, y=labels, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`FNetMaskedLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [f\_net\_base\_en](https://www.kaggle.com/models/keras/f_net/keras/f_net_base_en/3) | 82.86M | 12-layer FNet model where case is maintained. Trained on the C4 dataset. |
| [f\_net\_large\_en](https://www.kaggle.com/models/keras/f_net/keras/f_net_large_en/3) | 236.95M | 24-layer FNet model where case is maintained. Trained on the C4 dataset. |

* * *

### `backbone` property

Copied!

`keras_hub.models.FNetMaskedLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.FNetMaskedLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[FNetMaskedLM model](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm/#fnetmaskedlm-model)

[`FNetMaskedLM` class](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm/#fnetmaskedlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/f_net/f_net_masked_lm/#preprocessor-property)