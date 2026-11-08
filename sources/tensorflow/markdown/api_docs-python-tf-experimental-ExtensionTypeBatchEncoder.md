[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#methods)
    *   [batch](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#batch)
        
    *   [decode](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#decode)
        
    *   [encode](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#encode)
        
    *   [encoding\_specs](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#encoding_specs)
        
    *   [unbatch](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#unbatch)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.ExtensionTypeBatchEncoder Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#methods)
    *   [batch](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#batch)
        
    *   [decode](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#decode)
        
    *   [encode](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#encode)
        
    *   [encoding\_specs](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#encoding_specs)
        
    *   [unbatch](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder#unbatch)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L651-L801)

Class used to encode and decode extension type values for batching.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.ExtensionTypeBatchEncoder`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)

In order to be batched and unbatched by APIs such as [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
, and [`tf.map_fn`](https://www.tensorflow.org/api_docs/python/tf/map_fn)
, extension type values must be encoded as a list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s, where stacking, unstacking, or concatenating these encoded tensors and then decoding the result must be equivalent to stacking, unstacking, or concatenating the original values. `ExtensionTypeBatchEncoder`s are responsible for implementing this encoding.

The default `ExtensionTypeBatchEncoder` that is used by `BatchableExtensionType` assumes that extension type values can be stacked, unstacked, or concatenated by simply stacking, unstacking, or concatenating every nested `Tensor`, `ExtensionType`, `CompositeTensor`, and `TensorShape` field.

Extension types where this is not the case will need to override `__batch_encoder__` with a custom encoder that overrides the `batch`, `unbatch`, `encode`, and `decode` methods. E.g.:

    class CustomBatchEncoder(ExtensionTypeBatchEncoder):

    class CustomType(BatchableExtensionType):

For example, [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 and [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
 both use custom batch encodings which define ops to "box" and "unbox" individual values into [`tf.variant`](https://www.tensorflow.org/api_docs/python/tf#variant)
 tensors.

Methods
-------

### `batch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L686-L713)

batch(
        spec, batch_size
    )

Returns the TypeSpec representing a batch of values described by `spec`.

The default definition returns a `TypeSpec` that is equal to `spec`, except that an outer axis with size `batch_size` is added to every nested `TypeSpec` and `TensorShape` field. Subclasses may override this default definition, when necessary.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The `TypeSpec` for an individual value. |
| `batch_size` | An `int` indicating the number of values that are batched together, or `None` if the batch size is not known. |

|     |
| --- |
| Returns |     |
| A `TypeSpec` for a batch of values. |     |

### `decode`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L767-L785)

decode(
        spec, encoded_value
    )

Decodes `value` from a batchable tensor encoding.

See `encode` for a description of the default encoding. Subclasses may override this default definition, when necessary.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The TypeSpec for the result value. If encoded values with spec `s` were batched, then `spec` should be `s.batch(batch_size)`; or if encoded values with spec `s` were unbatched, then `spec` should be `s.unbatch()`. |
| `encoded_value` | A nest of values returned by `encode`; or a nest of values that was formed by stacking, unstacking, or concatenating the corresponding elements of values returned by `encode`. |

|     |
| --- |
| Returns |     |
| A value compatible with `type_spec`. |     |

### `encode`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L742-L765)

encode(
        spec, value, minimum_rank=0
    )

Encodes `value` as a nest of batchable Tensors or CompositeTensors.

The default definition returns a flat tuple of all the `Tensor`s, `CompositeTensor`s, and `ExtensionType`s from a depth-first traversal of `value`'s fields. Subclasses may override this default definition, when necessary.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The TypeSpec of the value to encode. |
| `value` | A value compatible with `spec`. |
| `minimum_rank` | The minimum rank for the returned Tensors, CompositeTensors, and ExtensionType values. This can be used to ensure that the encoded values can be unbatched this number of times. If `minimum_rank>0`, then `t.shape[:minimum_rank]` must be compatible for all values `t` returned by `encode`. |

|     |
| --- |
| Returns |     |
| A nest (as defined by [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br>) of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, batchable `tf.CompositeTensor`s, or `tf.ExtensionType`s. Stacking, unstacking, or concatenating these encoded values and then decoding the result must be equivalent to stacking, unstacking, or concatenating the original values. |     |

### `encoding_specs`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L787-L801)

encoding_specs(
        spec
    )

Returns a list of `TensorSpec`(s) describing the encoding for `spec`.

See `encode` for a description of the default encoding. Subclasses may override this default definition, when necessary.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The TypeSpec whose encoding should be described. |

|     |
| --- |
| Returns |     |
| A nest (as defined by `tf.nest) of`tf.TypeSpec`, describing the values that are returned by`self.encode(spec, ...)\`. All TypeSpecs in this nest must be batchable. |     |

### `unbatch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L715-L740)

unbatch(
        spec
    )

Returns the TypeSpec for a single unbatched element in `spec`.

The default definition returns a `TypeSpec` that is equal to `spec`, except that the outermost axis is removed from every nested `TypeSpec`, and `TensorShape` field. Subclasses may override this default definition, when necessary.

|     |     |
| --- | --- |
| Args |     |
| `spec` | The `TypeSpec` for a batch of values. |

|     |
| --- |
| Returns |     |
| A `TypeSpec` for an individual value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.