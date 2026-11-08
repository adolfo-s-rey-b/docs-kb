[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fio%2Fmatch_filenames_once&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.match\_filenames\_once Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L56-L76)

Save the list of files matching pattern, so it is only computed once.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.match_filenames_once`](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once)
, [`tf.compat.v1.train.match_filenames_once`](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once)

tf.io.match_filenames_once(
        pattern, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pattern` | A file pattern (glob), or 1D tensor of file patterns. |
| `name` | A name for the operations (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A variable that is initialized to the list of files matching the pattern(s). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.