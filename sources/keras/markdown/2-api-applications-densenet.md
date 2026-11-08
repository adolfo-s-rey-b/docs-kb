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
 / DenseNet

DenseNet
========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/densenet.py#L346)

### `DenseNet121` function

Copied!

`tf_keras.applications.DenseNet121(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the Densenet121 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your TF-Keras config at `~/.keras/keras.json`.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`tf.keras.applications.densenet.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/densenet/preprocess_input)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.

**Returns**

A TF-Keras model instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/densenet.py#L371)

### `DenseNet169` function

Copied!

`tf_keras.applications.DenseNet169(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the Densenet169 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your TF-Keras config at `~/.keras/keras.json`.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`tf.keras.applications.densenet.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/densenet/preprocess_input)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.

**Returns**

A TF-Keras model instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/densenet.py#L396)

### `DenseNet201` function

Copied!

`tf_keras.applications.DenseNet201(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the Densenet201 architecture.

**Reference**

*   [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
     (CVPR 2017)

Optionally loads weights pre-trained on ImageNet. Note that the data format convention used by the model is the one specified in your TF-Keras config at `~/.keras/keras.json`.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For DenseNet, call [`tf.keras.applications.densenet.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/densenet/preprocess_input)
 on your inputs before passing them to the model.

**Arguments**

*   **include\_top**: whether to include the fully-connected layer at the top of the network.
*   **weights**: one of `None` (random initialization), 'imagenet' (pre-training on ImageNet), or the path to the weights file to be loaded.
*   **input\_tensor**: optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **input\_shape**: optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(224, 224, 3)` (with `'channels_last'` data format) or `(3, 224, 224)` (with `'channels_first'` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. `(200, 200, 3)` would be one valid value.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.

**Returns**

A TF-Keras model instance.

* * *

[DenseNet](https://keras.io/2/api/applications/densenet/#densenet)

[`DenseNet121` function](https://keras.io/2/api/applications/densenet/#densenet121-function)

[`DenseNet169` function](https://keras.io/2/api/applications/densenet/#densenet169-function)

[`DenseNet201` function](https://keras.io/2/api/applications/densenet/#densenet201-function)