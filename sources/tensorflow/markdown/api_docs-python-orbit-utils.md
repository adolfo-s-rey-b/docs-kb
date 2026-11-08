[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit/utils#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/orbit/utils#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: orbit.utils Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit/utils#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/orbit/utils#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/__init__.py)

Defines exported symbols for the [`orbit.utils`](https://www.tensorflow.org/api_docs/python/orbit/utils)
 package.

Classes
-------

[`class EpochHelper`](https://www.tensorflow.org/api_docs/python/orbit/utils/EpochHelper)
: A helper class handle bookkeeping of epochs in custom training loops.

[`class LoopFnWithSummaries`](https://www.tensorflow.org/api_docs/python/orbit/utils/LoopFnWithSummaries)
: Implements a two-program approach for optimizing summaries on TPU.

[`class OptionalSummariesFunction`](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction)
: Wrapper that provides versions of a function with and without summaries.

[`class SummaryManager`](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager)
: A utility class for managing summary writing.

[`class SummaryManagerInterface`](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface)
: A utility interface for managing summary writing.

Functions
---------

[`create_global_step(...)`](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step)
: Creates a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 suitable for use as a global step counter.

[`create_loop_fn(...)`](https://www.tensorflow.org/api_docs/python/orbit/utils/create_loop_fn)
: Creates a loop function driven by a Python `while` loop.

[`create_tf_while_loop_fn(...)`](https://www.tensorflow.org/api_docs/python/orbit/utils/create_tf_while_loop_fn)
: Creates a loop function compatible with TF's AutoGraph loop conversion.

[`get_value(...)`](https://www.tensorflow.org/api_docs/python/orbit/utils/get_value)
: Returns input values, converting any TensorFlow values to NumPy values.

[`make_distributed_dataset(...)`](https://www.tensorflow.org/api_docs/python/orbit/utils/make_distributed_dataset)
: A utility function to help create a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.