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
 / Qwen3\_5MoeTokenizer

Qwen3\_5MoeTokenizer
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5_moe/qwen3_5_moe_tokenizer.py#L8)

### `Qwen3_5MoeTokenizer` class

Copied!

`keras_hub.models.Qwen3_5MoeTokenizer(     vocabulary=None, merges=None, has_vision_tokens=True, **kwargs )`

Tokenizer for Qwen3.5 MoE models.

This tokenizer implements byte-pair encoding (BPE) for Qwen3.5 MoE models.

**Arguments**

*   **vocabulary**: Dictionary mapping tokens to token IDs, or path to vocabulary file.
*   **merges**: List of BPE merges, or path to merges file.
*   **has\_vision\_tokens**: bool. Whether to register vision-related special tokens. Default `True`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`Qwen3_5MoeTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

| Preset | Parameters | Description |
| --- | --- | --- |
| [qwen\_agent\_world\_35b\_a3b](https://www.kaggle.com/models/keras/qwen-agentworld/keras/qwen_agent_world_35b_a3b/1) | 34.66B | 35 billion total parameter Qwen AgentWorld model with ~3 billion active parameters per token. Optimized for agentic applications and tool use. |
| [qwen3\_5\_moe\_35b\_a3b\_base](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b_base/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE base model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward for highly efficient inference. Supports text and multimodal inputs. |
| [qwen3\_5\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for chat, reasoning, coding, and multimodal tasks. |
| [qwen3\_6\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-6-moe/keras/qwen3_6_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.6 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for fast inference and extended context lengths. |

* * *

[Qwen3\_5MoeTokenizer](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_tokenizer/#qwen35moetokenizer)

[`Qwen3_5MoeTokenizer` class](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_tokenizer/#qwen35moetokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_tokenizer/#frompreset-method)