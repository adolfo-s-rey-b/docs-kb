[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Ftree%2Fmap_structure_up_to&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.map\_structure\_up\_to Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/map_structure_up_to#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L215-L249)

Maps `func` through given structures up to `shallow_structure`.

tf.keras.tree.map_structure_up_to(
        shallow_structure, func, *structures
    )

This is a variant of `map_structure` which only maps the given structures up to `shallow_structure`. All further nested components are retained as-is.

#### Examples:

    shallow_structure = [None, None]

    shallow_structure = [None, [None, None]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shallow_structure` | A structure with layout common to all `structures`. |
| `func` | A callable that accepts as many arguments as there are structures. |
| `*structures` | Arbitrarily nested structures of the same layout. |

|     |
| --- |
| Returns<br>------- |     |
| A new structure with the same layout as `shallow_structure`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `structures` is empty or `func` is not callable. |
| `ValueError` | If one of the items in `structures` doesn't match the nested structure of `shallow_structure` according to the rules of `assert_same_structure`. Items in `structures` are allowed to be nested deeper than `shallow_structure`, but they cannot be shallower. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.