[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.extract\_jpeg\_shape Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape#returns)
    

Extract the shape information of a JPEG-encoded image.

#### View aliases

**Main aliases**

[`tf.image.extract_jpeg_shape`](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.extract_jpeg_shape`](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)
, [`tf.compat.v1.io.extract_jpeg_shape`](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)

tf.io.extract_jpeg_shape(
        contents: Annotated[Any, _atypes.String],
        output_type: TV_ExtractJpegShape_output_type = tf.dtypes.int32,
        name=None
    ) -> Annotated[Any, TV_ExtractJpegShape_output_type]

This op only parses the image header, so it is much faster than DecodeJpeg.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The JPEG-encoded image. |
| `output_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. (Optional) The output type of the operation (int32 or int64). Defaults to int32. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `output_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.