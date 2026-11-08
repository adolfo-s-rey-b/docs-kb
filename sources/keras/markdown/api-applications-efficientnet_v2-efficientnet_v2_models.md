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
 / [EfficientNetV2 B0 to B3 and S, M, L](https://keras.io/api/applications/efficientnet_v2/)
 / EfficientNetV2 models

EfficientNetV2 models
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1092)

### `EfficientNetV2B0` function

Copied!

`keras.applications.EfficientNetV2B0(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-b0", )`

Instantiates the EfficientNetV2B0 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

**Guides and examples using `EfficientNetV2B0`**

*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1126)

### `EfficientNetV2B1` function

Copied!

`keras.applications.EfficientNetV2B1(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-b1", )`

Instantiates the EfficientNetV2B1 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1160)

### `EfficientNetV2B2` function

Copied!

`keras.applications.EfficientNetV2B2(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-b2", )`

Instantiates the EfficientNetV2B2 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1194)

### `EfficientNetV2B3` function

Copied!

`keras.applications.EfficientNetV2B3(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-b3", )`

Instantiates the EfficientNetV2B3 architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1228)

### `EfficientNetV2S` function

Copied!

`keras.applications.EfficientNetV2S(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-s", )`

Instantiates the EfficientNetV2S architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1262)

### `EfficientNetV2M` function

Copied!

`keras.applications.EfficientNetV2M(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-m", )`

Instantiates the EfficientNetV2M architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1296)

### `EfficientNetV2L` function

Copied!

`keras.applications.EfficientNetV2L(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     include_preprocessing=True,     name="efficientnetv2-l", )`

Instantiates the EfficientNetV2L architecture.

**Reference**

*   [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298)
     (ICML 2021)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNetV2, by default input preprocessing is included as a part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet_v2.preprocess_input`](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing#preprocessinput-function)
 is actually a pass-through function. In this use case, EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[0, 255]` range. At the same time, preprocessing as a part of the model (i.e. `Rescaling` layer) can be disabled by setting `include_preprocessing` argument to `False`. With preprocessing disabled EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the `[-1, 1]` range.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is `False`. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to None.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `"avg"` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `"max"` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000 (number of ImageNet classes).
*   **classifier\_activation**: A string or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `"softmax"`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[EfficientNetV2 models](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2-models)

[`EfficientNetV2B0` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2b0-function)

[`EfficientNetV2B1` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2b1-function)

[`EfficientNetV2B2` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2b2-function)

[`EfficientNetV2B3` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2b3-function)

[`EfficientNetV2S` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2s-function)

[`EfficientNetV2M` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2m-function)

[`EfficientNetV2L` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_models/#efficientnetv2l-function)