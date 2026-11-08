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
 / [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
 / Mistral3Backbone model

Mistral3Backbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral3/mistral3_backbone.py#L23)

### `Mistral3Backbone` class

Copied!

`keras_hub.models.Mistral3Backbone(     vocabulary_size,     num_layers,     num_query_heads,     hidden_dim,     intermediate_dim,     num_key_value_heads,     vision_encoder=None,     multimodal_projector=None,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     rope_type="linear",     beta_fast=32.0,     beta_slow=1.0,     original_max_position_embeddings=4096,     layer_norm_epsilon=1e-06,     sliding_window=None,     head_dim=None,     dropout=0,     image_token_index=10,     tie_word_embeddings=False,     llama_4_scaling_beta=None,     attention_factor=None,     dtype=None,     **kwargs )`

The Mistral3 (Pixtral vision + Mistral text) core architecture.

This network implements a multimodal Transformer-based decoder network, Mistral3, as used by models such as Mistral Small 3.1/3.2. It includes the token embedding lookups, a Pixtral-style vision encoder, and transformer decoder layers.

The default constructor gives a fully customizable, randomly initialized Mistral3 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of query attention heads for each transformer.
*   **hidden\_dim**: int. The size of the transformer encoding and pooling layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a three-layer feedforward network for each transformer.
*   **num\_key\_value\_heads**: int. The number of key and value attention heads for each transformer.
*   **vision\_encoder**: A [`keras_hub.models.Mistral3VisionEncoder`](https://keras.io/keras_hub/api/models/mistral3/mistral3_vision_encoder#mistral3visionencoder-class)
     instance, or `None`. When `None`, the backbone is text-only and does not declare `pixel_values`, `image_sizes`, or `placeholder_indices` inputs.
*   **multimodal\_projector**: A `Mistral3MultiModalProjector` instance, or `None`. Required when `vision_encoder` is not `None`.
*   **rope\_max\_wavelength**: int, optional. The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   **rope\_scaling\_factor**: float, optional. The scaling factor for calculation of rotary embedding. Defaults to `1.0`.
*   **rope\_type**: str, optional. The type of RoPE scaling to apply. Supports `"linear"` and `"yarn"`. Defaults to `"linear"`. Use `"yarn"` for checkpoints with YaRN-scaled rotary embeddings (e.g. Ministral 3).
*   **beta\_fast**: float, optional. The YaRN beta fast parameter. Only used when `rope_type="yarn"`. Defaults to `32.0`.
*   **beta\_slow**: float, optional. The YaRN beta slow parameter. Only used when `rope_type="yarn"`. Defaults to `1.0`.
*   **original\_max\_position\_embeddings**: int, optional. The pretraining context length before YaRN scaling. Only used when `rope_type="yarn"`. Defaults to `4096`.
*   **attention\_factor**: float, optional. The YaRN temperature scale applied to the rotary cos/sin embeddings. Only used when `rope_type="yarn"`. Defaults to `None`, which derives the scale as `0.1 * log(rope_scaling_factor) + 1.0` (the standard YaRN default). Pass an explicit value for checkpoints that compute a different scale from `mscale`/`mscale_all_dim` — e.g. Ministral 3 and Shieldstral set both to `1.0`, giving `attention_factor=1.0`.
*   **layer\_norm\_epsilon**: float, optional. Epsilon for the layer normalization layers in the transformer decoder. Defaults to `1e-6`.
*   **sliding\_window**: int, optional. The sliding window for the mistral attention layers. This controls the maximum cache size for the attention layers in each transformer decoder. Only `sliding_window` number of tokens are saved in the cache and used to generate the next token. Defaults to `None`.
*   **head\_dim**: int, optional. The size of each attention head. When `None` (the default), falls back to `hidden_dim // num_query_heads`. Set explicitly when the model's head size is not equal to `hidden_dim // num_query_heads` — e.g. Magistral uses `head_dim=128` with `hidden_dim=5120` and `num_query_heads=32`.
*   **dropout**: float, optional. The dropout probability for the attention layers. Defaults to `0`.
*   **image\_token\_index**: int, optional. The token ID in `token_ids` that marks image placeholder positions. Defaults to `10`.
*   **tie\_word\_embeddings**: bool, optional. Whether to tie the input token embedding and the output (LM head) projection to the same weights. Defaults to `False`.
*   **llama\_4\_scaling\_beta**: float, optional. When set, scales query magnitude by absolute position with a Llama4-style `attn_temperature_tuning`: `query *= 1 + llama_4_scaling_beta * log(1 + floor(pos / original_max_position_embeddings))`. Defaults to `None` (no scaling).
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]),     "pixel_values": np.ones(shape=(1, 3, 64, 64), dtype="float32"),     "image_sizes": np.array([[64, 64]], dtype="int32"),     "placeholder_indices": np.zeros(shape=(1, 16), dtype="int32"), }  # Pretrained Mistral3 decoder. model = keras_hub.models.Mistral3Backbone.from_preset(     "mistral_small_3.1_24b_instruct_2503_en" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Mistral3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [ministral\_3\_3b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_base_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_instruct_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_reasoning_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [shieldstral\_1.0\_3b\_en](https://www.kaggle.com/models/keras/shieldstral/keras/shieldstral_1.0_3b_en/1) | 3.85B | 3 billion parameter, 26-layer Shieldstral model with a Pixtral vision encoder. The model checks text and image content against a safety policy written in natural language. The model returns one safety score for each input. |
| [ministral\_3\_8b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_base_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_instruct_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_reasoning_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_base_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_instruct_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_reasoning_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_base\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_base_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, pretrained Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_instruct\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_instruct_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.2\_24b\_instruct\_2506\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.2_24b_instruct_2506_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. An updated version of mistral\_small\_3.1\_24b\_instruct\_2503\_en with improved instruction-following and reduced repetition. |
| [devstral\_small\_2\_24b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/devstral2/keras/devstral_small_2_24b_instruct_2512_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Devstral Small 2 model for agentic software engineering, with a Pixtral vision encoder for image input. |
| [magistral\_small\_2509\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2509_en/1) | 24.01B | 24 billion parameter, 40-layer, reasoning-tuned Magistral Small model with a Pixtral vision encoder for image input. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Mistral3Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Mistral3Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Mistral3Backbone model](https://keras.io/keras_hub/api/models/mistral3/mistral3_backbone/#mistral3backbone-model)

[`Mistral3Backbone` class](https://keras.io/keras_hub/api/models/mistral3/mistral3_backbone/#mistral3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral3/mistral3_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/mistral3/mistral3_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/mistral3/mistral3_backbone/#enablelora-method)