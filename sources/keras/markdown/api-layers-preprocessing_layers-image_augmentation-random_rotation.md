None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Image augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/)
 / RandomRotation layer

RandomRotation layer
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_rotation.py#L14)

### `RandomRotation` class

Copied!

`keras.layers.RandomRotation(     factor,     fill_mode="reflect",     interpolation="bilinear",     seed=None,     fill_value=0.0,     data_format=None,     **kwargs )`

A preprocessing layer which randomly rotates images during training.

Copied!

``This layer will apply random rotations to each image, filling empty space according to `fill_mode`.  By default, random rotations are only applied during training. At inference time, the layer does nothing. If you need to apply random rotations at inference time, pass `training=True` when calling the layer.  Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Input shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format  # Output shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format  # Arguments     factor: a float represented as fraction of 2 Pi, or a tuple of size 2         representing lower and upper bound for rotating clockwise and         counter-clockwise. A positive values means rotating         counter clock-wise,         while a negative value means clock-wise.         When represented as a single         float, this value is used for both the upper and lower bound.         For instance, `factor=(-0.2, 0.3)`         results in an output rotation by a random         amount in the range `[-20% * 360, 30% * 360]`.         `factor=0.2` results in an         output rotating by a random amount         in the range `[-20% * 360, 20% * 360]`.     fill_mode: Points outside the boundaries of the input are filled         according to the given mode         (one of `{"constant", "reflect", "wrap", "nearest"}`).         - *reflect*: `(d c b a | a b c d | d c b a)`             The input is extended by reflecting about             the edge of the last pixel.         - *constant*: `(k k k k | a b c d | k k k k)`             The input is extended by             filling all values beyond the edge with             the same constant value k = 0.         - *wrap*: `(a b c d | a b c d | a b c d)` The input is extended by             wrapping around to the opposite edge.         - *nearest*: `(a a a a | a b c d | d d d d)`             The input is extended by the nearest pixel.     interpolation: Interpolation mode. Supported values: `"nearest"`,         `"bilinear"`.     seed: Integer. Used to create a random seed.     fill_value: a float represents the value to be filled outside         the boundaries when `fill_mode="constant"`.     data_format: string, either `"channels_last"` or `"channels_first"`.         The ordering of the dimensions in the inputs. `"channels_last"`         corresponds to inputs with shape `(batch, height, width, channels)`         while `"channels_first"` corresponds to inputs with shape         `(batch, channels, height, width)`. It defaults to the         `image_data_format` value found in your Keras config file at         `~/.keras/keras.json`. If you never set it, then it will be         `"channels_last"`.  # Example``\
\
Copied!\
\
`layer = keras.layers.RandomRotation(bounding_box_format="xyxy") images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")  bounding_boxes = {     "boxes": np.array([         [[10, 20, 100, 150], [50, 60, 200, 250]],         [[15, 25, 110, 160], [55, 65, 210, 260]],         [[20, 30, 120, 170], [60, 70, 220, 270]],         [[25, 35, 130, 180], [65, 75, 230, 280]],     ], dtype="float32"),     "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32") }  labels = keras.ops.one_hot(     np.array([0, 1, 2, 3]),     num_classes=4 )  segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "bounding_boxes": bounding_boxes,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`\
\
* * *\
\
[RandomRotation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_rotation/#randomrotation-layer)\
\
[`RandomRotation` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_rotation/#randomrotation-class)