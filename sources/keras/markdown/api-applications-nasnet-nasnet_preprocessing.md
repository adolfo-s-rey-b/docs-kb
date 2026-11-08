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
 / [NasNetLarge and NasNetMobile](https://keras.io/api/applications/nasnet/)
 / NASNet preprocessing utilities

NASNet preprocessing utilities
==============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/nasnet.py#L859)

### `decode_predictions` function

Copied!

`keras.applications.nasnet.decode_predictions(preds, top=5)`

Decodes the prediction of an ImageNet model.

**Arguments**

*   **preds**: NumPy array encoding a batch of predictions.
*   **top**: Integer, how many top-guesses to return. Defaults to `5`.

**Returns**

A list of lists of top class prediction tuples `(class_name, class_description, score)`. One list of tuples per sample in batch input.

**Raises**

*   **ValueError**: In case of invalid shape of the `pred` array (must be 2D).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/nasnet.py#L852)

### `preprocess_input` function

Copied!

`keras.applications.nasnet.preprocess_input(x, data_format=None)`

Preprocesses a tensor or Numpy array encoding a batch of images.

Usage example with `applications.MobileNet`:

Copied!

`i = keras.layers.Input([None, None, 3], dtype="uint8") x = ops.cast(i, "float32") x = keras.applications.mobilenet.preprocess_input(x) core = keras.applications.MobileNet() x = core(x) model = keras.Model(inputs=[i], outputs=[x]) result = model(image)`

**Arguments**

*   **x**: A floating point `numpy.array` or a backend-native tensor, 3D or 4D with 3 color channels, with values in the range \[0, 255\]. The preprocessed data are written over the input data if the data types are compatible. To avoid this behaviour, `numpy.copy(x)` can be used.
*   **data\_format**: Optional data format of the image tensor/array. None, means the global setting `keras.backend.image_data_format()` is used (unless you changed it, it uses "channels\_last"). Defaults to `None`.

**Returns**

Preprocessed array with type `float32`.

The inputs pixel values are scaled between -1 and 1, sample-wise.

**Raises**

*   **ValueError**: In case of unknown `data_format` argument.

* * *

[NASNet preprocessing utilities](https://keras.io/api/applications/nasnet/nasnet_preprocessing/#nasnet-preprocessing-utilities)

[`decode_predictions` function](https://keras.io/api/applications/nasnet/nasnet_preprocessing/#decodepredictions-function)

[`preprocess_input` function](https://keras.io/api/applications/nasnet/nasnet_preprocessing/#preprocessinput-function)