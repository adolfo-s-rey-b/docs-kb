[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/summary#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/summary#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/summary#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.summary Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/summary#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/summary#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/summary#functions)
    

Public API for tf.\_api.v2.summary namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental)
 module: Public API for tf.\_api.v2.summary.experimental namespace

Classes
-------

[`class SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
: Interface representing a stateful summary writer object.

Functions
---------

[`audio(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/audio)
: Write an audio summary.

[`create_file_writer(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer)
: Creates a summary file writer for the given log directory.

[`create_noop_writer(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/create_noop_writer)
: Returns a summary writer that does nothing.

[`flush(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/flush)
: Forces summary writer to send any buffered data to storage.

[`graph(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/graph)
: Writes a TensorFlow graph summary.

[`histogram(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
: Write a histogram summary.

[`image(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/image)
: Write an image summary.

[`record_if(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/record_if)
: Sets summary recording on or off per the provided boolean value.

[`scalar(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
: Write a scalar summary.

[`should_record_summaries(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/should_record_summaries)
: Returns boolean Tensor which is True if summaries will be recorded.

[`text(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/text)
: Write a text summary.

[`trace_export(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export)
: Stops and exports the active trace as a Summary and/or profile file.

[`trace_off(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_off)
: Stops the current trace and discards any collected information.

[`trace_on(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on)
: Starts a trace to record computation graphs and profiling information.

[`write(...)`](https://www.tensorflow.org/api_docs/python/tf/summary/write)
: Writes a generic summary to the default SummaryWriter if one exists.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.