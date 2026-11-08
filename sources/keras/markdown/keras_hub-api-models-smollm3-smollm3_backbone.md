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
 / [SmolLM3](https://keras.io/keras_hub/api/models/smollm3/)
 / SmolLM3Backbone model

SmolLM3Backbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smollm3/smollm3_backbone.py#L9)

### `SmolLM3Backbone` class

Copied!

`keras_hub.models.SmolLM3Backbone(     vocabulary_size,     hidden_dim,     intermediate_dim,     num_layers,     num_attention_heads,     num_key_value_heads,     attention_bias,     attention_dropout,     rope_layer_enabled_list,     layer_types,     mlp_bias,     layer_norm_epsilon,     max_position_embeddings,     rope_theta,     partial_rotary_factor,     **kwargs )`

SmolLM3 core network with hyperparameters.

This network implements a Transformer-based decoder network, SmolLM3, as described in the SmolLM3 model architecture. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized SmolLM3 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in the MLP network of each transformer layer.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_attention\_heads**: int. The number of attention heads for each transformer layer.
*   **num\_key\_value\_heads**: int. The number of key-value heads for grouped query attention in each transformer layer.
*   **attention\_bias**: bool. Whether to use bias in the query, key, value, and output projection layers in the attention blocks.
*   **attention\_dropout**: float. Dropout probability for the attention layers.
*   **rope\_layer\_enabled\_list**: list of bool. List indicating whether RoPE (Rotary Position Embedding) is enabled for each layer. Typically, some layers may disable RoPE for architectural variations.
*   **layer\_types**: list of str. List of layer types for each transformer layer (e.g., "attention" or other custom types).
*   **mlp\_bias**: bool. Whether to use bias in the MLP (feedforward) layers.
*   **layer\_norm\_epsilon**: float. Epsilon value for layer normalization layers to prevent division by zero.
*   **max\_position\_embeddings**: int. The maximum sequence length that this model might ever be used with.
*   **rope\_theta**: float. The base period of the RoPE embeddings.
*   **partial\_rotary\_factor**: float. The percentage of hidden dimensions to rotate in RoPE. A value of 1.0 rotates all dimensions, while values less than 1.0 only rotate a subset.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained SmolLM3 decoder. model = keras_hub.models.SmolLM3Backbone.from_preset(     "hf://HuggingFaceTB/SmolLM3-3B" ) model(input_data)  # Randomly initialized SmolLM3 decoder with custom config. model = keras_hub.models.SmolLM3Backbone(     vocabulary_size=49152,     hidden_dim=576,     intermediate_dim=1536,     num_layers=30,     num_attention_heads=9,     num_key_value_heads=3,     attention_bias=False,     attention_dropout=0.0,     rope_layer_enabled_list=[True] * 30,     layer_types=["attention"] * 30,     mlp_bias=False,     layer_norm_epsilon=1e-5,     max_position_embeddings=2048,     rope_theta=10000.0,     partial_rotary_factor=1.0, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SmolLM3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [smollm3\_3b\_en](https://www.kaggle.com/models/keras/smollm3/keras/smollm3_3b_en/1) | 3.08B | Dense decoder-only model has 3 billion total parameters, built on 36 layers and utilizes 16 query and 4 key/value attention heads. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.SmolLM3Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[SmolLM3Backbone model](https://keras.io/keras_hub/api/models/smollm3/smollm3_backbone/#smollm3backbone-model)

[`SmolLM3Backbone` class](https://keras.io/keras_hub/api/models/smollm3/smollm3_backbone/#smollm3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smollm3/smollm3_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/smollm3/smollm3_backbone/#tokenembedding-property)