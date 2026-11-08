[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/queue#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/queue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/queue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fqueue&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/queue#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.queue Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/queue#classes)
    

Public API for tf.\_api.v2.queue namespace

Classes
-------

[`class FIFOQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/FIFOQueue)
: A queue implementation that dequeues elements in first-in first-out order.

[`class PaddingFIFOQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/PaddingFIFOQueue)
: A FIFOQueue that supports batching variable-sized tensors by padding.

[`class PriorityQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/PriorityQueue)
: A queue implementation that dequeues elements in prioritized order.

[`class QueueBase`](https://www.tensorflow.org/api_docs/python/tf/queue/QueueBase)
: Base class for queue implementations.

[`class RandomShuffleQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/RandomShuffleQueue)
: A queue implementation that dequeues elements in a random order.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.