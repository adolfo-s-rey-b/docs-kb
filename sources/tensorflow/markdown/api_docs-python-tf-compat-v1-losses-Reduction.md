[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#methods)
    *   [all](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#all)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#validate)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.Reduction Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#methods)
    *   [all](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#all)
        
    *   [validate](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#validate)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L35-L71)

Types of loss reduction.

Contains the following values:

*   `NONE`: Un-reduced weighted losses with the same shape as input.
*   `SUM`: Scalar sum of weighted losses.
*   `MEAN`: Scalar `SUM` divided by sum of weights. DEPRECATED.
*   `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses.
*   `SUM_OVER_NONZERO_WEIGHTS`: Scalar `SUM` divided by number of non-zero weights. DEPRECATED.
*   `SUM_BY_NONZERO_WEIGHTS`: Same as `SUM_OVER_NONZERO_WEIGHTS`. DEPRECATED.

Methods
-------

### `all`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L57-L65)

@classmethod

### `validate`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L67-L71)

@classmethod

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| MEAN | `'weighted_mean'` |
| NONE | `'none'` |
| SUM | `'weighted_sum'` |
| SUM\_BY\_NONZERO\_WEIGHTS | `'weighted_sum_by_nonzero_weights'` |
| SUM\_OVER\_BATCH\_SIZE | `'weighted_sum_over_batch_size'` |
| SUM\_OVER\_NONZERO\_WEIGHTS | `'weighted_sum_by_nonzero_weights'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.