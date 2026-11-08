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
 / RandomErasing layer

RandomErasing layer
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_erasing.py#L11)

### `RandomErasing` class

Copied!

`keras.layers.RandomErasing(     factor=1.0,     scale=(0.02, 0.33),     fill_value=None,     value_range=(0, 255),     seed=None,     data_format=None,     **kwargs )`

Random Erasing data augmentation technique.

Copied!

``Random Erasing is a data augmentation method where random patches of an image are erased (replaced by a constant value or noise) during training to improve generalization.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  References:    - [Random Erasing paper](https://arxiv.org/abs/1708.04896).  # Arguments     factor: A single float or a tuple of two floats.         `factor` controls the probability of applying the transformation.         - `factor=0.0` ensures no erasing is applied.         - `factor=1.0` means erasing is always applied.         - If a tuple `(min, max)` is provided, a probability value           is sampled between `min` and `max` for each image.         - If a single float is provided, a probability is sampled           between `0.0` and the given float.         Default is 1.0.     scale: A tuple of two floats representing the aspect ratio range of         the erased patch. This defines the width-to-height ratio of         the patch to be erased. It can help control the rw shape of         the erased region. Default is (0.02, 0.33).     fill_value: A value to fill the erased region with. This can be set to         a constant value or `None` to sample a random value         from a normal distribution. Default is `None`.     value_range: the range of values the incoming images will have.         Represented as a two-number tuple written `[low, high]`. This is         typically either `[0, 1]` or `[0, 255]` depending on how your         preprocessing pipeline is set up.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomErasing(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomErasing layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_erasing/#randomerasing-layer)

[`RandomErasing` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_erasing/#randomerasing-class)