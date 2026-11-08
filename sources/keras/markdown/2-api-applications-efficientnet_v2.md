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
 / EfficientNetV2 B0 to B3 and S, M, L

EfficientNetV2 B0 to B3 and S, M, L
===================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1116)

### `EfficientNetV2B0` function

Copied!

`tf_keras.applications.EfficientNetV2B0(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2B0 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1146)

### `EfficientNetV2B1` function

Copied!

`tf_keras.applications.EfficientNetV2B1(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2B1 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1176)

### `EfficientNetV2B2` function

Copied!

`tf_keras.applications.EfficientNetV2B2(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2B2 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1206)

### `EfficientNetV2B3` function

Copied!

`tf_keras.applications.EfficientNetV2B3(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2B3 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1236)

### `EfficientNetV2S` function

Copied!

`tf_keras.applications.EfficientNetV2S(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2S architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1266)

### `EfficientNetV2M` function

Copied!

`tf_keras.applications.EfficientNetV2M(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2M architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/efficientnet_v2.py#L1296)

### `EfficientNetV2L` function

Copied!

`tf_keras.applications.EfficientNetV2L(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True, )`

Instantiates the EfficientNetV2L architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`tf.keras.applications.efficientnet_v2.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet_v2/preprocess_input)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[0-255\] range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to False. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the \[-1, 1\] range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied. Defaults to `None`.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A string or callable. The activation function to use on the `"top"` layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`. Defaults to `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[EfficientNetV2 B0 to B3 and S, M, L](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2-b0-to-b3-and-s-m-l)

[`EfficientNetV2B0` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2b0-function)

[`EfficientNetV2B1` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2b1-function)

[`EfficientNetV2B2` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2b2-function)

[`EfficientNetV2B3` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2b3-function)

[`EfficientNetV2S` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2s-function)

[`EfficientNetV2M` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2m-function)

[`EfficientNetV2L` function](https://keras.io/2/api/applications/efficientnet_v2/#efficientnetv2l-function)