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
 / [MPNet](https://keras.io/keras_hub/api/models/mpnet/)
 / MPNetBackbone model

MPNetBackbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mpnet/mpnet_backbone.py#L16)

### `MPNetBackbone` class

Copied!

`keras_hub.models.MPNetBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     layer_norm_epsilon=1e-05,     dtype=None,     **kwargs )`

An MPNet encoder network.

This network implements the bi-directional Transformer encoder described in ["MPNet: Masked and Permuted Pre-training for Language Understanding"](https://arxiv.org/abs/2004.09297)
. It includes the embedding lookups and transformer layers, but does not include the masked and permuted language modeling head used during pretraining.

MPNet combines learned absolute position embeddings with a bucketed relative position bias, which is shared by all transformer layers.

The default constructor gives a fully customizable, randomly initialized MPNet encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/microsoft/MPNet)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the embeddings and the Transformer encoder. Defaults to `0.1`.
*   **max\_sequence\_length**: int. The maximum sequence length this encoder can consume. This determines the variable shape for the absolute position embeddings. Defaults to `512`.
*   **layer\_norm\_epsilon**: float. The epsilon of the layer normalization layers. Defaults to `1e-5`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], dtype="int32"     ), }  # Pretrained MPNet encoder. model = keras_hub.models.MPNetBackbone.from_preset("all_mpnet_base_v2") model(input_data)  # Randomly initialized MPNet encoder with a custom config. model = keras_hub.models.MPNetBackbone(     vocabulary_size=30527,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MPNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [all\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/all_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model. Maps sentences and paragraphs to 768-dimensional normalized vectors. Trained on 1B+ sentence pairs for semantic search, clustering, and similarity. |
| [nli\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/nli_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on natural language inference (NLI) data. Maps sentences to 768-dimensional dense vectors that are not normalized. Inputs are truncated to 75 tokens. |
| [paraphrase\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/paraphrase_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on paraphrase data. Maps sentences and paragraphs to 768-dimensional dense vectors that are not normalized, for paraphrase mining, clustering, and semantic search. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.MPNetBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[MPNetBackbone model](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone/#mpnetbackbone-model)

[`MPNetBackbone` class](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone/#mpnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/mpnet/mpnet_backbone/#tokenembedding-property)