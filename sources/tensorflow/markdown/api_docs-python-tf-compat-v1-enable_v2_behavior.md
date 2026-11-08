[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#used-in-the-notebooks)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.enable\_v2\_behavior Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_v2_behavior#used-in-the-notebooks)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compat/v2_compat.py#L39-L70)

Enables TensorFlow 2.x behaviors.

tf.compat.v1.enable_v2_behavior()

Migrate to TF2
--------------

This function is not necessary if you are using TF2. V2 behavior is enabled by default.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Pandas DataFrame to Fairness Indicators Case Study](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_Pandas_Case_Study)<br>    <br>*   [Migrating tf.summary usage to TF 2.x](https://www.tensorflow.org/tensorboard/migrate) |

This function can be called at the beginning of the program (before `Tensors`, `Graphs` or other structures have been created, and before devices have been initialized. It switches all global behaviors that are different between TensorFlow 1.x and 2.x to behave as intended for 2.x.

This function is called in the main TensorFlow `__init__.py` file, user should not need to call it, except during complex migrations.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.