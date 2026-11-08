[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/make_tensor_proto#main-content)

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
    

tf.make\_tensor\_proto Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_util.py#L548-L752)

Create a TensorProto.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.make_tensor_proto`](https://www.tensorflow.org/api_docs/python/tf/make_tensor_proto)

tf.make_tensor_proto(
        values, dtype=None, shape=None, verify_shape=False, allow_broadcast=False
    )

In TensorFlow 2.0, representing tensors as protos should no longer be a common workflow. That said, this utility function is still useful for generating TF Serving request protos:

  request = tensorflow_serving.apis.predict_pb2.PredictRequest()
      request.model_spec.name = "my_model"
      request.model_spec.signature_name = "serving_default"
      request.inputs["images"].CopyFrom(tf.make_tensor_proto(X_new))

`make_tensor_proto` accepts "values" of a python scalar, a python list, a numpy ndarray, or a numpy scalar.

If "values" is a python scalar or a python list, make\_tensor\_proto first convert it to numpy ndarray. If dtype is None, the conversion tries its best to infer the right numpy data type. Otherwise, the resulting numpy array has a compatible data type with the given dtype.

In either case above, the numpy ndarray (either the caller provided or the auto-converted) must have the compatible type with dtype.

`make_tensor_proto` then converts the numpy array to a tensor proto.

If "shape" is None, the resulting tensor proto represents the numpy array precisely.

Otherwise, "shape" specifies the tensor's shape and the numpy array can not have more elements than what "shape" specifies.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | Values to put in the TensorProto. |
| `dtype` | Optional tensor\_pb2 DataType value. |
| `shape` | List of integers representing the dimensions of tensor. |
| `verify_shape` | Boolean that enables verification of a shape of values. |
| `allow_broadcast` | Boolean that enables allowing scalars and 1 length vector broadcasting. Cannot be true when verify\_shape is true. |

|     |
| --- |
| Returns<br>------- |     |
| A `TensorProto`. Depending on the type, it may contain data in the "tensor\_content" attribute, which is not directly useful to Python programs. To access the values you should convert the proto back to a numpy ndarray with [`tf.make_ndarray(proto)`](https://www.tensorflow.org/api_docs/python/tf/make_ndarray)<br>.<br><br>If `values` is a `TensorProto`, it is immediately returned; `dtype` and `shape` are ignored. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if unsupported types are provided. |
| `ValueError` | if arguments have inappropriate values or if verify\_shape is True and shape of values is not equals to a shape from the argument. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.