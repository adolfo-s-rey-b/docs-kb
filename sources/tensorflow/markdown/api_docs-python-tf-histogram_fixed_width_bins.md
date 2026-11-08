[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.histogram\_fixed\_width\_bins Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/histogram_ops.py#L31-L100)

Bins the given values for use in a histogram.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.histogram_fixed_width_bins`](https://www.tensorflow.org/api_docs/python/tf/histogram_fixed_width_bins)

tf.histogram_fixed_width_bins(
        values,
        value_range,
        nbins=100,
        dtype=tf.dtypes.int32,
        name=None
    )

Given the tensor `values`, this operation returns a rank 1 `Tensor` representing the indices of a histogram into which each element of `values` would be binned. The bins are equal width and determined by the arguments `value_range` and `nbins`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | Numeric `Tensor`. |
| `value_range` | Shape \[2\] `Tensor` of same `dtype` as `values`. values <= value\_range\[0\] will be mapped to hist\[0\], values >= value\_range\[1\] will be mapped to hist\[-1\]. |
| `nbins` | Scalar `int32 Tensor`. Number of histogram bins. |
| `dtype` | dtype for returned histogram. |
| `name` | A name for this operation (defaults to 'histogram\_fixed\_width'). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` holding the indices of the binned values whose shape matches `values`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If any unsupported dtype is provided. |
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError) | If value\_range does not satisfy value\_range\[0\] < value\_range\[1\]. |

#### Examples:

    # Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.