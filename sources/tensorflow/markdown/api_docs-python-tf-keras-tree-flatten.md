[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Ftree%2Fflatten&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.flatten Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L108-L146)

Flattens a possibly nested structure into a list.

tf.keras.tree.flatten(
        structure
    )

In the case of dict instances, the sequence consists of the values, sorted by key to ensure deterministic behavior. However, instances of `collections.OrderedDict` are handled differently: their sequence order is used instead of the sorted keys. The same convention is followed in `pack_sequence_as`. This correctly unflattens dicts and `OrderedDict` after they have been flattened, or vice-versa.

Dictionaries with non-sortable keys are not supported.

#### Examples:

    keras.tree.flatten([[1, 2, 3], [4, [5], [[6]]]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `structure` | An arbitrarily nested structure. |

|     |
| --- |
| Returns<br>------- |     |
| A list, the flattened version of the input `structure`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.