[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/disable_mixed_precision_graph_rewrite#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/disable_mixed_precision_graph_rewrite)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/disable_mixed_precision_graph_rewrite?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.disable\_mixed\_precision\_graph\_rewrite Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/mixed_precision.py#L216-L248)

Disables the mixed precision graph rewrite.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.disable_mixed_precision_graph_rewrite`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/disable_mixed_precision_graph_rewrite)

tf.compat.v1.mixed_precision.disable_mixed_precision_graph_rewrite()

After this is called, the mixed precision graph rewrite will no longer run for new Sessions, and so float32 operations will no longer be converted to float16 in such Sessions. However, any existing Sessions will continue to have the graph rewrite enabled if they were created after `enable_mixed_precision_graph_rewrite` was called but before `disable_mixed_precision_graph_rewrite` was called.

This does not undo the effects of loss scaling. Any optimizers wrapped with a LossScaleOptimizer will continue to do loss scaling, although this loss scaling will no longer be useful if the optimizer is used in new Sessions, as the graph rewrite no longer converts the graph to use float16.

This function is useful for unit testing. A unit tests can test using the mixed precision graph rewrite, then disable it so future unit tests continue using float32. If this is done, unit tests should not share a single session, as `enable_mixed_precision_graph_rewrite` and `disable_mixed_precision_graph_rewrite` have no effect on existing sessions.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.