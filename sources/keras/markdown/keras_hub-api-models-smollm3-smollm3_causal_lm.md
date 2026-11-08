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
 / [SmolLM3](https://keras.io/keras_hub/api/models/smollm3/)
 / SmolLM3CausalLM model

SmolLM3CausalLM model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smollm3/smollm3_causal_lm.py#L13)

### `SmolLM3CausalLM` class

Copied!

`keras_hub.models.SmolLM3CausalLM(backbone, preprocessor=None, **kwargs)`

Base class for generative language modeling tasks.

`CausalLM` tasks wrap a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for generation and generative fine-tuning.

`CausalLM` tasks provide an additional, high-level `generate()` function which can be used to auto-regressively sample a model token by token with a string in, string out signature. The `compile()` method of all `CausalLM` classes contains an additional `sampler` argument, which can be used to pass a [`keras_hub.samplers.Sampler`](https://keras.io/keras_hub/api/samplers/samplers#sampler-class)
 to control how the predicted distribution will be sampled.

When calling `fit()`, the tokenized input will be predicted token-by-token with a causal mask applied, which gives both a pre-training and supervised fine-tuning setup for controlling inference-time generation.

All `CausalLM` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.

**Example**

Copied!

`# Load a GPT2 backbone with pre-trained weights. causal_lm = keras_hub.models.CausalLM.from_preset(     "gpt2_base_en", ) causal_lm.compile(sampler="top_k") causal_lm.generate("Keras is a", max_length=64)  # Load a Mistral instruction tuned checkpoint at bfloat16 precision. causal_lm = keras_hub.models.CausalLM.from_preset(     "mistral_instruct_7b_en",     dtype="bfloat16", ) causal_lm.compile(sampler="greedy") causal_lm.generate("Keras is a", max_length=64)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`SmolLM3CausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [smollm3\_3b\_en](https://www.kaggle.com/models/keras/smollm3/keras/smollm3_3b_en/1) | 3.08B | Dense decoder-only model has 3 billion total parameters, built on 36 layers and utilizes 16 query and 4 key/value attention heads. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`SmolLM3CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

Generate text given prompt `inputs`.

This method generates text based on given `inputs`. The sampling method used for generation can be set via the `compile()` method.

If `inputs` are a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, outputs will be generated "batch-by-batch" and concatenated. Otherwise, all inputs will be handled as a single batch.

If a `preprocessor` is attached to the model, `inputs` will be preprocessed inside the `generate()` function and should match the structure expected by the `preprocessor` layer (usually raw strings). If a `preprocessor` is not attached, inputs should match the structure expected by the `backbone`. See the example usage above for a demonstration of each.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . If a `preprocessor` is attached to the model, `inputs` should match the structure expected by the `preprocessor` layer. If a `preprocessor` is not attached, `inputs` should match the structure expected the `backbone` model.
*   **max\_length**: Optional. int. The max length of the generated sequence. Will default to the max configured `sequence_length` of the `preprocessor`. If `preprocessor` is `None`, `inputs` should be should be padded to the desired maximum length and this argument will be ignored.
*   **stop\_token\_ids**: Optional. `None`, "auto", or tuple of token ids. Defaults to "auto" which uses the `preprocessor.tokenizer.end_token_id`. Not specifying a processor will produce an error. None stops generation after generating `max_length` tokens. You may also specify a list of token id's the model should stop on. Note that sequences of tokens will each be interpreted as a stop token, multi-token stop sequences are not supported.
*   **strip\_prompt**: Optional. By default, generate() returns the full prompt followed by its completion generated by the model. If this option is set to True, only the newly generated text is returned.

* * *

### `backbone` property

Copied!

`keras_hub.models.SmolLM3CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.SmolLM3CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[SmolLM3CausalLM model](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#smollm3causallm-model)

[`SmolLM3CausalLM` class](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#smollm3causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/smollm3/smollm3_causal_lm/#preprocessor-property)