[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.walk Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L837-L892)

Recursive directory tree generator for directories.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.walk`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk)

tf.io.gfile.walk(
        top, topdown=True, onerror=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `top` | string, a Directory name |
| `topdown` | bool, Traverse pre order if True, post order if False. |
| `onerror` | optional handler for errors. Should be a function, it will be called with the error as argument. Rethrowing the error aborts the walk. Errors that happen while listing directories are ignored. |

|     |
| --- |
| Yields<br>------ |     |
| Each yield is a 3-tuple: the pathname of a directory, followed by lists of all its subdirectories and leaf files. That is, each yield looks like: `(dirname, [subdirname, subdirname, ...], [filename, filename, ...])`. Each item is a string. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.