[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dtypes.saturate\_cast Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1057-L1158)

Performs a safe saturating cast of `value` to `dtype`.

#### View aliases

**Main aliases**

[`tf.saturate_cast`](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.dtypes.saturate_cast`](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast)
, [`tf.compat.v1.saturate_cast`](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast)

tf.dtypes.saturate_cast(
        value, dtype, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression) |

This function casts the input to `dtype` without overflow. If there is a danger that values would over or underflow in the cast, this op applies the appropriate clamping before the cast. See [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
 for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A `Tensor`. |
| `dtype` | The desired output `DType`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| `value` safely cast to `dtype`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.