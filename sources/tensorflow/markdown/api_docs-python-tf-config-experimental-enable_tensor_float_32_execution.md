[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.enable\_tensor\_float\_32\_execution Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L50-L105)

Enable or disable the use of TensorFloat-32 on supported hardware.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.enable_tensor_float_32_execution`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution)

tf.config.experimental.enable_tensor_float_32_execution(
        enabled
    )

[TensorFloat-32](https://blogs.nvidia.com/blog/2020/05/14/tensorfloat-32-precision-format)
, or TF32 for short, is a math mode for NVIDIA Ampere GPUs and above. TensorFloat-32 execution causes certain float32 ops, such as matrix multiplications and convolutions, to run much faster on such GPUs but with reduced precision. This reduced precision should not impact convergence of deep learning models in practice.

TensorFloat-32 is enabled by default. TensorFloat-32 is only supported on NVIDIA GPUs starting with the Ampere generation, so older NVIDIA GPUs will use the full float32 precision regardless of whether TensorFloat-32 is enabled or not. If you want to use the full float32 precision on all GPUs, you can disable TensorFloat-32 execution with this function. For example:

x = tf.fill((1024, 1024), 1.0001)
    y = tf.fill((1024, 1024), 1.)
    # TensorFloat-32 is enabled, so matmul is run with reduced precision
    print(tf.linalg.matmul(x, y)[0, 0])  # 1024.0
    tf.config.experimental.enable_tensor_float_32_execution(False)
    # Matmul is run with full precision
    print(tf.linalg.matmul(x, y)[0, 0])  # ~1024.1

To check whether TensorFloat-32 execution is currently enabled, use [`tf.config.experimental.tensor_float_32_execution_enabled`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/tensor_float_32_execution_enabled)
.

If TensorFloat-32 is enabled, float32 inputs of supported ops, such as [`tf.linalg.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
, will be rounded from 23 bits of precision to 10 bits of precision in most cases. This allows the ops to execute much faster by utilizing the GPU's tensor cores. TensorFloat-32 has the same dynamic range as float32, meaning it is no more likely to underflow or overflow than float32. Ops still use float32 accumulation when TensorFloat-32 is enabled. Enabling or disabling TensorFloat-32 only affects Ampere GPUs and above.

Note TensorFloat-32 is not always used in supported ops, as only inputs of certain shapes are supported. Support for more input shapes and more ops may be added in the future. As a result, precision of float32 ops may decrease in minor versions of TensorFlow.

TensorFloat-32 is also used for some complex64 ops. Currently, TensorFloat-32 is used in fewer cases for complex64 as it is for float32.

Similarly to GPUs, TPUs also run certain float32 ops, like matrix multiplications and convolutions, with lower precision by default. Unlike GPUs, TPUs use bfloat16 precision instead of TensorFloat-32 precision for such ops. Disabling TensorFloat-32 with this function also causes TPUs to run float32 ops with the full float32 precision but with lower performance.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enabled` | Bool indicating whether to enable TensorFloat-32 execution. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.