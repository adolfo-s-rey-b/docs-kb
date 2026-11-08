[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/get_logger#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/get_logger)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/get_logger?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/get_logger#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/get_logger#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.get\_logger Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/get_logger#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/get_logger#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/tf_logging.py#L93-L179)

Return TF logger instance.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.get_logger`](https://www.tensorflow.org/api_docs/python/tf/get_logger)

tf.get_logger()

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite)<br>    <br>*   [Customizing MinDiffModel](https://www.tensorflow.org/responsible_ai/model_remediation/min_diff/guide/customizing_min_diff_model)<br>    <br>*   [Integrating MinDiff with MinDiffModel](https://www.tensorflow.org/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_with_min_diff_model)<br>    <br>*   [Integrating MinDiff without MinDiffModel](https://www.tensorflow.org/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_without_min_diff_model)<br>    <br>*   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) | *   [TensorFlow Hub Object Detection Colab](https://www.tensorflow.org/hub/tutorials/tf2_object_detection)<br>    <br>*   [Implement Differential Privacy with TensorFlow Privacy](https://www.tensorflow.org/responsible_ai/privacy/tutorials/classification_privacy)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning)<br>    <br>*   [Object Detection with TensorFlow Lite Model Maker](https://www.tensorflow.org/lite/models/modify/model_maker/object_detection)<br>    <br>*   [Text classification with TensorFlow Lite Model Maker](https://www.tensorflow.org/lite/models/modify/model_maker/text_classification) |

|     |
| --- |
| Returns<br>------- |     |
| An instance of the Python logging library Logger. |     |

See Python documentation ([https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)
) for detailed API. Below is only a summary.

The logger has 5 levels of logging from the most serious to the least:

1.  FATAL
2.  ERROR
3.  WARN
4.  INFO
5.  DEBUG

The logger has the following methods, based on these logging levels:

1.  fatal(msg, \*args, \*\*kwargs)
2.  error(msg, \*args, \*\*kwargs)
3.  warn(msg, \*args, \*\*kwargs)
4.  info(msg, \*args, \*\*kwargs)
5.  debug(msg, \*args, \*\*kwargs)

The `msg` can contain string formatting. An example of logging at the `ERROR` level using string formatting is:

    tf.get_logger().error("The value %d is invalid.", 3)

You can also specify the logging verbosity. In this case, the WARN level log will not be emitted:

    tf.get_logger().setLevel(ERROR)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.