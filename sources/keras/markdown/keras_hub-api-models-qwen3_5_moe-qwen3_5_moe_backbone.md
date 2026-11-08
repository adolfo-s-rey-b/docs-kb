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
 / Qwen3\_5MoeBackbone model

Qwen3\_5MoeBackbone model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_5_moe/qwen3_5_moe_backbone.py#L16)

### `Qwen3_5MoeBackbone` class

Copied!

`keras_hub.models.Qwen3_5MoeBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     head_dim,     hidden_dim,     moe_intermediate_dim,     shared_expert_intermediate_size,     num_experts,     top_k,     layer_types=None,     partial_rotary_factor=0.25,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     dropout=0.0,     tie_word_embeddings=False,     sliding_window_size=32768,     linear_num_key_heads=16,     linear_num_value_heads=32,     linear_key_head_dim=128,     linear_value_head_dim=128,     linear_conv_kernel_dim=4,     vision_encoder=None,     mrope_section=None,     router_aux_loss_coefficient=0.001,     dtype=None,     **kwargs )`

The Qwen3.5 MoE Transformer core architecture with hyperparameters.

This network implements a hybrid Transformer-based decoder with two layer types and a Mixture-of-Experts (MoE) feedforward: - `full_attention`: Standard grouped-query attention with partial rotary embeddings and sigmoid output gating. - `linear_attention`: GatedDeltaNet recurrent linear attention with causal conv1d and delta rule recurrence.

The feedforward in every layer is a SparseMoeBlock with top-k expert routing and a shared expert with sigmoid gating.

The backbone optionally accepts a `vision_encoder` to enable multimodal (image + text) inputs.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of query attention heads.
*   **num\_key\_value\_heads**: int. The number of key and value attention heads.
*   **head\_dim**: int. Dimension of each attention head.
*   **hidden\_dim**: int. The size of the transformer hidden dimension.
*   **moe\_intermediate\_dim**: int. Intermediate dim per expert.
*   **shared\_expert\_intermediate\_size**: int. Intermediate dim for the shared expert.
*   **num\_experts**: int. Total number of routed experts.
*   **top\_k**: int. Number of experts per token.
*   **layer\_types**: list. List of layer types, one per layer.
*   **partial\_rotary\_factor**: float. Fraction of head\_dim that gets RoPE. Defaults to `0.25`.
*   **rope\_max\_wavelength**: int. Maximum wavelength for RoPE. Defaults to `10000`.
*   **rope\_scaling\_factor**: float. Scaling factor for RoPE. Defaults to `1.0`.
*   **layer\_norm\_epsilon**: float. Epsilon for layer norms. Defaults to `1e-6`.
*   **dropout**: float. Dropout rate. Defaults to `0.0`.
*   **tie\_word\_embeddings**: bool. Whether to tie input and output embeddings. Defaults to `False`.
*   **sliding\_window\_size**: int. Sliding window size for full attention layers. Defaults to `32768`.
*   **linear\_num\_key\_heads**: int. Key heads for linear attention.
*   **linear\_num\_value\_heads**: int. Value heads for linear attention.
*   **linear\_key\_head\_dim**: int. Key head dim for linear attention.
*   **linear\_value\_head\_dim**: int. Value head dim for linear attention.
*   **linear\_conv\_kernel\_dim**: int. Conv kernel size for linear attention.
*   **vision\_encoder**: optional vision encoder for multimodal inputs.
*   **mrope\_section**: list or None. M-RoPE section sizes.
*   **router\_aux\_loss\_coefficient**: float. Coefficient for the router's auxiliary load-balancing loss.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  model = keras_hub.models.Qwen3_5MoeBackbone(     vocabulary_size=248320,     num_layers=4,     num_query_heads=16,     num_key_value_heads=2,     head_dim=256,     hidden_dim=2048,     moe_intermediate_dim=512,     shared_expert_intermediate_size=512,     num_experts=8,     top_k=2, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Qwen3_5MoeBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [qwen\_agent\_world\_35b\_a3b](https://www.kaggle.com/models/keras/qwen-agentworld/keras/qwen_agent_world_35b_a3b/1) | 34.66B | 35 billion total parameter Qwen AgentWorld model with ~3 billion active parameters per token. Optimized for agentic applications and tool use. |
| [qwen3\_5\_moe\_35b\_a3b\_base](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b_base/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE base model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward for highly efficient inference. Supports text and multimodal inputs. |
| [qwen3\_5\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for chat, reasoning, coding, and multimodal tasks. |
| [qwen3\_6\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-6-moe/keras/qwen3_6_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.6 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for fast inference and extended context lengths. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Qwen3_5MoeBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Qwen3_5MoeBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Qwen3\_5MoeBackbone model](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_backbone/#qwen35moebackbone-model)

[`Qwen3_5MoeBackbone` class](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_backbone/#qwen35moebackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/qwen3_5_moe/qwen3_5_moe_backbone/#enablelora-method)