[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fio%2Fgfile%2Fmkdir&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.mkdir Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L470-L483)

Creates a directory with the name given by `path`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.mkdir`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir)

tf.io.gfile.mkdir(
        path
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Azure blob storage with TensorFlow](https://www.tensorflow.org/io/tutorials/azure) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | string, name of the directory to be created |

Notes: The parent directories need to exist. Use [`tf.io.gfile.makedirs`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/makedirs)
 instead if there is the possibility that the parent dirs don't exist.

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | If the operation fails. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.