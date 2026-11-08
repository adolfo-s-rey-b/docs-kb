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
 / [XLNet](https://keras.io/keras_hub/api/models/xlnet/)
 / XLNetBackbone model

XLNetBackbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/xlnet/xlnet_backbone.py#L13)

### `XLNetBackbone` class

Copied!

`keras_hub.models.XLNetBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.0,     activation="gelu",     kernel_initializer_range=0.02,     bias_initializer="zeros",     dtype=None,     **kwargs )`

XLNet encoder network.

This class implements a XLNet Transformer.

The default constructor gives a fully customizable, randomly initialized XLNet encoder with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Attributes**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer encoder layers.
*   **num\_heads**: int, the number of heads in the `keras.layers.TwoStreamRelativeAttention` layer.
*   **hidden\_dim**: int, the size hidden states.
*   **intermediate\_dim**: int, the hidden size of feedforward network.
*   **dropout**: float, defaults to 0.0 the dropout value, shared by `keras.layers.TwoStreamRelativeAttention` and feedforward network.
*   **activation**: string or `keras.activations`, defaults to "gelu". the activation function of feedforward network.
*   **kernel\_initializer\_range**: int, defaults to 0.02. The kernel initializer range for the dense and relative attention layers.
*   **bias\_initializer**: string or `keras.initializers` initializer, defaults to "zeros". The bias initializer for the dense and multiheaded relative attention layers.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Call arguments**

*   **token\_ids**: Indices of input sequence tokens in the vocabulary of shape `[batch_size, sequence_length]`.
*   **segment\_ids**: Segment token indices to indicate first and second portions of the inputs of shape `[batch_size, sequence_length]`.
*   **padding\_mask**: Mask to avoid performing attention on padding token indices of shape `[batch_size, sequence_length]`.

**Example**

Copied!

`import numpy as np from keras_hub.src.models import XLNetBackbone  input_data = {     "token_ids": np.array(         [460, 5272, 1758, 4905, 9, 4, 3], shape=(1, 7),     ),     "segment_ids": np.array(         [0, 0, 0, 0, 0, 0, 2], shape=(1, 7),     ),     "padding_mask": np.array(         [1, 1, 1, 1, 1, 1, 1], shape=(1, 7)     ), }  # Randomly initialized XLNet encoder with a custom config model = keras_hub.models.XLNetBackbone(     vocabulary_size=32000,     num_layers=12,     num_heads=12,     hidden_dim=768,     intermediate_dim=3072, ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`XLNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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

`keras_hub.models.XLNetBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[XLNetBackbone model](https://keras.io/keras_hub/api/models/xlnet/xlnet_backbone/#xlnetbackbone-model)

[`XLNetBackbone` class](https://keras.io/keras_hub/api/models/xlnet/xlnet_backbone/#xlnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/xlnet/xlnet_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/xlnet/xlnet_backbone/#tokenembedding-property)