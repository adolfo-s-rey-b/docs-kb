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
 / [FNet](https://keras.io/keras_hub/api/models/f_net/)
 / FNetBackbone model

FNetBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/f_net/f_net_backbone.py#L19)

### `FNetBackbone` class

Copied!

`keras_hub.models.FNetBackbone(     vocabulary_size,     num_layers,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=512,     num_segments=4,     dtype=None,     **kwargs )`

A FNet encoder network.

This class implements a bi-directional Fourier Transform-based encoder as described in ["FNet: Mixing Tokens with Fourier Transforms"](https://arxiv.org/abs/2105.03824)
. It includes the embedding lookups and [`keras_hub.layers.FNetEncoder`](https://keras.io/keras_hub/api/modeling_layers/fnet_encoder#fnetencoder-class)
 layers, but not the masked language model or next sentence prediction heads.

The default constructor gives a fully customizable, randomly initialized FNet encoder with any number of layers and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Note: unlike other models, FNet does not take in a `"padding_mask"` input, the `"<pad>"` token is handled equivalently to all other tokens in the input sequence.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of FNet layers.
*   **hidden\_dim**: int. The size of the FNet encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each FNet layer.
*   **dropout**: float. Dropout probability for the embeddings and FNet encoder.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **num\_segments**: int. The number of types that the 'segment\_ids' input can take.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "segment_ids": np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained BERT encoder. model = keras_hub.models.FNetBackbone.from_preset("f_net_base_en") model(input_data)  # Randomly initialized FNet encoder with a custom config. model = keras_hub.models.FNetBackbone(     vocabulary_size=32000,     num_layers=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`FNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [f\_net\_base\_en](https://www.kaggle.com/models/keras/f_net/keras/f_net_base_en/3) | 82.86M | 12-layer FNet model where case is maintained. Trained on the C4 dataset. |
| [f\_net\_large\_en](https://www.kaggle.com/models/keras/f_net/keras/f_net_large_en/3) | 236.95M | 24-layer FNet model where case is maintained. Trained on the C4 dataset. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.FNetBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[FNetBackbone model](https://keras.io/keras_hub/api/models/f_net/f_net_backbone/#fnetbackbone-model)

[`FNetBackbone` class](https://keras.io/keras_hub/api/models/f_net/f_net_backbone/#fnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/f_net/f_net_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/f_net/f_net_backbone/#tokenembedding-property)