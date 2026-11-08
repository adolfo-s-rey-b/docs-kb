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
 / [GPT-NeoX](https://keras.io/keras_hub/api/models/gpt_neo_x/)
 / GPTNeoXBackbone model

GPTNeoXBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt_neo_x/gpt_neo_x_backbone.py#L14)

### `GPTNeoXBackbone` class

Copied!

`keras_hub.models.GPTNeoXBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.0,     rotary_percentage=0.25,     rotary_max_wavelength=10000,     layer_norm_epsilon=1e-05,     max_sequence_length=512,     dtype=None,     **kwargs )`

GPT-NeoX core network with hyperparameters.

This network implements a Transformer-based decoder network, Generative Pretrained Transformer-Neo-X (GPTNeoX), as described in ["GPT-NeoX-20B: An Open-Source Autoregressive Language Model"](https://arxiv.org/abs/2204.06745)
. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized GPT-NeoX model with any number of layers, heads, and embedding dimensions.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/EleutherAI/gpt-neox/)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **layer\_norm\_epsilon**: float. a value added to the denominator for numerical stability.
*   **rotary\_max\_wavelength**: int. The maximum angular wavelength of the sine/cosine curves, for rotary embeddings.
*   **rotary\_percentage**: float. The percentage by which query, key, value matrices are to be rotated
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If `None`, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`GPTNeoXBackbone.from_preset(preset, load_weights=True, **kwargs)`

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

* * *

### `token_embedding` property

Copied!

`keras_hub.models.GPTNeoXBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`GPTNeoXBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[GPTNeoXBackbone model](https://keras.io/keras_hub/api/models/gpt_neo_x/gpt_neo_x_backbone/#gptneoxbackbone-model)

[`GPTNeoXBackbone` class](https://keras.io/keras_hub/api/models/gpt_neo_x/gpt_neo_x_backbone/#gptneoxbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt_neo_x/gpt_neo_x_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gpt_neo_x/gpt_neo_x_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/gpt_neo_x/gpt_neo_x_backbone/#enablelora-method)