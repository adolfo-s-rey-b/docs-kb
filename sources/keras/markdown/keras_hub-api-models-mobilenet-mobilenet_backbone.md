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
 / [MobileNet](https://keras.io/keras_hub/api/models/mobilenet/)
 / MobileNetBackbone model

MobileNetBackbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mobilenet/mobilenet_backbone.py#L571)

### `MobileNetBackbone` class

Copied!

`keras_hub.models.MobileNetBackbone(     stackwise_expansion,     stackwise_num_blocks,     stackwise_num_filters,     stackwise_kernel_size,     stackwise_num_strides,     stackwise_se_ratio,     stackwise_activation,     stackwise_padding,     output_num_filters,     depthwise_filters,     depthwise_stride,     depthwise_residual,     last_layer_filter,     squeeze_and_excite=None,     image_shape=(None, None, 3),     input_activation="hard_swish",     output_activation="hard_swish",     input_num_filters=16,     dtype=None,     **kwargs )`

Instantiates the MobileNet architecture.

MobileNet is a lightweight convolutional neural network (CNN) optimized for mobile and edge devices, striking a balance between accuracy and efficiency. By employing depthwise separable convolutions and techniques like Squeeze-and-Excitation (SE) blocks, MobileNet models are highly suitable for real-time applications on resource-constrained devices.

**References**

*   [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
     - [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
     (CVPR 2018) - [Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)
     (ICCV 2019)

**Arguments**

*   **stackwise\_expansion**: list of list of ints, the expanded filters for each inverted residual block for each block in the model.
*   **stackwise\_num\_blocks**: list of ints, number of inversted residual blocks per block
*   **stackwise\_num\_filters**: list of list of ints, number of filters for each inverted residual block in the model.
*   **stackwise\_kernel\_size**: list of list of ints, kernel size for each inverted residual block in the model.
*   **stackwise\_num\_strides**: list of list of ints, stride length for each inverted residual block in the model.
*   **stackwise\_se\_ratio**: se ratio for each inverted residual block in the model. 0 if dont want to add Squeeze and Excite layer.
*   **stackwise\_activation**: list of list of activation functions, for each inverted residual block in the model.
*   **stackwise\_padding**: list of list of int, to provide padding values for each inverted residual block in the model.
*   **output\_num\_filters**: specifies whether to add conv and batch\_norm in the end, if set to None, it will not add these layers in the end. 'None' for MobileNetV1
*   **depthwise\_filters**: int, number of filters in depthwise separable convolution layer,
*   **last\_layer\_filter**: int, channels/filters for the head ConvBnAct block
*   **squeeze\_and\_excite**: float, squeeze and excite ratio in the depthwise layer, None, if dont want to do squeeze and excite
*   **image\_shape**: optional shape tuple, defaults to (224, 224, 3).
*   **input\_activation**: activation function to be used in the input layer 'hard\_swish' for MobileNetV3, 'relu6' for MobileNetV1 and MobileNetV2
*   **output\_activation**: activation function to be used in the output layer 'hard\_swish' for MobileNetV3, 'relu6' for MobileNetV1 and MobileNetV2
*   **input\_num\_filters**: int, channels/filters for the input before the stem input\_conv
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights.

**Example**

Copied!

`input_data = tf.ones(shape=(8, 224, 224, 3))  # Randomly initialized backbone with a custom config model = MobileNetBackbone(     stackwise_expansion=[             [40, 56],             [64, 144, 144],             [72, 72],             [144, 288, 288],         ],         stackwise_num_blocks=[2, 3, 2, 3],         stackwise_num_filters=[             [16, 16],             [24, 24, 24],             [24, 24],             [48, 48, 48],         ],         stackwise_kernel_size=[[3, 3], [5, 5, 5], [5, 5], [5, 5, 5]],         stackwise_num_strides=[[2, 1], [2, 1, 1], [1, 1], [2, 1, 1]],         stackwise_se_ratio=[             [None, None],             [0.25, 0.25, 0.25],             [0.3, 0.3],             [0.3, 0.25, 0.25],         ],         stackwise_activation=[             ["relu", "relu"],             ["hard_swish", "hard_swish", "hard_swish"],             ["hard_swish", "hard_swish"],             ["hard_swish", "hard_swish", "hard_swish"],         ],         output_num_filters=288,         input_activation="hard_swish",         output_activation="hard_swish",         input_num_filters=16,         image_shape=(224, 224, 3),         depthwise_filters=8,         squeeze_and_excite=0.5,  ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MobileNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [mobilenet\_v3\_small\_050\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_small_050_imagenet/1) | 278.78K | Small Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has half channel multiplier. |
| [mobilenet\_v3\_small\_100\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_small_100_imagenet/1) | 939.12K | Small Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has baseline channel multiplier. |
| [mobilenet\_v3\_large\_100\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_large_100_imagenet/1) | 3.00M | Large Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has baseline channel multiplier. |
| [mobilenet\_v3\_large\_100\_imagenet\_21k](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_large_100_imagenet_21k/1) | 3.00M | Large Mobilenet V3 model pre-trained on the ImageNet 21k dataset at a 224x224 resolution. Has baseline channel multiplier. |

* * *

[MobileNetBackbone model](https://keras.io/keras_hub/api/models/mobilenet/mobilenet_backbone/#mobilenetbackbone-model)

[`MobileNetBackbone` class](https://keras.io/keras_hub/api/models/mobilenet/mobilenet_backbone/#mobilenetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mobilenet/mobilenet_backbone/#frompreset-method)