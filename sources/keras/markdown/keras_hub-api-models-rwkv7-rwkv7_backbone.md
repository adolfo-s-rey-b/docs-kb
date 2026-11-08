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
 / [RWKV7](https://keras.io/keras_hub/api/models/rwkv7/)
 / RWKV7Backbone model

RWKV7Backbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/rwkv7/rwkv7_backbone.py#L13)

### `RWKV7Backbone` class

Copied!

`keras_hub.models.RWKV7Backbone(     hidden_size,     head_size,     num_layers,     vocabulary_size,     intermediate_dim,     gate_lora=128,     mv_lora=32,     aaa_lora=64,     decay_lora=64,     dtype=None,     dropout_rate=0,     **kwargs )`

The RWKV7 Transformer core architecture with hyperparameters.

This network implements a RNN-based decoder network, Goose, as described in [RWKV-7](https://arxiv.org/abs/2503.14456)
.

This network implements a Modern RNN architecture based on linear attention mechanisms with recurrent processing, as described in the RWKV papers. It includes the embedding lookups and RWKV-7 blocks.

The default constructor gives a fully customizable, randomly initialized RWKV-7 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **hidden\_size**: int. The size of the transformer encoding and pooling layers.
*   **head\_size**: int. The size of each attention head.
*   **num\_layers**: int. The number of transformer layers.
*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **gate\_lora**: int. LoRA dimension for gating. Defaults to `128` .
*   **mv\_lora**: int. LoRA dimension for value mixing. Defaults to `32` .
*   **aaa\_lora**: int. LoRA dimension for alpha parameters.Defaults to `64` .
*   **decay\_lora**: int. LoRA dimension for decay parameters.Defaults to `64` .
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.
*   **dropout\_rate**: float. Dropout rate for the dropout layer.

**Examples**

Copied!

`input_data = np.ones(shape=(1, 12), dtype="int32")  # Randomly initialized RWKV-7 decoder with custom config. model = keras_hub.models.RWKV7Backbone(     vocabulary_size=10,     hidden_size=512,     num_layers=2,     head_size=64,     intermediate_dim=1024,     dtype="float32" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`RWKV7Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [rwkv7\_g1a\_0.1b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.1b/1) | 150.00M | 150 million parameter RWKV7 model. Optimized for edge devices and mobile deployment. |
| [rwkv7\_g1a\_0.3b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.3b/1) | 400.00M | 400 million parameter RWKV7 model. Small variant balancing speed and instruction following. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.RWKV7Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[RWKV7Backbone model](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_backbone/#rwkv7backbone-model)

[`RWKV7Backbone` class](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_backbone/#rwkv7backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_backbone/#tokenembedding-property)