[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.HardwareFeature.EmbeddingFeature Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_hardware_feature.py#L34-L48)

Embedding feature flag strings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.HardwareFeature.EmbeddingFeature`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature/EmbeddingFeature)

UNSUPPORTED: No embedding lookup accelerator available on the tpu. V1: Embedding lookup accelerator V1. The embedding lookup operation can only be placed at the beginning of computation. Only one instance of embedding lookup layer is allowed. V2: Embedding lookup accelerator V2. The embedding lookup operation can be placed anywhere of the computation. Multiple instances of embedding lookup layer is allowed.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| UNSUPPORTED | `<EmbeddingFeature.UNSUPPORTED: 'UNSUPPORTED'>` |
| V1  | `<EmbeddingFeature.V1: 'V1'>` |
| V2  | `<EmbeddingFeature.V2: 'V2'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.