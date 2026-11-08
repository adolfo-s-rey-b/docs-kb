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
 / [DeiT](https://keras.io/keras_hub/api/models/deit/)
 / DeiTBackbone model

DeiTBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/deit/deit_backbone.py#L10)

### `DeiTBackbone` class

Copied!

`keras_hub.models.DeiTBackbone(     image_shape,     patch_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout_rate=0.0,     attention_dropout=0.0,     layer_norm_epsilon=1e-06,     use_mha_bias=True,     data_format=None,     dtype=None,     **kwargs )`

DeiT backbone.

This backbone implements the Data-efficient Image Transformer (DeiT) architecture as described in \[Training data-efficient image transformers & distillation through attention\] (https://arxiv.org/abs/2012.12877).

**Arguments**

*   **image\_shape**: A tuple or list of 3 integers representing the shape of the input image `(height, width, channels)`.
*   **patch\_size**: tuple or int. The size of each image patch. If an int is provided, it will be used for both height and width. The input image will be split into patches of shape `(patch_size_h, patch_size_w)`.
*   **num\_layers**: int. The number of transformer encoder layers.
*   **num\_heads**: int. The number of attention heads in each Transformer encoder layer.
*   **hidden\_dim**: int. The dimensionality of the hidden representations.
*   **intermediate\_dim**: int. The dimensionality of the intermediate MLP layer in each Transformer encoder layer.
*   **dropout\_rate**: float. The dropout rate for the Transformer encoder layers.
*   **attention\_dropout**: float. The dropout rate for the attention mechanism in each Transformer encoder layer.
*   **layer\_norm\_epsilon**: float. Value used for numerical stability in layer normalization.
*   **use\_mha\_bias**: bool. Whether to use bias in the multi-head attention layers.
*   **data\_format**: str. `"channels_last"` or `"channels_first"`, specifying the data format for the input image. If `None`, defaults to `"channels_last"`.
*   **dtype**: The dtype of the layer weights. Defaults to None.
*   **\*\*kwargs**: Additional keyword arguments to be passed to the parent `Backbone` class.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DeiTBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [deit\_tiny\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_tiny_distilled_patch16_224_imagenet/1) | 5.52M | DeiT-T16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |
| [deit\_small\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_small_distilled_patch16_224_imagenet/1) | 21.67M | DeiT-S16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |
| [deit\_base\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_base_distilled_patch16_224_imagenet/1) | 85.80M | DeiT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |
| [deit\_base\_distilled\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_base_distilled_patch16_384_imagenet/1) | 86.09M | DeiT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |

* * *

[DeiTBackbone model](https://keras.io/keras_hub/api/models/deit/deit_backbone/#deitbackbone-model)

[`DeiTBackbone` class](https://keras.io/keras_hub/api/models/deit/deit_backbone/#deitbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/deit/deit_backbone/#frompreset-method)