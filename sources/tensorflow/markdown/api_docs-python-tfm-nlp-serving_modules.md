[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.serving\_modules Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/serving/serving_modules.py)

Serving export modules for TF Model Garden NLP models.

Classes
-------

[`class MaskedLM`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/MaskedLM)
: The export module for the Bert Pretrain (MaskedLM) task.

[`class QuestionAnswering`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/QuestionAnswering)
: The export module for the question answering task.

[`class SentencePrediction`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/SentencePrediction)
: The export module for the sentence prediction task.

[`class Tagging`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/Tagging)
: The export module for the tagging task.

[`class Translation`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/Translation)
: The export module for the translation task.

Functions
---------

[`features_to_int32(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/serving_modules/features_to_int32)
: Converts tf.int64 features to tf.int32, keep other features the same.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.