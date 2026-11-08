[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.tree.pack\_sequence\_as Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/tree/pack_sequence_as#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L337-L396)

Returns a given flattened sequence packed into a given structure.

tf.keras.tree.pack_sequence_as(
        structure, flat_sequence
    )

If `structure` is an atom, `flat_sequence` must be a single-item list; in this case the return value is `flat_sequence[0]`.

If `structure` is or contains a dict instance, the keys will be sorted to pack the flat sequence in deterministic order. However, instances of `collections.OrderedDict` are handled differently: their sequence order is used instead of the sorted keys. The same convention is followed in `flatten`. This correctly repacks dicts and `OrderedDicts` after they have been flattened, or vice-versa.

Dictionaries with non-sortable keys are not supported.

#### Examples:

    structure = {"key3": "", "key1": "", "key2": ""}

    structure = (("a", "b"), ("c", "d", "e"), "f")

    structure = {"key3": {"c": ("alpha", "beta"), "a": ("gamma")},

    structure = ["a"]

    structure = ["a"]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `structure` | Arbitrarily nested structure. |
| `flat_sequence` | Flat sequence to pack. |

|     |
| --- |
| Returns<br>------- |     |
| `flat_sequence` converted to have the same recursive structure as `structure`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `flat_sequence` is not iterable. |
| `ValueError` | If `flat_sequence` cannot be repacked as `structure`; for instance, if `flat_sequence` has too few or too many elements. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.