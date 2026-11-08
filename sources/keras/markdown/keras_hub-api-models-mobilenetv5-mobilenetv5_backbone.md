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
 / [MobileNetV5](https://keras.io/keras_hub/api/models/mobilenetv5/)
 / MobileNetV5Backbone model

MobileNetV5Backbone model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mobilenetv5/mobilenetv5_backbone.py#L21)

### `MobileNetV5Backbone` class

Copied!

`keras_hub.models.MobileNetV5Backbone(     stackwise_block_types,     stackwise_num_blocks,     stackwise_num_filters,     stackwise_strides,     stackwise_act_layers,     stackwise_exp_ratios,     stackwise_se_ratios,     stackwise_dw_kernel_sizes,     stackwise_dw_start_kernel_sizes,     stackwise_dw_end_kernel_sizes,     stackwise_exp_kernel_sizes,     stackwise_pw_kernel_sizes,     stackwise_num_heads,     stackwise_key_dims,     stackwise_value_dims,     stackwise_kv_strides,     stackwise_use_cpe,     filters=3,     stem_size=16,     stem_bias=True,     fix_stem=False,     num_features=2048,     pad_type="same",     use_msfa=True,     msfa_indices=(-2, -1),     msfa_output_resolution=16,     act_layer="gelu",     norm_layer="rms_norm",     se_layer=keras_hub.src.models.mobilenet.mobilenet_backbone.SqueezeAndExcite2D,     se_from_exp=True,     round_chs_fn=round_channels,     drop_path_rate=0.0,     layer_scale_init_value=None,     image_shape=(None, None, 3),     data_format=None,     dtype=None,     **kwargs )`

MobileNetV5 backbone network.

This class represents the backbone of the MobileNetV5 architecture, which can be used as a feature extractor for various downstream tasks.

**Arguments**

*   **stackwise\_block\_types**: list of list of strings. The block type for each block in each stack.
*   **stackwise\_num\_blocks**: list of ints. The number of blocks for each stack.
*   **stackwise\_num\_filters**: list of list of ints. The number of filters for each block in each stack.
*   **stackwise\_strides**: list of list of ints. The stride for each block in each stack.
*   **stackwise\_act\_layers**: list of list of strings. The activation function for each block in each stack.
*   **stackwise\_exp\_ratios**: list of list of floats. The expansion ratio for each block in each stack.
*   **stackwise\_se\_ratios**: list of list of floats. The SE ratio for each block in each stack.
*   **stackwise\_dw\_kernel\_sizes**: list of list of ints. The depthwise kernel size for each block in each stack.
*   **stackwise\_dw\_start\_kernel\_sizes**: list of list of ints. The start depthwise kernel size for each `uir` block in each stack.
*   **stackwise\_dw\_end\_kernel\_sizes**: list of list of ints. The end depthwise kernel size for each `uir` block in each stack.
*   **stackwise\_exp\_kernel\_sizes**: list of list of ints. The expansion kernel size for each `er` block in each stack.
*   **stackwise\_pw\_kernel\_sizes**: list of list of ints. The pointwise kernel size for each `er` block in each stack.
*   **stackwise\_num\_heads**: list of list of ints. The number of heads for each `mqa` or `mha` block in each stack.
*   **stackwise\_key\_dims**: list of list of ints. The key dimension for each `mqa` or `mha` block in each stack.
*   **stackwise\_value\_dims**: list of list of ints. The value dimension for each `mqa` or `mha` block in each stack.
*   **stackwise\_kv\_strides**: list of list of ints. The key-value stride for each `mqa` or `mha` block in each stack.
*   **stackwise\_use\_cpe**: list of list of bools. Whether to use conditional position encoding for each `mqa` or `mha` block in each stack.
*   **filters**: int. The number of input channels.
*   **stem\_size**: int. The number of channels in the stem convolution.
*   **stem\_bias**: bool. If `True`, a bias term is used in the stem convolution.
*   **fix\_stem**: bool. If `True`, the stem size is not rounded.
*   **num\_features**: int. The number of output features, used when `use_msfa` is `True`.
*   **pad\_type**: str. The padding type for convolutions.
*   **use\_msfa**: bool. If `True`, the Multi-Scale Fusion Adapter is used.
*   **msfa\_indices**: tuple. The indices of the feature maps to be used by the MSFA.
*   **msfa\_output\_resolution**: int. The output resolution of the MSFA.
*   **act\_layer**: str. The activation function to use.
*   **norm\_layer**: str. The normalization layer to use.
*   **se\_layer**: keras.layers.Layer. The Squeeze-and-Excitation layer to use.
*   **se\_from\_exp**: bool. If `True`, SE channel reduction is based on the expanded channels.
*   **round\_chs\_fn**: callable. A function to round the number of channels.
*   **drop\_path\_rate**: float. The stochastic depth rate.
*   **layer\_scale\_init\_value**: float. The initial value for layer scale.
*   **image\_shape**: tuple. The shape of the input image. Defaults to `(None, None, 3)`.
*   **data\_format**: str, The data format of the image channels. Can be either `"channels_first"` or `"channels_last"`. If `None` is specified, it will use the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. Defaults to `None`.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Defaults to `None`.

**Example**

Copied!

`import keras from keras_hub.models import MobileNetV5Backbone  # Randomly initialized backbone with a custom config. model_args = {     "stackwise_block_types": [["er"], ["uir", "uir"]],     "stackwise_num_blocks": [1, 2],     "stackwise_num_filters": [[24], [48, 48]],     "stackwise_strides": [[2], [2, 1]],     "stackwise_act_layers": [["relu"], ["relu", "relu"]],     "stackwise_exp_ratios": [[4.0], [6.0, 6.0]],     "stackwise_se_ratios": [[0.0], [0.0, 0.0]],     "stackwise_dw_kernel_sizes": [[0], [5, 5]],     "stackwise_dw_start_kernel_sizes": [[0], [0, 0]],     "stackwise_dw_end_kernel_sizes": [[0], [0, 0]],     "stackwise_exp_kernel_sizes": [[3], [0, 0]],     "stackwise_pw_kernel_sizes": [[1], [0, 0]],     "stackwise_num_heads": [[0], [0, 0]],     "stackwise_key_dims": [[0], [0, 0]],     "stackwise_value_dims": [[0], [0, 0]],     "stackwise_kv_strides": [[0], [0, 0]],     "stackwise_use_cpe": [[False], [False, False]],     "use_msfa": False, } model = MobileNetV5Backbone(**model_args) input_data = keras.ops.ones((1, 224, 224, 3)) output = model(input_data)  # Load the backbone from a preset and run a prediction. backbone = MobileNetV5Backbone.from_preset("mobilenetv5_300m_gemma3n")  # Expected output shape = (1, 16, 16, 2048). outputs = backbone.predict(keras.ops.ones((1, 224, 224, 3)))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MobileNetV5Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [mobilenetv5\_300m\_enc\_gemma3n](https://www.kaggle.com/models/keras/mobilenetv5/keras/mobilenetv5_300m_enc_gemma3n/1) | 294.28M | Lightweight 300M-parameter convolutional vision encoder used as the image backbone for Gemma 3n |

* * *

[MobileNetV5Backbone model](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_backbone/#mobilenetv5backbone-model)

[`MobileNetV5Backbone` class](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_backbone/#mobilenetv5backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_backbone/#frompreset-method)