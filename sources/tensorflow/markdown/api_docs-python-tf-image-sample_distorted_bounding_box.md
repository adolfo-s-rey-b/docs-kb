[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fsample_distorted_bounding_box&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.sample\_distorted\_bounding\_box Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/sample_distorted_bounding_box#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3436-L3559)

Generate a single randomly distorted bounding box for an image.

tf.image.sample_distorted_bounding_box(
        image_size,
        bounding_boxes,
        seed=0,
        min_object_covered=0.1,
        aspect_ratio_range=None,
        area_range=None,
        max_attempts=None,
        use_image_if_no_bounding_boxes=None,
        name=None
    )

Bounding box annotations are often supplied in addition to ground-truth labels in image recognition or object localization tasks. A common technique for training such a system is to randomly distort an image while preserving its content, i.e. _data augmentation_. This Op outputs a randomly distorted localization of an object, i.e. bounding box, given an `image_size`, `bounding_boxes` and a series of constraints.

The output of this Op is a single bounding box that may be used to crop the original image. The output is returned as 3 tensors: `begin`, `size` and `bboxes`. The first 2 tensors can be fed directly into [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice)
 to crop the image. The latter may be supplied to [`tf.image.draw_bounding_boxes`](https://www.tensorflow.org/api_docs/python/tf/image/draw_bounding_boxes)
 to visualize what the bounding box looks like.

Bounding boxes are supplied and returned as `[y_min, x_min, y_max, x_max]`. The bounding box coordinates are floats in `[0.0, 1.0]` relative to the width and the height of the underlying image.

For example,

    # Generate a single distorted bounding box.
        begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
            tf.shape(image),
            bounding_boxes=bounding_boxes,
            min_object_covered=0.1)
    
        # Draw the bounding box in an image summary.
        image_with_box = tf.image.draw_bounding_boxes(tf.expand_dims(image, 0),
                                                      bbox_for_draw)
        tf.compat.v1.summary.image('images_with_box', image_with_box)
    
        # Employ the bounding box to distort the image.
        distorted_image = tf.slice(image, begin, size)

Note that if no bounding box information is available, setting `use_image_if_no_bounding_boxes = true` will assume there is a single implicit bounding box covering the whole image. If `use_image_if_no_bounding_boxes` is false and no bounding boxes are supplied, an error is raised.

For producing deterministic results given a `seed` value, use [`tf.image.stateless_sample_distorted_bounding_box`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_sample_distorted_bounding_box)
. Unlike using the `seed` param with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same results given the same seed independent of how many times the function is called, and independent of global seed settings (e.g. tf.random.set\_seed).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image_size` | A `Tensor`. Must be one of the following types: `uint8`, `int8`, `int16`, `int32`, `int64`. 1-D, containing `[height, width, channels]`. |
| `bounding_boxes` | A `Tensor` of type `float32`. 3-D with shape `[batch, N, 4]` describing the N bounding boxes associated with the image. |
| `seed` | An optional `int`. Defaults to `0`. If `seed` is set to non-zero, the random number generator is seeded by the given `seed`. Otherwise, it is seeded by a random seed. |
| `min_object_covered` | A Tensor of type `float32`. Defaults to `0.1`. The cropped area of the image must contain at least this fraction of any bounding box supplied. The value of this parameter should be non-negative. In the case of 0, the cropped area does not need to overlap any of the bounding boxes supplied. |
| `aspect_ratio_range` | An optional list of `floats`. Defaults to `[0.75, 1.33]`. The cropped area of the image must have an aspect `ratio = width / height` within this range. |
| `area_range` | An optional list of `floats`. Defaults to `[0.05, 1]`. The cropped area of the image must contain a fraction of the supplied image within this range. |
| `max_attempts` | An optional `int`. Defaults to `100`. Number of attempts at generating a cropped region of the image of the specified constraints. After `max_attempts` failures, return the entire image. |
| `use_image_if_no_bounding_boxes` | An optional `bool`. Defaults to `False`. Controls behavior if no bounding boxes supplied. If true, assume an implicit bounding box covering the whole input. If false, raise an error. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (begin, size, bboxes). |     |
| `begin` | A `Tensor`. Has the same type as `image_size`. 1-D, containing `[offset_height, offset_width, 0]`. Provide as input to [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice)<br>. |
| `size` | A `Tensor`. Has the same type as `image_size`. 1-D, containing `[target_height, target_width, -1]`. Provide as input to [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice)<br>. |
| `bboxes` | A `Tensor` of type `float32`. 3-D with shape `[1, 1, 4]` containing the distorted bounding box. Provide as input to [`tf.image.draw_bounding_boxes`](https://www.tensorflow.org/api_docs/python/tf/image/draw_bounding_boxes)<br>. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If no seed is specified and op determinism is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.