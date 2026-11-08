[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions#main-content)

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
    

tf.tpu.XLAOptions Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L230-L267)

XLA compilation options.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.XLAOptions`](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions)

tf.tpu.XLAOptions(
        use_spmd_for_xla_partitioning=True,
        enable_xla_dynamic_padder=True,
        use_shardy_partitioner=False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `use_spmd_for_xla_partitioning` | Boolean. Whether to use XLA's SPMD partitioner instead of MPMD partitioner when compiler partitioning is requested. |
| `enable_xla_dynamic_padder` | Boolean. Whether to enable XLA dynamic padder infrastructure to handle dynamic shapes inputs inside XLA. True by default. Disabling this may cause correctness issues with dynamic shapes inputs, as XLA will just assume the inputs are with padded shapes. However users can optionally set it to False to improve device time if masking is already handled in the user side. |
| `use_shardy_partitioner` | Boolean. Whether to use Shardy partitioner. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.