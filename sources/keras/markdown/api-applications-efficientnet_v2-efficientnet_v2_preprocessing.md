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
 / EfficientNetV2 preprocessing utilities

EfficientNetV2 preprocessing utilities
======================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1361)

### `decode_predictions` function

Copied!

`keras.applications.efficientnet_v2.decode_predictions(preds, top=5)`

Decodes the prediction of an ImageNet model.

**Arguments**

*   **preds**: NumPy array encoding a batch of predictions.
*   **top**: Integer, how many top-guesses to return. Defaults to `5`.

**Returns**

A list of lists of top class prediction tuples `(class_name, class_description, score)`. One list of tuples per sample in batch input.

**Raises**

*   **ValueError**: In case of invalid shape of the `pred` array (must be 2D).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/efficientnet_v2.py#L1339)

### `preprocess_input` function

Copied!

`keras.applications.efficientnet_v2.preprocess_input(x, data_format=None)`

A placeholder method for backward compatibility.

The preprocessing logic has been included in the EfficientNetV2 model implementation. Users are no longer required to call this method to normalize the input data. This method does nothing and only kept as a placeholder to align the API surface between old and new version of model.

**Arguments**

*   **x**: A floating point `numpy.array` or a tensor.
*   **data\_format**: Optional data format of the image tensor/array. Defaults to None, in which case the global setting `keras.backend.image_data_format()` is used (unless you changed it, it defaults to "channels\_last").{mode}

**Returns**

Unchanged `numpy.array` or tensor.

* * *

[EfficientNetV2 preprocessing utilities](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing/#efficientnetv2-preprocessing-utilities)

[`decode_predictions` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing/#decodepredictions-function)

[`preprocess_input` function](https://keras.io/api/applications/efficientnet_v2/efficientnet_v2_preprocessing/#preprocessinput-function)