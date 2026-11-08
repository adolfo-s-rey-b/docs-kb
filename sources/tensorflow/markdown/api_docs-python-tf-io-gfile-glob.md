[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.glob Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L385-L451)

Returns a list of files that match the given pattern(s).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.glob`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob)

tf.io.gfile.glob(
        pattern
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation) |

The patterns are defined as strings. Supported patterns are defined here. Note that the pattern can be a Python iteratable of string patterns.

The format definition of the pattern is:

**pattern**: `{ term }`

**term**:

*   `'*'`: matches any sequence of non-'/' characters
*   `'?'`: matches a single non-'/' character
*   `'[' [ '^' ] { match-list } ']'`: matches any single character (not) on the list
*   `c`: matches character `c` where `c != '*', '?', '\\', '['`\
*   `'\\' c`: matches character `c`\
\
**character range**:\
\
*   `c`: matches character `c` while `c != '\\', '-', ']'`
*   `'\\' c`: matches character `c`
*   `lo '-' hi`: matches character `c` for `lo <= c <= hi`

#### Examples:

    tf.io.gfile.glob("*.py")

    tf.io.gfile.glob("__init__.??")

    files = {"*.py"}

See the C++ function `GetMatchingPaths` in [`core/platform/file_system.h`](https://www.tensorflow.org/api_docs/python/core/platform/file_system.h)
 for implementation details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pattern` | string or iterable of strings. The glob pattern(s). |

|     |
| --- |
| Returns<br>------- |     |
| A list of strings containing filenames that match the given pattern(s). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | If there are filesystem / directory listing errors. |
| [`errors.NotFoundError`](https://www.tensorflow.org/api_docs/python/tf/errors/NotFoundError) | If pattern to be matched is an invalid directory. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.