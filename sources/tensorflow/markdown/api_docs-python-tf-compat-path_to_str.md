[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#returns)
    
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#usage)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.path\_to\_str Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#returns)
    
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str#usage)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/compat.py#L154-L190)

Converts input which is a `PathLike` object to `str` type.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.path_to_str`](https://www.tensorflow.org/api_docs/python/tf/compat/path_to_str)

tf.compat.path_to_str(
        path
    )

Converts from any python constant representation of a `PathLike` object to a string. If the input is not a `PathLike` object, simply returns the input.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | An object that can be converted to path representation. |

|     |
| --- |
| Returns<br>------- |     |
| A `str` object. |     |

|     |
| --- |
| Usage<br>----- |     |
| In case a simplified `str` version of the path is needed from an `os.PathLike` object. |     |

#### Examples:

$ tf.compat.path_to_str('C:\XYZ\tensorflow\./.././tensorflow')
    'C:\XYZ\tensorflow\./.././tensorflow' # Windows OS
    $ tf.compat.path_to_str(Path('C:\XYZ\tensorflow\./.././tensorflow'))
    'C:\XYZ\tensorflow\..\tensorflow' # Windows OS
    $ tf.compat.path_to_str(Path('./corpus'))
    'corpus' # Linux OS
    $ tf.compat.path_to_str('./.././Corpus')
    './.././Corpus' # Linux OS
    $ tf.compat.path_to_str(Path('./.././Corpus'))
    '../Corpus' # Linux OS
    $ tf.compat.path_to_str(Path('./..////../'))
    '../..' # Linux OS

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.