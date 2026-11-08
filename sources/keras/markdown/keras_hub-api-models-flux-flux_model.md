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
 / [Flux](https://keras.io/keras_hub/api/models/flux/)
 / FluxBackbone model

FluxBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/flux/flux_model.py#L13)

### `FluxBackbone` class

Copied!

`keras_hub.models.FluxBackbone(     input_channels,     hidden_size,     mlp_ratio,     num_heads,     depth,     depth_single_blocks,     axes_dim,     theta,     use_bias,     guidance_embed=False,     image_shape=(None, 768, 3072),     text_shape=(None, 768, 3072),     image_ids_shape=(None, 768, 3072),     text_ids_shape=(None, 768, 3072),     y_shape=(None, 128),     **kwargs )`

Transformer model for flow matching on sequences.

The model processes image and text data with associated positional and timestep embeddings, and optionally applies guidance embedding. Double-stream blocks handle separate image and text streams, while single-stream blocks combine these streams. Ported from: https://github.com/black-forest-labs/flux

**Arguments**

*   **input\_channels**: int. The number of input channels.
*   **hidden\_size**: int. The hidden size of the transformer, must be divisible by `num_heads`.
*   **mlp\_ratio**: float. The ratio of the MLP dimension to the hidden size.
*   **num\_heads**: int. The number of attention heads.
*   **depth**: int. The number of double-stream blocks.
*   **depth\_single\_blocks**: int. The number of single-stream blocks.
*   **axes\_dim**: list\[int\]. A list of dimensions for the positional embedding axes.
*   **theta**: int. The base frequency for positional embeddings.
*   **use\_bias**: bool. Whether to apply bias to the query, key, and value projections.
*   **guidance\_embed**: bool. If True, applies guidance embedding in the model.

**Call arguments**

*   **image**: KerasTensor. Image input tensor of shape (N, L, D) where N is the batch size, L is the sequence length, and D is the feature dimension.
*   **image\_ids**: KerasTensor. Image ID input tensor of shape (N, L, D) corresponding to the image sequences.
*   **text**: KerasTensor. Text input tensor of shape (N, L, D).
*   **text\_ids**: KerasTensor. Text ID input tensor of shape (N, L, D) corresponding to the text sequences.
*   **timesteps**: KerasTensor. Timestep tensor used to compute positional embeddings.
*   **y**: KerasTensor. Additional vector input, such as target values.
*   **guidance**: KerasTensor, optional. Guidance input tensor used in guidance-embedded models.

**Raises**

*   **ValueError**: If `hidden_size` is not divisible by `num_heads`, or if `sum(axes_dim)` is not equal to the positional embedding dimension.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`FluxBackbone.from_preset(preset, load_weights=True, **kwargs)`

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

[FluxBackbone model](https://keras.io/keras_hub/api/models/flux/flux_model/#fluxbackbone-model)

[`FluxBackbone` class](https://keras.io/keras_hub/api/models/flux/flux_model/#fluxbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/flux/flux_model/#frompreset-method)