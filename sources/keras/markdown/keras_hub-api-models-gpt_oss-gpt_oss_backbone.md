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
 / [GPT-OSS](https://keras.io/keras_hub/api/models/gpt_oss/)
 / GptOssBackbone model

GptOssBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt_oss/gpt_oss_backbone.py#L18)

### `GptOssBackbone` class

Copied!

`keras_hub.models.GptOssBackbone(     vocabulary_size,     num_layers,     num_query_heads,     hidden_dim,     intermediate_dim,     num_key_value_heads,     num_experts,     top_k=2,     rope_max_wavelength=10000,     rope_scaling_factor=1.0,     layer_norm_epsilon=1e-06,     sliding_window=4096,     head_dim=None,     dropout=0,     output_router_logits=False,     dtype=None,     **kwargs )`

A GPT-style Transformer with a Mixture of Experts.

This network implements a GPT-style decoder network with Mixture of Expert (MoE) layers, similar to the architecture described in ["Mixtral of Experts"](https://arxiv.org/pdf/2401.04088)
 but with customizations found in some open-source GPT models. It includes the embedding lookups and transformer layers.

The default constructor gives a fully customizable, randomly initialized GptOss model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of query attention heads for each transformer.
*   **hidden\_dim**: int. The size of the transformer encoding and pooling layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a three-layer feedforward network for each transformer.
*   **num\_key\_value\_heads**: int. The number of key and value attention heads for each transformer.
*   **num\_experts**: int. The number of experts for the MoE layers.
*   **top\_k**: int. The number of experts to use for each token. Defaults to `2`.
*   **rope\_max\_wavelength**: int. The maximum angular wavelength of the sine/cosine curves, for rotary embeddings. Defaults to `10000`.
*   **rope\_scaling\_factor**: float. The scaling factor for calculation of roatary embedding. Defaults to `1.0`.
*   **layer\_norm\_epsilon**: float. Epsilon for the layer normalization layers in the transformer decoder. Defaults to `1e-6`.
*   **sliding\_window**: int. The sliding window for the attention layers. This controls the maximum cache size for the attention layers in each transformer decoder. Only `sliding_window` number of tokens are saved in the cache and used to generate the next token. Defaults to `4096`.
*   **head\_dim**: int. Head dimension for attention layers. This parameter is accepted for HuggingFace compatibility but ignored. The head dimension is calculated dynamically as hidden\_dim // num\_query\_heads. Defaults to `None`.
*   **dropout**: float. Attention dropout probability.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at `float32` precision regardless of dtype.

**Examples**

Copied!

`import numpy as np import keras_hub  # Load a pretrained GptOss backbone from a preset. model = keras_hub.models.GptOssBackbone.from_preset("gpt_oss_20b_en")  input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], dtype="int32"     ), }  model(input_data)  # Randomly initialized GptOss decoder with custom config. model = keras_hub.models.GptOssBackbone(     vocabulary_size=10,     hidden_dim=512,     num_layers=2,     num_query_heads=32,     num_key_value_heads=8,     intermediate_dim=1024,     num_experts=4,     top_k=2,     sliding_window=256,     layer_norm_epsilon=1e-6,     dtype="float32" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`GptOssBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [gpt\_oss\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_20b_en/1) | 20.91B | This preset has 21 billion total parameters, with 3.6 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_20b_en/1) | 20.91B | Open-weight safety reasoning model with 21 billion total parameters,with 3.6 billion active parameters, a context length of over 128k, and is de-quantized from MXFP4. |
| [gpt\_oss\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_120b_en/1) | 116.83B | This preset has 117 billion total parameters, with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_120b_en/1) | 116.83B | Open-weight safety reasoning model with 117 billion total parameters,with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.GptOssBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[GptOssBackbone model](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_backbone/#gptossbackbone-model)

[`GptOssBackbone` class](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_backbone/#gptossbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_backbone/#tokenembedding-property)