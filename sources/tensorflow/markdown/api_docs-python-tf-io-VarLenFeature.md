[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.VarLenFeature Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_config.py#L44-L51)

Configuration for parsing a variable-length input feature.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.VarLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature)
, [`tf.compat.v1.io.VarLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature)

tf.io.VarLenFeature(
        dtype
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Introduction to Fairness Indicators](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_Example_Colab)<br>    <br>*   [Fairness Indicators TensorBoard Plugin Example Colab](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TensorBoard_Plugin_Example_Colab)<br>    <br>*   [Fairness Indicators on TF-Hub Text Embeddings](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_on_TF_Hub_Text_Embeddings)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `dtype` | Data type of input. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | A `namedtuple` alias for field number 0 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.