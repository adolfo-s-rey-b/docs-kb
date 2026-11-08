[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nest/flatten#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nest.flatten Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/nest.py#L198-L295)

Returns a flat list from a given structure.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nest.flatten`](https://www.tensorflow.org/api_docs/python/tf/nest/flatten)

tf.nest.flatten(
        structure, expand_composites=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns) | *   [Custom Federated Algorithms, Part 2: Implementing Federated Averaging](https://www.tensorflow.org/federated/tutorials/custom_federated_algorithms_2)<br>    <br>*   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution)<br>    <br>*   [Variational Inference on Probabilistic Graphical Models with Joint Distributions](https://www.tensorflow.org/probability/examples/Variational_Inference_and_Joint_Distributions)<br>    <br>*   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer)<br>    <br>*   [Networks](https://www.tensorflow.org/agents/tutorials/8_networks_tutorial) |

Refer to [tf.nest](https://www.tensorflow.org/api_docs/python/tf/nest)
 for the definition of a structure.

If the structure is an atom, then returns a single-item list: \[structure\].

This is the inverse of the [`nest.pack_sequence_as`](https://www.tensorflow.org/api_docs/python/tf/nest/pack_sequence_as)
 method that takes in a flattened list and re-packs it into the nested structure.

In the case of dict instances, the sequence consists of the values, sorted by key to ensure deterministic behavior. This is true also for OrderedDict instances: their sequence order is ignored, the sorting order of keys is used instead. The same convention is followed in [`nest.pack_sequence_as`](https://www.tensorflow.org/api_docs/python/tf/nest/pack_sequence_as)
. This correctly repacks dicts and OrderedDicts after they have been flattened, and also allows flattening an OrderedDict and then repacking it back using a corresponding plain dict, or vice-versa. Dictionaries with non-sortable keys cannot be flattened.

Users must not modify any collections used in nest while this function is running.

#### Examples:

1.  Python dict (ordered by key):
    
    dict = { "key3": "value3", "key1": "value1", "key2": "value2" }
      
2.  For a nested python tuple:
    
    tuple = ((1.0, 2.0), (3.0, 4.0, 5.0), 6.0)
      
3.  For a nested dictionary of dictionaries:
    
    dict = { "key3": {"c": (1.0, 2.0), "a": (3.0)},
      
4.  Numpy array (will not flatten):
    
    array = np.array([[1, 2], [3, 4]])
      
5.  [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     (will not flatten):
    
    tensor = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
      
6.  [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
    : This is a composite tensor thats representation consists of a flattened list of 'values' and a list of 'row\_splits' which indicate how to chop up the flattened list into different rows. For more details on [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
    , please visit https://www.tensorflow.org/api\_docs/python/tf/RaggedTensor.
    

with `expand_composites=False`, we just return the RaggedTensor as is.

  `tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2]])`
  `tf.nest.flatten(tensor, expand_composites=False)`
  `  [<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2]]>]`
    
  

with `expand_composites=True`, we return the component Tensors that make up the RaggedTensor representation (the values and row\_splits tensors)

  `tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2]])`
  `tf.nest.flatten(tensor, expand_composites=True)`
  `  [<tf.Tensor: shape=(7,), dtype=int32, numpy=array([3, 1, 4, 1, 5, 9, 2],`\
  `                                                    dtype=int32)>,`\
  `   <tf.Tensor: shape=(4,), dtype=int64, numpy=array([0, 4, 4, 7])>]`
    
  

|     |     |
| --- | --- |
| Args<br>---- |     |
| `structure` | an atom or a nested structure. Note, numpy arrays are considered atoms and are not flattened. |
| `expand_composites` | If true, then composite tensors such as [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> and [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> are expanded into their component tensors. |

|     |
| --- |
| Returns<br>------- |     |
| A Python list, the flattened version of the input. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | The nest is or contains a dict with non-sortable keys. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.