[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nest.map\_structure Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/nest.py#L542-L630)

Creates a new structure by applying `func` to each atom in `structure`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nest.map_structure`](https://www.tensorflow.org/api_docs/python/tf/nest/map_structure)

tf.nest.map_structure(
        func, *structure, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2)<br>    <br>*   [Variational Inference on Probabilistic Graphical Models with Joint Distributions](https://www.tensorflow.org/probability/examples/Variational_Inference_and_Joint_Distributions)<br>    <br>*   [Composing Learning Algorithms](https://www.tensorflow.org/federated/tutorials/composing_learning_algorithms)<br>    <br>*   [Implementing Custom Aggregations](https://www.tensorflow.org/federated/tutorials/custom_aggregators) |

Refer to [tf.nest](https://www.tensorflow.org/api_docs/python/tf/nest)
 for the definition of a structure.

Applies `func(x[0], x[1], ...)` where x\[i\] enumerates all atoms in `structure[i]`. All items in `structure` must have the same arity, and the return value will contain results with the same structure layout.

#### Examples:

*   A single Python dict:

    a = {"hello": 24, "world": 76}

*   Multiple Python dictionaries:

    d1 = {"hello": 24, "world": 76}

*   A single Python list:

    a = [24, 76, "ab"]

*   Scalars:

    tf.nest.map_structure(lambda x, y: x + y, 3, 4)

*   Empty structures:

    tf.nest.map_structure(lambda x: x + 1, ())

*   Check the types of iterables:

    s1 = (((1, 2), 3), 4, (5, 6))

*   Type check is set to False:

    s1 = (((1, 2), 3), 4, (5, 6))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A callable that accepts as many arguments as there are structures. |
| `*structure` | atom or nested structure. |
| `**kwargs` | Valid keyword args are:<br><br>*   `check_types`: If set to `True` (default) the types of iterables within the structures have to be same (e.g. `map_structure(func, [1], (1,))` raises a `TypeError` exception). To allow this set this argument to `False`. Note that namedtuples with identical name and fields are always considered to have the same shallow structure.<br>*   `expand_composites`: If set to `True`, then composite tensors such as [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>     and [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>     are expanded into their component tensors. If `False` (the default), then composite tensors are not expanded. |

|     |
| --- |
| Returns<br>------- |     |
| A new structure with the same arity as `structure[0]`, whose atoms correspond to `func(x[0], x[1], ...)` where `x[i]` is the atom in the corresponding location in `structure[i]`. If there are different structure types and `check_types` is `False` the structure types of the first structure will be used. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `func` is not callable or if the structures do not match each other by depth tree. |
| `ValueError` | If no structure is provided or if the structures do not match each other by type. |
| `ValueError` | If wrong keyword arguments are provided. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.