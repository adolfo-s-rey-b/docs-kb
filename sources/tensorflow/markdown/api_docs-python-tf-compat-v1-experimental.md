[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#functions_2)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#other-members_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.experimental Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#functions_2)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental?version=stable#other-members_1)
    

See Stable See Nightly

Public API for tf.\_api.v2.experimental namespace

Modules
-------

[`extension_type`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/extension_type)
 module: Public API for tf.\_api.v2.experimental.extension\_type namespace

Classes
-------

[`class BatchableExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType)
: An ExtensionType that can be batched and unbatched.

[`class DynamicRaggedShape`](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape)
: The shape of a ragged or dense tensor.

[`class ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)
: Base class for TensorFlow `ExtensionType` classes.

[`class ExtensionTypeBatchEncoder`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)
: Class used to encode and decode extension type values for batching.

[`class ExtensionTypeSpec`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeSpec)
: Base class for tf.ExtensionType TypeSpec.

[`class Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
: Represents a value that may or may not be present.

[`class RowPartition`](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition)
: Partitioning of a sequence of values into contiguous subsequences ("rows").

[`class StructuredTensor`](https://www.tensorflow.org/api_docs/python/tf/experimental/StructuredTensor)
: A multidimensional collection of structures with the same schema.

Functions
---------

[`async_clear_error(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/async_clear_error)
: Clear pending operations and error statuses in async execution.

[`async_scope(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope)
: Context manager for grouping async operations.

[`dispatch_for_api(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api)
: Decorator that overrides the default implementation for a TensorFlow API.

[`dispatch_for_binary_elementwise_apis(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis)
: Decorator to override default implementation for binary elementwise APIs.

[`dispatch_for_binary_elementwise_assert_apis(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis)
: Decorator to override default implementation for binary elementwise assert APIs.

[`dispatch_for_unary_elementwise_apis(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis)
: Decorator to override default implementation for unary elementwise APIs.

[`enable_strict_mode(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/enable_strict_mode)
: If called, enables strict mode for all behaviors.

[`function_executor_type(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type)
: Context manager for setting the executor of eager defined functions.

[`output_all_intermediates(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates)
: Whether to output all intermediates from functional control flow ops.

[`register_filesystem_plugin(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin)
: Loads a TensorFlow FileSystem plugin.

[`unregister_dispatch_for(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/unregister_dispatch_for)
: Unregisters a function that was registered with `@dispatch_for_*`.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| float4\_e2m1fn | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>4-bit float with 2 exponent bits and 1 mantissa bits, with extended finite range. This type has no representation for both inf and NaN. |
| float8\_e4m3b11fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range and 11 bits of bias. This type has no representation for inf, and only one NaN value: 0x80. |
| float8\_e4m3fn | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range. This type has no representation for inf, and only two NaN values: 0xFF for negative NaN, and 0x7F for positive NaN. |
| float8\_e4m3fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range. This type has no representation for inf, and only one NaN value: 0x80. |
| float8\_e5m2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 5 exponent bits and 2 mantissa bits. |
| float8\_e5m2fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 5 exponent bits and 2 mantissa bits, with extended finite range. This type has no representation for inf, and only one NaN value: 0x80. |
| int2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 2-bit integer. |
| int4 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 4-bit integer. |
| uint2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 2-bit integer. |
| uint4 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 4-bit integer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.