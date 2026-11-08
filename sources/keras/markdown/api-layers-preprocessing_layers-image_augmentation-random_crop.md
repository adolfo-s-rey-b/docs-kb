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
 / RandomCrop layer

RandomCrop layer
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_crop.py#L18)

### `RandomCrop` class

Copied!

`keras.layers.RandomCrop(     height, width, seed=None, data_format=None, name=None, **kwargs )`

A preprocessing layer which randomly crops images during training.

Copied!

``During training, this layer will randomly choose a location to crop images down to a target size. The layer will crop all the images in the same batch to the same cropping location.  At inference time, and during training if an input image is smaller than the target size, the input will be resized and cropped so as to return the largest possible window in the image that matches the target aspect ratio. If you need to apply random cropping at inference time, set `training` to True when calling the layer.  Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Input shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format.  # Output shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., target_height, target_width, channels)`.  # Arguments     height: Integer, the height of the output shape.     width: Integer, the width of the output shape.     seed: Integer. Used to create a random seed.     **kwargs: Base layer keyword arguments, such as         `name` and `dtype`.  # Example``\
\
Copied!\
\
`layer = keras.layers.RandomCrop(bounding_box_format="xyxy") images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")  bounding_boxes = {     "boxes": np.array([         [[10, 20, 100, 150], [50, 60, 200, 250]],         [[15, 25, 110, 160], [55, 65, 210, 260]],         [[20, 30, 120, 170], [60, 70, 220, 270]],         [[25, 35, 130, 180], [65, 75, 230, 280]],     ], dtype="float32"),     "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32") }  labels = keras.ops.one_hot(     np.array([0, 1, 2, 3]),     num_classes=4 )  segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "bounding_boxes": bounding_boxes,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`\
\
* * *\
\
[RandomCrop layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_crop/#randomcrop-layer)\
\
[`RandomCrop` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_crop/#randomcrop-class)