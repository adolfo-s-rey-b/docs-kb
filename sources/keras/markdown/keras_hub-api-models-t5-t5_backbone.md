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
 / [T5](https://keras.io/keras_hub/api/models/t5/)
 / T5Backbone model

T5Backbone model
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5/t5_backbone.py#L10)

### `T5Backbone` class

Copied!

`keras_hub.models.T5Backbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     key_value_dim=None,     dropout=0.1,     activation="relu",     use_gated_activation=True,     layer_norm_epsilon=1e-06,     tie_embedding_weights=True,     dtype=None,     **kwargs )`

T5 encoder-decoder backbone model.

T5 is a LLM pretrained on a mix of unsupervised and supervised tasks, where each task is converted to a sequence-to-sequence format. T5 works well on a variety of tasks out-of-the-box by prepending various prefixex to the input sequence, e.g., for translation: `"translate English to German: ..."`, for summarization: `"summarize: ..."`.

T5 was introduced in [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

The default constructor gives a fully customizable, randomly initialized T5 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of Transformer layers.
*   **num\_heads**: int. The number of attention heads for each Transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The hidden size of the Transformer layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each Transformer layer.
*   **key\_value\_dim**: int. The dimension of each head of the key/value projections in the multi-head attention layers. Defaults to hidden\_dim / num\_heads.
*   **dropout**: float. Dropout probability for the Transformer layers.
*   **activation**: string. The activation function to use in the dense blocks of the Transformer Layers.
*   **use\_gated\_activation**: boolean. Whether to use activation gating in the inner dense blocks of the Transformer layers. When used with the GELU activation function, this is referred to as GEGLU (gated GLU) from https://arxiv.org/pdf/2002.05202. The original T5 architecture didn't use gating, but more recent versions do. Defaults to `True`.
*   **layer\_norm\_epsilon**: float. Epsilon factor to be used in the layer normalization layers in the Transformer layers.
*   **tie\_embedding\_weights**: boolean. If `True`, the weights of the token embedding and the weights projecting language model outputs from `hidden_dim`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`T5Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [t5\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_small_multi/3) | 60.51M | 6-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_small](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_small/2) | 60.51M |     |
| [flan\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_small_multi/3) | 76.96M | 8-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_base_multi/3) | 222.90M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_base](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_base/2) | 247.58M |     |
| [flan\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_base_multi/3) | 247.58M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_large_multi/3) | 737.67M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_large](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_large/2) | 750.25M |     |
| [flan\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_large_multi/3) | 783.15M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_xl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xl/2) | 2.85B |     |
| [t5\_1.1\_xxl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xxl/2) | 11.14B |     |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.T5Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[T5Backbone model](https://keras.io/keras_hub/api/models/t5/t5_backbone/#t5backbone-model)

[`T5Backbone` class](https://keras.io/keras_hub/api/models/t5/t5_backbone/#t5backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5/t5_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/t5/t5_backbone/#tokenembedding-property)