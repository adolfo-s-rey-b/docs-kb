[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmlir%2Fexperimental%2Ftflite_to_tosa_bytecode&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.mlir.experimental.tflite\_to\_tosa\_bytecode Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compiler/mlir/mlir.py#L181-L206)

Converts TFLite flatbuffer to TOSA dialect in MLIR bytecode.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.mlir.experimental.tflite_to_tosa_bytecode`](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/tflite_to_tosa_bytecode)

tf.mlir.experimental.tflite_to_tosa_bytecode(
        flatbuffer,
        bytecode,
        use_external_constant=False,
        ordered_input_arrays=None,
        ordered_output_arrays=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `flatbuffer` | Path to flatbuffer. |
| `bytecode` | Path to output bytecode. |
| `use_external_constant` | Whether to create `tfl.external_const` instead of `tfl.const`. |
| `ordered_input_arrays` |     |
| `ordered_output_arrays` | If ordered\_output\_arrays is not empty, then the function will only return nodes in ordered\_output\_arrays in the same order |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.