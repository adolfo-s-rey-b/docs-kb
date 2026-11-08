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
 / [QwenMoe](https://keras.io/keras_hub/api/models/qwen_moe/)
 / QwenMoeBackbone model

QwenMoeBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen_moe/qwen_moe_backbone.py#L17)

### `QwenMoeBackbone` class

Copied!

`keras_hub.models.QwenMoeBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     moe_intermediate_dim,     shared_expert_intermediate_dim,     num_experts,     top_k=4,     norm_top_k_prob=False,     decoder_sparse_step=1,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     tie_word_embeddings=False,     use_sliding_window_attention=False,     sliding_window_size=32768,     output_router_logits=False,     router_aux_loss_coefficient=0.001,     mlp_only_layers=[],     **kwargs )`

Qwen MoE core network with hyperparameters.

This backbone implements the base Transformer network for the Qwen MoE model. It includes embedding lookups and transformer layers with a Mixture of Experts (MoE) architecture, where each layer uses a sparse set of experts for efficient computation. This backbone outputs the final hidden states for each token, not generative predictions over the vocabulary space. For higher -level object for text generation, see [`keras_hub.models.QwenMoeCausalLM`](https://keras.io/keras_hub/api/models/qwen_moe/qwen_moe_causal_lm#qwenmoecausallm-class)
.

The default constructor gives a fully customizable, randomly initialized Qwen MoE model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of heads for the query projections in the attention layer.
*   **num\_key\_value\_heads**: int. The number of heads for the key and value projections in the attention layer.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in the feedforward network for each transformer.
*   **moe\_intermediate\_dim**: int. The intermediate dimension for each expert in the MoE feedforward network.
*   **shared\_expert\_intermediate\_dim**: int. The intermediate dimension for the shared expert in the MoE feedforward network.
*   **num\_experts**: int. The number of experts in each MoE layer.
*   **top\_k**: int. The number of top experts to select for each token in the MoE layer.
*   **head\_dim**: int. The size of each attention head.
*   **layer\_norm\_epsilon**: float. The epsilon value used for every layer norm in the transformer model.
*   **dropout**: float. Dropout probability for the transformer encoder.
*   **use\_sliding\_window\_attention**: bool. Whether to use sliding local window attention. Defaults to False.
*   **sliding\_window\_size**: int. Size of the sliding local window. Defaults to 4096.
*   **max\_sequence\_length**: int. The maximum sequence length supported by the model. Defaults to 4096.
*   **dtype**: str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

``input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  __Pretrained Qwen MoE decoder__  .  model = keras_hub.models.QwenMoeBackbone.from_preset("qwen_moe_a2_7b") model(input_data)  __Randomly initialized Qwen MoE decoder with custom config__  .  model = keras_hub.models.QwenMoeBackbone(     vocabulary_size=151936,     num_layers=28,     num_query_heads=16,     num_key_value_heads=8,     hidden_dim=2048,     intermediate_dim=4096,     moe_intermediate_dim=128,     shared_expert_intermediate_dim=4096,     num_experts=60,     top_k=4,     head_dim=128,     max_sequence_length=4096, ) model(input_data)  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)</span>  ### `from_preset` method  ```python QwenMoeBackbone.from_preset(preset, load_weights=True, **kwargs)``

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
| [qwen1.5\_moe\_2.7b\_en](https://www.kaggle.com/models/keras/qwen-1.5-moe/Keras/qwen1.5_moe_2.7b_en/4) | 14.32B | 24-layer Qwen MoE model with 2.7 billion active parameters and 8 experts per MoE layer. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.QwenMoeBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`QwenMoeBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[QwenMoeBackbone model](https://keras.io/keras_hub/api/models/qwen_moe/qwen_moe_backbone/#qwenmoebackbone-model)

[`QwenMoeBackbone` class](https://keras.io/keras_hub/api/models/qwen_moe/qwen_moe_backbone/#qwenmoebackbone-class)

[Load a Gemma backbone with pre-trained weights.](https://keras.io/keras_hub/api/models/qwen_moe/qwen_moe_backbone/#load-a-gemma-backbone-with-pretrained-weights)

[Load a Bert backbone with a pre-trained config and random weights.](https://keras.io/keras_hub/api/models/qwen_moe/qwen_moe_backbone/#load-a-bert-backbone-with-a-pretrained-config-and-random-weights)