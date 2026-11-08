[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/central_crop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/central_crop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.central\_crop Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/central_crop#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L859-L1003)

Crop the central region of the image(s).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.central_crop`](https://www.tensorflow.org/api_docs/python/tf/image/central_crop)

tf.image.central_crop(
        image, central_fraction
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

Remove the outer parts of an image but retain the central region of the image along each dimension. If we specify `central_fraction = 0.5`, this function returns the region marked with "X" in the below diagram. The larger the value of `central_fraction`, the larger the dimension of the region to be cropped and retained.

 --------
    |        |
    |  XXXX  |
    |  XXXX  |
    |        |   where "X" is the central 50% of the image.
     --------

This function works on either a single image (`image` is a 3-D Tensor), or a batch of images (`image` is a 4-D Tensor).

#### Usage Example:

    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | Either a 3-D float Tensor of shape \[height, width, depth\], or a 4-D Tensor of shape \[batch\_size, height, width, depth\]. |\
| `central_fraction` | float (0, 1\], fraction of size to crop |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if central\_crop\_fraction is not within (0, 1\]. |

|     |
| --- |
| Returns<br>------- |     |
| 3-D / 4-D float Tensor, as per the input. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.