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
 / [DINOV3](https://keras.io/keras_hub/api/models/dinov3/)
 / DINOV3Backbone model

DINOV3Backbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/dinov3/dinov3_backbone.py#L13)

### `DINOV3Backbone` class

Copied!

`keras_hub.models.DINOV3Backbone(     patch_size,     num_layers,     hidden_dim,     num_heads,     intermediate_dim,     layer_scale_init_value=1.0,     num_register_tokens=4,     use_mask_token=True,     hidden_activation="gelu",     use_gated_mlp=False,     use_query_bias=True,     use_key_bias=True,     use_value_bias=True,     use_proj_bias=True,     use_mlp_bias=True,     attention_dropout=0.0,     drop_path_rate=0.0,     layer_norm_eps=1e-05,     image_shape=(518, 518, 3),     rope_theta=100.0,     apply_layernorm=False,     data_format=None,     dtype=None,     name=None,     **kwargs )`

DINOV3 core network with hyperparameters.

**Arguments**

*   **patch\_size**: int. The size of each square patch in the input image.
*   **num\_layers**: int. The number of transformer layers.
*   **hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer.
*   **num\_heads**: int. The number of attention heads for each transformer.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **layer\_scale\_init\_value**: float. The initial value for the layer scale in the transformer layers. Defaults to `1.0`.
*   **num\_register\_tokens**: int. The number of register tokens to use in the embedding layer. Defaults to `0`.
*   **use\_mask\_token**: bool. Whether to use a mask token in the embedding layer. Defaults to `True`.
*   **hidden\_activation**: str or callable. Activation to use in the MLP. Defaults to `"gelu"`.
*   **use\_gated\_mlp**: bool. Whether to use Gated MLP layers. Defaults to `False`.
*   **use\_query\_bias**: bool. Whether to use a bias for the query projection. Defaults to `True`.
*   **use\_key\_bias**: bool. Whether to use a bias for the key projection. Defaults to `True`.
*   **use\_value\_bias**: bool. Whether to use a bias for the value projection. Defaults to `True`.
*   **use\_proj\_bias**: bool. Whether to use a bias for the output projection. Defaults to `True`.
*   **use\_mlp\_bias**: bool. Whether to use a bias for the dense layers in MLP. Defaults to `True`.
*   **attention\_dropout**: float. The dropout rate for the attention probabilities. Defaults to `0.0`.
*   **drop\_path\_rate**: float. The drop path rate to use. Defaults to `0.0`.
*   **image\_shape**: tuple. The input shape without the batch size. Defaults to `(518, 518, 3)`.
*   **rope\_theta**: float. The base period of the rotary position embeddings. Defaults to `100.0`.
*   **apply\_layernorm**: bool. Whether to apply layer normalization to the outputs of each stage in the feature pyramid. Defaults to `False`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`# Pretrained DINOV3 model. input_data = {     "images": np.ones(shape=(1, 518, 518, 3), dtype="float32"), } model = keras_hub.models.DINOV3Backbone.from_preset(     "dinov3_vit_small_lvd1689m" ) model(input_data)  # Pretrained DINOV3 model with custom image shape. input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"), } model = keras_hub.models.DINOV3Backbone.from_preset(     "dinov3_vit_small_lvd1689m", image_shape=(224, 224, 3) ) model(input_data)  # Randomly initialized DINOV3 model with custom config. model = keras_hub.models.DINOV3Backbone(     patch_size=14,     num_layers=2,     hidden_dim=32,     num_heads=2,     intermediate_dim=128,     image_shape=(224, 224, 3), ) model(input_data)  # Accessing feature pyramid outputs. backbone = keras_hub.models.DINOV3Backbone.from_preset(     "dinov3_vit_small_lvd1689m", image_shape=(224, 224, 3) ) model = keras.Model(     inputs=backbone.inputs,     outputs=backbone.pyramid_outputs, ) features = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DINOV3Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [dinov3\_vit\_small\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_small_lvd1689m/1) | 21.60M | Vision Transformer (small-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_small\_plus\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_small_plus_lvd1689m/1) | 29.00M | Vision Transformer (small-plus-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_base\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_base_lvd1689m/1) | 86.00M | Vision Transformer (base-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_large\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_large_lvd1689m/1) | 300.00M | Vision Transformer (large-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_large\_sat493m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_large_sat493m/1) | 300.00M | Vision Transformer (large-sized model) trained on SAT-493M using DINOv3. |
| [dinov3\_vit\_huge\_plus\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_huge_plus_lvd1689m/1) | 840.00M | Vision Transformer (huge-plus-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_7b\_lvd1689m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_7b_lvd1689m/1) | 6.70B | Vision Transformer (7B-sized model) trained on LVD-1689M using DINOv3. |
| [dinov3\_vit\_7b\_sat493m](https://www.kaggle.com/models/keras/dinov3/keras/dinov3_vit_7b_sat493m/1) | 6.70B | Vision Transformer (7B-sized model) trained on SAT-493M using DINOv3. |

* * *

[DINOV3Backbone model](https://keras.io/keras_hub/api/models/dinov3/dinov3_backbone/#dinov3backbone-model)

[`DINOV3Backbone` class](https://keras.io/keras_hub/api/models/dinov3/dinov3_backbone/#dinov3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/dinov3/dinov3_backbone/#frompreset-method)