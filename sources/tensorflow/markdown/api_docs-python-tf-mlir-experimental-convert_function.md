[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.mlir.experimental.convert\_function Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compiler/mlir/mlir.py#L48-L92)

Import a ConcreteFunction and convert it to a textual MLIR module.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.mlir.experimental.convert_function`](https://www.tensorflow.org/api_docs/python/tf/mlir/experimental/convert_function)

tf.mlir.experimental.convert_function(
        concrete_function,
        pass_pipeline='tf-standard-pipeline',
        show_debug_info=False
    )

This API is only intended for inspecting the internals of TensorFlow and the string returned is at the moment intended for debugging purposes.

A [tf.function](https://www.tensorflow.org/api_docs/python/tf/function)
 can be imported and converted from TensorFlow to TensorFlow MLIR with this API by extracting its ConcreteFunction (eagerly-executing wrapper around a [tf.Graph](https://www.tensorflow.org/api_docs/python/tf/Graph)
).

#### For example:

    @tf.function

    concrete_function = add.get_concrete_function(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `concrete_function` | An object of type ConcreteFunction. |
| `pass_pipeline` | A textual description of an MLIR Pass Pipeline to run on the module, see MLIR documentation for the [textual pass pipeline syntax](https://mlir.llvm.org/docs/PassManagement/#textual-pass-pipeline-specification)<br>. |
| `show_debug_info` | Whether to include locations in the emitted textual form. |

|     |
| --- |
| Returns<br>------- |     |
| A textual representation of the MLIR module corresponding to the ConcreteFunction. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if concrete\_function is invalid or cannot be converted to MLIR. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.