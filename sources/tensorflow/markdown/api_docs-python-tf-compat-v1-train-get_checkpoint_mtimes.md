[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fget_checkpoint_mtimes&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.get\_checkpoint\_mtimes Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_checkpoint_mtimes#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L414-L457)

Returns the mtimes (modification timestamps) of the checkpoints. (deprecated)

tf.compat.v1.train.get_checkpoint_mtimes(
        checkpoint_prefixes
    )

Globs for the checkpoints pointed to by `checkpoint_prefixes`. If the files exist, collect their mtime. Both V2 and V1 checkpoints are considered, in that priority.

This is the recommended way to get the mtimes, since it takes into account the naming difference between V1 and V2 formats.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint_prefixes` | a list of checkpoint paths, typically the results of `Saver.save()` or those of [`tf.train.latest_checkpoint()`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)<br>, regardless of sharded/non-sharded or V1/V2. |

|     |
| --- |
| Returns<br>------- |     |
| A list of mtimes (in microseconds) of the found checkpoints. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.