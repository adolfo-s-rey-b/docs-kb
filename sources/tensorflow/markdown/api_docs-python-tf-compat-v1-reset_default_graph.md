[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#used-in-the-notebooks)
        
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reset\_default\_graph Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#used-in-the-notebooks)
        
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reset_default_graph#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5112-L5139)

Clears the default graph stack and resets the global default graph.

tf.compat.v1.reset_default_graph() -> None

Migrate to TF2
--------------

`reset_default_graph` does not work with either eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, and you should not invoke it directly. To migrate code that uses Graph-related functions to TF2, rewrite the code without them. See the [migration guide](https://www.tensorflow.org/guide/migrate)
 for more description about the behavior and semantic changes between Tensorflow 1 and Tensorflow 2.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Generating Images with BigGAN](https://www.tensorflow.org/hub/tutorials/biggan_generation_with_tf_hub)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector)<br>    <br>*   [Generating Images with Little Data Using S3GAN](https://www.tensorflow.org/hub/tutorials/s3gan_generation_with_tf_hub)<br>    <br>*   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `AssertionError` | If this function is called within a nested graph. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.