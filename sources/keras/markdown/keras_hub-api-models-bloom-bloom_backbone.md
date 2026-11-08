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
 / [Bloom](https://keras.io/keras_hub/api/models/bloom/)
 / BloomBackbone model

BloomBackbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bloom/bloom_backbone.py#L13)

### `BloomBackbone` class

Copied!

`keras_hub.models.BloomBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.0,     layer_norm_epsilon=1e-05,     dtype=None,     **kwargs )`

A BLOOM decoder network.

This network implements a Transformer-based decoder network, BigScience Language Open-science Open-access Multilingual (BLOOM), as descriped in ["BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"](https://arxiv.org/pdf/2211.05100.pdf)
.

The default constructor gives a fully customizable, randomly initialized Bloom model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://huggingface.co/spaces/bigscience/license)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The dimensionality of the embeddings and hidden states.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in the MLP network of each transformer.
*   **dropout**: float. Dropout probability for the Transformer decoder.
*   **layer\_norm\_epsilon**: float. Epsilon for the layer normalization layers in the transformer decoder.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained BLOOM decoder. model = keras_hub.models.BloomBackbone.from_preset("bloom_560m_multi") model(input_data)  # Randomly initialized BLOOM decoder with a custom config. model = keras_hub.models.BloomBackbone(     vocabulary_size=10,     num_layers=2,     num_heads=2,     hidden_dim=32,     intermediate_dim=32*4,     dropout=0.0,     layer_norm_epsilon=1e-5, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`BloomBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [bloom\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_560m_multi/4) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_560m_multi/2) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. finetuned on crosslingual task mixture (xP3) dataset. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.BloomBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`BloomBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[BloomBackbone model](https://keras.io/keras_hub/api/models/bloom/bloom_backbone/#bloombackbone-model)

[`BloomBackbone` class](https://keras.io/keras_hub/api/models/bloom/bloom_backbone/#bloombackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bloom/bloom_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/bloom/bloom_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/bloom/bloom_backbone/#enablelora-method)