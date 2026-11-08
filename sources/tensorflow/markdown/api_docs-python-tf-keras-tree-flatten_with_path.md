[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.flatten\_with\_path Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/flatten_with_path#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L149-L172)

Flattens a possibly nested structure into a list.

tf.keras.tree.flatten_with_path(
        structure
    )

This is a variant of flattens() which produces a list of pairs: `(path, item)`. A path is a tuple of indices and/or keys which uniquely identifies the position of the corresponding item.

Dictionaries with non-sortable keys are not supported.

#### Examples:

    keras.flatten_with_path([{"foo": 42}])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `structure` | An arbitrarily nested structure. |

|     |
| --- |
| Returns<br>------- |     |
| A list of `(path, item)` pairs corresponding to the flattened version of the input `structure`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.