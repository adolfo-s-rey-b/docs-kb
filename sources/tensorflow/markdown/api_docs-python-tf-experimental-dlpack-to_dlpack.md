[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dlpack/to_dlpack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dlpack.to\_dlpack Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/dlpack/dlpack.py#L22-L41)

Returns the dlpack capsule representing the tensor.

tf.experimental.dlpack.to_dlpack(
        tf_tensor
    )

This operation ensures the underlying data memory is ready when returns.

  a = tf.tensor([1, 10])
      dlcapsule = tf.experimental.dlpack.to_dlpack(a)
      # dlcapsule represents the dlpack data structure

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tf_tensor` | Tensorflow eager tensor, to be converted to dlpack capsule. |

|     |
| --- |
| Returns<br>------- |     |
| A PyCapsule named as dltensor, which shares the underlying memory to other framework. This PyCapsule can be consumed only once. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.