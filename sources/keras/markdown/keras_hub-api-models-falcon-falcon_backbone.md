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
 / [Falcon](https://keras.io/keras_hub/api/models/falcon/)
 / FalconBackbone model

FalconBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/falcon/falcon_backbone.py#L11)

### `FalconBackbone` class

Copied!

`keras_hub.models.FalconBackbone(     vocabulary_size,     num_layers,     num_attention_heads,     hidden_dim,     intermediate_dim,     layer_norm_epsilon=1e-05,     attention_dropout_rate=0,     feedforward_dropout_rate=0,     dtype=None,     **kwargs )`

The Falcon core architecure.

This network implements a Transformer-based decoder-only network, [Falcon](https://arxiv.org/abs/2306.01116)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_attention\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The dimensionality of the embeddings and hidden states.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in the MLP network of each transformer.
*   **layer\_norm\_epsilon**: float. Epsilon for the layer normalization layers in the transformer decoder.
*   **attention\_dropout\_rate**: float. Dropout probability for the attention.
*   **feedforward\_dropout\_rate**: float. Dropout probability for the feedforward.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained Falcon decoder. # TODO: Update the preset. model = keras_hub.models.FalconBackbone.from_preset("falcon_preset") model(input_data)  # Randomly initialized Falcon decoder with a custom config. model = keras_hub.models.FalconBackbone(     vocabulary_size=10,     num_layers=2,     num_attention_heads=2,     hidden_dim=32,     intermediate_dim=32*4,     layer_norm_epsilon=1e-5,     attention_dropout_rate=0,     feedforward_dropout_rate=0,     dtype="float32", ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`FalconBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [falcon\_refinedweb\_1b\_en](https://www.kaggle.com/models/keras/falcon/keras/falcon_refinedweb_1b_en/2) | 1.31B | 24-layer Falcon model (Falcon with 1B parameters), trained on 350B tokens of RefinedWeb dataset. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.FalconBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[FalconBackbone model](https://keras.io/keras_hub/api/models/falcon/falcon_backbone/#falconbackbone-model)

[`FalconBackbone` class](https://keras.io/keras_hub/api/models/falcon/falcon_backbone/#falconbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/falcon/falcon_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/falcon/falcon_backbone/#tokenembedding-property)