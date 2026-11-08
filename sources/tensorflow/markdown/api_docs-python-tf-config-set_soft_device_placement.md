[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.set\_soft\_device\_placement Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L287-L313)

Enable or disable soft device placement.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.set_soft_device_placement`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)

tf.config.set_soft_device_placement(
        enabled
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu) |

If enabled, ops can be placed on different devices than the device explicitly assigned by the user. This potentially has a large performance cost due to an increase in data communication between devices.

Some cases where soft\_device\_placement would modify device assignment are:

1.  no GPU/TPU implementation for the OP
2.  no GPU devices are known or registered
3.  need to co-locate with reftype input(s) which are from CPU
4.  an OP can not be compiled by XLA. Common for TPU which always requires the XLA compiler.

For TPUs, if this option is true, a feature called automatic outside compilation is enabled. Automatic outside compilation will move uncompilable ops within a TPU program to instead run on the host. This can be used when encountering compilation failures due to unsupported ops.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enabled` | A boolean indicating whether to enable soft placement. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.