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
 / [T5Gemma](https://keras.io/keras_hub/api/models/t5gemma/)
 / T5GemmaBackbone model

T5GemmaBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_backbone.py#L15)

### `T5GemmaBackbone` class

Copied!

`keras_hub.models.T5GemmaBackbone(     vocabulary_size,     encoder_hidden_dim,     encoder_intermediate_dim,     encoder_num_layers,     encoder_num_attention_heads,     encoder_num_key_value_heads,     encoder_head_dim,     encoder_layer_types,     decoder_hidden_dim,     decoder_intermediate_dim,     decoder_num_layers,     decoder_num_attention_heads,     decoder_num_key_value_heads,     decoder_head_dim,     decoder_layer_types,     dropout_rate=0.0,     rms_norm_eps=1e-06,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate",     tie_word_embeddings=True,     initializer_range=0.02,     attention_dropout=0.0,     sliding_window=None,     cross_attention_hidden_size=None,     attn_logit_softcapping=None,     final_logit_softcapping=None,     rope_max_wavelength=10000.0,     dtype=None,     **kwargs )`

T5Gemma backbone model.

This class implements the encoder-decoder backbone of the T5Gemma model, consisting of an embedding layer, a stack of encoder layers, and a stack of decoder layers.

**Arguments**

*   **vocabulary\_size**: int, The size of the vocabulary.
*   **encoder\_hidden\_dim**: int, The hidden dimensionality of the encoder.
*   **encoder\_intermediate\_dim**: int, The intermediate size of the encoder's feed-forward networks.
*   **encoder\_num\_layers**: int, The number of encoder layers.
*   **encoder\_num\_attention\_heads**: int, The number of attention heads in the encoder.
*   **encoder\_num\_key\_value\_heads**: int, The number of key-value heads in the encoder.
*   **encoder\_head\_dim**: int, The dimensionality of each attention head in the encoder.
*   **encoder\_layer\_types**: list of str, A list of strings specifying the type of attention layer for each encoder layer. Each element can be either `"sliding_attention"` or `"full_attention"`. For example, `["full_attention", "sliding_attention", ...]`.
*   **decoder\_hidden\_dim**: int, The hidden dimensionality of the decoder.
*   **decoder\_intermediate\_dim**: int, The intermediate size of the decoder's feed-forward networks.
*   **decoder\_num\_layers**: int, The number of decoder layers.
*   **decoder\_num\_attention\_heads**: int, The number of attention heads in the decoder.
*   **decoder\_num\_key\_value\_heads**: int, The number of key-value heads in the decoder.
*   **decoder\_head\_dim**: int, The dimensionality of each attention head in the decoder.
*   **decoder\_layer\_types**: list of str, A list of strings specifying the type of attention layer for each decoder layer. Each element can be either `"sliding_attention"` or `"full_attention"`. For example, `["full_attention", "sliding_attention", ...]`.
*   **dropout\_rate**: float, The dropout rate applied throughout the model. Defaults to `0.0`.
*   **rms\_norm\_eps**: float, The epsilon value for RMS normalization. Defaults to `1e-6`.
*   **query\_pre\_attn\_scalar**: float, Scalar to multiply queries by before attention. Defaults to `1.0`.
*   **attention\_bias**: bool, Whether to include bias in attention computations. Defaults to `False`.
*   **hidden\_activation**: str, The activation function used in the feed-forward networks. Defaults to `"gelu_approximate"`.
*   **tie\_word\_embeddings**: bool, Whether to tie input and output word embeddings. Defaults to `True`.
*   **initializer\_range**: float, The range for the random normal initializer. Defaults to `0.02`.
*   **attention\_dropout**: float, The dropout rate applied to attention weights. Defaults to `0.0`.
*   **sliding\_window**: int, optional, The window size for sliding attention. Required if any `layer_type` is `"sliding_attention"`. Defaults to `None`.
*   **cross\_attention\_hidden\_size**: int, optional, The hidden size for cross-attention in the decoder layers. If None, it defaults to `encoder_hidden_dim`. Defaults to `None`.
*   **attn\_logit\_softcapping**: float, optional, The softcapping value for attention logits. Defaults to `None`.
*   **final\_logit\_softcapping**: float, optional, The softcapping value for final logits. Defaults to `None`.
*   **rope\_max\_wavelength**: float, The maximum wavelength for Rotary Positional Embeddings. Defaults to `10000.0`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments passed to the parent `Backbone` class.

**Examples**

Copied!

`import numpy as np from keras_hub.models import T5GemmaBackbone  input_data = {     "encoder_token_ids": np.ones(shape=(1, 12), dtype="int32"),     "encoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], dtype="int32"     ),     "decoder_token_ids": np.ones(shape=(1, 8), dtype="int32"),     "decoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1]], dtype="int32"     ), }  # Randomly initialized T5Gemma backbone with custom config. model = T5GemmaBackbone(     vocabulary_size=32000,     # Encoder parameters.     encoder_hidden_dim=256,     encoder_intermediate_dim=512,     encoder_num_layers=4,     encoder_num_attention_heads=4,     encoder_num_key_value_heads=2,     encoder_head_dim=64,     encoder_layer_types=["full_attention"] * 4,     # Decoder parameters.     decoder_hidden_dim=256,     decoder_intermediate_dim=512,     decoder_num_layers=4,     decoder_num_attention_heads=4,     decoder_num_key_value_heads=2,     decoder_head_dim=64,     decoder_layer_types=["full_attention"] * 4,     # Common parameters.     dropout_rate=0.1,     rms_norm_eps=1e-6,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate", ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`T5GemmaBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [t5gemma\_s\_s\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model. |
| [t5gemma\_s\_s\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model. |
| [t5gemma\_s\_s\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_s\_s\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model. |
| [t5gemma\_b\_b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model. |
| [t5gemma\_b\_b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model. |
| [t5gemma\_l\_l\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model. |
| [t5gemma\_l\_l\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model. |
| [t5gemma\_ml\_ml\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model. |
| [t5gemma\_ml\_ml\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model. |
| [t5gemma\_xl\_xl\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model. |
| [t5gemma\_xl\_xl\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_2b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_2b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_9b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_9b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.T5GemmaBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[T5GemmaBackbone model](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_backbone/#t5gemmabackbone-model)

[`T5GemmaBackbone` class](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_backbone/#t5gemmabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_backbone/#tokenembedding-property)