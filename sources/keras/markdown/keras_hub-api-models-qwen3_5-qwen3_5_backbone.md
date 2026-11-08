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
 / Qwen3\_5Backbone model

Qwen3\_5Backbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5/qwen3_5_backbone.py#L54)

### `Qwen3_5Backbone` class

Copied!

`keras_hub.models.Qwen3_5Backbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     head_dim,     hidden_dim,     intermediate_dim,     layer_types=None,     partial_rotary_factor=0.25,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     dropout=0.0,     tie_word_embeddings=False,     sliding_window_size=32768,     linear_num_key_heads=16,     linear_num_value_heads=32,     linear_key_head_dim=128,     linear_value_head_dim=128,     linear_conv_kernel_dim=4,     vision_encoder=None,     mrope_section=None,     dtype=None,     **kwargs )`

The Qwen3.5 Transformer core architecture with hyperparameters.

This network implements a hybrid Transformer-based decoder with two layer types: - `full_attention`: Standard grouped-query attention with partial rotary embeddings and sigmoid output gating. - `linear_attention`: GatedDeltaNet recurrent linear attention with causal conv1d and delta rule recurrence.

The backbone optionally accepts a `vision_encoder` to enable multimodal (image + text) inputs. When present, visual token embeddings are interleaved into the text embedding sequence before the transformer layers. M-RoPE (multi-dimensional RoPE) position encoding is used for the full-attention layers when `mrope_section` is provided.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of query attention heads.
*   **num\_key\_value\_heads**: int. The number of key and value attention heads.
*   **head\_dim**: int. Dimension of each attention head.
*   **hidden\_dim**: int. The size of the transformer hidden dimension.
*   **intermediate\_dim**: int. The FFN intermediate dimension.
*   **layer\_types**: list. List of layer types, one per layer. Each element is `"full_attention"` or `"linear_attention"`.
*   **partial\_rotary\_factor**: float. Fraction of head\_dim that gets RoPE. Defaults to `0.25`.
*   **rope\_max\_wavelength**: int. Maximum wavelength for RoPE. Defaults to `10000`.
*   **rope\_scaling\_factor**: float. Scaling factor for RoPE. Defaults to `1.0`.
*   **layer\_norm\_epsilon**: float. Epsilon for layer norms. Defaults to `1e-6`.
*   **dropout**: float. Dropout rate. Defaults to `0.0`.
*   **tie\_word\_embeddings**: bool. Whether to tie input and output embeddings. Defaults to `False`.
*   **sliding\_window\_size**: int. Sliding window size for full attention layers. Defaults to `32768`.
*   **linear\_num\_key\_heads**: int. Key heads for linear attention. Defaults to `16`.
*   **linear\_num\_value\_heads**: int. Value heads for linear attention. Defaults to `32`.
*   **linear\_key\_head\_dim**: int. Key head dim for linear attention. Defaults to `128`.
*   **linear\_value\_head\_dim**: int. Value head dim for linear attention. Defaults to `128`.
*   **linear\_conv\_kernel\_dim**: int. Conv kernel size for linear attention. Defaults to `4`.
*   **vision\_encoder**: `Qwen3_5VisionEncoder` or None. When supplied, the backbone accepts `pixel_values`, `image_grid_thw`, and `vision_indices` in addition to text inputs.
*   **mrope\_section**: list or None. `[s_t, s_h, s_w]` — number of _pairs_ of rotary dimensions assigned to temporal, height, and width axes. Required for M-RoPE in multimodal mode. e.g. `[11, 11, 10]` for the 27B model. Defaults to `None` (plain 1D RoPE).
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Qwen3_5Backbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

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

[Qwen3\_5Backbone model](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_backbone/#qwen35backbone-model)

[`Qwen3_5Backbone` class](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_backbone/#qwen35backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5/qwen3_5_backbone/#frompreset-method)