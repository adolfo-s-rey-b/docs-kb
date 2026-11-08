[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.assert\_same\_structure Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/assert_same_structure#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L252-L305)

Asserts that two structures are nested in the same way.

tf.keras.tree.assert_same_structure(
        a, b, check_types=None
    )

This function verifies that the nested structures match. The leafs can be of any type. At each level, the structures must be of the same type and have the same number of elements. Instances of `dict`, `OrderedDict` and `defaultdict` are all considered the same as long as they have the same set of keys. However, `list`, `tuple`, `namedtuple` and `deque` are not the same structures. Two namedtuples with identical fields and even identical names are not the same structures.

#### Examples:

    keras.tree.assert_same_structure([(0, 1)], [(2, 3)])

Foo = collections.namedtuple('Foo', ['a', 'b'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | an arbitrarily nested structure. |
| `b` | an arbitrarily nested structure. |
| `check_types` | Deprecated. The behavior of this flag was inconsistent, it no longer has any effect. For a looser check, use `assert_same_paths` instead, which considers `list`, `tuple`, `namedtuple` and `deque` as matching structures. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the two structures `a` and `b` don't match. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.