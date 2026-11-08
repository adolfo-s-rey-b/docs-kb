None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [The Operation class](https://keras.io/api/ops/operation/)
 [NumPy ops](https://keras.io/api/ops/numpy/)
 [NN ops](https://keras.io/api/ops/nn/)
 [Linear algebra ops](https://keras.io/api/ops/linalg/)
 [Core ops](https://keras.io/api/ops/core/)
 [Image ops](https://keras.io/api/ops/image/)
 [FFT ops](https://keras.io/api/ops/fft/)
 [Einops ops](https://keras.io/api/ops/einops/)
 [Math ops](https://keras.io/api/ops/math/)
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
 / [Ops API](https://keras.io/api/ops/)
 / Image ops

Image ops
=========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L475)

### `affine_transform` function

Copied!

`keras.ops.image.affine_transform(     images,     transform,     interpolation="bilinear",     fill_mode="constant",     fill_value=0,     data_format=None, )`

Applies the given transform(s) to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **transform**: Projective transform matrix/matrices. A vector of length 8 or tensor of size N x 8. If one row of transform is `[a0, a1, a2, b0, b1, b2, c0, c1]`, then it maps the output point `(x, y)` to a transformed input point `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`, where `k = c0 x + c1 y + 1`. The transform is inverted compared to the transform mapping input points to output points. Note that gradients are not backpropagated into transformation parameters. Note that `c0` and `c1` are only effective when using TensorFlow backend and will be considered as `0` when using other backends.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill\_mode**: Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel.
*   **fill\_value**: Value used for points outside the boundaries of the input if `fill_mode="constant"`. Defaults to `0`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Applied affine transform image or batch of images.

**Examples**

Copied!

`>>> x = np.random.random((2, 64, 80, 3)) # batch of 2 RGB images >>> transform = np.array( ...     [ ...         [1.5, 0, -20, 0, 1.5, -16, 0, 0],  # zoom ...         [1, 0, -20, 0, 1, -16, 0, 0],  # translation ...     ] ... ) >>> y = keras.ops.image.affine_transform(x, transform) >>> y.shape (2, 64, 80, 3)`

Copied!

`>>> x = np.random.random((64, 80, 3)) # single RGB image >>> transform = np.array([1.0, 0.5, -20, 0.5, 1.0, -16, 0, 0])  # shear >>> y = keras.ops.image.affine_transform(x, transform) >>> y.shape (64, 80, 3)`

Copied!

`>>> x = np.random.random((2, 3, 64, 80)) # batch of 2 RGB images >>> transform = np.array( ...     [ ...         [1.5, 0, -20, 0, 1.5, -16, 0, 0],  # zoom ...         [1, 0, -20, 0, 1, -16, 0, 0],  # translation ...     ] ... ) >>> y = keras.ops.image.affine_transform(x, transform, ...     data_format="channels_first") >>> y.shape (2, 3, 64, 80)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1484)

### `crop_images` function

Copied!

`keras.ops.image.crop_images(     images,     top_cropping=None,     left_cropping=None,     bottom_cropping=None,     right_cropping=None,     target_height=None,     target_width=None,     data_format=None, )`

Crop `images` to a specified `height` and `width`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **top\_cropping**: Number of columns to crop from the top.
*   **left\_cropping**: Number of columns to crop from the left.
*   **bottom\_cropping**: Number of columns to crop from the bottom.
*   **right\_cropping**: Number of columns to crop from the right.
*   **target\_height**: Height of the output images.
*   **target\_width**: Width of the output images.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Cropped image or batch of images.

**Example**

Copied!

`>>> images = np.reshape(np.arange(1, 28, dtype="float32"), [3, 3, 3]) >>> images[:,:,0] # print the first channel of the images array([[ 1.,  4.,  7.],        [10., 13., 16.],        [19., 22., 25.]], dtype=float32) >>> cropped_images = keras.image.crop_images(images, 0, 0, 2, 2) >>> cropped_images[:,:,0] # print the first channel of the cropped images array([[ 1.,  4.],        [10., 13.]], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1912)

### `elastic_transform` function

Copied!

`keras.ops.image.elastic_transform(     images,     alpha=20.0,     sigma=5.0,     interpolation="bilinear",     fill_mode="reflect",     fill_value=0.0,     seed=None,     data_format=None, )`

Applies elastic deformation to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **alpha**: Scaling factor that controls the intensity of the deformation.
*   **sigma**: Standard deviation of the Gaussian filter used for smoothing the displacement fields.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill\_mode**: Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel.
*   **fill\_value**: Value used for points outside the boundaries of the input if `fill_mode="constant"`. Defaults to `0`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Transformed image or batch of images with elastic deformation.

**Examples**

Copied!

`>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images >>> y = keras.ops.image.elastic_transform(x) >>> y.shape (2, 64, 80, 3)`

Copied!

`>>> x = np.random.random((64, 80, 3))  # single RGB image >>> y = keras.ops.image.elastic_transform(x) >>> y.shape (64, 80, 3)`

Copied!

`>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images >>> y = keras.ops.image.elastic_transform( ...     x, data_format="channels_first") >>> y.shape (2, 3, 64, 80)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L657)

### `extract_patches` function

Copied!

`keras.ops.image.extract_patches(     images, size, strides=None, dilation_rate=1, padding="valid", data_format=None )`

Extracts patches from the image(s) or volume(s).

This function supports both 2D and 3D patch extraction based on the `size` argument length, similar to how [`keras.ops.conv`](https://keras.io/api/ops/nn#conv-function)
 handles different dimensions.

**Arguments**

*   **images**: Input image/volume or batch of images/volumes. For 2D patches: 3D `(H, W, C)` or 4D `(N, H, W, C)`. For 3D patches: 4D `(D, H, W, C)` or 5D `(N, D, H, W, C)`.
*   **size**: Patch size as int or tuple. Length 2 tuple `(patch_height, patch_width)` or int for 2D patches. Length 3 tuple `(patch_depth, patch_height, patch_width)` for 3D patches.
*   **strides**: Strides for patch extraction. If not specified, defaults to `size` (non-overlapping patches).
*   **dilation\_rate**: Dilation rate for patch extraction. Note that `dilation_rate > 1` is not supported with `strides > 1`.
*   **padding**: The type of padding algorithm to use: `"same"` or `"valid"`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. If not specified, defaults to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

*   **Extracted patches with shape depending on input and `size`**:
*   **\- 2D patches**: 3D (unbatched) or 4D (batched)
*   **\- 3D patches**: 4D (unbatched) or 5D (batched)

**Examples**

Copied!

`>>> # 2D patches from batch of images >>> image = np.random.random( ...     (2, 20, 20, 3) ... ).astype("float32") >>> patches = keras.ops.image.extract_patches(image, (5, 5)) >>> patches.shape (2, 4, 4, 75)`

Copied!

`>>> # 2D patches from single image >>> image = np.random.random((20, 20, 3)).astype("float32") >>> patches = keras.ops.image.extract_patches(image, (3, 3), (1, 1)) >>> patches.shape (18, 18, 27)`

Copied!

`>>> # 3D patches from batch of volumes >>> volumes = np.random.random( ...     (2, 10, 10, 10, 3) ... ).astype("float32") >>> patches = keras.ops.image.extract_patches(volumes, (3, 3, 3)) >>> patches.shape (2, 3, 3, 3, 81)`

Copied!

`>>> # 3D patches from single volume >>> volume = np.random.random((10, 10, 10, 3)).astype("float32") >>> patches = keras.ops.image.extract_patches(volume, (3, 3, 3)) >>> patches.shape (3, 3, 3, 81)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1813)

### `gaussian_blur` function

Copied!

`keras.ops.image.gaussian_blur(     images, kernel_size=(3, 3), sigma=(1.0, 1.0), data_format=None )`

Applies a Gaussian blur to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **kernel\_size**: A tuple of two integers, specifying the height and width of the Gaussian kernel.
*   **sigma**: A tuple of two floats, specifying the standard deviation of the Gaussian kernel along height and width.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Blurred image or batch of images.

**Examples**

Copied!

`>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images >>> y = keras.ops.image.gaussian_blur(x) >>> y.shape (2, 64, 80, 3)`

Copied!

`>>> x = np.random.random((64, 80, 3))  # single RGB image >>> y = keras.ops.image.gaussian_blur(x) >>> y.shape (64, 80, 3)`

Copied!

`>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images >>> y = keras.ops.image.gaussian_blur( ...     x, data_format="channels_first") >>> y.shape (2, 3, 64, 80)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L194)

### `hsv_to_rgb` function

Copied!

`keras.ops.image.hsv_to_rgb(images, data_format=None)`

Convert HSV images to RGB.

`images` must be of float dtype, and the output is only well defined if the values in `images` are in `[0, 1]`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

RGB image or batch of RGB images.

**Examples**

Copied!

`>>> import numpy as np >>> from keras import ops >>> x = np.random.random((2, 4, 4, 3)) >>> y = ops.image.hsv_to_rgb(x) >>> y.shape (2, 4, 4, 3)`

Copied!

`>>> x = np.random.random((4, 4, 3)) # Single HSV image >>> y = ops.image.hsv_to_rgb(x) >>> y.shape (4, 4, 3)`

Copied!

`>>> x = np.random.random((2, 3, 4, 4)) >>> y = ops.image.hsv_to_rgb(x, data_format="channels_first") >>> y.shape (2, 3, 4, 4)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L963)

### `map_coordinates` function

Copied!

`keras.ops.image.map_coordinates(     inputs, coordinates, order, fill_mode="constant", fill_value=0 )`

Map the input array to new coordinates by interpolation.

Note that interpolation near boundaries differs from the scipy function, because we fixed an outstanding bug [scipy/issues/2640](https://github.com/scipy/scipy/issues/2640)
.

**Arguments**

*   **inputs**: The input array.
*   **coordinates**: The coordinates at which inputs is evaluated.
*   **order**: The order of the spline interpolation. The order must be `0` or `1`. `0` indicates the nearest neighbor and `1` indicates the linear interpolation.
*   **fill\_mode**: Points outside the boundaries of the inputs are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"mirror"` and `"reflect"`. Defaults to `"constant"`.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The inputs is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The inputs is extended by the nearest pixel.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The inputs is extended by wrapping around to the opposite edge.
    *   `"mirror"`: `(c d c b | a b c d | c b a b)` The inputs is extended by mirroring about the edge.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The inputs is extended by reflecting about the edge of the last pixel.
*   **fill\_value**: Value used for points outside the boundaries of the inputs if `fill_mode="constant"`. Defaults to `0`.

**Returns**

Output input or batch of inputs.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1205)

### `pad_images` function

Copied!

`keras.ops.image.pad_images(     images,     top_padding=None,     left_padding=None,     bottom_padding=None,     right_padding=None,     target_height=None,     target_width=None,     data_format=None, )`

Pad `images` with zeros to the specified `height` and `width`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **top\_padding**: Number of rows of zeros to add on top.
*   **left\_padding**: Number of columns of zeros to add on the left.
*   **bottom\_padding**: Number of rows of zeros to add at the bottom.
*   **right\_padding**: Number of columns of zeros to add on the right.
*   **target\_height**: Height of output images.
*   **target\_width**: Width of output images.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Padded image or batch of images.

**Example**

Copied!

`>>> images = np.random.random((15, 25, 3)) >>> padded_images = keras.ops.image.pad_images( ...     images, 2, 3, target_height=20, target_width=30 ... ) >>> padded_images.shape (20, 30, 3)`

Copied!

`>>> batch_images = np.random.random((2, 15, 25, 3)) >>> padded_batch = keras.ops.image.pad_images( ...     batch_images, 2, 3, target_height=20, target_width=30 ... ) >>> padded_batch.shape (2, 20, 30, 3)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1686)

### `perspective_transform` function

Copied!

`keras.ops.image.perspective_transform(     images,     start_points,     end_points,     interpolation="bilinear",     fill_value=0,     data_format=None, )`

Applies a perspective transformation to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **start\_points**: A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the source points in the original image that define the transformation.
*   **end\_points**: A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the target points in the output image after transformation.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill\_value**: Value used for points outside the boundaries of the input if extrapolation is needed. Defaults to `0`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Applied perspective transform image or batch of images.

**Examples**

Copied!

`>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images >>> start_points = np.array( ...     [ ...         [[0, 0], [0, 64], [80, 0], [80, 64]], ...         [[0, 0], [0, 64], [80, 0], [80, 64]], ...     ] ... ) >>> end_points = np.array( ...     [ ...         [[3, 5], [7, 64], [76, -10], [84, 61]], ...         [[8, 10], [10, 61], [65, 3], [88, 43]], ...     ] ... ) >>> y = keras.ops.image.perspective_transform(x, start_points, end_points) >>> y.shape (2, 64, 80, 3)`

Copied!

`>>> x = np.random.random((64, 80, 3))  # single RGB image >>> start_points = np.array([[0, 0], [0, 64], [80, 0], [80, 64]]) >>> end_points = np.array([[3, 5], [7, 64], [76, -10], [84, 61]]) >>> y = keras.ops.image.perspective_transform(x, start_points, end_points) >>> y.shape (64, 80, 3)`

Copied!

`>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images >>> start_points = np.array( ...     [ ...         [[0, 0], [0, 64], [80, 0], [80, 64]], ...         [[0, 0], [0, 64], [80, 0], [80, 64]], ...     ] ... ) >>> end_points = np.array( ...     [ ...         [[3, 5], [7, 64], [76, -10], [84, 61]], ...         [[8, 10], [10, 61], [65, 3], [88, 43]], ...     ] ... ) >>> y = keras.ops.image.perspective_transform( ...     x, start_points, end_points, data_format="channels_first" ... ) >>> y.shape (2, 3, 64, 80)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L292)

### `resize` function

Copied!

`keras.ops.image.resize(     images,     size,     interpolation="bilinear",     antialias=False,     crop_to_aspect_ratio=False,     pad_to_aspect_ratio=False,     fill_mode="constant",     fill_value=0.0,     data_format=None, )`

Resize images to size using the specified interpolation method.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **size**: Size of output image in `(height, width)` format.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. Defaults to `"bilinear"`.
*   **antialias**: Whether to use an antialiasing filter when downsampling an image. Defaults to `False`.
*   **crop\_to\_aspect\_ratio**: If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved.
*   **pad\_to\_aspect\_ratio**: If `True`, pad the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be evenly padded on the short side.
*   **fill\_mode**: When using `pad_to_aspect_ratio=True`, padded areas are filled according to the given mode. Only `"constant"` is supported at this time (fill with constant value, equal to `fill_value`).
*   **fill\_value**: Float. Padding value to use when `pad_to_aspect_ratio=True`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Resized image or batch of images.

**Examples**

Copied!

`>>> x = np.random.random((2, 4, 4, 3)) # batch of 2 RGB images >>> y = keras.ops.image.resize(x, (2, 2)) >>> y.shape (2, 2, 2, 3)`

Copied!

`>>> x = np.random.random((4, 4, 3)) # single RGB image >>> y = keras.ops.image.resize(x, (2, 2)) >>> y.shape (2, 2, 3)`

Copied!

`>>> x = np.random.random((2, 3, 4, 4)) # batch of 2 RGB images >>> y = keras.ops.image.resize(x, (2, 2), ...     data_format="channels_first") >>> y.shape (2, 3, 2, 2)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L39)

### `rgb_to_grayscale` function

Copied!

`keras.ops.image.rgb_to_grayscale(images, data_format=None)`

Convert RGB images to grayscale.

This function converts RGB images to grayscale images. It supports both 3D and 4D tensors.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

Grayscale image or batch of grayscale images.

**Examples**

Copied!

`>>> import numpy as np >>> from keras import ops >>> x = np.random.random((2, 4, 4, 3)) >>> y = ops.image.rgb_to_grayscale(x) >>> y.shape (2, 4, 4, 1)`

Copied!

`>>> x = np.random.random((4, 4, 3)) # Single RGB image >>> y = ops.image.rgb_to_grayscale(x) >>> y.shape (4, 4, 1)`

Copied!

`>>> x = np.random.random((2, 3, 4, 4)) >>> y = ops.image.rgb_to_grayscale(x, data_format="channels_first") >>> y.shape (2, 1, 4, 4)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L115)

### `rgb_to_hsv` function

Copied!

`keras.ops.image.rgb_to_hsv(images, data_format=None)`

Convert RGB images to HSV.

`images` must be of float dtype, and the output is only well defined if the values in `images` are in `[0, 1]`.

All HSV values are in `[0, 1]`. A hue of `0` corresponds to pure red, `1/3` is pure green, and `2/3` is pure blue.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

HSV image or batch of HSV images.

**Examples**

Copied!

`>>> import numpy as np >>> from keras import ops >>> x = np.random.random((2, 4, 4, 3)) >>> y = ops.image.rgb_to_hsv(x) >>> y.shape (2, 4, 4, 3)`

Copied!

`>>> x = np.random.random((4, 4, 3)) # Single RGB image >>> y = ops.image.rgb_to_hsv(x) >>> y.shape (4, 4, 3)`

Copied!

`>>> x = np.random.random((2, 3, 4, 4)) >>> y = ops.image.rgb_to_hsv(x, data_format="channels_first") >>> y.shape (2, 3, 4, 4)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2021)

### `scale_and_translate` function

Copied!

`keras.ops.image.scale_and_translate(     images, output_shape, scale, translation, spatial_dims, method, antialias=True )`

Apply a scale and translation to the images.

Generates a new image of `output_shape` by resampling from the input image using the sampling method corresponding to method. For 2D images, this operation transforms a location in the input images, (x, y), to a location in the output image according to:

`(x * scale[1] + translation[1], y * scale[0] + translation[0])`.

(Note the inverse warp is used to generate the sample locations.) Assumes half-centered pixels, i.e the pixel at integer location row, col has coordinates y, x = row + 0.5, col + 0.5, and similarly for other input image dimensions.

If an output location(pixel) maps to an input sample location that is outside the input boundaries then the value for the output location will be set to zero.

The `method` argument expects one of the following resize methods:

*   `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`: Linear interpolation. If `antialias` is True, uses a triangular filter when downsampling.
*   `"cubic"`, `"bicubic"`, `"tricubic"`: Cubic interpolation, using the Keys cubic kernel.
*   `"lanczos3"`: Lanczos resampling, using a kernel of radius 3.
*   `"lanczos5"`: Lanczos resampling, using a kernel of radius 5.

**Arguments**

*   **images**: The input array.
*   **output\_shape**: The output shape, as a sequence of integers with length equal to the number of dimensions of image.
*   **scale**: A \[K\] array with the same number of dimensions as `images`, containing the scale to apply in each dimension.
*   **translation**: A \[K\] array with the same number of dimensions as `images`, containing the translation to apply in each dimension.
*   **spatial\_dims**: A length K tuple specifying the spatial dimensions that the passed `scale` and `translation` should be applied to.
*   **method**: A string specifying the resizing method to use. Available methods are `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`, `"cubic"`, `"bicubic"`, `"tricubic"`, `"lanczos3"` and `"lanczos5"`.
*   **antialias**: Whether an antialiasing filter should be applied when downsampling. Has no effect when upsampling. Defaults to `True`.

**Returns**

The scale and translated images.

**Example**

Copied!

`>>> images = np.arange(9, dtype="float32").reshape((3, 3)) >>> scale = np.array([2.0, 2.0]).astype("float32") >>> translation = -(scale / 2.0 - 0.5) >>> resized_images = keras.image.scale_and_translate( ...     images, (5, 5), scale, translation, (0, 1), "linear" ... ) >>> resized_images array([[0.0 0.5 1.0 1.5 2.0]        [1.5 2.0 2.5 3.0 3.5]        [3.0 3.5 4.0 4.5 5.0]        [4.5 5.0 5.5 6.0 6.5]        [6.0 6.5 7.0 7.5 8.0]], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2128)

### `sobel_edges` function

Copied!

`keras.ops.image.sobel_edges(images, data_format=None)`

Computes Sobel edge detection on images.

The Sobel operator computes the gradient of the image intensity at each pixel, giving the direction of the largest increase from light to dark and the rate of change in that direction.

**Arguments**

*   **images**: Input tensor of shape `(batch, height, width, channels)` if `data_format="channels_last"`, or `(batch, channels, height, width)` if `data_format="channels_first"`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

A tensor containing the Sobel edges. For `data_format="channels_last"`, the output shape is `(batch, height, width, channels, 2)` where the last dimension contains `[dy, dx]` representing the vertical and horizontal gradients. For `data_format="channels_first"`, the output shape is `(batch, channels, height, width, 2)`.

**Example**

Copied!

`>>> import numpy as np >>> from keras import ops >>> # Create image with vertical edge >>> image = np.zeros((1, 8, 8, 1), dtype="float32") >>> image[0, :, 4:, 0] = 1.0 >>> edges = ops.image.sobel_edges(image) >>> edges.shape (1, 8, 8, 1, 2)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2224)

### `ssim` function

Copied!

`keras.ops.image.ssim(     image1,     image2,     max_val=1.0,     filter_size=11,     filter_sigma=1.5,     k1=0.01,     k2=0.03,     data_format=None, )`

Computes the Structural Similarity Index (SSIM) between two images.

The SSIM index is a method for measuring the similarity between two images. It is based on the comparison of luminance, contrast, and structure between the images. The resulting SSIM index is a value between -1 and 1, where 1 indicates identical images.

This implementation is based on the original SSIM paper: Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). "Image quality assessment: from error visibility to structural similarity." IEEE Transactions on Image Processing.

**Arguments**

*   **image1**: First image or batch of images. Must be 3D or 4D.
*   **image2**: Second image or batch of images. Must have the same shape as `image1`.
*   **max\_val**: The maximum possible pixel value of the images. Defaults to `1.0` (for normalized images). Use `255.0` for images with pixel values in `[0, 255]`.
*   **filter\_size**: Size of the Gaussian filter used for computing SSIM. Defaults to `11`. Must be an odd integer >= 1.
*   **filter\_sigma**: Standard deviation of the Gaussian filter. Defaults to `1.5`.
*   **k1**: First stabilization constant. Defaults to `0.01`.
*   **k2**: Second stabilization constant. Defaults to `0.03`.
*   **data\_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function)
    .

**Returns**

A tensor of SSIM values. For batched inputs, returns a 1D tensor with one SSIM value per image pair. For unbatched inputs, returns a scalar tensor.

**Examples**

Copied!

`>>> import numpy as np >>> from keras import ops >>> # Two identical images should have SSIM = 1 >>> image = np.random.random((32, 32, 3)).astype("float32") >>> ssim_value = ops.image.ssim(image, image, max_val=1.0) >>> float(ssim_value) > 0.99 True`

Copied!

`>>> # Batched images >>> images1 = np.random.random((2, 32, 32, 3)).astype("float32") >>> images2 = np.random.random((2, 32, 32, 3)).astype("float32") >>> ssim_values = ops.image.ssim(images1, images2, max_val=1.0) >>> ssim_values.shape (2,)`

* * *

[Image ops](https://keras.io/api/ops/image/#image-ops)

[`affine_transform` function](https://keras.io/api/ops/image/#affinetransform-function)

[`crop_images` function](https://keras.io/api/ops/image/#cropimages-function)

[`elastic_transform` function](https://keras.io/api/ops/image/#elastictransform-function)

[`extract_patches` function](https://keras.io/api/ops/image/#extractpatches-function)

[`gaussian_blur` function](https://keras.io/api/ops/image/#gaussianblur-function)

[`hsv_to_rgb` function](https://keras.io/api/ops/image/#hsvtorgb-function)

[`map_coordinates` function](https://keras.io/api/ops/image/#mapcoordinates-function)

[`pad_images` function](https://keras.io/api/ops/image/#padimages-function)

[`perspective_transform` function](https://keras.io/api/ops/image/#perspectivetransform-function)

[`resize` function](https://keras.io/api/ops/image/#resize-function)

[`rgb_to_grayscale` function](https://keras.io/api/ops/image/#rgbtograyscale-function)

[`rgb_to_hsv` function](https://keras.io/api/ops/image/#rgbtohsv-function)

[`scale_and_translate` function](https://keras.io/api/ops/image/#scaleandtranslate-function)

[`sobel_edges` function](https://keras.io/api/ops/image/#sobeledges-function)

[`ssim` function](https://keras.io/api/ops/image/#ssim-function)