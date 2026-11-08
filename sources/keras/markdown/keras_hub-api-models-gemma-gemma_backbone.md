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
 / [Gemma](https://keras.io/keras_hub/api/models/gemma/)
 / GemmaBackbone model

GemmaBackbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma/gemma_backbone.py#L11)

### `GemmaBackbone` class

Copied!

`keras_hub.models.GemmaBackbone(     vocabulary_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     query_head_dim_normalize=True,     use_post_ffw_norm=False,     use_post_attention_norm=False,     attention_logit_soft_cap=None,     final_logit_soft_cap=None,     use_sliding_window_attention=False,     sliding_window_size=4096,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     **kwargs )`

Gemma core network with hyperparameters.

This backbone implements the base Transformer network for the Gemma model. It includes the embedding lookups and transformer layers. This backbone will output the final hidden states for each token, not generative predictions over the vocabulary space. For a higher-level object for text generation, see [`keras_hub.models.GemmaCausalLM`](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm#gemmacausallm-class)
.

The default constructor gives a fully customizable, randomly initialized Gemma model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer layers.
*   **num\_query\_heads**: int. The number of heads for the query projections in the attention layer.
*   **num\_key\_value\_heads**: int. The number of heads for the key and value projections in the attention layer.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **head\_dim**: int. The size of each attention head.
*   **layer\_norm\_epsilon**: float. The epsilon value user for every layer norm in the transformer model.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **query\_head\_dim\_normalize**: boolean. If `True` normalize the query before attention with `head_dim`. If `False`, normalize the query with `hidden_dim / num_query_heads`. Defaults to True.
*   **use\_post\_ffw\_norm**: boolean. Whether to normalize after the feedforward block. Defaults to False.
*   **use\_post\_attention\_norm**: boolean. Whether to normalize after the attention block. Defaults to False.
*   **attention\_logit\_soft\_cap**: None or int. Soft cap for the attention logits. Defaults to None.
*   **final\_logit\_soft\_cap**: None or int. Soft cap for the final logits. Defaults to None. use\_sliding\_window\_attention boolean. Whether to use sliding local window attention. Defaults to False.
*   **sliding\_window\_size**: int. Size of the sliding local window. Defaults to 4096.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained Gemma decoder. model = keras_hub.models.GemmaBackbone.from_preset("gemma_2b_en") model(input_data)  # Randomly initialized Gemma decoder with custom config. model = keras_hub.models.GemmaBackbone(     vocabulary_size=50257,     num_layers=12,     num_query_heads=12,     num_key_value_heads=1,     hidden_dim=768,     intermediate_dim=3072,     head_dim=64, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`GemmaBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [vault\_gemma\_1b\_en](https://www.kaggle.com/models/keras/vaultgemma/keras/vault_gemma_1b_en/2) | 1.04B | 1 billion parameter, 26-layer, VaultGemma model. |
| [gemma\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, base Gemma model. |
| [gemma\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_2b_en/4) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_1.1\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. The 1.1 update improves model quality. |
| [code\_gemma\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [gemma2\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, base Gemma model. |
| [gemma2\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, instruction tuned Gemma model. |
| [shieldgemma\_2b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_2b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_2b_en/1) | 2.61B | A 2 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
| [gemma\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, base Gemma model. |
| [gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_7b_en/5) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [code\_gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. |
| [code\_gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. The 1.1 update improves model quality. |
| [gemma2\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_9b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_9b_en/2) | 9.24B | 9 billion parameter, 42-layer, ShieldGemma model. |
| [gemma2\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_27b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_27b_en/2) | 27.23B | 27 billion parameter, 42-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_27b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_27b_en/1) | 27.23B | A 27 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.GemmaBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`GemmaBackbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma/gemma_backbone.py#L212)

### `get_layout_map` method

Copied!

`GemmaBackbone.get_layout_map(     device_mesh, model_parallel_dim_name="model", data_parallel_dim_name="batch" )`

Get a [`keras.distribution.LayoutMap`](https://keras.io/api/distribution/layout_map#layoutmap-class)
 for model parallel distribution.

The returned `LayoutMap` contains the sharding spec for the gemma backbone weights, so that you can use it to distribute weights across the accelerators.

**Example**

Copied!

`# Feel free to change the mesh shape to balance data and model # parallelism mesh = keras.distribution.DeviceMesh(     shape=(1, 8), axis_names=('batch', 'model'),     devices=keras.distribution.list_devices()) layout_map = GemmaBackbone.get_layout_map(     mesh, model_parallel_dim_name="model")  distribution = keras.distribution.ModelParallel(     layout_map=layout_map, batch_dim_name='batch') with distribution.scope():    gemma_model = keras_hub.models.GemmaCausalLM.from_preset()`

To see how the layout map was applied, load the model then run (for one decoder block):

Copied!

`embedding_layer = gemma_model.backbone.get_layer("token_embedding") decoder_block_1 = gemma_model.backbone.get_layer('decoder_block_1') for variable in embedding_layer.weights + decoder_block_1.weights:     print(         f'{variable.path:<58}  {str(variable.shape):<16} '         f'{str(variable.value.sharding.spec)}'     )`

**Arguments**

*   **device\_mesh**: The [`keras.distribution.DeviceMesh`](https://keras.io/api/distribution/layout_map#devicemesh-class)
     instance for distribution.
*   **model\_parallel\_dim\_name**: The axis name of the device mesh, where the weights should be partition on.
*   **data\_parallel\_dim\_name**: The axis name of the device mesh, where the data should be partition on.

Return: [`keras.distribution.LayoutMap`](https://keras.io/api/distribution/layout_map#layoutmap-class)
 that contains the sharding spec for all the model weights.

* * *

[GemmaBackbone model](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#gemmabackbone-model)

[`GemmaBackbone` class](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#gemmabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#enablelora-method)

[`get_layout_map` method](https://keras.io/keras_hub/api/models/gemma/gemma_backbone/#getlayoutmap-method)