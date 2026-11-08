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
 / [Gemma4](https://keras.io/keras_hub/api/models/gemma4/)
 / Gemma4Backbone model

Gemma4Backbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_backbone.py#L16)

### `Gemma4Backbone` class

Copied!

`keras_hub.models.Gemma4Backbone(     vocabulary_size,     image_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     query_head_dim_normalize=True,     attention_logit_soft_cap=None,     final_logit_soft_cap=None,     use_sliding_window_attention=True,     sliding_window_size=512,     sliding_window_pattern=6,     layer_types=None,     global_head_dim=None,     local_rope_scaling_factor=1.0,     global_rope_scaling_factor=1.0,     vision_encoder=None,     audio_encoder=None,     num_audio_tokens_per_clip=None,     layer_norm_epsilon=1e-06,     use_bidirectional_attention=False,     use_vision_bidirectional_attention=False,     dropout=0,     is_embedding_model=False,     pooling_intermediate_dim=None,     embedding_dim=None,     num_kv_shared_layers=0,     num_global_key_value_heads=None,     hidden_size_per_layer_input=0,     vocab_size_per_layer_input=None,     global_rope_wavelength=None,     local_rope_wavelength=None,     global_rope_partial_rotary_factor=1.0,     use_double_wide_mlp=False,     enable_moe_block=False,     num_experts=None,     expert_intermediate_dim=None,     num_experts_per_token=8,     dtype=None,     **kwargs )`

Gemma4 core network with hyperparameters.

This backbone implements the Gemma4 model architecture. Gemma4 is a multimodal vision-language model (image + text in, text out). The text input is encoded with a scaled embedding layer; images are encoded by a separate vision transformer (`Gemma4VisionEncoder`). After encoding, image embeddings are placed at the correct positions in the text-embedding sequence, and the combined sequence is processed by transformer decoder layers.

Compared to Gemma3, Gemma4 introduces:

*   **Four norms per decoder block** — pre + post for both attention and FFW, always enabled (no `use_post_*_norm` flags).
*   **Q / K / V normalisation** in attention always on.
*   **Attention scaling = 1.0** — Q/K normalisation provides stability instead of the classic `1/sqrt(head_dim)` scaling.
*   **New vision encoder** — uses the same Gemma4 decoder blocks with bidirectional attention, 2D learnable position embeddings, and spatial average-pooling.
*   **Smaller default sliding window** — 512 tokens (vs. 1 024 in Gemma3).
*   **Audio encoder** — an optional Universal Speech Model (USM) conformer that encodes mel spectrograms into audio token embeddings.

For a higher-level object for text generation see [`keras_hub.models.Gemma4CausalLM`](https://keras.io/keras_hub/api/models/gemma4/gemma4_causal_lm#gemma4causallm-class)
.

The default constructor gives a fully customised, randomly initialised Gemma4 model. To load preset weights use the `from_preset` constructor.

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
*   **query\_head\_dim\_normalize**: bool. If `True` normalise query pre-attention using `head_dim`; otherwise use `hidden_dim / num_query_heads`. **Unused in Gemma4 (always Q-normalised via `q_norm`).** Kept for API compatibility. Defaults to `True`.
*   **attention\_logit\_soft\_cap**: `None` or float. Tanh soft-cap on attention logits. Defaults to `None`.
*   **final\_logit\_soft\_cap**: `None` or float. Tanh soft-cap on output logits. Defaults to `None`.
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
*   **num\_audio\_tokens\_per\_clip**: int or `None`. Number of audio soft tokens produced per audio clip (including zero-padded positions). Must be provided when `audio_encoder` is not `None`.
*   **layer\_norm\_epsilon**: float. Epsilon for all RMS norms. Defaults `1e-6`.
*   **use\_bidirectional\_attention**: bool. When `True` the model uses fully bidirectional attention for ALL tokens, e.g. for embedding models. This is distinct from `use_vision_bidirectional_attention` which only affects vision token attention. Defaults to `False`.
*   **use\_vision\_bidirectional\_attention**: bool. When `True`, vision tokens within the same image attend to each other bidirectionally while text tokens remain causal. Corresponds to HF `use_bidirectional_attention: "vision"` (present in 26B and 31B models; `null` for the 2B and 4B models). Defaults to `False`.
*   **dropout**: float. Dropout probability. Defaults to `0`.
*   **is\_embedding\_model**: bool. When `True` add mean-pooling and dense projection heads for embedding models. Defaults to `False`.
*   **pooling\_intermediate\_dim**: int or `None`. Intermediate dimension of the first projection in the pooling head. Required when `is_embedding_model=True`.
*   **embedding\_dim**: int or `None`. Final embedding dimension. Required when `is_embedding_model=True`.
*   **num\_kv\_shared\_layers**: int. Number of trailing decoder layers that share K/V projections with the most recent non-shared layer of the same attention type. Defaults to `0`.
*   **num\_global\_key\_value\_heads**: int or `None`. When set, global attention layers use this many K/V heads instead of `num_key_value_heads` and enable the K=V projection. Defaults to `None`.
*   **hidden\_size\_per\_layer\_input**: int. Size of the per-token, per-layer conditioning vector that gates each decoder layer's output. Set to `0` to disable. Defaults to `0`.
*   **vocab\_size\_per\_layer\_input**: int or `None`. Vocabulary size for the per-layer token embedding table. When `None` falls back to `vocabulary_size`. Defaults to `None`.
*   **use\_double\_wide\_mlp**: bool. When `True`, KV-shared layers (`is_kv_shared_layer=True`) use `2 × intermediate_dim` for their FFW sub-block. Defaults to `False`.
*   **enable\_moe\_block**: bool. When `True`, every decoder layer runs a parallel Mixture-of-Experts path alongside the dense FFW path. The two outputs are summed before the shared post-FFW norm. Requires `num_experts` and `expert_intermediate_dim` to be set. Defaults to `False`.
*   **num\_experts**: int or `None`. Total number of expert MLPs in the MoE bank. Required when `enable_moe_block=True`. Defaults to `None`.
*   **expert\_intermediate\_dim**: int or `None`. Intermediate dimension of each expert MLP. Required when `enable_moe_block=True`. Defaults to `None`.
*   **num\_experts\_per\_token**: int. Top-k experts selected per token by the MoE router. Defaults to `8`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. Compute dtype. Defaults to `None`.

**Examples**

Copied!

`# Load a pretrained Gemma4 backbone (multimodal: text, image, audio, video). model = keras_hub.models.Gemma4Backbone.from_preset("gemma4_instruct_2b")  # Randomly initialized Gemma4 backbone with a custom config. vision_encoder = keras_hub.models.Gemma4VisionEncoder(     image_size=896,     patch_size=14,     pool_size=2,     num_layers=27,     num_heads=16,     head_dim=64,     num_key_value_heads=16,     hidden_dim=1024,     intermediate_dim=4096,     output_dim=2048, ) model = keras_hub.models.Gemma4Backbone(     vocabulary_size=262208,     image_size=896,     num_layers=26,     num_query_heads=8,     num_key_value_heads=4,     hidden_dim=2048,     intermediate_dim=16384,     head_dim=256,     vision_encoder=vision_encoder,     dtype="float32", )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Gemma4Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [gemma4\_instruct\_2b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b_assistant/1) | 77.73M | Gemma 4 E2B MTP Assistant model: 4-layer speculative-decoding assistant for the 2B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b_assistant/1) | 77.73M | Gemma 4 E4B MTP Assistant model: 4-layer speculative-decoding assistant for the 4B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_26b\_a4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b_assistant/1) | 412.76M | Gemma 4 26B A4B MTP Assistant model: 4-layer speculative-decoding assistant for the 26B MoE model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_31b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b_assistant/1) | 454.71M | Gemma 4 31B MTP Assistant model: 4-layer speculative-decoding assistant for the 31B dense model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_2b/2) | 5.10B | Gemma 4 E2B base model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b/2) | 5.10B | Gemma 4 E2B instruction-tuned model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_4b/2) | 7.90B | Gemma 4 E4B base model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b/2) | 7.90B | Gemma 4 E4B instruction-tuned model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_26b_a4b/2) | 26.00B | Gemma 4 26B A4B base model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text pretrained Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_instruct\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b/2) | 26.00B | Gemma 4 26B A4B instruction-tuned model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text instruction-tuned Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_31b/2) | 31.00B | Gemma 4 31B base model: 31B parameter, 60-layer, dense vision+text pretrained Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |
| [gemma4\_instruct\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b/2) | 31.00B | Gemma 4 31B instruction-tuned model: 31B parameter, 60-layer, dense vision+text instruction-tuned Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Gemma4Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Gemma4Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Gemma4Backbone model](https://keras.io/keras_hub/api/models/gemma4/gemma4_backbone/#gemma4backbone-model)

[`Gemma4Backbone` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_backbone/#gemma4backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gemma4/gemma4_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_backbone/#enablelora-method)