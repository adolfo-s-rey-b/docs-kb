None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Xception](https://keras.io/2/api/applications/xception/)
 [EfficientNet B0 to B7](https://keras.io/2/api/applications/efficientnet/)
 [EfficientNetV2 B0 to B3 and S, M, L](https://keras.io/2/api/applications/efficientnet_v2/)
 [ConvNeXt Tiny, Small, Base, Large, XLarge](https://keras.io/2/api/applications/convnext/)
 [VGG16 and VGG19](https://keras.io/2/api/applications/vgg/)
 [ResNet and ResNetV2](https://keras.io/2/api/applications/resnet/)
 [MobileNet, MobileNetV2, and MobileNetV3](https://keras.io/2/api/applications/mobilenet/)
 [DenseNet](https://keras.io/2/api/applications/densenet/)
 [NasNetLarge and NasNetMobile](https://keras.io/2/api/applications/nasnet/)
 [InceptionV3](https://keras.io/2/api/applications/inceptionv3/)
 [InceptionResNetV2](https://keras.io/2/api/applications/inceptionresnetv2/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Keras Applications](https://keras.io/2/api/applications/)
 / MobileNet, MobileNetV2, and MobileNetV3

MobileNet, MobileNetV2, and MobileNetV3
=======================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/mobilenet.py#L82)

### `MobileNet` function

Copied!

`tf_keras.applications.MobileNet(     input_shape=None,     alpha=1.0,     depth_multiplier=1,     dropout=0.001,     include_top=True,     weights="imagenet",     input_tensor=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     **kwargs )`

Instantiates the MobileNet architecture.

**Reference**

*   [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
    

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For MobileNet, call [`tf.keras.applications.mobilenet.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet/preprocess_input)
 on your inputs before passing them to the model. `mobilenet.preprocess_input` will scale input pixels between -1 and 1.

**Arguments**

*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `channels_last` data format) or (3, 224, 224) (with `channels_first` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value. Defaults to `None`. `input_shape` will be ignored if the `input_tensor` is provided.
*   **alpha**: Controls the width of the network. This is known as the width multiplier in the MobileNet paper. - If `alpha` < 1.0, proportionally decreases the number of filters in each layer. - If `alpha` > 1.0, proportionally increases the number of filters in each layer. - If `alpha` = 1, default number of filters from the paper are used at each layer. Defaults to `1.0`.
*   **depth\_multiplier**: Depth multiplier for depthwise convolution. This is called the resolution multiplier in the MobileNet paper. Defaults to `1.0`.
*   **dropout**: Dropout rate. Defaults to `0.001`.
*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `imagenet`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model. `input_tensor` is useful for sharing inputs between multiple different networks. Defaults to `None`.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` (default) means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **\*\*kwargs**: For backwards compatibility only.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/mobilenet_v2.py#L96)

### `MobileNetV2` function

Copied!

`tf_keras.applications.MobileNetV2(     input_shape=None,     alpha=1.0,     include_top=True,     weights="imagenet",     input_tensor=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     **kwargs )`

Instantiates the MobileNetV2 architecture.

MobileNetV2 is very similar to the original MobileNet, except that it uses inverted residual blocks with bottlenecking features. It has a drastically lower parameter count than the original MobileNet. MobileNets support any input size greater than 32 x 32, with larger image sizes offering better performance.

**Reference**

*   [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
     (CVPR 2018)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For MobileNetV2, call [`tf.keras.applications.mobilenet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet_v2/preprocess_input)
 on your inputs before passing them to the model. `mobilenet_v2.preprocess_input` will scale input pixels between -1 and 1.

**Arguments**

*   **input\_shape**: Optional shape tuple, to be specified if you would like to use a model with an input image resolution that is not (224, 224, 3). It should have exactly 3 inputs channels (224, 224, 3). You can also omit this option if you would like to infer input\_shape from an input\_tensor. If you choose to include both input\_tensor and input\_shape then input\_shape will be used if they match, if the shapes do not match then we will throw an error. E.g. `(160, 160, 3)` would be one valid value.
*   **alpha**: Float, larger than zero, controls the width of the network. This is known as the width multiplier in the MobileNetV2 paper, but the name is kept for consistency with `applications.MobileNetV1` model in TF-Keras.
    *   If `alpha` < 1.0, proportionally decreases the number of filters in each layer.
    *   If `alpha` > 1.0, proportionally increases the number of filters in each layer.
    *   If `alpha` = 1.0, default number of filters from the paper are used at each layer.
*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: String, one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **pooling**: String, optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional integer number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **\*\*kwargs**: For backwards compatibility only.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/mobilenet_v3.py#L423)

### `MobileNetV3Small` function

Copied!

`tf_keras.applications.MobileNetV3Small(     input_shape=None,     alpha=1.0,     minimalistic=False,     include_top=True,     weights="imagenet",     input_tensor=None,     classes=1000,     pooling=None,     dropout_rate=0.2,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the MobileNetV3Small architecture.

**Reference**

*   [Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)
     (ICCV 2019)

The following table describes the performance of MobileNets v3:
---------------------------------------------------------------

MACs stands for Multiply Adds

| Classification Checkpoint | MACs(M) | Parameters(M) | Top1 Accuracy | Pixel1 CPU(ms) |
| --- | --- | --- | --- | --- |
| mobilenet\_v3\_large\_1.0\_224 | 217 | 5.4 | 75.6 | 51.2 |
| mobilenet\_v3\_large\_0.75\_224 | 155 | 4.0 | 73.3 | 39.8 |
| mobilenet\_v3\_large\_minimalistic\_1.0\_224 | 209 | 3.9 | 72.3 | 44.1 |
| mobilenet\_v3\_small\_1.0\_224 | 66  | 2.9 | 68.1 | 15.8 |
| mobilenet\_v3\_small\_0.75\_224 | 44  | 2.4 | 65.4 | 12.8 |
| mobilenet\_v3\_small\_minimalistic\_1.0\_224 | 65  | 2.0 | 61.9 | 12.2 |

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For MobileNetV3, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.mobilenet_v3.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet_v3/preprocess_input)
 is actually a pass-through function. In this use case, MobileNetV3 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled MobileNetV3 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **input\_shape**: Optional shape tuple, to be specified if you would like to use a model with an input image resolution that is not (224, 224, 3). It should have exactly 3 inputs channels (224, 224, 3). You can also omit this option if you would like to infer input\_shape from an input\_tensor. If you choose to include both input\_tensor and input\_shape then input\_shape will be used if they match, if the shapes do not match then we will throw an error. E.g. `(160, 160, 3)` would be one valid value.
*   **alpha**: controls the width of the network. This is known as the depth multiplier in the MobileNetV3 paper, but the name is kept for consistency with MobileNetV1 in TF-Keras.
    *   If `alpha` < 1.0, proportionally decreases the number of filters in each layer.
    *   If `alpha` > 1.0, proportionally increases the number of filters in each layer.
    *   If `alpha` = 1, default number of filters from the paper are used at each layer.
*   **minimalistic**: In addition to large and small models this module also contains so-called minimalistic models, these models have the same per-layer dimensions characteristic as MobilenetV3 however, they don't utilize any of the advanced blocks (squeeze-and-excite units, hard-swish, and 5x5 convolutions). While these models are less efficient on CPU, they are much more performant on GPU/DSP.
*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: String, one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **pooling**: String, optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Integer, optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **dropout\_rate**: fraction of the input units to drop on the last layer.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **include\_preprocessing**: Boolean, whether to include the preprocessing layer (`Rescaling`) at the bottom of the network. Defaults to `True`.

**Call arguments**

*   **inputs**: A floating point `numpy.array` or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    , 4D with 3 color channels, with values in the range \[0, 255\] if `include_preprocessing` is True and in the range \[-1, 1\] otherwise.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/mobilenet_v3.py#L488)

### `MobileNetV3Large` function

Copied!

`tf_keras.applications.MobileNetV3Large(     input_shape=None,     alpha=1.0,     minimalistic=False,     include_top=True,     weights="imagenet",     input_tensor=None,     classes=1000,     pooling=None,     dropout_rate=0.2,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the MobileNetV3Large architecture.

**Reference**

*   [Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)
     (ICCV 2019)

The following table describes the performance of MobileNets v3:
---------------------------------------------------------------

MACs stands for Multiply Adds

| Classification Checkpoint | MACs(M) | Parameters(M) | Top1 Accuracy | Pixel1 CPU(ms) |
| --- | --- | --- | --- | --- |
| mobilenet\_v3\_large\_1.0\_224 | 217 | 5.4 | 75.6 | 51.2 |
| mobilenet\_v3\_large\_0.75\_224 | 155 | 4.0 | 73.3 | 39.8 |
| mobilenet\_v3\_large\_minimalistic\_1.0\_224 | 209 | 3.9 | 72.3 | 44.1 |
| mobilenet\_v3\_small\_1.0\_224 | 66  | 2.9 | 68.1 | 15.8 |
| mobilenet\_v3\_small\_0.75\_224 | 44  | 2.4 | 65.4 | 12.8 |
| mobilenet\_v3\_small\_minimalistic\_1.0\_224 | 65  | 2.0 | 61.9 | 12.2 |

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For MobileNetV3, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.mobilenet_v3.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet_v3/preprocess_input)
 is actually a pass-through function. In this use case, MobileNetV3 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled MobileNetV3 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **input\_shape**: Optional shape tuple, to be specified if you would like to use a model with an input image resolution that is not (224, 224, 3). It should have exactly 3 inputs channels (224, 224, 3). You can also omit this option if you would like to infer input\_shape from an input\_tensor. If you choose to include both input\_tensor and input\_shape then input\_shape will be used if they match, if the shapes do not match then we will throw an error. E.g. `(160, 160, 3)` would be one valid value.
*   **alpha**: controls the width of the network. This is known as the depth multiplier in the MobileNetV3 paper, but the name is kept for consistency with MobileNetV1 in TF-Keras.
    *   If `alpha` < 1.0, proportionally decreases the number of filters in each layer.
    *   If `alpha` > 1.0, proportionally increases the number of filters in each layer.
    *   If `alpha` = 1, default number of filters from the paper are used at each layer.
*   **minimalistic**: In addition to large and small models this module also contains so-called minimalistic models, these models have the same per-layer dimensions characteristic as MobilenetV3 however, they don't utilize any of the advanced blocks (squeeze-and-excite units, hard-swish, and 5x5 convolutions). While these models are less efficient on CPU, they are much more performant on GPU/DSP.
*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: String, one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **pooling**: String, optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Integer, optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **dropout\_rate**: fraction of the input units to drop on the last layer.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **include\_preprocessing**: Boolean, whether to include the preprocessing layer (`Rescaling`) at the bottom of the network. Defaults to `True`.

**Call arguments**

*   **inputs**: A floating point `numpy.array` or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    , 4D with 3 color channels, with values in the range \[0, 255\] if `include_preprocessing` is True and in the range \[-1, 1\] otherwise.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[MobileNet, MobileNetV2, and MobileNetV3](https://keras.io/2/api/applications/mobilenet/#mobilenet-mobilenetv2-and-mobilenetv3)

[`MobileNet` function](https://keras.io/2/api/applications/mobilenet/#mobilenet-function)

[`MobileNetV2` function](https://keras.io/2/api/applications/mobilenet/#mobilenetv2-function)

[`MobileNetV3Small` function](https://keras.io/2/api/applications/mobilenet/#mobilenetv3small-function)

[`MobileNetV3Large` function](https://keras.io/2/api/applications/mobilenet/#mobilenetv3large-function)