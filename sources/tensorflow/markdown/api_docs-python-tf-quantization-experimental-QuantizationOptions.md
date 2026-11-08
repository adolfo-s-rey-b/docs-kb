[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.experimental.QuantizationOptions Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/compiler/mlir/quantization/tensorflow/quantization_options.proto)

A ProtocolMessage

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.quantization.experimental.QuantizationOptions`](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `calibration_options` | `CalibrationOptions calibration_options` |
| `debugger_config` | `DebuggerConfig debugger_config` |
| `enable_legacy_weight_only` | `bool enable_legacy_weight_only` |
| `enable_per_channel_quantization` | `bool enable_per_channel_quantization` |
| `enable_two_input_tensors` | `bool enable_two_input_tensors` |
| `experimental_enable_tpu_model_support` | `bool experimental_enable_tpu_model_support` |
| `force_graph_mode_calibration` | `bool force_graph_mode_calibration` |
| `freeze_all_variables` | `bool freeze_all_variables` |
| `min_num_elements_for_weights` | `int64 min_num_elements_for_weights` |
| `op_set` | `OpSet op_set` |
| `quantization_method` | `QuantizationMethod quantization_method` |
| `representative_datasets` | `repeated RepresentativeDatasetsEntry representative_datasets` |
| `signature_keys` | `repeated string signature_keys` |
| `tags` | `repeated string tags` |
| `unit_wise_quantization_specs` | `repeated UnitWiseQuantizationSpec unit_wise_quantization_specs` |

Child Classes
-------------

[`class RepresentativeDatasetsEntry`](https://www.tensorflow.org/api_docs/python/tf/quantization/experimental/QuantizationOptions/RepresentativeDatasetsEntry)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.