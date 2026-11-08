[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#methods)
    *   [from\_spec](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#from_spec)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#to_proto)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.Variable.SaveSliceInfo Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#methods)
    *   [from\_spec](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#from_spec)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo#to_proto)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1249-L1396)

Information on how to save this Variable as a slice.

#### View aliases

**Main aliases**

[`tf.experimental.dtensor.DVariable.SaveSliceInfo`](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.Variable.SaveSliceInfo`](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo)

tf.Variable.SaveSliceInfo(
        full_name=None,
        full_shape=None,
        var_offset=None,
        var_shape=None,
        save_slice_info_def=None,
        import_scope=None
    )

Provides internal support for saving variables as slices of a larger variable. This API is not public and is subject to change.

#### Available properties:

*   full\_name
*   full\_shape
*   var\_offset
*   var\_shape

|     |     |
| --- | --- |
| Args<br>---- |     |
| `full_name` | Name of the full variable of which this `Variable` is a slice. |
| `full_shape` | Shape of the full variable, as a list of int. |
| `var_offset` | Offset of this `Variable` into the full variable, as a list of int. |
| `var_shape` | Shape of this `Variable`, as a list of int. |
| `save_slice_info_def` | `SaveSliceInfoDef` protocol buffer. If not `None`, recreates the SaveSliceInfo object its contents. `save_slice_info_def` and other arguments are mutually exclusive. |
| `import_scope` | Optional `string`. Name scope to add. Only used when initializing from protocol buffer. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `spec` | Computes the spec string used for saving. |

Methods
-------

### `from_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1306-L1372)

@classmethod

Parses a SaveSliceInfo spec string and returns a SaveSliceInfo object.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The tensor slice spec string according to the SaveSliceInfo.spec property. The spec contains the space-separated shape of the full variable, followed by colon-separated pairs of the variable's offset and shape, where each pair is comma-separated. For example, consider a variable whose full shape is \[4 3 5\], offset is \[0 1 3\], and shape is \[4 1 2\]. This variable's SaveSliceInfo.spec would be "4 3 5 0,4:1,1:3,2". |

|     |
| --- |
| Returns |     |
| A SaveSliceInfo object containing the extracted information. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the input string is not in the expected format. |

### `to_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1374-L1396)

to_proto(
        export_scope=None
    )

Returns a SaveSliceInfoDef() proto.

|     |     |
| --- | --- |
| Args |     |
| `export_scope` | Optional `string`. Name scope to remove. |

|     |
| --- |
| Returns |     |
| A `SaveSliceInfoDef` protocol buffer, or None if the `Variable` is not in the specified name scope. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.