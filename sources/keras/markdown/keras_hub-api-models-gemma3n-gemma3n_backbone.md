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
 / [Gemma3n](https://keras.io/keras_hub/api/models/gemma3n/)
 / Gemma3nBackbone model

Gemma3nBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3n/gemma3n_backbone.py#L456)

### `Gemma3nBackbone` class

Copied!

`keras_hub.models.Gemma3nBackbone(     text_vocab_size,     text_hidden_size,     num_hidden_layers,     pad_token_id,     num_attention_heads,     num_key_value_heads,     head_dim,     intermediate_size,     hidden_activation,     layer_types,     sliding_window,     rope_theta,     max_position_embeddings,     vocab_size_per_layer_input,     hidden_size_per_layer_input,     altup_num_inputs,     laurel_rank,     attention_bias=False,     attention_dropout=0.0,     rope_scaling=None,     rope_local_base_freq=10000.0,     activation_sparsity_pattern=None,     altup_coef_clip=None,     altup_active_idx=0,     altup_correct_scale=True,     num_kv_shared_layers=0,     final_logit_soft_cap=None,     vision_encoder_config=None,     vision_hidden_size=2048,     vision_vocab_size=128,     vision_vocab_offset=100,     vision_soft_tokens_per_image=256,     image_token_id=98,     audio_encoder_config=None,     audio_hidden_size=32,     audio_vocab_size=128,     audio_vocab_offset=228,     audio_soft_tokens_per_image=188,     audio_token_id=99,     rms_norm_eps=1e-06,     dtype=None,     **kwargs )`

The Gemma3n model backbone.

This model is a multimodal transformer that can process text, image, and audio inputs. It consists of a text decoder and optional vision and audio encoders.

**Arguments**

*   **text\_vocab\_size**: int. The size of the text vocabulary.
*   **text\_hidden\_size**: int. The hidden size of the text model.
*   **num\_hidden\_layers**: int. The number of hidden layers in the text model.
*   **pad\_token\_id**: int. The ID of the padding token.
*   **num\_attention\_heads**: int. The number of attention heads in the text model.
*   **num\_key\_value\_heads**: int. The number of key-value heads for GQA.
*   **head\_dim**: int. The dimension of each attention head.
*   **intermediate\_size**: list\[int\]. A list of intermediate sizes for the MLP layers.
*   **hidden\_activation**: str. The activation function for the MLP layers.
*   **layer\_types**: list\[str\]. A list of layer types ('full\_attention' or 'sliding\_attention').
*   **sliding\_window**: int. The sliding window size for sliding window attention.
*   **rope\_theta**: float. The theta value for RoPE.
*   **max\_position\_embeddings**: int. The maximum sequence length.
*   **vocab\_size\_per\_layer\_input**: int. The vocab size for per-layer inputs.
*   **hidden\_size\_per\_layer\_input**: int. The hidden size for per-layer inputs.
*   **altup\_num\_inputs**: int. The number of inputs for the Alternating Updates (AltUp) mechanism.
*   **laurel\_rank**: int. The rank for the Laurel block.
*   **attention\_bias**: bool. Whether to use a bias in the attention projections.
*   **attention\_dropout**: float. The dropout rate for attention weights.
*   **rope\_scaling**: float. The scaling factor for RoPE.
*   **rope\_local\_base\_freq**: float. The base frequency for local RoPE.
*   **activation\_sparsity\_pattern**: list\[float\]. The sparsity pattern for MLP activations.
*   **altup\_coef\_clip**: float. The coefficient clipping value for AltUp.
*   **altup\_active\_idx**: int. The active index for AltUp.
*   **altup\_correct\_scale**: bool. Whether to correct the scale in AltUp.
*   **num\_kv\_shared\_layers**: int. The number of shared KV layers.
*   **vision\_encoder\_config**: dict. The config for the vision encoder.
*   **vision\_hidden\_size**: int. The hidden size of the vision embeddings.
*   **vision\_vocab\_size**: int. The vocabulary size for vision tokens.
*   **vision\_vocab\_offset**: int. The vocabulary offset for vision tokens.
*   **vision\_soft\_tokens\_per\_image**: int. The number of tokens per image.
*   **image\_token\_id**: int. The special token ID for images.
*   **audio\_encoder\_config**: dict. The config for the audio encoder.
*   **audio\_hidden\_size**: int. The hidden size of the audio embeddings.
*   **audio\_vocab\_size**: int. The vocabulary size for audio tokens.
*   **audio\_vocab\_offset**: int. The vocabulary offset for audio tokens.
*   **audio\_soft\_tokens\_per\_image**: int. The number of tokens per audio clip.
*   **audio\_token\_id**: int. The special token ID for audio.
*   **rms\_norm\_eps**: float. The epsilon value for RMS normalization.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Defaults to `None`.

**Example**

Copied!

`import numpy as np from keras_hub.src.models.gemma3n.gemma3n_audio_encoder import (     Gemma3nAudioEncoder, ) from keras_hub.src.models.gemma3n.gemma3n_backbone import Gemma3nBackbone from keras_hub.src.models.mobilenetv5.mobilenetv5_backbone import (     MobileNetV5Backbone, ) from keras_hub.src.models.mobilenetv5.mobilenetv5_builder import (     convert_arch_def_to_stackwise, )  # Vision encoder config. vision_arch_def = [["er_r1_k3_s1_e1_c16"]] stackwise_params = convert_arch_def_to_stackwise(vision_arch_def) vision_encoder = MobileNetV5Backbone(     **stackwise_params,     num_features=4,     image_shape=(224, 224, 3),     use_msfa=False, )  # Audio encoder config. audio_encoder = Gemma3nAudioEncoder(     hidden_size=8,     input_feat_size=32,     sscp_conv_channel_size=[4, 8],     sscp_conv_kernel_size=[(3, 3), (3, 3)],     sscp_conv_stride_size=[(2, 2), (2, 2)],     sscp_conv_group_norm_eps=1e-5,     conf_num_hidden_layers=1,     rms_norm_eps=1e-6,     gradient_clipping=1.0,     conf_residual_weight=0.5,     conf_num_attention_heads=1,     conf_attention_chunk_size=4,     conf_attention_context_right=5,     conf_attention_context_left=5,     conf_attention_logit_cap=50.0,     conf_conv_kernel_size=5,     conf_reduction_factor=1, )  # Backbone config. backbone = Gemma3nBackbone(     text_vocab_size=50,     text_hidden_size=8,     num_hidden_layers=1,     pad_token_id=0,     num_attention_heads=1,     num_key_value_heads=1,     head_dim=8,     intermediate_size=[16],     hidden_activation="gelu_approximate",     layer_types=["full_attention"],     sliding_window=4,     rope_theta=10000.0,     max_position_embeddings=16,     vocab_size_per_layer_input=50,     hidden_size_per_layer_input=2,     altup_num_inputs=2,     laurel_rank=1,     vision_encoder_config=vision_encoder.get_config(),     vision_hidden_size=16,     audio_encoder_config=audio_encoder.get_config(),     audio_hidden_size=8, )  # Create dummy inputs. input_data = {     "token_ids": np.random.randint(0, 50, size=(1, 16), dtype="int32"),     "attention_mask": np.ones((1, 1, 16, 16), dtype=bool),     "images": np.random.rand(1, 1, 224, 224, 3).astype("float32"),     "input_features": np.random.rand(1, 16, 32).astype("float32"),     "input_features_mask": np.zeros((1, 16), dtype=bool), }  # Forward pass. outputs = backbone(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Gemma3nBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [gemma3n\_e2b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b/1) | 5.44B | Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e2b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b_it/1) | 5.44B | Instruction-tuned Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b/1) | 7.85B | Gemma 3n E4B multimodal with ( ~8B total ~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b_it/1) | 7.85B | Instruction-tuned Gemma 3n E4B multimodal with ~8B total (~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Gemma3nBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Gemma3nBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Gemma3nBackbone model](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone/#gemma3nbackbone-model)

[`Gemma3nBackbone` class](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone/#gemma3nbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone/#enablelora-method)