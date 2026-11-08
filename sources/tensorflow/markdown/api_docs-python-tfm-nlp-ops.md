[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.ops Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/__init__.py)

Ops package definition.

Classes
-------

[`class SamplingModule`](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule)
: Implementation for sampling strategies (go/decoding-tf-nlp).

[`class SequenceBeamSearch`](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch)
: Implementation of beam search loop.

Functions
---------

[`get_next_sentence_labels(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels)
: Extracts the next sentence label from sentences.

[`get_sentence_order_labels(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels)
: Extract segments and labels for sentence order prediction (SOP) task.

[`sequence_beam_search(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search)
: Search for sequence of subtoken ids with the largest probability.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.