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
 / RandomShear layer

RandomShear layer
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_shear.py#L18)

### `RandomShear` class

Copied!

`keras.layers.RandomShear(     x_factor=0.0,     y_factor=0.0,     interpolation="bilinear",     fill_mode="reflect",     fill_value=0.0,     data_format=None,     seed=None,     **kwargs )`

A preprocessing layer that randomly applies shear transformations to images.

Copied!

``This layer shears the input images along the x-axis and/or y-axis by a randomly selected factor within the specified range. The shear transformation is applied to each image independently in a batch. Empty regions created during the transformation are filled according to the `fill_mode` and `fill_value` parameters.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     x_factor: A tuple of two floats. For each augmented image, a value         is sampled from the provided range. If a float is passed, the         range is interpreted as `(0, x_factor)`. Values represent a         percentage of the image to shear over. For example, 0.3 shears         pixels up to 30% of the way across the image. All provided values         should be positive.     y_factor: A tuple of two floats. For each augmented image, a value         is sampled from the provided range. If a float is passed, the         range is interpreted as `(0, y_factor)`. Values represent a         percentage of the image to shear over. For example, 0.3 shears         pixels up to 30% of the way across the image. All provided values         should be positive.     interpolation: Interpolation mode. Supported values: `"nearest"`,         `"bilinear"`.     fill_mode: Points outside the boundaries of the input are filled         according to the given mode. Available methods are `"constant"`,         `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.         - `"reflect"`: `(d c b a | a b c d | d c b a)`             The input is extended by reflecting about the edge of the             last pixel.         - `"constant"`: `(k k k k | a b c d | k k k k)`             The input is extended by filling all values beyond the edge             with the same constant value `k` specified by `fill_value`.         - `"wrap"`: `(a b c d | a b c d | a b c d)`             The input is extended by wrapping around to the opposite edge.         - `"nearest"`: `(a a a a | a b c d | d d d d)`             The input is extended by the nearest pixel.         Note that when using torch backend, `"reflect"` is redirected to         `"mirror"` `(c d c b | a b c d | c b a b)` because torch does         not support `"reflect"`.         Note that torch backend does not support `"wrap"`.     fill_value: A float representing the value to be filled outside the         boundaries when `fill_mode="constant"`.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomShear(bounding_box_format="xyxy") images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")  bounding_boxes = {     "boxes": np.array([         [[10, 20, 100, 150], [50, 60, 200, 250]],         [[15, 25, 110, 160], [55, 65, 210, 260]],         [[20, 30, 120, 170], [60, 70, 220, 270]],         [[25, 35, 130, 180], [65, 75, 230, 280]],     ], dtype="float32"),     "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32") }  labels = keras.ops.one_hot(     np.array([0, 1, 2, 3]),     num_classes=4 )  segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "bounding_boxes": bounding_boxes,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomShear layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_shear/#randomshear-layer)

[`RandomShear` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_shear/#randomshear-class)