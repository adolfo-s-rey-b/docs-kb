[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsaved_model%2Fexperimental%2Fread_fingerprint&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.experimental.read\_fingerprint Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/read_fingerprint#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/fingerprinting.py#L151-L178)

Reads the fingerprint of a SavedModel in `export_dir`.

tf.saved_model.experimental.read_fingerprint(
        export_dir: str
    ) -> tf.saved_model.experimental.Fingerprint

Returns a [`tf.saved_model.experimental.Fingerprint`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint)
 object that contains the values of the SavedModel fingerprint, which is persisted on disk in the `fingerprint.pb` file in the `export_dir`.

Read more about fingerprints in the SavedModel guide at [https://www.tensorflow.org/guide/saved\_model](https://www.tensorflow.org/guide/saved_model)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | The directory that contains the SavedModel. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.saved_model.experimental.Fingerprint`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/Fingerprint)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `FileNotFoundError` | If no or an invalid fingerprint is found. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.