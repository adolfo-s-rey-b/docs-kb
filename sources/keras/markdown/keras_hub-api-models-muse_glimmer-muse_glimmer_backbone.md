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
 / [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
 / MuseGlimmerBackbone model

MuseGlimmerBackbone model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_backbone.py#L21)

### `MuseGlimmerBackbone` class

Copied!

`keras_hub.models.MuseGlimmerBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     sliding_window_size=2048,     rope_max_wavelength=500000.0,     rms_norm_eps=1e-05,     post_norm_eps=1e-08,     qk_scale_factor=3.87,     output_multiplier=0.19611613513818404,     final_logit_softcapping=20.0,     layer_types=None,     vision_encoder=None,     projector_hidden_dim=None,     projector_hidden_act="gelu",     dropout=0,     use_bidirectional_attention=False,     context_projection_layer_ids=None,     use_external_embeddings=False,     enable_qk_scale_and_gate=True,     qk_norm_with_scale=False,     use_sandwich_norm=True,     use_centered_norm=True,     dtype=None,     **kwargs )`

MuseGlimmer core network with hyperparameters.

MuseGlimmer is a dense causal decoder-transformer. It uses Gemma-lineage normalization and softcapping. It uses a Llama3-lineage BPE tokenizer. The backbone can fuse a windowed-attention perception encoder (`MuseGlimmerVisionEncoder`) for image-text-to-text generation.

The text tower alternates sliding-window and full attention every 4 layers. Full-attention layers receive no rotary position encoding (NoPE). Each layer applies a scaleless QK-RMSNorm. Each layer also applies an extra `qk_scale_factor` to the query. Each layer gates the attention output with a sigmoid of the pre-attention normed input.

When a vision encoder is attached, its output passes through a double-activation adapter, a projection, and a final scaleless RMSNorm. The backbone then scatters the result into the text embedding sequence. See `modeling_muse_glimmer.py`, `MuseGlimmerModel.get_image_features`.

This class also supports the DFlash speculative-decoding assistant configuration (`meta-models/Muse-Glimmer-30B-assistant`, see `modeling_muse_glimmer_assistant.py`). Seven opt-in flags enable it. Each flag defaults to the main model behavior: `use_bidirectional_attention`, `context_projection_layer_ids`, `use_external_embeddings`, `enable_qk_scale_and_gate`, `qk_norm_with_scale`, `use_sandwich_norm`, and `use_centered_norm`.

The assistant configuration has no token embedding of its own. It consumes `noise_embeds` instead of `token_ids`. `noise_embeds` is a window of denoising-block hidden states. The assistant also consumes `context_hidden_states`. This input holds hidden states from several layers of a separate, larger main model, concatenated.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary. The backbone ignores this argument when `use_external_embeddings=True`.
*   **num\_layers**: int. The number of transformer decoder layers.
*   **num\_query\_heads**: int. The number of query attention heads.
*   **num\_key\_value\_heads**: int. The number of key/value attention heads.
*   **hidden\_dim**: int. The transformer hidden dimension.
*   **intermediate\_dim**: int. The SwiGLU MLP intermediate dimension.
*   **head\_dim**: int. Per-head dimension.
*   **sliding\_window\_size**: int. Sliding window size for `"sliding_attention"` layers. Defaults to `2048`.
*   **rope\_max\_wavelength**: float. RoPE base theta for layers that use rotary position embeddings. Defaults to `500000.0`.
*   **rms\_norm\_eps**: float. Epsilon for pre-sublayer norms, QK-norm, the normed embedding, and the final sequence norm. Defaults to `1e-5`.
*   **post\_norm\_eps**: float. Epsilon for the post-sublayer sandwich norms. Defaults to `1e-8`.
*   **qk\_scale\_factor**: float. Extra multiplier applied to Q after QK-norm, on top of the standard `1/sqrt(head_dim)` attention scaling. Defaults to `3.87`.
*   **output\_multiplier**: float. Scale applied to logits before the final tanh softcap. Defaults to `0.19611613513818404`.
*   **final\_logit\_softcapping**: float. Softcap value `T` in `T * tanh(logits / T)`. Defaults to `20.0`.
*   **layer\_types**: list of str or `None`. Per-layer `"sliding_attention"` or `"full_attention"`. Defaults to full attention on every 4th layer from the end. All other layers use sliding attention. Full-attention layers use NoPE (no rotary embedding) in the target text tower only. Assistant layers always use RoPE.
*   **vision\_encoder**: MuseGlimmerVisionEncoder or None. Use `None` for a text-only model.
*   **projector\_hidden\_dim**: int or `None`. Intermediate/output dimension of the multimodal adapter. Required if `vision_encoder` is set.
*   **projector\_hidden\_act**: str. Activation for the adapter and the top-level projection. Defaults to `"gelu"`.
*   **dropout**: float. Dropout probability. Defaults to `0`.
*   **use\_bidirectional\_attention**: bool. Assistant configuration only. If `True`, every decoder layer attends to all positions and to unmasked context. If `False`, the attention is causal. Defaults to `False`.
*   **context\_projection\_layer\_ids**: list of int or `None`. Assistant configuration only. When set, the backbone builds a `MuseGlimmerContextProjection` sub-layer. The backbone then accepts a `context_hidden_states` input of shape `(batch, sequence, len(context_projection_layer_ids) * hidden_dim)`. The sub-layer projects this input to `hidden_dim`. Every decoder layer receives the result as cross-model context for K/V. Defaults to `None`.
*   **use\_external\_embeddings**: bool. Assistant configuration only. If `True`, the backbone skips `ReversibleEmbedding` and the `token_ids` input. The backbone instead accepts a `noise_embeds` float input of shape `(batch, sequence, hidden_dim)`. The transformer stack receives this input directly. Defaults to `False`.
*   **enable\_qk\_scale\_and\_gate**: bool. The backbone passes this value to `MuseGlimmerTextAttention` in every decoder layer. Defaults to `True`. The assistant configuration sets this to `False`.
*   **qk\_norm\_with\_scale**: bool. The backbone passes this value to `MuseGlimmerTextAttention` in every decoder layer. Defaults to `False`. The assistant configuration sets this to `True`.
*   **use\_sandwich\_norm**: bool. The backbone passes this value to every decoder layer. If `False`, the layer skips the two post-sublayer sandwich norms. Defaults to `True`. The assistant configuration sets this to `False`.
*   **use\_centered\_norm**: bool. The backbone passes this value to every decoder layer. If `False`, the layer builds `input_layernorm` and `pre_feedforward_layernorm` as plain RMSNorm. Otherwise, they use the centered `(1 + weight)` variant. Defaults to `True`. The assistant configuration sets this to `False`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1] * 10 + [0] * 2], dtype="int32"), }  # Pretrained MuseGlimmer decoder. model = keras_hub.models.MuseGlimmerBackbone.from_preset(     "muse_glimmer_30b" ) model(input_data)  # Randomly initialized text-only MuseGlimmer decoder. model = keras_hub.models.MuseGlimmerBackbone(     vocabulary_size=1000,     num_layers=4,     num_query_heads=4,     num_key_value_heads=2,     hidden_dim=64,     intermediate_dim=128,     head_dim=16, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MuseGlimmerBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.MuseGlimmerBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`MuseGlimmerBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[MuseGlimmerBackbone model](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone/#museglimmerbackbone-model)

[`MuseGlimmerBackbone` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone/#museglimmerbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone/#enablelora-method)