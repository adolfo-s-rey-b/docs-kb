[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fgfile%2FExists&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.gfile.Exists Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L296-L298)

Determines whether a path exists or not.

tf.compat.v1.gfile.Exists(
        filename
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

    with open("/tmp/x", "w") as f:

You can also specify the URI scheme for selecting a different filesystem:

    # for a GCS filesystem path:

This currently returns `True` for existing directories but don't rely on this behavior, especially if you are using cloud filesystems (e.g., GCS, S3, Hadoop):

    tf.io.gfile.exists("/tmp")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | string, a path |

|     |
| --- |
| Returns<br>------- |     |
| True if the path exists, whether it's a file or a directory. False if the path does not exist and there are no filesystem errors. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Propagates any errors reported by the FileSystem API. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.