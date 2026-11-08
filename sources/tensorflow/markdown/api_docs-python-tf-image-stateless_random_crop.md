[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fstateless_random_crop&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.stateless\_random\_crop Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_crop#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_crop_ops.py#L85-L135)

Randomly crops a tensor to a given size in a deterministic manner.

tf.image.stateless_random_crop(
        value, size, seed, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

Slices a shape `size` portion out of `value` at a uniformly chosen offset. Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension. For example, RGB images can be cropped with `size = [crop_height, crop_width, 3]`.

Guarantees the same results given the same `seed` independent of how many times the function is called, and independent of global seed settings (e.g. [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)
).

#### Usage Example:

    image = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | Input tensor to crop. |
| `size` | 1-D tensor with size the rank of `value`. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A cropped tensor of the same rank as `value` and shape `size`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.