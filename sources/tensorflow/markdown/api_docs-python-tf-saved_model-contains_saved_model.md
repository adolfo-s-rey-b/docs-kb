[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsaved_model%2Fcontains_saved_model&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.contains\_saved\_model Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/loader_impl.py#L257-L275)

Checks whether the provided export directory could contain a SavedModel.

tf.saved_model.contains_saved_model(
        export_dir
    )

Note that the method does not load any data by itself. If the method returns `false`, the export directory definitely does not contain a SavedModel. If the method returns `true`, the export directory may contain a SavedModel but provides no guarantee that it can be loaded.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | Absolute path to possible export location. For example, '/my/foo/model'. |

|     |
| --- |
| Returns<br>------- |     |
| True if the export directory contains SavedModel files, False otherwise. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.