[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_at_index#main-content)

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
    

tf.compat.dimension\_at\_index Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L139-L185)

Compatibility utility required to allow for both V1 and V2 behavior in TF.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.dimension_at_index`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_at_index)
, [`tf.compat.v1.dimension_at_index`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_at_index)

tf.compat.dimension_at_index(
        shape, index
    ) -> 'Dimension'

Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to coexist with the new behavior. This utility is a bridge between the two.

If you want to retrieve the Dimension instance corresponding to a certain index in a TensorShape instance, use this utility, like this:

# If you had this in your V1 code:
    dim = tensor_shape[i]
    
    # Use `dimension_at_index` as direct replacement compatible with both V1 & V2:
    dim = dimension_at_index(tensor_shape, i)
    
    # Another possibility would be this, but WARNING: it only works if the
    # tensor_shape instance has a defined rank.
    dim = tensor_shape.dims[i]  # `dims` may be None if the rank is undefined!
    
    # In native V2 code, we recommend instead being more explicit:
    if tensor_shape.rank is None:
      dim = Dimension(None)
    else:
      dim = tensor_shape.dims[i]
    
    # Being more explicit will save you from the following trap (present in V1):
    # you might do in-place modifications to `dim` and expect them to be reflected
    # in `tensor_shape[i]`, but they would not be (as the Dimension object was
    # instantiated on the fly.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A TensorShape instance. |
| `index` | An integer index. |

|     |
| --- |
| Returns<br>------- |     |
| A dimension object. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.