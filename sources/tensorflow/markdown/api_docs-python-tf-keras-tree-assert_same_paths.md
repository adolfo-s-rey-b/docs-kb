[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.assert\_same\_paths Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_paths#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L308-L334)

Asserts that two structures have identical paths in their tree structure.

tf.keras.tree.assert_same_paths(
        a, b
    )

This function verifies that two nested structures have the same paths. Unlike `assert_same_structure`, this function only checks the paths and ignores the collection types. For Sequences, to path is the index: 0, 1, 2, etc. For Mappings, the path is the key, for instance "a", "b", "c". Note that namedtuples also use indices and not field names for the path.

#### Examples:

    keras.tree.assert_same_paths([0, 1], (2, 3))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | an arbitrarily nested structure. |
| `b` | an arbitrarily nested structure. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the paths in structure `a` don't match the paths in structure `b`. The error message will include the specific paths that differ. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.