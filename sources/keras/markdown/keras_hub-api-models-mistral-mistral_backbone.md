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
 / [Mistral](https://keras.io/keras_hub/api/models/mistral/)
 / MistralBackbone model

MistralBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral/mistral_backbone.py#L19)

### `MistralBackbone` class

Copied!

`keras_hub.models.MistralBackbone(     vocabulary_size,     num_layers,     num_query_heads,     hidden_dim,     intermediate_dim,     num_key_value_heads,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     rope_type="linear",     beta_fast=32.0,     beta_slow=1.0,     original_max_position_embeddings=4096,     attention_factor=None,     layer_norm_epsilon=1e-06,     sliding_window=512,     head_dim=None,     dropout=0,     llama_4_scaling_beta=None,     dtype=None,     **kwargs )`

The Mistral Transformer core architecture with hyperparameters.

This network implements a Transformer-based decoder network, Mistral, as described in ["Mistral 7B"](https://arxiv.org/pdf/2310.06825.pdf)
. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized Mistral model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size (int)**: The size of the token vocabulary.
*   **num\_layers (int)**: The number of transformer layers.
*   **num\_query\_heads (int)**: The number of query attention heads for each transformer.
*   **hidden\_dim (int)**: The size of the transformer encoding and pooling layers.
*   **intermediate\_dim (int)**: The output dimension of the first Dense layer in a three-layer feedforward network for each transformer.
*   **num\_key\_value\_heads (int)**: The number of key and value attention heads for each transformer.
*   **rope\_max\_wavelength (int, optional)**: The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   **rope\_scaling\_factor (float, optional)**: The scaling factor for calculation of rotary embedding. Defaults to `1.0`.
*   **rope\_type**: str, optional. The type of RoPE scaling to apply. Supports `"linear"` and `"yarn"`. Defaults to `"linear"`.
*   **beta\_fast**: float, optional. The YaRN beta fast parameter. Only used when `rope_type="yarn"`. Defaults to `32.0`.
*   **beta\_slow**: float, optional. The YaRN beta slow parameter. Only used when `rope_type="yarn"`. Defaults to `1.0`.
*   **original\_max\_position\_embeddings**: int, optional. The pretraining context length before YaRN scaling. Only used when `rope_type="yarn"`. Defaults to `4096`.
*   **attention\_factor**: float, optional. The YaRN temperature scale applied to the rotary cos/sin embeddings. Only used when `rope_type="yarn"`. Defaults to `None`, which derives the scale as `0.1 * log(rope_scaling_factor) + 1.0` (the standard YaRN default). Pass an explicit value for checkpoints that compute a different scale from `mscale`/`mscale_all_dim`.
*   **layer\_norm\_epsilon (float, optional)**: Epsilon for the layer normalization layers in the transformer decoder. Defaults to `1e-6`.
*   **sliding\_window (int, optional)**: The sliding window for the mistral attention layers. This controls the maximum cache size for the attention layers in each transformer decoder. Only `sliding_window` number of tokens are saved in the cache and used to generate the next token. Defaults to `512`. Pass `None` to disable sliding window attention entirely (e.g. Magistral).
*   **head\_dim (int, optional)**: The size of each attention head. When `None` (the default), falls back to `hidden_dim // num_query_heads`. Set explicitly when the model's head size is not equal to `hidden_dim // num_query_heads` — e.g. Magistral uses `head_dim=128` with `hidden_dim=5120` and `num_query_heads=32`.
*   **llama\_4\_scaling\_beta**: float, optional. When set, scales query magnitude by absolute position with a Llama4-style `attn_temperature_tuning`: `query *= 1 + llama_4_scaling_beta * log(1 + floor(pos / original_max_position_embeddings))`. Defaults to `None` (no scaling).
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained Mistral decoder. model = keras_hub.models.MistralBackbone.from_preset("mistral7b_base_en") model(input_data)  # Randomly initialized Mistral decoder with custom config. model = keras_hub.models.MistralBackbone(     vocabulary_size=10,     hidden_dim=512,     num_layers=2,     num_query_heads=32,     num_key_value_heads=8,     intermediate_dim=1024,     sliding_window=512,     layer_norm_epsilon=1e-6,     dtype="float32" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MistralBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [mistral\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_7b_en/8) | 7.24B | Mistral 7B base model |
| [mistral\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_instruct_7b_en/8) | 7.24B | Mistral 7B instruct model |
| [mistral\_0.2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.2_instruct_7b_en/3) | 7.24B | Mistral 7B instruct version 0.2 model |
| [mistral\_0.3\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_7b_en/1) | 7.25B | Mistral 7B base version 0.3 model |
| [mistral\_0.3\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_instruct_7b_en/1) | 7.25B | Mistral 7B instruct version 0.3 model |
| [magistral\_small\_2506\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2506_en/1) | 23.57B | Magistral Small 2506 model |
| [magistral\_small\_2507\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2507_en/1) | 23.57B | Magistral Small 2507 model |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.MistralBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`MistralBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[MistralBackbone model](https://keras.io/keras_hub/api/models/mistral/mistral_backbone/#mistralbackbone-model)

[`MistralBackbone` class](https://keras.io/keras_hub/api/models/mistral/mistral_backbone/#mistralbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral/mistral_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/mistral/mistral_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/mistral/mistral_backbone/#enablelora-method)