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
 / [Llama3](https://keras.io/keras_hub/api/models/llama3/)
 / Llama3Backbone model

Llama3Backbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/llama3/llama3_backbone.py#L7)

### `Llama3Backbone` class

Copied!

`keras_hub.models.Llama3Backbone(     vocabulary_size,     num_layers,     num_query_heads,     hidden_dim,     intermediate_dim,     num_key_value_heads,     rope_max_wavelength=10000,     rope_position_scaling_factor=1.0,     rope_frequency_adjustment_factor=None,     rope_low_freq_factor=None,     rope_high_freq_factor=None,     rope_pretraining_sequence_length=None,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     tie_word_embeddings=False,     **kwargs )`

The Llama Transformer core architecture with hyperparameters.

This network implements a Transformer-based decoder network, Llama, as described in ["Llama 7B"](https://arxiv.org/pdf/2310.06825.pdf)
. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized Llama model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size (int)**: The size of the token vocabulary.
*   **num\_layers (int)**: The number of transformer layers.
*   **num\_query\_heads (int)**: The number of query attention heads for each transformer.
*   **hidden\_dim (int)**: The size of the transformer encoding and pooling layers.
*   **intermediate\_dim (int)**: The output dimension of the first Dense layer in a three-layer feedforward network for each transformer.
*   **num\_key\_value\_heads (int)**: The number of key and value attention heads fo each transformer.
*   **rope\_max\_wavelength (int, optional)**: The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   **rope\_position\_scaling\_factor (float, optional)**: The scaling factor for calculation of roatary embedding. Defaults to `1.0`
*   **rope\_requency\_adjustment\_factor (float, optional)**: The scaling factor used to scale the inverse frequencies.
*   **rope\_low\_freq\_factor (float, optional)**: The low frequency factor. Defaults to None.
*   **rope\_high\_freq\_factor**: (float, optional) Used for Llama3.1+. The high frequency factor. Defaults to None.
*   **rope\_pretraining\_sequence\_length**: (int, optional) Sequence length during original pretraining. Defaults to None.
*   **layer\_norm\_epsilon (float, optional)**: Epsilon for the layer normalization layers in the transformer decoder. Defaults to `1e-6`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained Llama decoder. model = keras_hub.models.Llama3Backbone.from_preset("llama3_8b_en") model(input_data)  # Randomly initialized Llama decoder with custom config. model = keras_hub.models.Llama3Backbone(     vocabulary_size=10,     hidden_dim=512,     num_layers=2,     num_query_heads=32,     num_key_value_heads=8,     intermediate_dim=1024,     layer_norm_epsilon=1e-6,     dtype="float32" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Llama3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [llama3.2\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_1b/1) | 1.50B | 1 billion parameter, 16-layer, instruction tuned LLaMA 3.2. |
| [llama3.2\_guard\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_guard_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model fine-tuned for consent safety classification. |
| [llama3.2\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_3b/1) | 3.61B | 3 billion parameter, 26-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_3b/1) | 3.61B | 3 billion parameter, 28-layer, instruction tuned LLaMA 3.2. |
| [llama3\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model. |
| [llama3\_instruct\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model. |
| [llama3.1\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_8b/2) | 8.03B | 8 billion parameter, 32-layer, based LLaMA 3.1 model. |
| [llama3.1\_instruct\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_instruct_8b/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3.1. |
| [llama3.1\_guard\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_guard_8b/2) | 8.03B | 8 billion parameter, 32-layer, LLaMA 3.1 fine-tuned for consent safety classification. |
| [llama3\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model with activation and weights quantized to int8. |
| [llama3\_instruct\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model with activation and weights quantized to int8. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Llama3Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Llama3Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Llama3Backbone model](https://keras.io/keras_hub/api/models/llama3/llama3_backbone/#llama3backbone-model)

[`Llama3Backbone` class](https://keras.io/keras_hub/api/models/llama3/llama3_backbone/#llama3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/llama3/llama3_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/llama3/llama3_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/llama3/llama3_backbone/#enablelora-method)