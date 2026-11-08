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
 / [Qwen3.5](https://keras.io/keras_hub/api/models/qwen3_5/)
 / Qwen3\_5CausalLM model

Qwen3\_5CausalLM model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5/qwen3_5_causal_lm.py#L13)

### `Qwen3_5CausalLM` class

Copied!

`keras_hub.models.Qwen3_5CausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end Qwen3.5 model for causal language modeling.

This model predicts the next token based on previous tokens using the Qwen3.5 hybrid architecture (full attention + GatedDeltaNet linear attention layers). It optionally supports multimodal (image + text) inputs when the backbone has a `vision_encoder` attached.

This model has a `generate()` method for autoregressive text generation.

**Arguments**

*   **backbone**: A `[`keras\_hub.models.Qwen3\_5Backbone`](/keras_hub/api/models/qwen3_5/qwen3_5_backbone#qwen35backbone-class)` instance.
*   **preprocessor**: A `[`keras\_hub.models.Qwen3\_5CausalLMPreprocessor`](/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm_preprocessor#qwen35causallmpreprocessor-class)` or `None`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`Qwen3_5CausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [qwen3\_5\_0.8b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_0.8b_base/1) | 852.99M | Ultra-lightweight foundation model. Ideal for edge devices and efficient, task-specific fine-tuning. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_0.8b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_0.8b/1) | 852.99M | Instruction-tuned ultra-lightweight model. Best for simple chat and basic NLP tasks on resource-constrained devices. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_2b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_2b_base/1) | 2.21B | Lightweight foundation model. Balances speed and capability; great for mobile deployment and domain-specific fine-tuning. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_2b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_2b/1) | 2.21B | Instruction-tuned lightweight model. Optimized for fast chat applications and general assistance on consumer hardware. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_4b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_4b_base/1) | 4.54B | Mid-small foundation model. Offers improved reasoning and context understanding for custom fine-tuning tasks. |
| [qwen3\_5\_4b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_4b/1) | 4.54B | Instruction-tuned mid-small model. A capable assistant for general text generation and conversational tasks on standard GPUs. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_9b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_9b_base/1) | 9.41B | Mid-sized foundation model. Delivers strong reasoning, coding, and math baseline capabilities for advanced fine-tuning. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_9b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_9b/1) | 9.41B | Instruction-tuned mid-sized model. Highly capable chatbot offering strong logic, coding assistance, and multi-lingual support. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_27b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_27b/1) | 27.36B | Instruction-tuned large model. Delivers high-tier performance for complex reasoning, coding, and extensive contextual tasks. Supports Multimodal, video processing tasks. |
| [qwen3\_6\_27b](https://www.kaggle.com/models/keras/qwen3-6/keras/qwen3_6_27b/1) | 27.36B | Instruction-tuned 27B model. Delivers highly efficient, top-tier performance for complex reasoning, advanced coding, and extensive multilingual tasks. Optimized for fast inference and extended context lengths. |
| [qwen3\_8\_27b](https://www.kaggle.com/models/keras/qwen3-8/keras/qwen3_8_27b/1) | 27.36B | Qwen3.8-27B — instruction-tuned 27B dense vision-language model. Built on the Qwen3.5 foundation with substantial gains in coding, professional and research tasks, and long-horizon agentic workflows. Native image and video understanding. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`Qwen3_5CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.Qwen3_5CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.Qwen3_5CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[Qwen3\_5CausalLM model](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#qwen35causallm-model)

[`Qwen3_5CausalLM` class](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#qwen35causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_causal_lm/#preprocessor-property)