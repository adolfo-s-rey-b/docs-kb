[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fdisable_eager_execution&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#used-in-the-notebooks)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.disable\_eager\_execution Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution#used-in-the-notebooks)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4995-L5013)

Disables eager execution.

tf.compat.v1.disable_eager_execution() -> None

Migrate to TF2
--------------

This function is not necessary if you are using TF2. Eager execution is enabled by default. If you want to use Graph mode please consider [tf.function](https://www.tensorflow.org/api_docs/python/tf/function)
.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)<br>    <br>*   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings)<br>    <br>*   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm) |

This function can only be called before any Graphs, Ops, or Tensors have been created.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.