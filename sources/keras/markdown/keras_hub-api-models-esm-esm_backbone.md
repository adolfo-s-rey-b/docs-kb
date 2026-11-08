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
 / [ESM](https://keras.io/keras_hub/api/models/esm/)
 / ESMBackbone model

ESMBackbone model
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/esm/esm_backbone.py#L14)

### `ESMBackbone` class

Copied!

`keras_hub.models.ESMBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     use_bias=True,     activation="gelu",     dropout=0.1,     dtype=None,     max_sequence_length=1024,     max_wavelength=10000,     layer_norm_eps=1e-12,     use_pre_layer_norm=False,     position_embedding_type="rotary",     pad_token_id=0,     **kwargs )`

A ESM2 and ESM encoder network.

This class implements a bi-directional Transformer-based encoder as described in ["ESM"](https://github.com/facebookresearch/esm)
.

The default constructor gives a fully customizable, randomly initialized ESM2 encoder with any number of layers, heads, and embed dim.To load preset architectures and weights, use the `from_preset()` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder. Defaults to 0.1
*   **use\_pre\_layer\_norm**:bool.If true, then layer norm will be used before entering the transformer block. Since it's pre-norm, the default is false.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **position\_embedding\_type**: str. The position embedding type to use. One of "absolute" and "rotary". Use "absolute" for ESM1. Use "rotary" for ESM2. Defaults to "rotary"
*   \_\_max\_wavelength \_\_: int. The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   \_\_activation \_\_:string or keras.activations. The activation to use for the transformer. Defaults to `"gelu"`.
*   **pad\_token\_id**: int.padding token id. Normally 0, but is set to 1 in the esm2 model. Defaults to 0.
*   **dtype**: None or str or keras.mixed\_precision.DTypePolicy. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"), }  # Pretrained ESM2 encoder. model = keras_hub.models.ESM2Backbone.from_preset('hf://facebook/esm2_t6_8M_UR50D') model(input_data)  # Randomly initialized ESM2 encoder with a custom config. model = keras_hub.models.ESM2Backbone(     vocabulary_size=30552,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`ESMBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [esm2\_t6\_8M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t6_8M/1) | 7.41M | 6 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t12\_35M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t12_35M/1) | 33.27M | 12 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t30\_150M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t30_150M/1) | 147.73M | 30 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t33\_650M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t33_650M/1) | 649.40M | 33 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.ESMBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[ESMBackbone model](https://keras.io/keras_hub/api/models/esm/esm_backbone/#esmbackbone-model)

[`ESMBackbone` class](https://keras.io/keras_hub/api/models/esm/esm_backbone/#esmbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/esm/esm_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/esm/esm_backbone/#tokenembedding-property)