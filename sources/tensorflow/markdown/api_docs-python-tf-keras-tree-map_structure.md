[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.map\_structure Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L175-L212)

Maps `func` through given structures.

tf.keras.tree.map_structure(
        func, *structures, none_is_leaf=True
    )

#### Examples:

    structure = [[1], [2], [3]]

    Foo = collections.namedtuple('Foo', ['a', 'b'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A callable that accepts as many arguments as there are structures. |
| `*structures` | Arbitrarily nested structures of the same layout. |
| `none_is_leaf` | If True, `func` will be called on `None` leaves. If False, `None` values are not passed to `func` and are returned in the output directly. |

|     |
| --- |
| Returns<br>------- |     |
| A new structure with the same layout as the given ones. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `structures` is empty or `func` is not callable. |
| `ValueError` | If there is more than one items in `structures` and some of the nested structures don't match according to the rules of `assert_same_structure`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.