[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nest.assert\_same\_structure Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/nest.py#L298-L387)

Asserts that two structures are nested in the same way.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nest.assert_same_structure`](https://www.tensorflow.org/api_docs/python/tf/nest/assert_same_structure)

tf.nest.assert_same_structure(
        nest1, nest2, check_types=True, expand_composites=False
    )

Refer to [tf.nest](https://www.tensorflow.org/api_docs/python/tf/nest)
 for the definition of a structure.

Note the method does not check the types of atoms inside the structures.

#### Examples:

*   These atom vs. atom comparisons will pass:
    
    tf.nest.assert_same_structure(1.5, tf.Variable(1, tf.uint32))
      
*   These nested structure vs. nested structure comparisons will pass:
    
    structure1 = (((1, 2), 3), 4, (5, 6))
      
    
    import collections
      
    
    tf.nest.assert_same_structure(
      
    
    tf.nest.assert_same_structure(
      
    
    ragged_tensor1 = tf.RaggedTensor.from_row_splits(
      
*   These examples will raise exceptions:
    
    tf.nest.assert_same_structure([0, 1], np.array([0, 1]))
      
    
    tf.nest.assert_same_structure(
      

|     |     |
| --- | --- |
| Args<br>---- |     |
| `nest1` | an atom or a nested structure. |
| `nest2` | an atom or a nested structure. |
| `check_types` | if `True` (default) types of structures are checked as well, including the keys of dictionaries. If set to `False`, for example a list and a tuple of objects will look the same if they have the same size. Note that namedtuples with identical name and fields are always considered to have the same shallow structure. Two types will also be considered the same if they are both list subtypes (which allows "list" and "\_ListWrapper" from trackable dependency tracking to compare equal). `check_types=True` only checks type of sub-structures. The types of atoms are not checked. |
| `expand_composites` | If true, then composite tensors such as [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> and [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> are expanded into their component tensors. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the two structures do not have the same number of atoms or if the two structures are not nested in the same way. |
| `TypeError` | If the two structures differ in the type of sequence in any of their substructures. Only possible if `check_types` is `True`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.