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
 / [Qwen](https://keras.io/keras_hub/api/models/qwen/)
 / QwenBackbone model

QwenBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen/qwen_backbone.py#L15)

### `QwenBackbone` class

Copied!

`keras_hub.models.QwenBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     tie_word_embeddings=True,     use_sliding_window_attention=False,     sliding_window_size=32768,     **kwargs )`

The Qwen Transformer core architecture with hyperparameters.

This network implements a Transformer-based decoder network, Qwen, as described in the Qwen model architecture. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized Qwen model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size (int)**: The size of the token vocabulary.
*   **num\_layers (int)**: The number of transformer layers.
*   **num\_query\_heads (int)**: The number of query attention heads for each transformer.
*   **hidden\_dim (int)**: The size of the transformer encoding and pooling layers.
*   **intermediate\_dim (int)**: The output dimension of the first Dense layer in a three-layer feedforward network for each transformer.
*   **num\_key\_value\_heads (int)**: The number of key and value attention heads for each transformer.
*   **rope\_max\_wavelength (int, optional)**: The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   **rope\_scaling\_factor (float, optional)**: The scaling factor for calculation of rotary embedding. Defaults to `1.0`.
*   **layer\_norm\_epsilon (float, optional)**: Epsilon for the layer normalization layers in the transformer decoder. Defaults to `1e-6`.
*   **dropout (float, optional)**: Dropout rate for attention and hidden layers. Defaults to `0`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.
*   **tie\_word\_embeddings (bool, optional)**: Whether to tie input and output embeddings. Defaults to `True`.
*   **use\_sliding\_window\_attention (bool, optional)**: Whether to use sliding window attention for efficient processing of long sequences. Defaults to `False`.
*   **sliding\_window\_size (int, optional)**: Size of the sliding window for attention when enabled. Defaults to `32768`.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained Qwen decoder. model = keras_hub.models.QwenBackbone.from_preset("qwen2.5_0.5b_en") model(input_data)  # Randomly initialized Qwen decoder with custom config. model = keras_hub.models.QwenBackbone(     vocabulary_size=10,     hidden_dim=512,     num_layers=2,     num_query_heads=32,     num_key_value_heads=8,     intermediate_dim=1024,     layer_norm_epsilon=1e-6,     dtype="float32" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`QwenBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [qwen2.5\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_0.5b_en/1) | 494.03M | 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_instruct\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_0.5b_en/1) | 494.03M | Instruction fine-tuned 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_coder\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_0.5b/1) | 494.03M | Code-focused fine-tuned Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_0.5b/1) | 494.03M | Instruction-tuned code-focused Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_1.5b/1) | 1.54B | Code-focused fine-tuned 28-layer Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_1.5b/1) | 1.54B | Instruction-tuned code-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_1.5b_en/1) | 1.54B | Math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_instruct\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_1.5b_en/1) | 1.54B | Instruction-tuned math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_3b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_3b_en/1) | 3.09B | 36-layer Qwen model with 3.1 billion parameters. |
| [qwen2.5\_coder\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_3b/1) | 3.09B | Code-focused fine-tuned Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_coder\_instruct\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_3b/1) | 3.09B | Instruction-tuned code-focused Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_7b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_7b_en/3) | 6.99B | 48-layer Qwen model with 7 billion parameters. |
| [qwen2.5\_coder\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_7b/1) | 6.99B | Code-focused fine-tuned Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_instruct\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_7b/1) | 6.99B | Instruction-tuned code-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_7b_en/1) | 7.62B | Math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_instruct\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_7b_en/1) | 7.62B | Instruction-tuned math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_14b/1) | 14.00B | Code-focused fine-tuned Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_coder\_instruct\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_14b/1) | 14.00B | Instruction-tuned code-focused Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_instruct\_32b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_32b_en/2) | 32.76B | Instruction fine-tuned 64-layer Qwen model with 32 billion parameters. |
| [qwen2.5\_coder\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_32b/1) | 32.76B | Code-focused fine-tuned Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_coder\_instruct\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_32b/1) | 32.76B | Instruction-tuned code-focused Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_instruct\_72b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_72b_en/2) | 72.71B | Instruction fine-tuned 80-layer Qwen model with 72 billion parameters. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.QwenBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`QwenBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[QwenBackbone model](https://keras.io/keras_hub/api/models/qwen/qwen_backbone/#qwenbackbone-model)

[`QwenBackbone` class](https://keras.io/keras_hub/api/models/qwen/qwen_backbone/#qwenbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen/qwen_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/qwen/qwen_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/qwen/qwen_backbone/#enablelora-method)