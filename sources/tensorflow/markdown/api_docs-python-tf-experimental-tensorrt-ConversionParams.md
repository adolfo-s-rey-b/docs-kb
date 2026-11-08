[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.tensorrt.ConversionParams Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/tensorrt/ConversionParams#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compiler/tensorrt/trt_convert.py#L135-L181)

Parameters that are used for TF-TRT conversion.

tf.experimental.tensorrt.ConversionParams(
        max_workspace_size_bytes=DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES,
        precision_mode=TrtPrecisionMode.FP32,
        minimum_segment_size=3,
        maximum_cached_engines=1,
        use_calibration=True,
        allow_build_at_runtime=True
    )

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `max_workspace_size_bytes` | the maximum GPU temporary memory that the TRT engine can use at execution time. This corresponds to the 'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize(). |
| `precision_mode` | one of the strings in TrtPrecisionMode.supported\_precision\_modes(). |
| `minimum_segment_size` | the minimum number of nodes required for a subgraph to be replaced by TRTEngineOp. |
| `maximum_cached_engines` | max number of cached TRT engines for dynamic TRT ops. Created TRT engines for a dynamic dimension are cached. If the number of cached engines is already at max but none of them supports the input shapes, the TRTEngineOp will fall back to run the original TF subgraph that corresponds to the TRTEngineOp. |
| `use_calibration` | this argument is ignored if precision\_mode is not INT8. If set to True, a calibration graph will be created to calibrate the missing ranges. The calibration graph must be converted to an inference graph by running calibration with calibrate(). If set to False, quantization nodes will be expected for every tensor in the graph (excluding those which will be fused). If a range is missing, an error will occur. Please note that accuracy may be negatively affected if there is a mismatch between which tensors TRT quantizes and which tensors were trained with fake quantization. |
| `allow_build_at_runtime` | whether to allow building TensorRT engines during runtime if no prebuilt TensorRT engine can be found that can handle the given inputs during runtime, then a new TensorRT engine is built at runtime if allow\_build\_at\_runtime=True, and otherwise native TF is used. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `max_workspace_size_bytes` | A `namedtuple` alias for field number 0 |
| `precision_mode` | A `namedtuple` alias for field number 1 |
| `minimum_segment_size` | A `namedtuple` alias for field number 2 |
| `maximum_cached_engines` | A `namedtuple` alias for field number 3 |
| `use_calibration` | A `namedtuple` alias for field number 4 |
| `allow_build_at_runtime` | A `namedtuple` alias for field number 5 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.