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
 / [MetaCLIP 2](https://keras.io/keras_hub/api/models/metaclip_2/)
 / MetaCLIP2TextEncoder

MetaCLIP2TextEncoder
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/metaclip_2/metaclip_2_text_encoder.py#L13)

### `MetaCLIP2TextEncoder` class

Copied!

`keras_hub.models.MetaCLIP2TextEncoder(     vocabulary_size,     embedding_dim,     hidden_dim,     num_layers,     num_heads,     intermediate_dim,     intermediate_activation="quick_gelu",     intermediate_output_index=None,     max_sequence_length=77,     dtype=None,     name=None,     **kwargs )`

MetaCLIP 2 text encoder.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **embedding\_dim**: int. The output dimension of the embedding layer.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **intermediate\_activation**: activation function. The activation that is used for the first Dense layer in a two-layer feedforward network for each transformer. Defaults to "quick\_gelu".
*   **intermediate\_output\_index**: optional int. The index of the intermediate output. If specified, the output will include an additional `"intermediate_output"` key.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. Defaults to 77. Used for pooling. Defaults to 2.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done at float32 precision regardless of dtype.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MetaCLIP2TextEncoder.from_preset(preset, load_weights=True, **kwargs)`

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

[MetaCLIP2TextEncoder](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_text_encoder/#metaclip2textencoder)

[`MetaCLIP2TextEncoder` class](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_text_encoder/#metaclip2textencoder-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_text_encoder/#frompreset-method)