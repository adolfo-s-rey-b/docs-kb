[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_traceback_filtering#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_traceback_filtering)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_traceback_filtering?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.enable\_traceback\_filtering Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/traceback_utils.py#L18-L36)

Turn on traceback filtering.

tf.keras.config.enable_traceback_filtering()

Raw Keras tracebacks (also known as stack traces) involve many internal frames, which can be challenging to read through, while not being actionable for end users. By default, Keras filters internal frames in most exceptions that it raises, to keep traceback short, readable, and focused on what's actionable for you (your own code).

See also [`keras.config.disable_traceback_filtering()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/disable_traceback_filtering)
 and [`keras.config.is_traceback_filtering_enabled()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/is_traceback_filtering_enabled)
.

If you have previously disabled traceback filtering via [`keras.config.disable_traceback_filtering()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/disable_traceback_filtering)
, you can re-enable it via [`keras.config.enable_traceback_filtering()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_traceback_filtering)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.