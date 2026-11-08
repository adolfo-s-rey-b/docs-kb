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
 / InceptionV3

InceptionV3
===========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/applications/inception_v3.py#L47)

### `InceptionV3` function

Copied!

`tf_keras.applications.InceptionV3(     include_top=True,     weights="imagenet",     input_tensor=None,     input_shape=None,     pooling=None,     classes=1000,     classifier_activation="softmax", )`

Instantiates the Inception v3 architecture.

**Reference**

*   [Rethinking the Inception Architecture for Computer Vision](http://arxiv.org/abs/1512.00567)
     (CVPR 2016)

This function returns a TF-Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

For image classification use cases, see [this page for detailed examples](https://keras.io/api/applications/#usage-examples-for-image-classification-models)
.

For transfer learning use cases, make sure to read the [guide to transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
.

Note: each TF-Keras Application expects a specific kind of input preprocessing. For `InceptionV3`, call [`tf.keras.applications.inception_v3.preprocess_input`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/inception_v3/preprocess_input)
 on your inputs before passing them to the model. `inception_v3.preprocess_input` will scale input pixels between -1 and 1.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top, as the last layer of the network. Defaults to `True`.
*   **weights**: One of `None` (random initialization), `imagenet` (pre-training on ImageNet), or the path to the weights file to be loaded. Defaults to `imagenet`.
*   **input\_tensor**: Optional TF-Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model. `input_tensor` is useful for sharing inputs between multiple different networks. Defaults to `None`.
*   **input\_shape**: Optional shape tuple, only to be specified if `include_top` is False (otherwise the input shape has to be `(299, 299, 3)` (with `channels_last` data format) or `(3, 299, 299)` (with `channels_first` data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 75. E.g. `(150, 150, 3)` would be one valid value. `input_shape` will be ignored if the `input_tensor` is provided.
*   **pooling**: Optional pooling mode for feature extraction when `include_top` is `False`.
    *   `None` (default) means that the output of the model will be the 4D tensor output of the last convolutional block.
    *   `avg` means that global average pooling will be applied to the output of the last convolutional block, and thus the output of the model will be a 2D tensor.
    *   `max` means that global max pooling will be applied.
*   **classes**: optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified. Defaults to 1000.
*   **classifier\_activation**: A `str` or callable. The activation function to use on the "top" layer. Ignored unless `include_top=True`. Set `classifier_activation=None` to return the logits of the "top" layer. When loading pretrained weights, `classifier_activation` can only be `None` or `"softmax"`.

**Returns**

A [`keras.Model`](https://keras.io/api/models/model#model-class)
 instance.

* * *

[InceptionV3](https://keras.io/2/api/applications/inceptionv3/#inceptionv3)

[`InceptionV3` function](https://keras.io/2/api/applications/inceptionv3/#inceptionv3-function)