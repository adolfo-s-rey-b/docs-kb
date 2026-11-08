[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Foptimizer%2Fset_jit&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.optimizer.set\_jit Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L176-L199)

Configure JIT compilation. (deprecated argument values)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.optimizer.set_jit`](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_jit)

tf.config.optimizer.set_jit(
        enabled: Union[bool, str]
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Classifying CIFAR-10 with XLA](https://www.tensorflow.org/xla/tf2xla/tutorials/autoclustering_xla) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enabled` | JIT compilation configuration. Possible values:<br><br>*   `"autoclustering"` (`True` is a deprecated alias): perform [autoclustering](https://www.tensorflow.org/xla#auto-clustering)<br>     (automatically identify and compile clusters of nodes) on all graphs using [XLA](https://www.tensorflow.org/xla)<br>    .<br>*   `False`: do not automatically compile any graphs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.