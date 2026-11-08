[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fgraph_util%2Fimport_graph_def&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.graph\_util.import\_graph\_def Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/importer.py#L358-L416)

Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

#### View aliases

**Main aliases**

[`tf.import_graph_def`](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.graph_util.import_graph_def`](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def)
, [`tf.compat.v1.import_graph_def`](https://www.tensorflow.org/api_docs/python/tf/graph_util/import_graph_def)

tf.graph_util.import_graph_def(
        graph_def,
        input_map=None,
        return_elements=None,
        name=None,
        op_dict=None,
        producer_op_list=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite) |

This function provides a way to import a serialized TensorFlow [`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto)
 protocol buffer, and extract individual objects in the `GraphDef` as [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 and [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)
 objects. Once extracted, these objects are placed into the current default `Graph`. See [`tf.Graph.as_graph_def`](https://www.tensorflow.org/api_docs/python/tf/Graph#as_graph_def)
 for a way to create a `GraphDef` proto.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph_def` | A `GraphDef` proto containing operations to be imported into the default graph. |
| `input_map` | A dictionary mapping input names (as strings) in `graph_def` to `Tensor` objects. The values of the named input tensors in the imported graph will be re-mapped to the respective `Tensor` values. |
| `return_elements` | A list of strings containing operation names in `graph_def` that will be returned as `Operation` objects; and/or tensor names in `graph_def` that will be returned as `Tensor` objects. |
| `name` | (Optional.) A prefix that will be prepended to the names in `graph_def`. Note that this does not apply to imported function names. Defaults to `"import"`. |
| `op_dict` | (Optional.) Deprecated, do not use. |
| `producer_op_list` | (Optional.) An `OpList` proto with the (possibly stripped) list of `OpDef`s used by the producer of the graph. If provided, unrecognized attrs for ops in `graph_def` that have their default value according to `producer_op_list` will be removed. This will allow some more `GraphDef`s produced by later binaries to be accepted by earlier binaries. |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Operation` and/or `Tensor` objects from the imported graph, corresponding to the names in `return_elements`, and None if `returns_elements` is None. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `graph_def` is not a `GraphDef` proto, `input_map` is not a dictionary mapping strings to `Tensor` objects, or `return_elements` is not a list of strings. |
| `ValueError` | If `input_map`, or `return_elements` contains names that do not appear in `graph_def`, or `graph_def` is not well-formed (e.g. it refers to an unknown tensor). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.