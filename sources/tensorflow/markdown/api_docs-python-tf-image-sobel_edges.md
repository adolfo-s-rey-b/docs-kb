[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.sobel\_edges Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4713-L4779)

Returns a tensor holding Sobel edge maps.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.sobel_edges`](https://www.tensorflow.org/api_docs/python/tf/image/sobel_edges)

tf.image.sobel_edges(
        image
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

#### Example usage:

For general usage, `image` would be loaded from a file as below:

image_bytes = tf.io.read_file(path_to_image_file)
    image = tf.image.decode_image(image_bytes)
    image = tf.cast(image, tf.float32)
    image = tf.expand_dims(image, 0)

But for demo purposes, we are using randomly generated values for `image`:

    image = tf.random.uniform(

For displaying the sobel results, PIL's [Image Module](https://pillow.readthedocs.io/en/stable/reference/Image.html)
 can be used:

# Display edge maps for the first channel (at index 0)
    Image.fromarray(sobel_y[..., 0] / 4 + 0.5).show()
    Image.fromarray(sobel_x[..., 0] / 4 + 0.5).show()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | Image tensor with shape \[batch\_size, h, w, d\] and type float32 or float64. The image(s) must be 2x2 or larger. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor holding edge maps for each channel. Returns a tensor with shape \[batch\_size, h, w, d, 2\] where the last two dimensions hold \[\[dy\[0\], dx\[0\]\], \[dy\[1\], dx\[1\]\], ..., \[dy\[d-1\], dx\[d-1\]\]\] calculated using the Sobel filter. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.