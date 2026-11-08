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
 / [DenseNet](https://keras.io/api/applications/densenet/)
 / DenseNet models

DenseNet models
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/densenet.py#L325)

### `DenseNet121` function

Copied!

`keras.applications.DenseNet121(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="densenet121", )`

Instantiates the Densenet121 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your Keras config at `~/.keras/keras.json`.

Note: each Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`keras.applications.densenet.preprocess_input`](https://keras.io/api/applications/densenet/densenet_preprocessing#preprocessinput-function)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. input\_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A Keras model instance.

**Guides and examples using `DenseNet121`**

*   [Learning to Resize](https://keras.io/examples/vision/learnable_resizer/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/densenet.py#L355)

### `DenseNet169` function

Copied!

`keras.applications.DenseNet169(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="densenet169", )`

Instantiates the Densenet169 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your Keras config at `~/.keras/keras.json`.

Note: each Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`keras.applications.densenet.preprocess_input`](https://keras.io/api/applications/densenet/densenet_preprocessing#preprocessinput-function)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. input\_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A Keras model instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/densenet.py#L385)

### `DenseNet201` function

Copied!

`keras.applications.DenseNet201(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax",     name="densenet201", )`

Instantiates the Densenet201 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your Keras config at `~/.keras/keras.json`.

Note: each Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`keras.applications.densenet.preprocess_input`](https://keras.io/api/applications/densenet/densenet_preprocessing#preprocessinput-function)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), `"imagenet"` (pre-training on ImageNet), or the path to the weights file to be loaded. input\_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is `True`, and if no `weights` argument is specified. Defaults to 1000.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.
*   **name**: The name of the model (string).

**Returns**

A Keras model instance.

* * *

[DenseNet models](https://keras.io/api/applications/densenet/densenet_models/#densenet-models)

[`DenseNet121` function](https://keras.io/api/applications/densenet/densenet_models/#densenet121-function)

[`DenseNet169` function](https://keras.io/api/applications/densenet/densenet_models/#densenet169-function)

[`DenseNet201` function](https://keras.io/api/applications/densenet/densenet_models/#densenet201-function)