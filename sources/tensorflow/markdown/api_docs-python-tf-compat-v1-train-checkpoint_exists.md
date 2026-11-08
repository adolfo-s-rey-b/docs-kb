[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fcheckpoint_exists&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.checkpoint\_exists Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/checkpoint_exists#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L392-L411)

Checks whether a V1 or V2 checkpoint exists with the specified prefix. (deprecated)

tf.compat.v1.train.checkpoint_exists(
        checkpoint_prefix
    )

This is the recommended way to check if a checkpoint exists, since it takes into account the naming difference between V1 and V2 formats.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint_prefix` | the prefix of a V1 or V2 checkpoint, with V2 taking priority. Typically the result of `Saver.save()` or that of [`tf.train.latest_checkpoint()`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)<br>, regardless of sharded/non-sharded or V1/V2. |

|     |
| --- |
| Returns<br>------- |     |
| A bool, true if a checkpoint referred to by `checkpoint_prefix` exists. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.