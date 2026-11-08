[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fexperimental%2Fpartitioners&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.distribute.experimental.partitioners Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners#classes)
    

Public API for tf.\_api.v2.distribute.experimental.partitioners namespace

Classes
-------

[`class FixedShardsPartitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/FixedShardsPartitioner)
: Partitioner that allocates a fixed number of shards.

[`class MaxSizePartitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner)
: Partitioner that keeps shards below `max_shard_bytes`.

[`class MinSizePartitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MinSizePartitioner)
: Partitioner that allocates a minimum size per shard.

[`class Partitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner)
: Partitioner base class: all partitiners inherit from this class.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.