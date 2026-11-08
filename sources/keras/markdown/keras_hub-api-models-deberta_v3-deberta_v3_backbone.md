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
 / [DebertaV3](https://keras.io/keras_hub/api/models/deberta_v3/)
 / DebertaV3Backbone model

DebertaV3Backbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/deberta_v3/deberta_v3_backbone.py#L16)

### `DebertaV3Backbone` class

Copied!

`keras_hub.models.DebertaV3Backbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     bucket_size=256,     dtype=None,     **kwargs )`

DeBERTa encoder network.

This network implements a bi-directional Transformer-based encoder as described in ["DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing"](https://arxiv.org/abs/2111.09543)
. It includes the embedding lookups and transformer layers, but does not include the enhanced masked decoding head used during pretraining.

The default constructor gives a fully customizable, randomly initialized DeBERTa encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Note: `DebertaV3Backbone` has a performance issue on TPUs, and we recommend other models for TPU training and inference.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/microsoft/DeBERTa)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the DeBERTa model.
*   **max\_sequence\_length**: int. The maximum sequence length this encoder can consume. The sequence length of the input must be less than `max_sequence_length`.
*   **bucket\_size**: int. The size of the relative position buckets. Generally equal to `max_sequence_length // 2`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained DeBERTa encoder. model = keras_hub.models.DebertaV3Backbone.from_preset(     "deberta_v3_base_en", ) model(input_data)  # Randomly initialized DeBERTa encoder with custom config model = keras_hub.models.DebertaV3Backbone(     vocabulary_size=128100,     num_layers=12,     num_heads=6,     hidden_dim=384,     intermediate_dim=1536,     max_sequence_length=512,     bucket_size=256, ) # Call the model on the input data. model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DebertaV3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [deberta\_v3\_extra\_small\_en](https://www.kaggle.com/models/keras/deberta_v3/keras/deberta_v3_extra_small_en/3) | 70.68M | 12-layer DeBERTaV3 model where case is maintained. Trained on English Wikipedia, BookCorpus and OpenWebText. |
| [deberta\_v3\_small\_en](https://www.kaggle.com/models/keras/deberta_v3/keras/deberta_v3_small_en/3) | 141.30M | 6-layer DeBERTaV3 model where case is maintained. Trained on English Wikipedia, BookCorpus and OpenWebText. |
| [deberta\_v3\_base\_en](https://www.kaggle.com/models/keras/deberta_v3/keras/deberta_v3_base_en/3) | 183.83M | 12-layer DeBERTaV3 model where case is maintained. Trained on English Wikipedia, BookCorpus and OpenWebText. |
| [deberta\_v3\_base\_multi](https://www.kaggle.com/models/keras/deberta_v3/keras/deberta_v3_base_multi/3) | 278.22M | 12-layer DeBERTaV3 model where case is maintained. Trained on the 2.5TB multilingual CC100 dataset. |
| [deberta\_v3\_large\_en](https://www.kaggle.com/models/keras/deberta_v3/keras/deberta_v3_large_en/3) | 434.01M | 24-layer DeBERTaV3 model where case is maintained. Trained on English Wikipedia, BookCorpus and OpenWebText. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.DebertaV3Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[DebertaV3Backbone model](https://keras.io/keras_hub/api/models/deberta_v3/deberta_v3_backbone/#debertav3backbone-model)

[`DebertaV3Backbone` class](https://keras.io/keras_hub/api/models/deberta_v3/deberta_v3_backbone/#debertav3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/deberta_v3/deberta_v3_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/deberta_v3/deberta_v3_backbone/#tokenembedding-property)