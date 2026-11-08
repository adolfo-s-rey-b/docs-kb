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
 / [Qwen3Moe](https://keras.io/keras_hub/api/models/qwen3_moe/)
 / Qwen3MoeBackbone model

Qwen3MoeBackbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_moe/qwen3_moe_backbone.py#L17)

### `Qwen3MoeBackbone` class

Copied!

`keras_hub.models.Qwen3MoeBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     moe_intermediate_dim,     num_experts,     head_dim=None,     top_k=4,     norm_top_k_prob=False,     decoder_sparse_step=1,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     tie_word_embeddings=False,     sliding_window_size=32768,     router_aux_loss_coefficient=0.001,     mlp_only_layers=None,     **kwargs )`

Qwen3 MoE core network with hyperparameters.

This backbone implements the base Transformer network for the Qwen MoE model. It includes embedding lookups and transformer layers with a Mixture of Experts (MoE) architecture, where each layer uses a sparse set of experts for efficient computation. This backbone outputs the final hidden states for each token, not generative predictions over the vocabulary space. For higher -level object for text generation, see [`keras_hub.models.Qwen3MoeCausalLM`](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_causal_lm#qwen3moecausallm-class)
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
*   **num\_experts**: int. The number of experts in each MoE layer.
*   **top\_k**: int. The number of top experts to select for each token in the MoE layer.
*   **head\_dim**: int. The size of each attention head.
*   **layer\_norm\_epsilon**: float. The epsilon value used for every layer norm in the transformer model.
*   **dropout**: float. Dropout probability for the transformer encoder.
*   **sliding\_window\_size**: int. Size of the sliding local window. Defaults to 4096.
*   **max\_sequence\_length**: int. The maximum sequence length supported by the model. Defaults to 4096.
*   **dtype**: str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

``input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  __Pretrained Qwen MoE decoder__  .  model = keras_hub.models.Qwen3MoeBackbone.from_preset("qwen3_moe_a2_7b") model(input_data)  __Randomly initialized Qwen MoE decoder with custom config__  .  model = keras_hub.models.Qwen3MoeBackbone(     vocabulary_size=151936,     num_layers=28,     num_query_heads=16,     num_key_value_heads=8,     hidden_dim=2048,     intermediate_dim=4096,     moe_intermediate_dim=128,     num_experts=60,     top_k=4,     head_dim=128,     max_sequence_length=4096, ) model(input_data)  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)</span>  ### `from_preset` method  ```python Qwen3MoeBackbone.from_preset(preset, load_weights=True, **kwargs)``

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
| [qwen3\_moe\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_30b_a3b_en/2) | 30.53B | Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_coder\_instruct\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen3-coder/keras/qwen3_coder_instruct_30b_a3b_en/1) | 30.53B | A Code-Specific Model,Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_moe\_235b\_a22b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_235b_a22b_en/1) | 235.09B | Mixture-of-Experts (MoE) model has 235 billion total parameters with 22 billion activated, built on 94 layers and utilizes 64 query and 4 key/value attention heads with 128 experts (8 active). |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Qwen3MoeBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Qwen3MoeBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Qwen3MoeBackbone model](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_backbone/#qwen3moebackbone-model)

[`Qwen3MoeBackbone` class](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_backbone/#qwen3moebackbone-class)

[Load a Gemma backbone with pre-trained weights.](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_backbone/#load-a-gemma-backbone-with-pretrained-weights)

[Load a Bert backbone with a pre-trained config and random weights.](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_backbone/#load-a-bert-backbone-with-a-pretrained-config-and-random-weights)