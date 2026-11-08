[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.map\_shape\_structure Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_shape_structure#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L412-L424)

Variant of keras.tree.map\_structure that operates on shape tuples.

tf.keras.tree.map_shape_structure(
        func, structure
    )

Tuples containing ints and Nones are considered shapes and passed to `func`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `structure` | Arbitrarily nested structure. |

|     |
| --- |
| Returns<br>------- |     |
| The same structure with `func` applied. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.