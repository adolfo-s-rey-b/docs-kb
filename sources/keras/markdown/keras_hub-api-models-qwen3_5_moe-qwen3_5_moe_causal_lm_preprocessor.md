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
 / [Qwen3.5 MoE](https://keras.io/keras_hub/api/models/qwen3_5_moe/)
 / Qwen3\_5MoeCausalLMPreprocessor layer

Qwen3\_5MoeCausalLMPreprocessor layer
=====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5_moe/qwen3_5_moe_causal_lm_preprocessor.py#L13)

### `Qwen3_5MoeCausalLMPreprocessor` class

Copied!

`keras_hub.models.Qwen3_5MoeCausalLMPreprocessor(     tokenizer,     image_converter=None,     video_converter=None,     sequence_length=1024,     add_start_token=False,     add_end_token=True,     video_fps=2.0,     **kwargs )`

Qwen3.5 MoE Causal LM preprocessor with multimodal support.

Inherits all multimodal preprocessing logic from the Qwen3.5 dense preprocessor (image/video conversion, M-RoPE position IDs, vision indices, special token handling). The only differences are the `backbone_cls` and `tokenizer_cls` references.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Qwen3_5MoeCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [qwen\_agent\_world\_35b\_a3b](https://www.kaggle.com/models/keras/qwen-agentworld/keras/qwen_agent_world_35b_a3b/1) | 34.66B | 35 billion total parameter Qwen AgentWorld model with ~3 billion active parameters per token. Optimized for agentic applications and tool use. |
| [qwen3\_5\_moe\_35b\_a3b\_base](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b_base/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE base model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward for highly efficient inference. Supports text and multimodal inputs. |
| [qwen3\_5\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for chat, reasoning, coding, and multimodal tasks. |
| [qwen3\_6\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-6-moe/keras/qwen3_6_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.6 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for fast inference and extended context lengths. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Qwen3_5MoeCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Qwen3\_5MoeCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_causal_lm_preprocessor/#qwen35moecausallmpreprocessor-layer)

[`Qwen3_5MoeCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_causal_lm_preprocessor/#qwen35moecausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_causal_lm_preprocessor/#tokenizer-property)