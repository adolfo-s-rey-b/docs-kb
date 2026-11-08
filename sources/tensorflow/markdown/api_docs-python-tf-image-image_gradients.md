[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fimage_gradients&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage Example](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#usage-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.image\_gradients Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Usage Example](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#usage-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4639-L4710)

Returns image gradients (dy, dx) for each color channel.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.image_gradients`](https://www.tensorflow.org/api_docs/python/tf/image/image_gradients)

tf.image.image_gradients(
        image
    )

Both output tensors have the same shape as the input: \[batch\_size, h, w, d\]. The gradient values are organized so that \[I(x+1, y) - I(x, y)\] is in location (x, y). That means that dy will always have zeros in the last row, and dx will always have zeros in the last column.

|     |
| --- |
| Usage Example<br>------------- |     |
| BATCH_SIZE = 1<br>    IMAGE_HEIGHT = 5<br>    IMAGE_WIDTH = 5<br>    CHANNELS = 1<br>    image = tf.reshape(tf.range(IMAGE_HEIGHT * IMAGE_WIDTH * CHANNELS,<br>      delta=1, dtype=tf.float32),<br>      shape=(BATCH_SIZE, IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS))<br>    dy, dx = tf.image.image_gradients(image)<br>    print(image[0, :,:,0])<br>    tf.Tensor(<br>      [[ 0.  1.  2.  3.  4.]<br>      [ 5.  6.  7.  8.  9.]<br>      [10. 11. 12. 13. 14.]<br>      [15. 16. 17. 18. 19.]<br>      [20. 21. 22. 23. 24.]], shape=(5, 5), dtype=float32)<br>    print(dy[0, :,:,0])<br>    tf.Tensor(<br>      [[5. 5. 5. 5. 5.]<br>      [5. 5. 5. 5. 5.]<br>      [5. 5. 5. 5. 5.]<br>      [5. 5. 5. 5. 5.]<br>      [0. 0. 0. 0. 0.]], shape=(5, 5), dtype=float32)<br>    print(dx[0, :,:,0])<br>    tf.Tensor(<br>      [[1. 1. 1. 1. 0.]<br>      [1. 1. 1. 1. 0.]<br>      [1. 1. 1. 1. 0.]<br>      [1. 1. 1. 1. 0.]<br>      [1. 1. 1. 1. 0.]], shape=(5, 5), dtype=float32) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | Tensor with shape \[batch\_size, h, w, d\]. |

|     |
| --- |
| Returns<br>------- |     |
| Pair of tensors (dy, dx) holding the vertical and horizontal image gradients (1-step finite difference). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `image` is not a 4D tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.