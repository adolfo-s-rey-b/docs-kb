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
 / [T5Gemma2](https://keras.io/keras_hub/api/models/t5gemma2/)
 / T5Gemma2Backbone model

T5Gemma2Backbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_backbone.py#L17)

### `T5Gemma2Backbone` class

Copied!

`keras_hub.models.T5Gemma2Backbone(     vocabulary_size,     encoder_hidden_dim,     encoder_intermediate_dim,     encoder_num_layers,     encoder_num_attention_heads,     encoder_num_key_value_heads,     encoder_head_dim,     encoder_layer_types,     decoder_hidden_dim,     decoder_intermediate_dim,     decoder_num_layers,     decoder_num_attention_heads,     decoder_num_key_value_heads,     decoder_head_dim,     decoder_layer_types,     dropout_rate=0.0,     rms_norm_eps=1e-06,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate",     tie_word_embeddings=True,     initializer_range=0.02,     attention_dropout=0.0,     sliding_window=None,     cross_attention_hidden_size=None,     attn_logit_softcapping=None,     final_logit_softcapping=None,     rope_max_wavelength=10000.0,     global_rope_scaling_factor=1.0,     encoder_rope_max_wavelength=None,     encoder_global_rope_scaling_factor=None,     use_query_key_norm=True,     vision_encoder=None,     eoi_token_index=256000,     dtype=None,     **kwargs )`

T5Gemma2 backbone model.

This class implements the encoder-decoder backbone of the T5Gemma2 model. T5Gemma2 is based on Gemma3 and features merged self+cross attention in the decoder (unlike T5Gemma which used separate attention sublayers), Gemma3-style Q/K normalization, and per-layer-type sliding window attention patterns.

When a `vision_encoder` is provided, the model also accepts image inputs. Images are processed by the vision encoder and the resulting embeddings are interleaved into the encoder text embeddings at positions marked by image placeholder tokens.

**Arguments**

*   **vocabulary\_size**: int, The size of the vocabulary.
*   **encoder\_hidden\_dim**: int, Encoder hidden dimensionality.
*   **encoder\_intermediate\_dim**: int, Encoder FFN intermediate size.
*   **encoder\_num\_layers**: int, Number of encoder layers.
*   **encoder\_num\_attention\_heads**: int, Encoder attention heads.
*   **encoder\_num\_key\_value\_heads**: int, Encoder KV heads for GQA.
*   **encoder\_head\_dim**: int, Encoder head dimensionality.
*   **encoder\_layer\_types**: list of str, Attention layer types for each encoder layer (`"full_attention"` or `"sliding_attention"`).
*   **decoder\_hidden\_dim**: int, Decoder hidden dimensionality.
*   **decoder\_intermediate\_dim**: int, Decoder FFN intermediate size.
*   **decoder\_num\_layers**: int, Number of decoder layers.
*   **decoder\_num\_attention\_heads**: int, Decoder attention heads.
*   **decoder\_num\_key\_value\_heads**: int, Decoder KV heads for GQA.
*   **decoder\_head\_dim**: int, Decoder head dimensionality.
*   **decoder\_layer\_types**: list of str, Attention layer types for each decoder layer.
*   **dropout\_rate**: float, Dropout rate. Defaults to `0.0`.
*   **rms\_norm\_eps**: float, RMS normalization epsilon. Defaults to `1e-6`.
*   **query\_pre\_attn\_scalar**: float, Query scalar. Defaults to `1.0`.
*   **attention\_bias**: bool, Attention bias. Defaults to `False`.
*   **hidden\_activation**: str, FFN activation. Defaults to `"gelu_approximate"`.
*   **tie\_word\_embeddings**: bool, Tie input/output embeddings. Defaults to `True`.
*   **initializer\_range**: float, Initializer range. Defaults to `0.02`.
*   **attention\_dropout**: float, Attention dropout. Defaults to `0.0`.
*   **sliding\_window**: int, optional, Sliding window size.
*   **cross\_attention\_hidden\_size**: int, optional, Cross-attention hidden size. Defaults to `encoder_hidden_dim`.
*   **attn\_logit\_softcapping**: float, optional, Attention softcapping.
*   **final\_logit\_softcapping**: float, optional, Final logit softcapping.
*   **rope\_max\_wavelength**: float, RoPE maximum wavelength. Defaults to `10000.0`.
*   **global\_rope\_scaling\_factor**: float, RoPE scaling factor for full attention layers. Defaults to `1.0`.
*   **use\_query\_key\_norm**: bool, Whether to use Gemma3-style Q/K normalization. Defaults to `True`.
*   **vision\_encoder**: optional, A `Gemma3VisionEncoder` instance for multimodal inputs. When `None`, the model is text-only.
*   **eoi\_token\_index**: int, Token index for the end-of-image token. Defaults to `256000`.
*   **dtype**: dtype for computations. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments.

**Examples**

Copied!

`import numpy as np from keras_hub.models import T5Gemma2Backbone  input_data = {     "encoder_token_ids": np.ones(shape=(1, 12), dtype="int32"),     "encoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], dtype="int32"     ),     "decoder_token_ids": np.ones(shape=(1, 8), dtype="int32"),     "decoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1]], dtype="int32"     ), }  model = T5Gemma2Backbone(     vocabulary_size=32000,     encoder_hidden_dim=256,     encoder_intermediate_dim=512,     encoder_num_layers=4,     encoder_num_attention_heads=4,     encoder_num_key_value_heads=2,     encoder_head_dim=64,     encoder_layer_types=["full_attention"] * 4,     decoder_hidden_dim=256,     decoder_intermediate_dim=512,     decoder_num_layers=4,     decoder_num_attention_heads=4,     decoder_num_key_value_heads=2,     decoder_head_dim=64,     decoder_layer_types=["full_attention"] * 4,     dropout_rate=0.1,     rms_norm_eps=1e-6,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate", ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`T5Gemma2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.T5Gemma2Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[T5Gemma2Backbone model](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_backbone/#t5gemma2backbone-model)

[`T5Gemma2Backbone` class](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_backbone/#t5gemma2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_backbone/#tokenembedding-property)