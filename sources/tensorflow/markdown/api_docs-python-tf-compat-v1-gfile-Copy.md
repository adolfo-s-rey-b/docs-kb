[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.gfile.Copy Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L585-L587)

Copies data from `src` to `dst`.

tf.compat.v1.gfile.Copy(
        oldpath, newpath, overwrite=False
    )

    with open("/tmp/x", "w") as f:

You can also specify the URI scheme for selecting a different filesystem:

    with open("/tmp/x", "w") as f:

Note that you need to always specify a file name, even if moving into a new directory. This is because some cloud filesystems don't have the concept of a directory.

    with open("/tmp/x", "w") as f:

If you want to prevent errors if the path already exists, you can use `overwrite` argument:

    with open("/tmp/x", "w") as f:

Note that the above will still result in an error if you try to overwrite a directory with a file.

Note that you cannot copy a directory, only file arguments are supported.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `src` | string, name of the file whose contents need to be copied |
| `dst` | string, name of the file to which to copy to |
| `overwrite` | boolean, if false it's an error for `dst` to be occupied by an existing file. |

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