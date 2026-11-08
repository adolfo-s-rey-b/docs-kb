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
 / [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
 / DiffusionGemmaBackbone model

DiffusionGemmaBackbone model
============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_backbone.py#L19)

### `DiffusionGemmaBackbone` class

Copied!

`keras_hub.models.DiffusionGemmaBackbone(     vocabulary_size,     image_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     query_head_dim_normalize=True,     attention_logit_soft_cap=None,     final_logit_soft_cap=None,     use_sliding_window_attention=True,     sliding_window_size=512,     sliding_window_pattern=6,     layer_types=None,     global_head_dim=None,     local_rope_scaling_factor=1.0,     global_rope_scaling_factor=1.0,     vision_encoder=None,     layer_norm_epsilon=1e-06,     use_bidirectional_attention=False,     use_vision_bidirectional_attention=False,     dropout=0,     num_global_key_value_heads=None,     global_rope_wavelength=None,     local_rope_wavelength=None,     global_rope_partial_rotary_factor=1.0,     enable_moe_block=False,     num_experts=None,     expert_intermediate_dim=None,     num_experts_per_token=8,     dtype=None,     **kwargs )`

DiffusionGemma core network with hyperparameters.

This backbone implements the DiffusionGemma model architecture. DiffusionGemma extends Gemma4 with discrete block-diffusion generation support: the backbone is called twice per denoising iteration — once as a causal encoder to encode the prompt KV caches, and then repeatedly as a bidirectional decoder over a fixed-length canvas of tokens.

Two diffusion-specific features are always enabled:

*   **`encoder_layer_scalar`** — each decoder block has a second non-trainable scalar used during the causal encoder pass. The standard `layer_scalar` is used for decoder passes.
*   **`DiffusionGemmaSelfConditioning`** — refines canvas embeddings at the start of each denoising step using the logits predicted in the previous step.

In all other respects the architecture matches `Gemma4Backbone`. Shared Gemma4 layer classes (norms, vision encoder, etc.) are imported directly from `keras_hub.models.gemma4`.

The default constructor gives a fully customised, randomly initialised DiffusionGemmaBackbone. To load preset weights use `from_preset`.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **image\_size**: int. The spatial resolution of images (height = width). Stored as a config value for serialization purposes only; it does not affect the backbone's forward pass. Image patching and resizing are handled by [`keras_hub.layers.Gemma4ImageConverter`](https://keras.io/keras_hub/api/models/gemma4/gemma4_image_converter#gemma4imageconverter-class)
     before data reaches the backbone. The `vision_encoder` has its own `image_size` parameter that controls position embedding sizes.
*   **num\_layers**: int. Number of transformer decoder layers.
*   **num\_query\_heads**: int. Number of query heads per attention layer.
*   **num\_key\_value\_heads**: int. Number of key/value heads (GQA).
*   **hidden\_dim**: int. Hidden state dimension at the end of each layer.
*   **intermediate\_dim**: int. First dense layer output dimension in each FFW sub-block.
*   **head\_dim**: int. Per-head dimension in the decoder attention.
*   **query\_head\_dim\_normalize**: bool. If `True` normalise query pre-attention using `head_dim`; otherwise use `hidden_dim / num_query_heads`. **Unused in DiffusionGemma (always Q-normalised via `q_norm`).** Kept for API compatibility. Defaults to `True`.
*   **attention\_logit\_soft\_cap**: `None` or float. Tanh soft-cap on attention logits. Defaults to `None`.
*   **final\_logit\_soft\_cap**: `None` or float. Tanh soft-cap on output logits. Defaults to `None`.
*   **use\_sliding\_window\_attention**: bool. Whether to use sliding-window attention on the local layers. Defaults to `True`.
*   **sliding\_window\_size**: int. Size of the local attention window. Defaults to `512`.
*   **sliding\_window\_pattern**: int. Repeat period of the local/global attention pattern. The last layer in each group of this many consecutive layers uses global attention; all others use local (sliding-window) attention. Defaults to `6`.
*   **layer\_types**: list of str or `None`. Explicit specification of the attention type for every layer sequentially (e.g. `"full_attention"`, `"sliding_attention"`). When `None`, type sequence is derived from `sliding_window_pattern`. Defaults to `None`.
*   **global\_head\_dim**: int or `None`. Per-head dimension used specifically for global attention layers. When `None`, `head_dim` is used for all layers. Defaults to `None`.
*   **local\_rope\_scaling\_factor**: float. RoPE scaling factor for local layers. Defaults to `1.0`.
*   **global\_rope\_scaling\_factor**: float. RoPE scaling factor for global layers. Defaults to `1.0`.
*   **vision\_encoder**: [`keras_hub.models.Gemma4VisionEncoder`](https://keras.io/keras_hub/api/models/gemma4/gemma4_vision_encoder#gemma4visionencoder-class)
     or `None`. When `None` the model processes no images.
*   **layer\_norm\_epsilon**: float. Epsilon for all RMS norms. Defaults to `1e-6`.
*   **use\_bidirectional\_attention**: bool. When `True` the model uses fully bidirectional attention for ALL tokens. Defaults to `False`.
*   **use\_vision\_bidirectional\_attention**: bool. When `True`, image tokens attend to each other bidirectionally during the causal encoder pass. Defaults to `False`.
*   **dropout**: float. Dropout probability. Defaults to `0`.
*   **num\_global\_key\_value\_heads**: int or `None`. When set, global attention layers use this many K/V heads instead of `num_key_value_heads` and enable the K=V projection. Defaults to `None`.
*   **global\_rope\_wavelength**: float or `None`. Base RoPE wavelength for global attention layers. When `None`, defaults to `1_000_000.0`. Defaults to `None`.
*   **local\_rope\_wavelength**: float or `None`. Base RoPE wavelength for local (sliding-window) attention layers. When `None`, defaults to `10_000.0`. Defaults to `None`.
*   **global\_rope\_partial\_rotary\_factor**: float. Fraction of each head dimension that receives rotary position embeddings in global attention layers. Only the first `int(factor * head_dim)` dimensions are rotated; the remainder are left unchanged (NoPE). Local layers always use full RoPE (`factor = 1.0`). Defaults to `1.0`.
*   **enable\_moe\_block**: bool. When `True`, every decoder layer runs a parallel Mixture-of-Experts path alongside the dense FFW path. The two outputs are summed before the shared post-FFW norm. Requires `num_experts` and `expert_intermediate_dim` to be set. Defaults to `False`.
*   **num\_experts**: int or `None`. Total number of expert MLPs in the MoE bank. Required when `enable_moe_block=True`. Defaults to `None`.
*   **expert\_intermediate\_dim**: int or `None`. Intermediate dimension of each expert MLP. Required when `enable_moe_block=True`. Defaults to `None`.
*   **num\_experts\_per\_token**: int. Top-k experts selected per token by the MoE router. Defaults to `8`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. Compute dtype. Defaults to `None`.

**Examples**

Copied!

`model = keras_hub.models.DiffusionGemmaBackbone.from_preset(     "diffusion_gemma_26b_a4b_it" )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DiffusionGemmaBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [diffusion\_gemma\_26b\_a4b\_it](https://www.kaggle.com/models/keras/diffusion-gemma/keras/diffusion_gemma_26b_a4b_it/1) | 25.82B | DiffusionGemma 26B MoE instruction-tuned model. 25.8B total parameters (3.8B active), 30 layers, 128 experts. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.DiffusionGemmaBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`DiffusionGemmaBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[DiffusionGemmaBackbone model](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone/#diffusiongemmabackbone-model)

[`DiffusionGemmaBackbone` class](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone/#diffusiongemmabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone/#enablelora-method)