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
 / [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
 / SmolVLM2Backbone model

SmolVLM2Backbone model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_backbone.py#L18)

### `SmolVLM2Backbone` class

Copied!

`keras_hub.models.SmolVLM2Backbone(     vocabulary_size,     image_size,     patch_size,     vision_hidden_dim,     vision_intermediate_dim,     vision_num_layers,     vision_num_heads,     hidden_dim,     intermediate_dim,     num_layers,     num_query_heads,     num_key_value_heads,     scale_factor,     image_token_id,     rope_max_wavelength=10000,     layer_norm_epsilon=1e-05,     vision_layer_norm_epsilon=1e-06,     tie_word_embeddings=False,     dtype=None,     **kwargs )`

SmolVLM2 multimodal backbone.

This backbone implements the SmolVLM2 architecture, combining a SigLIP-based vision encoder, a pixel-shuffle connector, and a Llama-style text decoder. It can process text-only inputs or multimodal (image + text) inputs.

The vision encoder extracts patch features from images, the connector compresses and projects them to the text decoder's hidden dimension, and the `interleave_embeddings` layer replaces positions indicated by `vision_indices` in the text token sequence with the projected visual embeddings.

For text-only calls, a `__call__` override injects zero-sized dummy vision tensors so the functional graph receives all required keys. This follows the Qwen3.5/Gemma4 multimodal backbone pattern.

**Arguments**

*   **vocabulary\_size**: int. Size of the token vocabulary.
*   **image\_size**: int. Input image resolution (square).
*   **patch\_size**: int. Vision encoder patch size.
*   **vision\_hidden\_dim**: int. Vision encoder hidden dimension.
*   **vision\_intermediate\_dim**: int. Vision encoder MLP intermediate dim.
*   **vision\_num\_layers**: int. Number of vision encoder blocks.
*   **vision\_num\_heads**: int. Number of vision encoder attention heads.
*   **hidden\_dim**: int. Text decoder hidden dimension.
*   **intermediate\_dim**: int. Text decoder MLP intermediate dimension.
*   **num\_layers**: int. Number of text decoder blocks.
*   **num\_query\_heads**: int. Number of query attention heads.
*   **num\_key\_value\_heads**: int. Number of key/value attention heads.
*   **scale\_factor**: int. Pixel-shuffle spatial downsampling factor.
*   **image\_token\_id**: int. Token ID used as a placeholder for image embeddings in the text sequence.
*   **rope\_max\_wavelength**: float. Maximum wavelength for RoPE. Defaults to `10000`.
*   **layer\_norm\_epsilon**: float. Epsilon for normalization layers. Defaults to `1e-5`.
*   **vision\_layer\_norm\_epsilon**: float. Epsilon for vision encoder LayerNorm. Defaults to `1e-6`.
*   **tie\_word\_embeddings**: bool. Whether to tie the token embedding weights with the output projection. Defaults to `False`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`.

**Examples**

Copied!

`# Text-only forward pass (vision inputs injected automatically). backbone = keras_hub.models.SmolVLM2Backbone(     vocabulary_size=49280,     image_size=384,     patch_size=14,     vision_hidden_dim=1152,     vision_intermediate_dim=4304,     vision_num_layers=27,     vision_num_heads=16,     hidden_dim=2048,     intermediate_dim=8192,     num_layers=24,     num_query_heads=32,     num_key_value_heads=32,     scale_factor=3,     image_token_id=49190, ) input_data = {     "token_ids": np.ones((1, 12), dtype="int32"),     "padding_mask": np.ones((1, 12), dtype="int32"), } output = backbone(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SmolVLM2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.SmolVLM2Backbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L195)

### `enable_lora` method

Copied!

`SmolVLM2Backbone.enable_lora(rank, target_layer_names=None)`

Enable Lora on the backbone.

Calling this method will freeze all weights on the backbone, while enabling Lora on the query & value `EinsumDense` layers of the attention layers.

**Arguments**

*   **rank**: The rank of the LoRA factorization.
*   **target\_layer\_names**: A list of strings, the names of the layers to apply LoRA to. If `None`, this will be populated with the default LoRA layer names as returned by `backbone.default_lora_layer_names()`.

* * *

[SmolVLM2Backbone model](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_backbone/#smolvlm2backbone-model)

[`SmolVLM2Backbone` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_backbone/#smolvlm2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_backbone/#tokenembedding-property)

[`enable_lora` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_backbone/#enablelora-method)