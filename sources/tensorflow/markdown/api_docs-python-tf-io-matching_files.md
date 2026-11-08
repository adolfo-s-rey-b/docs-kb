[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/matching_files#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/matching_files)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/matching_files?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/matching_files#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/matching_files#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.matching\_files Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/matching_files#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/matching_files#returns)
    

Returns the set of files matching one or more glob patterns.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.matching_files`](https://www.tensorflow.org/api_docs/python/tf/io/matching_files)
, [`tf.compat.v1.matching_files`](https://www.tensorflow.org/api_docs/python/tf/io/matching_files)

tf.io.matching_files(
        pattern: Annotated[Any, _atypes.String], name=None
    ) -> Annotated[Any, _atypes.String]

Note that this routine only supports wildcard characters in the basename portion of the pattern, not in the directory portion. Note also that the order of filenames returned is deterministic.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pattern` | A `Tensor` of type `string`. Shell wildcard pattern(s). Scalar or vector of type string. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `string`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.