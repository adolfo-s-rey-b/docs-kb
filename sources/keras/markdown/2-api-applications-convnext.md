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
 / ConvNeXt Tiny, Small, Base, Large, XLarge

ConvNeXt Tiny, Small, Base, Large, XLarge
=========================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/convnext.py#L575)

### `ConvNeXtTiny` function

Copied!

`tf_keras.applications.ConvNeXtTiny(     model_name="convnext_tiny",     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the ConvNeXtTiny architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to TF-Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each TF-Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/convnext.py#L608)

### `ConvNeXtSmall` function

Copied!

`tf_keras.applications.ConvNeXtSmall(     model_name="convnext_small",     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the ConvNeXtSmall architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to TF-Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each TF-Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/convnext.py#L641)

### `ConvNeXtBase` function

Copied!

`tf_keras.applications.ConvNeXtBase(     model_name="convnext_base",     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the ConvNeXtBase architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to TF-Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each TF-Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/convnext.py#L674)

### `ConvNeXtLarge` function

Copied!

`tf_keras.applications.ConvNeXtLarge(     model_name="convnext_large",     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the ConvNeXtLarge architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to TF-Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each TF-Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/convnext.py#L707)

### `ConvNeXtXLarge` function

Copied!

`tf_keras.applications.ConvNeXtXLarge(     model_name="convnext_xlarge",     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the ConvNeXtXLarge architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to TF-Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each TF-Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[ConvNeXt Tiny, Small, Base, Large, XLarge](https://keras.io/2/api/applications/convnext/#convnext-tiny-small-base-large-xlarge)

[`ConvNeXtTiny` function](https://keras.io/2/api/applications/convnext/#convnexttiny-function)

[`ConvNeXtSmall` function](https://keras.io/2/api/applications/convnext/#convnextsmall-function)

[`ConvNeXtBase` function](https://keras.io/2/api/applications/convnext/#convnextbase-function)

[`ConvNeXtLarge` function](https://keras.io/2/api/applications/convnext/#convnextlarge-function)

[`ConvNeXtXLarge` function](https://keras.io/2/api/applications/convnext/#convnextxlarge-function)