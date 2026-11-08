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
 / [Swin Transformer](https://keras.io/keras_hub/api/models/swin_transformer/)
 / SwinTransformerBackbone model

SwinTransformerBackbone model
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/swin_transformer/swin_transformer_backbone.py#L18)

### `SwinTransformerBackbone` class

Copied!

`keras_hub.models.SwinTransformerBackbone(     image_shape,     embed_dim,     depths,     num_heads,     window_size,     patch_size=4,     mlp_ratio=4.0,     qkv_bias=True,     dropout_rate=0.0,     attention_dropout=0.0,     drop_path=0.1,     patch_norm=True,     data_format=None,     dtype=None,     **kwargs )`

A Swin Transformer backbone network.

This network implements a hierarchical vision transformer as described in ["Swin Transformer: Hierarchical Vision Transformer using Shifted Windows"](https://arxiv.org/abs/2103.14030)
. It includes the patch embedding, transformer stages with shifted windows, and final normalization, but not the classification head.

The default constructor gives a fully customizable, randomly initialized Swin Transformer with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

**Arguments**

*   **image\_shape**: tuple of ints. The shape of the input images, excluding batch dimension.
*   **embed\_dim**: int. Base dimension of the transformer.
*   **depths**: tuple of ints. Number of transformer blocks in each stage.
*   **num\_heads**: tuple of ints. Number of attention heads in each stage.
*   **window\_size**: int. Size of the attention window.
*   **patch\_size**: int. Size of the patches to be extracted from the input images. Defaults to `4`.
*   **mlp\_ratio**: float. Ratio of mlp hidden dim to embedding dim. Defaults to `4.0`.
*   **qkv\_bias**: bool. If True, add a learnable bias to query, key, value. Defaults to `True`.
*   **dropout\_rate**: float. Dropout rate. Defaults to `0.0`.
*   **attention\_dropout**: float. Dropout rate for attention. Defaults to `0.0`.
*   **drop\_path**: float. Stochastic depth rate. Defaults to `0.1`.
*   **patch\_norm**: bool. If True, add normalization after patch embedding. Defaults to `True`.
*   **data\_format**: str. Format of the input data, either `"channels_last"` or `"channels_first"`. Defaults to `None` (which uses `"channels_last"`).
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Defaults to `None`.

**Examples**

Copied!

`# Pretrained Swin Transformer backbone. model = keras_hub.models.SwinTransformerBackbone.from_preset(     "swin_tiny_224" ) model(np.ones((1, 224, 224, 3)))  # Randomly initialized Swin Transformer with custom config. model = keras_hub.models.SwinTransformerBackbone(     image_shape=(224, 224, 3),     embed_dim=96,     depths=(2, 2, 6, 2),     num_heads=(3, 6, 12, 24),     window_size=7, ) model(np.ones((1, 224, 224, 3)))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SwinTransformerBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [swin\_tiny\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_tiny_patch4_window7_224/1) | 27.52M | Swin-Tiny model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |
| [swin\_small\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_small_patch4_window7_224/1) | 48.84M | Swin-Small model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |
| [swin\_base\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window7_224/1) | 86.74M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |
| [swin\_base\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window12_384/1) | 86.88M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |
| [swin\_large\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window7_224/1) | 195.00M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |
| [swin\_large\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window12_384/1) | 195.20M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |

* * *

[SwinTransformerBackbone model](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_backbone/#swintransformerbackbone-model)

[`SwinTransformerBackbone` class](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_backbone/#swintransformerbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/swin_transformer/swin_transformer_backbone/#frompreset-method)