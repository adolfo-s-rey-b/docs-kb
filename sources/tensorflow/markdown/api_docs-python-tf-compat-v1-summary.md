[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsummary&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.summary Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary#functions)
    

Public API for tf.\_api.v2.summary namespace

Classes
-------

[`class Event`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Event)
: A ProtocolMessage

[`class FileWriter`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter)
: Writes `Summary` protocol buffers to event files.

[`class FileWriterCache`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriterCache)
: Cache for file writers.

[`class SessionLog`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SessionLog)
: A ProtocolMessage

[`class Summary`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Summary)
: A ProtocolMessage

[`class SummaryDescription`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/SummaryDescription)
: A ProtocolMessage

[`class TaggedRunMetadata`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/TaggedRunMetadata)
: A ProtocolMessage

Functions
---------

[`all_v2_summary_ops(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops)
: Returns all V2-style summary ops defined in the current default graph.

[`audio(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio)
: Outputs a `Summary` protocol buffer with audio.

[`get_summary_description(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description)
: Given a TensorSummary node\_def, retrieve its SummaryDescription.

[`histogram(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram)
: Outputs a `Summary` protocol buffer with a histogram.

[`image(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image)
: Outputs a `Summary` protocol buffer with images.

[`initialize(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize)
: Initializes summary writing for graph execution mode.

[`merge(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge)
: Merges summaries.

[`merge_all(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge_all)
: Merges all summaries collected in the default graph.

[`scalar(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/scalar)
: Outputs a `Summary` protocol buffer containing a single scalar value.

[`tensor_summary(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/tensor_summary)
: Outputs a `Summary` protocol buffer with a serialized tensor.proto.

[`text(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text)
: Summarizes textual data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.