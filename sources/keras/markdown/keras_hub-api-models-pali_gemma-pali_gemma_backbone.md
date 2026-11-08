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
 / [PaliGemma](https://keras.io/keras_hub/api/models/pali_gemma/)
 / PaliGemmaBackbone model

PaliGemmaBackbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/pali_gemma/pali_gemma_backbone.py#L14)

### `PaliGemmaBackbone` class

Copied!

`keras_hub.models.PaliGemmaBackbone(     vocabulary_size,     image_size,     num_layers,     num_query_heads,     num_key_value_heads,     hidden_dim,     intermediate_dim,     head_dim,     vit_patch_size,     vit_num_heads,     vit_hidden_dim,     vit_num_layers,     vit_intermediate_dim=None,     vit_pooling=None,     vit_classifier_activation=None,     vit_name=None,     query_head_dim_normalize=True,     use_post_ffw_norm=False,     use_post_attention_norm=False,     attention_logit_soft_cap=None,     final_logit_soft_cap=None,     use_sliding_window_attention=False,     sliding_window_size=4096,     layer_norm_epsilon=1e-06,     dropout=0,     dtype=None,     **kwargs )`

PaliGemma core network with hyperparameters.

This backbone implements the mixed-modality PaliGemma architecture. It contains a Visual Transformer network, as well as text token embedding layer, followed by a backend-agnostic concatenation operation to construct a sequence of representations of mixed type embeddings (visual and textual). Then, the concatenated sequence is passed through a series of Mixed Modality Decoder Blocks. The returned value from calling this model represents probabilistic values for output tokens.

For a higher-level object for text-generation, see [`keras_hub.models.PaliGemmaCausalLM`](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_causal_lm#paligemmacausallm-class)
.

The default constructor gives a fully customizable, randomly initialized PaliGemma model with any number of vit layers, heads, embedding dimensions, and equivalent configuration for Paligemma Decoder layers. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **image\_size**: int. The resolution of the image in both width and height. Note: input images must be square.
*   **num\_layers**: int. The number of transformer mixed decoder layers.
*   **num\_query\_heads**: int. The number of heads for the query projections in the mixed decoder attention layer.
*   **num\_key\_value\_heads**: int. The number of heads for the key and value projections in the mixed decoder attention layers.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each mixed transformer layer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer decoder block.
*   **head\_dim**: int. The size of each attention head in the mixed decoder.
*   **vit\_patch\_size**: int. The size of each square patch in the input image.
*   **vit\_num\_heads**: int. The number of attention heads for the vision (image) transformer encoder.
*   **vit\_hidden\_dim**: int. The size of the transformer hidden state at the end of each vision transformer layer.
*   **vit\_num\_layers**: int. The number of vision transformer layers.
*   **vit\_intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for vision transformer. Defaults to `4304`.
*   **vit\_pooling**: `None` or string. The encoded vision embeddings are pooled using the specified pooling setting. The accepted values are `"map"`, `"gap"`, `"zero"` or `None`. Defaults to `None`.
*   **vit\_classifier\_activation**: activation function. The activation that is used for final output classification in the vision transformer. Defaults to `None`.
*   **vit\_name**: string. The name used for vision transformer layers.
*   **query\_head\_dim\_normalize**: boolean. If `True` normalize the query before attention with `head_dim`. If `False`, normalize the query with `hidden_dim / num_query_heads`. Defaults to `True`.
*   **use\_post\_ffw\_norm**: boolean. Whether to normalize after the feedforward block. Defaults to `False`.
*   **use\_post\_attention\_norm**: boolean. Whether to normalize after the attention block. Defaults to `False`.
*   **attention\_logit\_soft\_cap**: `None` or int. Soft cap for the attention logits. Defaults to `None`.
*   **final\_logit\_soft\_cap**: `None` or int. Soft cap for the final logits. Defaults to `None`.
*   **use\_sliding\_window\_attention**: boolean. Whether to use sliding local window attention. Defaults to `False`.
*   **sliding\_window\_size**: int. Size of the sliding local window. Defaults to `4096`.
*   **layer\_norm\_epsilon**: float. The epsilon value user for every layer norm in all transformer blocks. Defaults to `1e-6`.
*   **dropout**: float. Dropout probability for the Transformer decoder blocks. Defaults to `0`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "token_ids": np.ones(shape=(1, 12), dtype="int32"),     "images": np.random.uniform(size=(1, 224, 224, 3)),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), }  # Pretrained PaliGemma decoder. model = keras_hub.models.PaliGemmaBackbone.from_preset("pali_gemma_mix_224") model(input_data)  # Randomly initialized PaliGemma decoder with custom config. model = keras_hub.models.PaliGemmaBackbone(     vocabulary_size=50257,     image_size=224,     num_layers=12,     num_query_heads=12,     num_key_value_heads=1,     hidden_dim=768,     intermediate_dim=3072,     head_dim=64,     vit_patch_size=14,     vit_num_heads=8,     vit_hidden_dim=768,     vit_intermediate_dim=3072,     vit_num_layers=2, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`PaliGemmaBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [pali\_gemma\_3b\_mix\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_224/4) | 2.92B | image size 224, mix fine tuned, text sequence length is 256 |
| [pali\_gemma\_3b\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_224/4) | 2.92B | image size 224, pre trained, text sequence length is 128 |
| [pali\_gemma\_3b\_mix\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_448/4) | 2.92B | image size 448, mix fine tuned, text sequence length is 512 |
| [pali\_gemma\_3b\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_448/4) | 2.92B | image size 448, pre trained, text sequence length is 512 |
| [pali\_gemma\_3b\_896](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_896/4) | 2.93B | image size 896, pre trained, text sequence length is 512 |
| [pali\_gemma2\_mix\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma\_2\_ft\_docci\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma_2_ft_docci_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_3b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_896/2) | 3.04B | 3 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_ft\_docci\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_ft_docci_10b_448/3) | 9.66B | 10 billion parameter, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_10b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_896/3) | 9.67B | 10 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_224/3) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_mix\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_224/4) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_896/3) | 27.65B | 28 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.PaliGemmaBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[PaliGemmaBackbone model](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_backbone/#paligemmabackbone-model)

[`PaliGemmaBackbone` class](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_backbone/#paligemmabackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_backbone/#tokenembedding-property)