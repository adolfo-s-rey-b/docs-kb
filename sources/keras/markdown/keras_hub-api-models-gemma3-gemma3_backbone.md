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
 / [Gemma3](https://keras.io/keras_hub/api/models/gemma3/)
 / Gemma3Backbone model

Gemma3Backbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3/gemma3_backbone.py#L14)

### `Gemma3Backbone` class

Copied!

`keras_hub.models.Gemma3Backbone(     vocabulary_size,     image_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     query_head_dim_normalize=True,     use_query_key_norm=True,     use_post_ffw_norm=False,     use_post_attention_norm=False,     attention_logit_soft_cap=None,     final_logit_soft_cap=None,     use_sliding_window_attention=False,     sliding_window_size=1024,     local_rope_scaling_factor=1.0,     global_rope_scaling_factor=1.0,     vision_encoder=None,     layer_norm_epsilon=1e-06,     use_bidirectional_attention=False,     dropout=0,     is_embedding_model=False,     pooling_intermediate_dim=None,     embedding_dim=None,     dtype=None,     **kwargs )`

Gemma3 core network with hyperparameters.

This backbone implements the Gemma3 model architecture. Gemma3 is a vision-language model (image-text in, text out). The text input is encoded using an embedding layer; images are encoded using a vision transformer (ViT). After encoding these two modalities, the image embeddings are placed in the correct position in the text embedding sequence. The mixed sequence of embeddings is then passed through transformer decoder layers.

For a higher-level object for text-generation, see [`keras_hub.models.Gemma3CausalLM`](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm#gemma3causallm-class)
.

This backbone can also function as an end-to-end embedding model by setting the `is_embedding_model` argument to `True`. When configured as an embedding model with bi-directional attention, it matches the `EmbeddingGemma` architecture.

The default constructor gives a fully customizable, randomly initialized Gemma3 model with any vision encoder, number of heads, embedding dimensions, and equivalent configuration for the decoder layers. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **image\_size**: int. The resolution of the image in both width and height. The input images must be square.
*   **num\_layers**: int. The number of transformer mixed decoder layers.
*   **num\_query\_heads**: int. The number of heads for the query projections in the mixed decoder attention layer.
*   **num\_key\_value\_heads**: int. The number of heads for the key and value projections in the mixed decoder attention layers.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each mixed transformer layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer decoder block.
*   **head\_dim**: int. The size of each attention head in the mixed decoder.
*   **query\_head\_dim\_normalize**: boolean. If `True` normalize the query before attention with `head_dim`. If `False`, normalize the query with `hidden_dim / num_query_heads`. Defaults to `True`.
*   **use\_query\_key\_norm**: bool. If `True`, apply a RMS Norm layer to query and key before projecting them. Defaults to `True`.
*   **use\_post\_ffw\_norm**: boolean. Whether to normalize after the feedforward block. Defaults to `False`.
*   **use\_post\_attention\_norm**: boolean. Whether to normalize after the attention block. Defaults to `False`.
*   **attention\_logit\_soft\_cap**: `None` or int. Soft cap for the attention logits. Defaults to `None`.
*   **final\_logit\_soft\_cap**: `None` or int. Soft cap for the final logits. Defaults to `None`.
*   **use\_sliding\_window\_attention**: boolean. Whether to use sliding local window attention. Defaults to `False`.
*   **sliding\_window\_size**: int. Size of the sliding local window. Defaults to `4096`.
*   **vision\_encoder**: A `Gemma3VisionEncoder` instance. `call()` takes in images and returns corresponding sequence of embeddings. If `None`, the model is a text-only model.
*   **layer\_norm\_epsilon**: float. The epsilon value user for every layer norm in all transformer blocks. Defaults to `1e-6`.
*   **dropout**: float. Dropout probability for the Transformer decoder blocks. Defaults to `0`.
*   **is\_embedding\_model (bool, optional)**: If `True`, the model will function as an embedding model. This adds mean pooling layer and a two-layer dense projection head to the final sequence output. The model output will be a dictionary containing `'sequence_output'` and `'pooled_output'`. Defaults to `False`.
*   **pooling\_intermediate\_dim (int, optional)**: The intermediate dimension of the first dense layer in the two-layer pooling projection head. Required if `is_embedding_model` is `True`. Defaults to `None`.
*   **embedding\_dim (int, optional)**: The dimension of the final projected embedding. Required if `is_embedding_model` is `True`. Defaults to `None`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done in float32 precision regardless of dtype. Defaults to `bfloat16`.

**Example**

Copied!

`# === Language Gemma3 model === input_data = {} input_data["token_ids"] = np.ones(shape=(1, 300), dtype="int32") input_data["padding_mask"] = (     np.expand_dims(np.array([1] * 280 + [0] * (300 - 280)), axis=0)     .astype(bool) )  # Pretrained Gemma3 decoder. model = keras_hub.models.Gemma3Backbone.from_preset(     "gemma3_instruct_4b_text" ) model(input_data)  # Randomly initialized Gemma3 decoder with a custom config. model = keras_hub.models.Gemma3Backbone(     vocabulary_size=262144,     image_size=896,     num_layers=34,     num_query_heads=8,     num_key_value_heads=4,     hidden_dim=2560,     intermediate_dim=10240,     head_dim=256,     query_head_dim_normalize=True,     use_post_ffw_norm=True,     use_post_attention_norm=True,     final_logit_soft_cap=None,     attention_logit_soft_cap=None,     sliding_window_size=1024,     use_sliding_window_attention=True,     vision_encoder=None,     layer_norm_epsilon=1e-06,     dtype="bfloat16", ) model(input_data)  # === Vision + Language Gemma3 model === input_data = {} input_data["images"] = np.ones(shape=(1, 1, 896, 896, 3)) input_data["token_ids"] = np.ones(shape=(1, 300), dtype="int32") # images after the text part of the sequence. input_data["vision_mask"] = np.expand_dims(     np.array([0] * 30 + [1] * 256 + [0] * 14),     axis=0, ).astype(bool) input_data["vision_indices"] = (     np.expand_dims(np.arange(30, 286), axis=0) ) input_data["padding_mask"] = (     np.expand_dims(np.array([1] * 286 + [0] * (300 - 286)), axis=0)     .astype(bool) )  # Pretrained Gemma3 decoder. model = keras_hub.models.Gemma3Backbone.from_preset("gemma3_instruct_4b") model(input_data)  # Randomly initialized Gemma3 decoder with a custom config. vision_encoder = Gemma3VisionEncoder(     image_size=896,     patch_size=14,     num_heads=16,     hidden_dim=1152,     num_layers=27,     intermediate_dim=4304,     output_dim=2560,     pool_size=4,     layer_norm_epsilon=1e-6,     dtype="float32", )  model = keras_hub.models.Gemma3Backbone(     vocabulary_size=262144,     image_size=896,     num_layers=34,     num_query_heads=8,     num_key_value_heads=4,     hidden_dim=2560,     intermediate_dim=10240,     head_dim=256,     query_head_dim_normalize=True,     use_post_ffw_norm=True,     use_post_attention_norm=True,     final_logit_soft_cap=None,     attention_logit_soft_cap=None,     sliding_window_size=1024,     use_sliding_window_attention=True,     vision_encoder=vision_encoder,     layer_norm_epsilon=1e-06,     dtype="bfloat16" ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`Gemma3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [gemma3\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_270m/3) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [gemma3\_instruct\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_270m/4) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only,instruction-tuned model designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [function\_gemma\_instruct\_270m](https://www.kaggle.com/models/keras/function-gemma/keras/function_gemma_instruct_270m/1) | 268.10M | A 270M Million parameter text-only model based on Gemma 3. This model is trained specifically for function calling improvements. |
| [harrier\_embedding\_oss\_270m](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_270m/1) | 268.10M | Microsoft harrier-oss-v1 270M multilingual text embedding model based on the Gemma3-270M architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 66.5 on Multilingual MTEB v2. |
| [embedding\_gemma3\_300m](https://www.kaggle.com/models/keras/embeddinggemma/keras/embedding_gemma3_300m/2) | 307.58M | Embedding-focused Gemma 3 model (300M parameters, 24 layers). |
| [gemma3\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b_text/2) | 3.88B | 4 billion parameter, 34-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b_text/3) | 3.88B | 4 billion parameter, 34-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_4b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_4b_it/1) | 4.30B | 4 billion parameter, 34-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is pre-trained for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_1.5\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_1.5_instruct_4b/1) | 4.30B | A 4 billion parameter,Instruct-tuned MedGemma 1.5 4B is an updated version of the Instruction-tuned MedGemma 4B model. |
| [gemma3\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_12b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_12b_it/1) | 12.19B | 12 billion parameter, 48-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [gemma3\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b_text/4) | 27.01B | 27 billion parameter, 62-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b_text/3) | 27.01B | 27 billion parameter, 62-layer, text-only instruction-tuned Gemma3 model. |
| [medgemma\_instruct\_27b\_text](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b_text/1) | 27.01B | A 27 billion parameter text-only model based on Gemma 3. This model is instruction-tuned (No images) for performance on medical text comprehension and is optimized for medical applications that involve a text generation component. |
| [gemma3\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_27b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_27b_it/1) | 27.43B | 27 billion parameter, 62-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_instruct\_27b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b/1) | 27.43B | A 27 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.Gemma3Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`Gemma3Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[Gemma3Backbone model](https://keras.io/keras_hub/api/models/gemma3/gemma3_backbone/#gemma3backbone-model)

[`Gemma3Backbone` class](https://keras.io/keras_hub/api/models/gemma3/gemma3_backbone/#gemma3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3/gemma3_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/gemma3/gemma3_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/gemma3/gemma3_backbone/#enablelora-method)