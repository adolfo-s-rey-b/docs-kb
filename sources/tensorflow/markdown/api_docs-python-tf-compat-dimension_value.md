[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.dimension\_value Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_shape.py#L103-L136)

Compatibility utility required to allow for both V1 and V2 behavior in TF.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.dimension_value`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value)
, [`tf.compat.v1.dimension_value`](https://www.tensorflow.org/api_docs/python/tf/compat/dimension_value)

tf.compat.dimension_value(
        dimension: Union['Dimension', int, None]
    ) -> Union[int, None]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Learnable Distributions Zoo](https://www.tensorflow.org/probability/examples/Learnable_Distributions_Zoo) |

Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to coexist with the new behavior. This utility is a bridge between the two.

When accessing the value of a TensorShape dimension, use this utility, like this:

# If you had this in your V1 code:
    value = tensor_shape[i].value
    
    # Use `dimension_value` as direct replacement compatible with both V1 & V2:
    value = dimension_value(tensor_shape[i])
    
    # This would be the V2 equivalent:
    value = tensor_shape[i]  # Warning: this will return the dim value in V2!

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dimension` | Either a `Dimension` instance, an integer, or None. |

|     |
| --- |
| Returns<br>------- |     |
| A plain value, i.e. an integer or None. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.