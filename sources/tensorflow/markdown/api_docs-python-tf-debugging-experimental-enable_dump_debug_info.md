[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fexperimental%2Fenable_dump_debug_info&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.experimental.enable\_dump\_debug\_info Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/debug/lib/dumping_callback.py#L672-L860)

Enable dumping debugging information from a TensorFlow program.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.experimental.enable_dump_debug_info`](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental/enable_dump_debug_info)

tf.debugging.experimental.enable_dump_debug_info(
        dump_root,
        tensor_debug_mode=DEFAULT_TENSOR_DEBUG_MODE,
        circular_buffer_size=1000,
        op_regex=None,
        tensor_dtypes=None
    )

The debugging information is dumped to a directory on the file system specified as `dump_root`.

The dumped debugging information can be ingested by debugger UIs.

The files in the dump directory contain the following information:

*   TensorFlow Function construction (e.g., compilation of Python functions decorated with @tf.function), the op types, names (if available), context, the input and output tensors, and the associated stack traces.
*   Execution of TensorFlow operations (ops) and Functions and their stack traces, op types, names (if available) and contexts. In addition, depending on the value of the `tensor_debug_mode` argument (see Args section below), the value(s) of the output tensors or more concise summaries of the tensor values will be dumped.
*   A snapshot of Python source files involved in the execution of the TensorFlow program.

Once enabled, the dumping can be disabled with the corresponding `disable_dump_debug_info()` method under the same Python namespace. Calling this method more than once with the same `dump_root` is idempotent. Calling this method more than once with different `tensor_debug_mode`s leads to a `ValueError`. Calling this method more than once with different `circular_buffer_size`s leads to a `ValueError`. Calling this method with a different `dump_root` abolishes the previously-enabled `dump_root`.

#### Usage example:

tf.debugging.experimental.enable_dump_debug_info('/tmp/my-tfdbg-dumps')
    
    # Code to build, train and run your TensorFlow model...

tf.config.set_soft_device_placement(True)
    tf.debugging.experimental.enable_dump_debug_info(
        logdir, tensor_debug_mode="FULL_HEALTH")
    
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    strategy = tf.distribute.TPUStrategy(resolver)
    with strategy.scope():
      # ...

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dump_root` | The directory path where the dumping information will be written. |
| `tensor_debug_mode` | Debug mode for tensor values, as a string. The currently supported options are:<br><br>*   "NO\_TENSOR": (Default) Only traces the output tensors of all executed ops (including those executed eagerly at the Python level or as a part of a TensorFlow graph) and functions, while not extracting any information from the values of the tensors.<br>*   "CURT\_HEALTH": For each floating-dtype tensor (e.g., tensors of dtypes such as `float32`, `float64` and `bfloat16`), extracts a binary bit indicating whether it contains any -infinity, +infinity or NaN.<br>*   "CONCISE\_HEALTH": For each floating-dtype tensor, extract total element count, and counts of -infinity, +infinity and NaN elements.<br>*   "FULL\_HEALTH": For each floating-dtype tensor, extracts the dtype, rank (number of dimensions), total element count, and counts of -infinity, +infinity and NaN elements.<br>*   "SHAPE": For each tensor (regardless of dtype), extracts its dtype, rank, total element count and shape. |
| `circular_buffer_size` | Size of the circular buffers for execution events. These circular buffers are designed to reduce the overhead of debugging dumping. They hold the most recent debug events concerning eager execution of ops and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s and traces of tensor values computed inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s. They are written to the file system only when the proper flushing method is called (see description of return values below). Expected to be an integer. If <= 0, the circular-buffer behavior will be disabled, i.e., the execution debug events will be written to the file writers in the same way as non-execution events such as op creations and source-file snapshots. |
| `op_regex` | Dump data from only the tensors from op types that matches to the regular expression (through Python's `re.match()`). "Op type" refers to the names of the TensorFlow operations (e.g., "MatMul", "LogSoftmax"), which may repeat in a TensorFlow function. It does _not_ refer to the names of nodes (e.g., "dense/MatMul", "dense\_1/MatMul\_1") which are unique within a function.*   Example 1: Dump tensor data from only MatMul and Relu ops `op_regex="^(MatMul\|Relu)$"`.<br>*   Example 2: Dump tensors from all ops _except_ Relu: `op_regex="(?!^Relu$)"`. This filter operates in a logical AND relation with `tensor_dtypes`. |
| `tensor_dtypes` | Dump data from only the tensors of which the specified dtypes. This optional argument can be in any of the following format:*   a list or tuple of `DType` objects or strings that can be converted to `DType` objects via [`tf.as_dtype()`](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)<br>    . Examples:<br>    *   `tensor_dtype=[tf.float32, tf.float64]`,<br>    *   `tensor_dtype=["float32", "float64"]`,<br>    *   `tensor_dtypes=(tf.int32, tf.bool)`,<br>    *   `tensor_dtypes=("int32", "bool")`<br>*   a callable that takes a single `DType` argument and returns a Python `boolean` indicating whether the dtype is to be included in the data dumping. Examples:<br>    *   `tensor_dtype=lambda dtype: dtype.is_integer`. This filter operates in a logical AND relation with `op_regex`. |

|     |
| --- |
| Returns<br>------- |     |
| A DebugEventsWriter instance used by the dumping callback. The caller may use its flushing methods, including `FlushNonExecutionFiles()` and `FlushExecutionFiles()`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.