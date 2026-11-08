[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.models Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/nlp/models#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/__init__.py)

Models are combinations of [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 layers and models that can be trained.

Several pre-built canned models are provided to train encoder networks. These models are intended as both convenience functions and canonical examples.

Classes
-------

[`class BertClassifier`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertClassifier)
: Classifier model based on a BERT-style transformer-based encoder.

[`class BertPretrainer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer)
: BERT pretraining model.

[`class BertPretrainerV2`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2)
: BERT pretraining model V2.

[`class BertSpanLabeler`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler)
: Span labeler model based on a BERT-style transformer-based encoder.

[`class BertTokenClassifier`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertTokenClassifier)
: Token classifier model based on a BERT-style transformer-based encoder.

[`class DualEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder)
: A dual encoder model based on a transformer-based encoder.

[`class ElectraPretrainer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer)
: ELECTRA network training model.

[`class Seq2SeqTransformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer)
: Transformer model with Keras.

[`class T5Transformer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer)
: Transformer Encoder+Decoder for sequence to sequence.

[`class T5TransformerParams`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams)
: Transformer parameters.

[`class TransformerDecoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder)
: Transformer decoder.

[`class TransformerEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder)
: Transformer encoder.

[`class XLNetClassifier`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier)
: Classifier model based on XLNet.

[`class XLNetPretrainer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetPretrainer)
: XLNet-based pretrainer.

[`class XLNetSpanLabeler`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetSpanLabeler)
: Span labeler model based on XLNet.

Functions
---------

[`attention_initializer(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/attention_initializer)
: Initializer for attention layers in Seq2SeqTransformer.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| EOS\_ID | `1` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.