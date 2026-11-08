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
 / RandomGaussianBlur layer

RandomGaussianBlur layer
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L11)

### `RandomGaussianBlur` class

Copied!

`keras.layers.RandomGaussianBlur(     factor=1.0,     kernel_size=3,     sigma=1.0,     value_range=(0, 255),     data_format=None,     seed=None,     **kwargs )`

Applies random Gaussian blur to images for data augmentation.

Copied!

``This layer performs a Gaussian blur operation on input images with a randomly selected degree of blurring, controlled by the `factor` and `sigma` arguments.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     factor: A single float or a tuple of two floats.         `factor` controls the extent to which the image hue is impacted.         `factor=0.0` makes this layer perform a no-op operation,         while a value of `1.0` performs the most aggressive         blurring available. If a tuple is used, a `factor` is         sampled between the two values for every image augmented. If a         single float is used, a value between `0.0` and the passed float is         sampled. Default is 1.0.     kernel_size: Integer. Size of the Gaussian kernel used for blurring.         Must be an odd integer. Default is 3.     sigma: Float or tuple of two floats. Standard deviation of the Gaussian         kernel. Controls the intensity of the blur. If a tuple is provided,         a value is sampled between the two for each image. Default is 1.0.     value_range: the range of values the incoming images will have.         Represented as a two-number tuple written `[low, high]`. This is         typically either `[0, 1]` or `[0, 255]` depending on how your         preprocessing pipeline is set up.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomGaussianBlur(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomGaussianBlur layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_gaussian_blur/#randomgaussianblur-layer)

[`RandomGaussianBlur` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_gaussian_blur/#randomgaussianblur-class)