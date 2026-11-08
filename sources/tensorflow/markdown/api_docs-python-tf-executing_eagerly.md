[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.executing\_eagerly Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L2575-L2633)

Checks whether the current thread has eager execution enabled.

tf.executing_eagerly()

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Fast Style Transfer for Arbitrary Styles](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization)<br>    <br>*   [Text Classification with Movie Reviews](https://www.tensorflow.org/hub/tutorials/tf2_text_classification)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

Eager execution is enabled by default and this API returns `True` in most of cases. However, this API might return `False` in the following use cases.

*   Executing inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    , unless under [`tf.init_scope`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
     or [`tf.config.run_functions_eagerly(True)`](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)
     is previously called.
*   Executing inside a transformation function for `tf.dataset`.
*   [`tf.compat.v1.disable_eager_execution()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/disable_eager_execution)
     is called.

#### General case:

    print(tf.executing_eagerly())

Inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
:

    @tf.function

Inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 after [`tf.config.run_functions_eagerly(True)`](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)
 is called:

    tf.config.run_functions_eagerly(True)

Inside a transformation function for `tf.dataset`:

    def data_fn(x):

|     |
| --- |
| Returns<br>------- |     |
| `True` if the current thread has eager execution enabled. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.