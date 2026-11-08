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
 / AugMix layer

AugMix layer
============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L39)

### `AugMix` class

Copied!

`keras.layers.AugMix(     value_range=(0, 255),     num_chains=3,     chain_depth=3,     factor=0.3,     alpha=1.0,     all_ops=True,     interpolation="bilinear",     seed=None,     data_format=None,     **kwargs )`

Performs the AugMix data augmentation technique.

Copied!

``AugMix aims to produce images with variety while preserving the image semantics and local statistics. During the augmentation process, the same augmentation is applied across all images in the batch in num_chains different ways, with each chain consisting of chain_depth augmentations.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  References:     - [AugMix paper](https://arxiv.org/pdf/1912.02781)     - [Official Code](https://github.com/google-research/augmix)  # Arguments     value_range: the range of values the incoming images will have.         Represented as a two number tuple written (low, high).         This is typically either `(0, 1)` or `(0, 255)` depending         on how your preprocessing pipeline is set up.     num_chains: an integer representing the number of different chains to         be mixed, defaults to 3.     chain_depth: an integer representing the maximum number of         transformations to be applied in each chain. The actual number         of transformations in each chain will be sampled randomly         from the range `[0, `chain_depth`]`. Defaults to 3.     factor: The strength of the augmentation as a normalized value         between 0 and 1. Default is 0.3.     alpha: a float value used as the probability coefficients for the         Beta and Dirichlet distributions, defaults to 1.0.     all_ops: Use all operations (including random_brightness,         random_color_degeneration, random_contrast and random_sharpness).         Default is True.     interpolation: The interpolation method to use for resizing operations.         Options include `"nearest"`, `"bilinear"`. Default is `"bilinear"`.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.AugMix(bounding_box_format="xyxy") images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")  bounding_boxes = {     "boxes": np.array([         [[10, 20, 100, 150], [50, 60, 200, 250]],         [[15, 25, 110, 160], [55, 65, 210, 260]],         [[20, 30, 120, 170], [60, 70, 220, 270]],         [[25, 35, 130, 180], [65, 75, 230, 280]],     ], dtype="float32"),     "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32") }  labels = keras.ops.one_hot(     np.array([0, 1, 2, 3]),     num_classes=4 )  segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "bounding_boxes": bounding_boxes,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[AugMix layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/aug_mix/#augmix-layer)

[`AugMix` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/aug_mix/#augmix-class)