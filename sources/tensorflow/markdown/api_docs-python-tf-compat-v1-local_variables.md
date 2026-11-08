[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flocal_variables&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.local\_variables Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1832-L1857)

Returns local variables.

tf.compat.v1.local_variables(
        scope=None
    )

Local variables - per process variables, usually not saved/restored to checkpoint and used for temporary or intermediate values. For example, they can be used as counters for metrics computation or number of epochs this machine has read data. The `tf.contrib.framework.local_variable()` function automatically adds the new variable to `GraphKeys.LOCAL_VARIABLES`. This convenience function returns the contents of that collection.

An alternative to local variables are global variables. See [`tf.compat.v1.global_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scope` | (Optional.) A string. If supplied, the resulting list is filtered to include only items whose `name` attribute matches `scope` using `re.match`. Items without a `name` attribute are never returned if a scope is supplied. The choice of `re.match` means that a `scope` without special tokens filters by prefix. |

|     |
| --- |
| Returns<br>------- |     |
| A list of local `Variable` objects. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.