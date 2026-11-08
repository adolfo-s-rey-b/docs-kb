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
 / [EmbeddingGemma2](https://keras.io/keras_hub/api/models/embedding_gemma2/)
 / EmbeddingGemma2Backbone model

EmbeddingGemma2Backbone model
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_backbone.py#L31)

### `EmbeddingGemma2Backbone` class

Copied!

`keras_hub.models.EmbeddingGemma2Backbone(     vocabulary_size,     image_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     use_sliding_window_attention=True,     sliding_window_size=512,     sliding_window_pattern=6,     layer_types=None,     global_head_dim=None,     local_rope_scaling_factor=1.0,     global_rope_scaling_factor=1.0,     vision_encoder=None,     audio_encoder=None,     layer_norm_epsilon=1e-06,     dropout=0,     embedding_dim=None,     num_global_key_value_heads=None,     hidden_size_per_layer_input=0,     global_rope_wavelength=None,     local_rope_wavelength=None,     global_rope_partial_rotary_factor=1.0,     dtype=None,     **kwargs )`

EmbeddingGemma 2 core network with hyperparameters.

This backbone implements the EmbeddingGemma 2 encoder: the Gemma 4 text stack run with fully bidirectional attention, followed by a dense `embedding_projection` applied to every token's final hidden state. Mean pooling and L2 normalisation live in [`keras_hub.models.EmbeddingGemma2TextEmbedder`](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_text_embedder#embeddinggemma2textembedder-class)
.

Images, video frames and audio clips are encoded by the optional `vision_encoder` (`Gemma4VisionEncoder`) and `audio_encoder` (`Gemma4AudioEncoder`); their soft tokens are interleaved into the text embedding sequence at the placeholder positions before the encoder blocks run.

The default constructor gives a fully customised, randomly initialised model. To load preset weights use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **image\_size**: int. The spatial resolution of images (height = width). Stored as a config value for serialization purposes only; it does not affect the backbone's forward pass. Image patching and resizing are handled by [`keras_hub.layers.EmbeddingGemma2ImageConverter`](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_image_converter#embeddinggemma2imageconverter-class)
     before data reaches the backbone. The `vision_encoder` has its own `image_size` parameter that controls position embedding sizes.
*   **num\_layers**: int. Number of transformer decoder layers.
*   **num\_query\_heads**: int. Number of query heads per attention layer.
*   **num\_key\_value\_heads**: int. Number of key/value heads (GQA).
*   **hidden\_dim**: int. Hidden state dimension at the end of each layer.
*   **intermediate\_dim**: int. First dense layer output dimension in each FFW sub-block.
*   **head\_dim**: int. Per-head dimension in the encoder attention.
*   **use\_sliding\_window\_attention**: bool. Whether to use sliding-window attention on the local layers. Defaults to `True`.
*   **sliding\_window\_size**: int. Size of the local attention window. Defaults to `512`.
*   **sliding\_window\_pattern**: int. Repeat period of the local/global attention pattern. The last layer in each group of this many consecutive layers uses global attention; all others use local (sliding-window) attention. Defaults to `6`.
*   **layer\_types**: list of str or `None`. Explicit specification of the attention type for every layer sequentially (e.g. `"full_attention"`, `"sliding_attention"`). When `None`, type sequence is derived from `sliding_window_pattern`. Defaults to `None`.
*   **global\_head\_dim**: int or `None`. Per-head dimension used specifically for global attention layers. When `None`, `head_dim` is used for all layers. Defaults to `None`.
*   **local\_rope\_scaling\_factor**: float. RoPE scaling factor for local layers. Defaults to `1.0`.
*   **global\_rope\_scaling\_factor**: float. RoPE scaling factor for global layers. Defaults to `1.0`.
*   **global\_rope\_partial\_rotary\_factor**: float. Fraction of each head dimension that receives rotary position embeddings in global attention layers. Only the first `int(factor * head_dim)` dimensions are rotated; the remainder are left unchanged (NoPE). Local layers always use full RoPE (`factor = 1.0`). Defaults to `1.0`.
*   **vision\_encoder**: [`keras_hub.models.Gemma4VisionEncoder`](https://keras.io/keras_hub/api/models/gemma4/gemma4_vision_encoder#gemma4visionencoder-class)
     or `None`. When `None` the model processes no images.
*   **audio\_encoder**: [`keras_hub.models.Gemma4AudioEncoder`](https://keras.io/keras_hub/api/models/gemma4/gemma4_audio_encoder#gemma4audioencoder-class)
     or `None`. When `None` the model processes no audio.
*   **layer\_norm\_epsilon**: float. Epsilon for all RMS norms. Defaults `1e-6`.
*   **dropout**: float. Dropout probability. Defaults to `0`.
*   **embedding\_dim**: int. Output dimension of the final dense `embedding_projection` applied to every token's hidden state.
*   **num\_global\_key\_value\_heads**: int or `None`. When set, global attention layers use this many K/V heads instead of `num_key_value_heads` (separate K and V projections are kept). Defaults to `None`.
*   **hidden\_size\_per\_layer\_input**: int. Size of the per-token, per-layer conditioning vector that gates each decoder layer's output. Set to `0` to disable. Defaults to `0`.
*   \_\_ dtype\_\_: string or `keras.mixed_precision.DTypePolicy`. Compute dtype. Defaults to `None`.

**Examples**

Copied!

`# Load a pretrained EmbeddingGemma 2 backbone. model = keras_hub.models.EmbeddingGemma2Backbone.from_preset(     "embedding_gemma2" )  # Randomly initialised text-only backbone with a custom config. model = keras_hub.models.EmbeddingGemma2Backbone(     vocabulary_size=262144,     image_size=896,     num_layers=24,     num_query_heads=4,     num_key_value_heads=2,     hidden_dim=512,     intermediate_dim=2048,     head_dim=256,     embedding_dim=768,     dtype="float32", )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`EmbeddingGemma2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.EmbeddingGemma2Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`EmbeddingGemma2Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[EmbeddingGemma2Backbone model](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone/#embeddinggemma2backbone-model)

[`EmbeddingGemma2Backbone` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone/#embeddinggemma2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_backbone/#enablelora-method)