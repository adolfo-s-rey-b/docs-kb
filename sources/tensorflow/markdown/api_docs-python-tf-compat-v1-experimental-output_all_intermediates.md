[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fexperimental%2Foutput_all_intermediates&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.experimental.output\_all\_intermediates Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_util_v2.py#L404-L429)

Whether to output all intermediates from functional control flow ops.

tf.compat.v1.experimental.output_all_intermediates(
        state
    )

The "default" behavior to is to output all intermediates when using v2 control flow inside Keras models in graph mode. This is needed to support taking gradients of v2 control flow. In graph mode, Keras can sometimes freeze the forward graph before the gradient computation which does not work for v2 control flow since it requires updating the forward ops to output the needed intermediates. We work around this by proactively outputting the needed intermediates when building the forward pass itself. Ideally any such extra tensors should be pruned out at runtime. However, if for any reason this doesn't work for you or if you have an inference-only model you can turn this behavior off using [`tf.compat.v1.experimental.output_all_intermediates(False)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates)
.

If with the default behavior you are still seeing errors of the form "Connecting to invalid output X of source node Y which has Z outputs" try setting [`tf.compat.v1.experimental.output_all_intermediates(True)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/experimental/output_all_intermediates)
 and please file an issue at https://github.com/tensorflow/tensorflow/issues.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `state` | True, False or None. None restores the default behavior. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.