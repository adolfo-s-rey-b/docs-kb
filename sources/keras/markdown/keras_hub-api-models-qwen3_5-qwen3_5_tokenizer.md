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
 / Qwen3\_5Tokenizer

Qwen3\_5Tokenizer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5/qwen3_5_tokenizer.py#L6)

### `Qwen3_5Tokenizer` class

Copied!

`keras_hub.models.Qwen3_5Tokenizer(     vocabulary=None, merges=None, has_vision_tokens=True, **kwargs )`

Tokenizer for Qwen3.5 models.

This tokenizer implements byte-pair encoding (BPE) for Qwen3.5 models.

**Arguments**

*   **vocabulary**: Dictionary mapping tokens to token IDs, or path to vocabulary file.
*   **merges**: List of BPE merges, or path to merges file.
*   **has\_vision\_tokens**: bool. Whether to register vision-related special tokens. Default `True`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`Qwen3_5Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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

[Qwen3\_5Tokenizer](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_tokenizer/#qwen35tokenizer)

[`Qwen3_5Tokenizer` class](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_tokenizer/#qwen35tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_tokenizer/#frompreset-method)