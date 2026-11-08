None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Xception](https://keras.io/api/applications/xception/)
 [EfficientNet B0 to B7](https://keras.io/api/applications/efficientnet/)
 [EfficientNetV2 B0 to B3 and S, M, L](https://keras.io/api/applications/efficientnet_v2/)
 [ConvNeXt Tiny, Small, Base, Large, XLarge](https://keras.io/api/applications/convnext/)
 [VGG16 and VGG19](https://keras.io/api/applications/vgg/)
 [ResNet and ResNetV2](https://keras.io/api/applications/resnet/)
 [MobileNet, MobileNetV2, and MobileNetV3](https://keras.io/api/applications/mobilenet/)
 [DenseNet](https://keras.io/api/applications/densenet/)
 [NasNetLarge and NasNetMobile](https://keras.io/api/applications/nasnet/)
 [InceptionV3](https://keras.io/api/applications/inceptionv3/)
 [InceptionResNetV2](https://keras.io/api/applications/inceptionresnetv2/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Keras Applications](https://keras.io/api/applications/)
 / [ConvNeXt Tiny, Small, Base, Large, XLarge](https://keras.io/api/applications/convnext/)
 / ConvNeXt models

ConvNeXt models
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L575)

### `ConvNeXtTiny` function

Copied!

`keras.applications.ConvNeXtTiny(     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="convnext_tiny", )`

Instantiates the ConvNeXtTiny architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L611)

### `ConvNeXtSmall` function

Copied!

`keras.applications.ConvNeXtSmall(     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="convnext_small", )`

Instantiates the ConvNeXtSmall architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L647)

### `ConvNeXtBase` function

Copied!

`keras.applications.ConvNeXtBase(     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="convnext_base", )`

Instantiates the ConvNeXtBase architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L683)

### `ConvNeXtLarge` function

Copied!

`keras.applications.ConvNeXtLarge(     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="convnext_large", )`

Instantiates the ConvNeXtLarge architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/convnext.py#L719)

### `ConvNeXtXLarge` function

Copied!

`keras.applications.ConvNeXtXLarge(     include_top=True,     include_preprocessing=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="convnext_xlarge", )`

Instantiates the ConvNeXtXLarge architecture.

**References**

*   [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
     (CVPR 2022)

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
. For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

The `base`, `large`, and `xlarge` models were first pre-trained on the ImageNet-21k dataset and then fine-tuned on the ImageNet-1k dataset. The pre-trained parameters of the models were assembled from the [official repository](https://github.com/facebookresearch/ConvNeXt)
. To get a sense of how these parameters were converted to Keras compatible parameters, please refer to [this repository](https://github.com/sayakpaul/keras-convnext-conversion)
.

Note: Each Keras Application expects a specific kind of input preprocessing. For ConvNeXt, preprocessing is included in the model using a `Normalization` layer. ConvNeXt models expect their inputs to be float or uint8 tensors of pixels with values in the \[0-255\] range.

When calling the `summary()` method after instantiating a ConvNeXt model, prefer setting the `expand_nested` argument `summary()` to `True` to better investigate the instantiated model.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet-1k), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[ConvNeXt models](https://keras.io/api/applications/convnext/convnext_models/#convnext-models)

[`ConvNeXtTiny` function](https://keras.io/api/applications/convnext/convnext_models/#convnexttiny-function)

[`ConvNeXtSmall` function](https://keras.io/api/applications/convnext/convnext_models/#convnextsmall-function)

[`ConvNeXtBase` function](https://keras.io/api/applications/convnext/convnext_models/#convnextbase-function)

[`ConvNeXtLarge` function](https://keras.io/api/applications/convnext/convnext_models/#convnextlarge-function)

[`ConvNeXtXLarge` function](https://keras.io/api/applications/convnext/convnext_models/#convnextxlarge-function)