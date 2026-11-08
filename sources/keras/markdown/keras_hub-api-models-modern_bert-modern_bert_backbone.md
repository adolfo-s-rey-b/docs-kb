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
 / [ModernBERT](https://keras.io/keras_hub/api/models/modern_bert/)
 / ModernBertBackbone model

ModernBertBackbone model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_backbone.py#L17)

### `ModernBertBackbone` class

Copied!

`keras_hub.models.ModernBertBackbone(     vocabulary_size=50368,     hidden_dim=768,     intermediate_dim=1152,     num_layers=22,     num_heads=12,     local_attention_window=128,     global_attn_every_n_layers=3,     rotary_max_wavelength=160000,     local_rotary_max_wavelength=10000,     layer_norm_epsilon=1e-05,     dtype=None,     **kwargs )`

ModernBERT backbone model.

ModernBERT features Rotary Positional Embeddings (RoPE), GeGLU activations, Layer Normalization, and alternating local and global attention layers.

The backbone accepts a dictionary of token IDs and padding masks, and outputs the raw hidden sequence representations.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **hidden\_dim**: int. The size of the transformer hidden state.
*   **intermediate\_dim**: int. The output dimension of the GeGLU MLP.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_heads**: int. The number of attention heads.
*   **local\_attention\_window**: int. Window size for local attention layers. Defaults to `128`.
*   **global\_attn\_every\_n\_layers**: int. Frequency of global attention layers. Defaults to `3`.
*   **rotary\_max\_wavelength**: int. Max wavelength for RoPE. Defaults to `160000`.
*   **local\_rotary\_max\_wavelength**: int or None. Max wavelength for local RoPE. If `None`, uses `rotary_max_wavelength`. Defaults to `10000`.
*   **layer\_norm\_epsilon**: float. Epsilon used by the Layer Normalization layers. Defaults to `1e-5`.
*   **dtype**: string or `keras.DTypePolicy`. The dtype of the layers. Defaults to `None`.

**Examples**

Copied!

`import keras_hub import numpy as np  # Instantiate a ModernBERT backbone backbone = keras_hub.models.ModernBertBackbone(     vocabulary_size=50368,     hidden_dim=768,     intermediate_dim=1152,     num_layers=22,     num_heads=12, )  # Prepare dummy input data input_data = {     "token_ids": np.random.randint(0, 50368, size=(2, 512), dtype="int32"),     "padding_mask": np.ones((2, 512), dtype="int32"), }  # Extract hidden states outputs = backbone(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`ModernBertBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [modern\_bert\_base\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_base_en/1) | 149.01M | 22-layer ModernBERT Base encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [modern\_bert\_embed\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/modern_bert_embed_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Nomic AI (nomic-ai/modernbert-embed-base). Produces 768-dimensional, L2-normalized, mean-pooled embeddings for inputs of up to 8192 tokens. Prefix queries with 'search\_query: ' and documents with 'search\_document: '. |
| [gte\_modern\_bert\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/gte_modern_bert_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Alibaba-NLP (Alibaba-NLP/gte-modernbert-base). Produces 768-dimensional \[CLS\]-pooled embeddings that are not normalized, so compare them with cosine similarity. The model supports inputs of up to 8192 tokens. |
| [modern\_bert\_large\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_large_en/1) | 394.78M | 28-layer ModernBERT Large encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.ModernBertBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[ModernBertBackbone model](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone/#modernbertbackbone-model)

[`ModernBertBackbone` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone/#modernbertbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_backbone/#tokenembedding-property)