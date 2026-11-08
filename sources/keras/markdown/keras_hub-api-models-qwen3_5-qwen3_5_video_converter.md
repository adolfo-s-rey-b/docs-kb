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
 / Qwen3\_5VideoConverter

Qwen3\_5VideoConverter
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5/qwen3_5_video_converter.py#L17)

### `Qwen3_5VideoConverter` class

Copied!

`keras_hub.layers.Qwen3_5VideoConverter(     patch_size=16,     temporal_patch_size=2,     spatial_merge_size=2,     min_pixels=65536,     max_pixels=16777216,     interpolation="bicubic",     antialias=True,     **kwargs )`

Video pre-processor for Qwen3.5.

Converts videos to the patch tensor format expected by `Qwen3_5VisionEncoder` and also returns `grid_thw` metadata.

**Arguments**

*   **patch\_size**: int. Spatial size of each patch in pixels. Default 16.
*   **temporal\_patch\_size**: int. Frames grouped per temporal patch. Default 2.
*   **spatial\_merge\_size**: int. Spatial merge downsampling factor. Default 2.
*   **min\_pixels**: int. Minimum pixel budget for the resized frames. Frames smaller than this will be upscaled. Default 65536.
*   **max\_pixels**: int. Maximum pixel budget. Frames larger than this will be downscaled. Default 16777216 (= 4096×4096).
*   **interpolation**: str. Interpolation method for resizing. Defaults to `"bicubic"`.
*   **antialias**: bool. Whether to apply antialiasing when resizing. Defaults to `True`.
*   **scale**: float or list of floats. Per-channel scale for normalisation.
*   **offset**: float or list of floats. Per-channel offset for normalisation.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/video_converter.py#L35)

### `from_preset` method

Copied!

`Qwen3_5VideoConverter.from_preset(preset, **kwargs)`

Instantiate a `keras_hub.layers.VideoConverter` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'gemma4_2b_it'`
2.  a Kaggle Models handle like `'kaggle://user/gemma4/keras/gemma4_2b_it'`
3.  a Hugging Face handle like `'hf://google/gemma-4-2b-it'`
4.  a path to a local preset directory like `'./gemma4_2b_it'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.VideoConverter.from_preset()`, or from a model class like `keras_hub.models.Gemma4VideoConverter.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a video converter from a preset. converter = keras_hub.layers.VideoConverter.from_preset(     "hf://google/gemma-4-2b-it" )`

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
| [qwen\_agent\_world\_35b\_a3b](https://www.kaggle.com/models/keras/qwen-agentworld/keras/qwen_agent_world_35b_a3b/1) | 34.66B | 35 billion total parameter Qwen AgentWorld model with ~3 billion active parameters per token. Optimized for agentic applications and tool use. |
| [qwen3\_5\_moe\_35b\_a3b\_base](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b_base/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE base model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward for highly efficient inference. Supports text and multimodal inputs. |
| [qwen3\_5\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for chat, reasoning, coding, and multimodal tasks. |
| [qwen3\_6\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-6-moe/keras/qwen3_6_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.6 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for fast inference and extended context lengths. |

* * *

[Qwen3\_5VideoConverter](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_video_converter/#qwen35videoconverter)

[`Qwen3_5VideoConverter` class](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_video_converter/#qwen35videoconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_video_converter/#frompreset-method)