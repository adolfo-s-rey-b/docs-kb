[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftest%2Fgpu_device_name&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name#used-in-the-notebooks)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.gpu\_device\_name Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name#used-in-the-notebooks)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L170-L189)

Returns the name of a GPU device if available or a empty string.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.gpu_device_name`](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name)

tf.test.gpu_device_name() -> str

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fitting Generalized Linear Mixed-effects Models Using Variational Inference](https://www.tensorflow.org/probability/examples/Linear_Mixed_Effects_Model_Variational_Inference)<br>    <br>*   [Linear Mixed Effects Models](https://www.tensorflow.org/probability/examples/Linear_Mixed_Effects_Models)<br>    <br>*   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution)<br>    <br>*   [TFP Probabilistic Layers: Regression](https://www.tensorflow.org/probability/examples/Probabilistic_Layers_Regression)<br>    <br>*   [TFP Probabilistic Layers: Variational Auto Encoder](https://www.tensorflow.org/probability/examples/Probabilistic_Layers_VAE) |

This method should only be used in tests written with [`tf.test.TestCase`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)
.

    class MyTest(tf.test.TestCase):

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.