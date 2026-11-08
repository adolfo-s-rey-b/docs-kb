[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.export\_meta\_graph Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/export_meta_graph#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1644-L1727)

Returns `MetaGraphDef` proto.

tf.compat.v1.train.export_meta_graph(
        filename=None,
        meta_info_def=None,
        graph_def=None,
        saver_def=None,
        collection_list=None,
        as_text=False,
        graph=None,
        export_scope=None,
        clear_devices=False,
        clear_extraneous_savers=False,
        strip_default_attrs=False,
        save_debug_info=False,
        **kwargs
    )

Optionally writes it to filename.

This function exports the graph, saver, and collection objects into `MetaGraphDef` protocol buffer with the intention of it being imported at a later time or location to restart training, run inference, or be a subgraph.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filename` | Optional filename including the path for writing the generated `MetaGraphDef` protocol buffer. |
| `meta_info_def` | `MetaInfoDef` protocol buffer. |
| `graph_def` | `GraphDef` protocol buffer. |
| `saver_def` | `SaverDef` protocol buffer. |
| `collection_list` | List of string keys to collect. |
| `as_text` | If `True`, writes the `MetaGraphDef` as an ASCII proto. |
| `graph` | The `Graph` to export. If `None`, use the default graph. |
| `export_scope` | Optional `string`. Name scope under which to extract the subgraph. The scope name will be striped from the node definitions for easy import later into new name scopes. If `None`, the whole graph is exported. graph\_def and export\_scope cannot both be specified. |
| `clear_devices` | Whether or not to clear the device field for an `Operation` or `Tensor` during export. |
| `clear_extraneous_savers` | Remove any Saver-related information from the graph (both Save/Restore ops and SaverDefs) that are not associated with the provided SaverDef. |
| `strip_default_attrs` | Boolean. If `True`, default-valued attributes will be removed from the NodeDefs. For a detailed guide, see [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)<br>. |
| `save_debug_info` | If `True`, save the GraphDebugInfo to a separate file, which in the same directory of filename and with `_debug` added before the file extend. |
| `**kwargs` | Optional keyed arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A `MetaGraphDef` proto. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When the `GraphDef` is larger than 2GB. |
| `RuntimeError` | If called with eager execution enabled. |

eager compatibility
-------------------

Exporting/importing meta graphs is not supported unless both `graph_def` and `graph` are provided. No graph exists when eager execution is enabled.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.