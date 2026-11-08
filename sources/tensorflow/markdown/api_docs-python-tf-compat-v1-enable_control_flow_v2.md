[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_control_flow_v2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_control_flow_v2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_control_flow_v2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.enable\_control\_flow\_v2 Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_v2_toggles.py#L24-L44)

Use control flow v2.

tf.compat.v1.enable_control_flow_v2()

control flow v2 (cfv2) is an improved version of control flow in TensorFlow with support for higher order derivatives. Enabling cfv2 will change the graph/function representation of control flow, e.g., [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
 and [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
 will generate functional `While` and `If` ops instead of low-level `Switch`, `Merge` etc. ops. Note: Importing and running graphs exported with old control flow will still be supported.

Calling tf.enable\_control\_flow\_v2() lets you opt-in to this TensorFlow 2.0 feature.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.