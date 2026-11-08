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
 / [EfficientNet B0 to B7](https://keras.io/api/applications/efficientnet/)
 / EfficientNet models

EfficientNet models
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L559)

### `EfficientNetB0` function

Copied!

`keras.applications.EfficientNetB0(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb0", )`

Instantiates the EfficientNetB0 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

**Guides and examples using `EfficientNetB0`**

*   [Creating TFRecords](https://keras.io/examples/keras_recipes/creating_tfrecords/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L592)

### `EfficientNetB1` function

Copied!

`keras.applications.EfficientNetB1(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb1", )`

Instantiates the EfficientNetB1 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L625)

### `EfficientNetB2` function

Copied!

`keras.applications.EfficientNetB2(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb2", )`

Instantiates the EfficientNetB2 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L658)

### `EfficientNetB3` function

Copied!

`keras.applications.EfficientNetB3(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb3", )`

Instantiates the EfficientNetB3 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L691)

### `EfficientNetB4` function

Copied!

`keras.applications.EfficientNetB4(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb4", )`

Instantiates the EfficientNetB4 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L724)

### `EfficientNetB5` function

Copied!

`keras.applications.EfficientNetB5(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb5", )`

Instantiates the EfficientNetB5 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L757)

### `EfficientNetB6` function

Copied!

`keras.applications.EfficientNetB6(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb6", )`

Instantiates the EfficientNetB6 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet.py#L790)

### `EfficientNetB7` function

Copied!

`keras.applications.EfficientNetB7(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="efficientnetb7", )`

Instantiates the EfficientNetB7 architecture.

**Reference**

*   [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)
     (ICML 2019)

This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each Keras Application expects a specific kind of input preprocessing. For EfficientNet, input preprocessing is included as part of the model (as a `Rescaling` layer), and thus [`keras.applications.efficientnet.preprocess_input`](https://keras.io/api/applications/efficientnet/efficientnet_preprocessing#preprocessinput-function)
 is actually a pass-through function. EfficientNet models expect their inputs to be float tensors of pixels with values in the `[0-255]` range.

**Arguments**

*   **include\_top**: Whether to include the fully-connected layer at the top of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `"imagenet"`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False. It should have exactly 3 inputs channels.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`. Defaults to `None`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional layer.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. 1000 is how many ImageNet classes there are. Defaults to `1000`.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. Defaults to `'softmax'`. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A model instance.

* * *

[EfficientNet models](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnet-models)

[`EfficientNetB0` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb0-function)

[`EfficientNetB1` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb1-function)

[`EfficientNetB2` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb2-function)

[`EfficientNetB3` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb3-function)

[`EfficientNetB4` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb4-function)

[`EfficientNetB5` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb5-function)

[`EfficientNetB6` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb6-function)

[`EfficientNetB7` function](https://keras.io/api/applications/efficientnet/efficientnet_models/#efficientnetb7-function)