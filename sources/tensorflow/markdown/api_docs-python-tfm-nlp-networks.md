[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.networks Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/__init__.py)

Networks are combinations of [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 layers (and possibly other networks).

They are [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 models that would not be trained alone. It encapsulates common network structures like a transformer encoder into an easily handled object with a standardized configuration.

Classes
-------

[`class AlbertEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder)
: ALBERT ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
) text encoder network.

[`class BertEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder)
: Bi-directional Transformer-based encoder network.

[`class BertEncoderV2`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoderV2)
: Bi-directional Transformer-based encoder network.

[`class Classification`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification)
: Classification network head for BERT modeling.

[`class EncoderScaffold`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold)
: Bi-directional Transformer-based encoder network scaffold.

[`class FNet`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet)
: FNet encoder network.

[`class FunnelTransformerEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FunnelTransformerEncoder)
: Funnel Transformer-based encoder network.

[`class MobileBERTEncoder`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder)
: A Keras functional API implementation for MobileBERT encoder.

[`class PackedSequenceEmbedding`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding)
: An embedding network supporting packed sequences and position ids.

[`class SpanLabeling`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SpanLabeling)
: Span labeling network head for BERT modeling.

[`class SparseMixer`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer)
: Sparse Mixer encoder network.

[`class XLNetBase`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase)
: Base XLNet model.

[`class XLNetSpanLabeling`](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling)
: Span labeling network head for XLNet on SQuAD2.0.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.