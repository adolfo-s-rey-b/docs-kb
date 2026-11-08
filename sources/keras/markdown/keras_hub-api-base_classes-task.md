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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / Task

Task
====

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L21)

### `Task` class

Copied!

`keras_hub.models.Task(*args, compile=True, **kwargs)`

Base class for all Task models.

A `Task` wraps a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be directly used for training, fine-tuning, and prediction for a given text problem.

All `Task` models have `backbone` and `preprocessor` properties. By default `fit()`, `predict()` and `evaluate()` will preprocess all inputs automatically. To preprocess inputs separately or with a custom function, you can set `task.preprocessor = None`, which disable any automatic preprocessing on inputs.

All `Task` classes include a `from_preset()` constructor which can be used to load a pre-trained config and weights. Calling `from_preset()` on a task will automatically instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
.

**Arguments**

*   **compile**: boolean, defaults to `True`. If `True` will compile the model with default parameters on construction. Model can still be recompiled with a new loss, optimizer and metrics before training.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`Task.from_preset(preset, load_weights=True, **kwargs)`

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

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L271)

### `save_to_preset` method

Copied!

`Task.save_to_preset(preset_dir, max_shard_size=10)`

Save task to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `10`.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.Task.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

### `backbone` property

Copied!

`keras_hub.models.Task.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[Task](https://keras.io/keras_hub/api/base_classes/task/#task)

[`Task` class](https://keras.io/keras_hub/api/base_classes/task/#task-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/task/#frompreset-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/task/#savetopreset-method)

[`preprocessor` property](https://keras.io/keras_hub/api/base_classes/task/#preprocessor-property)

[`backbone` property](https://keras.io/keras_hub/api/base_classes/task/#backbone-property)