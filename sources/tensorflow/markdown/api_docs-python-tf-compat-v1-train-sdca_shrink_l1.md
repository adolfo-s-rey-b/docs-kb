[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/sdca_shrink_l1#main-content)

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
    

tf.compat.v1.train.sdca\_shrink\_l1 Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

Applies L1 regularization shrink step on the parameters.

tf.compat.v1.train.sdca_shrink_l1(
        weights: Annotated[List[Any], _atypes.Float32],
        l1: float,
        l2: float,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weights` | A list of `Tensor` objects with type mutable `float32`. a list of vectors where each value is the weight associated with a feature group. |
| `l1` | A `float`. Symmetric l1 regularization strength. |
| `l2` | A `float`. Symmetric l2 regularization strength. Should be a positive float. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The created Operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.