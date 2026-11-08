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
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)
 [Experiment management utilities](https://keras.io/api/utils/experiment_management_utils/)
 [Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/api/utils/feature_space/)
 [Tensor utilities](https://keras.io/api/utils/tensor_utils/)
 [Bounding boxes](https://keras.io/api/utils/bounding_boxes/)
 [Python & NumPy utilities](https://keras.io/api/utils/python_utils/)
 [Bounding boxes utilities](https://keras.io/api/utils/bounding_boxes_utils/)
 [Visualization utilities](https://keras.io/api/utils/visualization_utils/)
 [Preprocessing utilities](https://keras.io/api/utils/preprocessing_utils/)
 [Backend utilities](https://keras.io/api/utils/backend_utils/)
 [Scikit-Learn API wrappers](https://keras.io/api/utils/sklearn_wrappers/)
 [Keras configuration utilities](https://keras.io/api/utils/config_utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Utilities](https://keras.io/api/utils/)
 / Preprocessing utilities

Preprocessing utilities
=======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L308)

### `smart_resize` function

Copied!

`keras.preprocessing.image.smart_resize(     x, size, interpolation="bilinear", data_format="channels_last", **kwargs )`

Resize images to a target size without aspect ratio distortion.

Image datasets typically yield images that have each a different size. However, these images need to be batched before they can be processed by Keras layers. To be batched, images need to share the same height and width.

You could simply do, in TF (or JAX equivalent):

Copied!

`size = (200, 200) ds = ds.map(lambda img: resize(img, size))`

However, if you do this, you distort the aspect ratio of your images, since in general they do not all have the same aspect ratio as `size`. This is fine in many cases, but not always (e.g. for image generation models this can be a problem).

Note that passing the argument `preserve_aspect_ratio=True` to `resize` will preserve the aspect ratio, but at the cost of no longer respecting the provided target size.

This calls for:

Copied!

`size = (200, 200) ds = ds.map(lambda img: smart_resize(img, size))`

Your output images will actually be `(200, 200)`, and will not be distorted. Instead, the parts of the image that do not fit within the target size get cropped out.

The resizing process is:

1.  Take the largest centered crop of the image that has the same aspect ratio as the target size. For instance, if `size=(200, 200)` and the input image has size `(340, 500)`, we take a crop of `(340, 340)` centered along the width.
2.  Resize the cropped image to the target size. In the example above, we resize the `(340, 340)` crop to `(200, 200)`.

**Arguments**

*   **x**: Input image or batch of images (as a tensor or NumPy array). Must be in format `(height, width, channels)` or `(batch_size, height, width, channels)`.
*   **size**: Tuple of `(height, width)` integer. Target size.
*   **interpolation**: String, interpolation to use for resizing. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"lanczos3"`, `"lanczos5"`. Defaults to `"bilinear"`.
*   **data\_format**: `"channels_last"` or `"channels_first"`.

**Returns**

Array with shape `(size[0], size[1], channels)`. If the input image was a NumPy array, the output is a NumPy array, and if it was a backend-native tensor, the output is a backend-native tensor.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L199)

### `load_img` function

Copied!

`keras.preprocessing.image.load_img(     path,     color_mode="rgb",     target_size=None,     interpolation="nearest",     keep_aspect_ratio=False, )`

Loads an image into PIL format.

**Example**

Copied!

`image = keras.utils.load_img(image_path) input_arr = keras.utils.img_to_array(image) input_arr = np.array([input_arr])  # Convert single image to a batch. predictions = model.predict(input_arr)`

**Arguments**

*   **path**: Path to image file.
*   **color\_mode**: One of `"grayscale"`, `"rgb"`, `"rgba"`. Default: `"rgb"`. The desired image format.
*   **target\_size**: Either `None` (default to original size) or tuple of ints `(img_height, img_width)`.
*   **interpolation**: Interpolation method used to resample the image if the target size is different from that of the loaded image. Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. If PIL version 1.1.3 or newer is installed, `"lanczos"` is also supported. If PIL version 3.4.0 or newer is installed, `"box"` and `"hamming"` are also supported. By default, `"nearest"` is used.
*   **keep\_aspect\_ratio**: Boolean, whether to resize images to a target size without aspect ratio distortion. The image is cropped in the center with target aspect ratio before resizing.

**Returns**

A PIL Image instance.

**Guides and examples using `load_img`**

*   [Segment Anything](https://keras.io/keras_hub/guides/segment_anything_in_keras_hub/)
    
*   [Image Classification](https://keras.io/keras_hub/guides/classification_with_keras_hub/)
    
*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
    
*   [Object Detection Fine-tuning with KerasHub](https://keras.io/keras_hub/guides/object_detection_retinanet/)
    
*   [Image classification from scratch](https://keras.io/examples/vision/image_classification_from_scratch/)
    
*   [Highly accurate boundaries segmentation using BASNet](https://keras.io/examples/vision/basnet_segmentation/)
    
*   [Object detection with Vision Transformers](https://keras.io/examples/vision/object_detection_using_vision_transformer/)
    
*   [Model interpretability with Integrated Gradients](https://keras.io/examples/vision/integrated_gradients/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L162)

### `save_img` function

Copied!

`keras.preprocessing.image.save_img(     path, x, data_format=None, file_format=None, scale=True, **kwargs )`

Saves an image stored as a NumPy array to a path or file object.

**Arguments**

*   **path**: Path or file object.
*   **x**: NumPy array.
*   **data\_format**: Image data format, either `"channels_first"` or `"channels_last"`.
*   **file\_format**: Optional file format override. If omitted, the format to use is determined from the filename extension. If a file object was used instead of a filename, this parameter should always be used.
*   **scale**: Whether to rescale image values to be within `[0, 255]`.
*   **\*\*kwargs**: Additional keyword arguments passed to `PIL.Image.save()`.

**Guides and examples using `save_img`**

*   [Deep Dream](https://keras.io/examples/generative/deep_dream/)
    
*   [PixelCNN](https://keras.io/examples/generative/pixelcnn/)
    
*   [Neural style transfer](https://keras.io/examples/generative/neural_style_transfer/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/py_dataset_adapter.py#L17)

### `PyDataset` class

Copied!

`keras.utils.PyDataset(workers=1, use_multiprocessing=False, max_queue_size=10)`

Base class for defining a parallel dataset using Python code.

Every `PyDataset` must implement the `__getitem__()` and the `__len__()` methods. If you want to modify your dataset between epochs, you may additionally implement `on_epoch_end()`, or `on_epoch_begin` to be called at the start of each epoch. The `__getitem__()` method should return a complete batch (not a single sample), and the `__len__` method should return the number of batches in the dataset (rather than the number of samples).

**Arguments**

*   **workers**: Number of workers to use in multithreading or multiprocessing.
*   **use\_multiprocessing**: Whether to use Python multiprocessing for parallelism. Setting this to `True` means that your dataset will be replicated in multiple forked processes. This is necessary to gain compute-level (rather than I/O level) benefits from parallelism. However it can only be set to `True` if your dataset can be safely pickled.
*   **max\_queue\_size**: Maximum number of batches to keep in the queue when iterating over the dataset in a multithreaded or multiprocessed setting. Reduce this value to reduce the CPU memory consumption of your dataset. Defaults to 10.

Notes:

*   `PyDataset` is a safer way to do multiprocessing. This structure guarantees that the model will only train once on each sample per epoch, which is not the case with Python generators.
*   The arguments `workers`, `use_multiprocessing`, and `max_queue_size` exist to configure how `fit()` uses parallelism to iterate over the dataset. They are not being used by the `PyDataset` class directly. When you are manually iterating over a `PyDataset`, no parallelism is applied.

**Example**

Copied!

``from skimage.io import imread from skimage.transform import resize import numpy as np import math  # Here, `x_set` is list of path to the images # and `y_set` are the associated classes.  class CIFAR10PyDataset(keras.utils.PyDataset):      def __init__(self, x_set, y_set, batch_size, **kwargs):         super().__init__(**kwargs)         self.x, self.y = x_set, y_set         self.batch_size = batch_size      def __len__(self):         # Return number of batches.         return math.ceil(len(self.x) / self.batch_size)      def __getitem__(self, idx):         # Return x, y for batch idx.         low = idx * self.batch_size         # Cap upper bound at array length; the last batch may be smaller         # if the total number of items is not a multiple of batch size.         high = min(low + self.batch_size, len(self.x))         batch_x = self.x[low:high]         batch_y = self.y[low:high]          return np.array([             resize(imread(file_name), (200, 200))                for file_name in batch_x]), np.array(batch_y)``

**Guides and examples using `PyDataset`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
    
*   [Image classification via fine-tuning with EfficientNet](https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/)
    
*   [When Recurrence meets Transformers](https://keras.io/examples/vision/temporal_latent_bottleneck/)
    
*   [Highly accurate boundaries segmentation using BASNet](https://keras.io/examples/vision/basnet_segmentation/)
    
*   [Keypoint Detection with Transfer Learning](https://keras.io/examples/vision/keypoint_detection/)
    
*   [Monocular depth estimation](https://keras.io/examples/vision/depth_estimation/)
    
*   [Semi-supervision and domain adaptation with AdaMatch](https://keras.io/examples/vision/adamatch/)
    
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)
    

* * *

[Preprocessing utilities](https://keras.io/api/utils/preprocessing_utils/#preprocessing-utilities)

[`smart_resize` function](https://keras.io/api/utils/preprocessing_utils/#smartresize-function)

[`load_img` function](https://keras.io/api/utils/preprocessing_utils/#loadimg-function)

[`save_img` function](https://keras.io/api/utils/preprocessing_utils/#saveimg-function)

[`PyDataset` class](https://keras.io/api/utils/preprocessing_utils/#pydataset-class)