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
 / [Llama](https://keras.io/keras_hub/api/models/llama/)
 / LlamaCausalLM model

LlamaCausalLM model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/llama/llama_causal_lm.py#L13)

### `LlamaCausalLM` class

Copied!

`keras_hub.models.LlamaCausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end Llama model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a LLaMA model, simply by calling `fit()`.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"top_k"` sampling will be used.

**Arguments**

*   **backbone**: A [`keras_hub.models.LlamaBackbone`](https://keras.io/keras_hub/api/models/llama/llama_backbone#llamabackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.LlamaCausalLMPreprocessor`](https://keras.io/keras_hub/api/models/llama/llama_causal_lm_preprocessor#llamacausallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`LlamaCausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [llama2\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model. |
| [llama2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model. |
| [vicuna\_1.5\_7b\_en](https://www.kaggle.com/models/keras/vicuna/keras/vicuna_1.5_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned Vicuna v1.5 model. |
| [llama2\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model with activation and weights quantized to int8. |
| [llama2\_instruct\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model with activation and weights quantized to int8. |
| [llama3.2\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_1b/1) | 1.50B | 1 billion parameter, 16-layer, instruction tuned LLaMA 3.2. |
| [llama3.2\_guard\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_guard_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model fine-tuned for consent safety classification. |
| [llama3.2\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_3b/1) | 3.61B | 3 billion parameter, 26-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_3b/1) | 3.61B | 3 billion parameter, 28-layer, instruction tuned LLaMA 3.2. |
| [llama3\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model. |
| [llama3\_instruct\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model. |
| [llama3.1\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_8b/2) | 8.03B | 8 billion parameter, 32-layer, based LLaMA 3.1 model. |
| [llama3.1\_instruct\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_instruct_8b/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3.1. |
| [llama3.1\_guard\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_guard_8b/2) | 8.03B | 8 billion parameter, 32-layer, LLaMA 3.1 fine-tuned for consent safety classification. |
| [llama3\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model with activation and weights quantized to int8. |
| [llama3\_instruct\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model with activation and weights quantized to int8. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`LlamaCausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.LlamaCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.LlamaCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[LlamaCausalLM model](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#llamacausallm-model)

[`LlamaCausalLM` class](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#llamacausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/llama/llama_causal_lm/#preprocessor-property)