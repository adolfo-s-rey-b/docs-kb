[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fget_strategy&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.get\_strategy Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L542-L559)

Returns the current [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 object.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.get_strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)

tf.distribute.get_strategy() -> 'StrategyBase'

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) |

Typically only used in a cross-replica context:

if tf.distribute.in_cross_replica_context():
      strategy = tf.distribute.get_strategy()
      ...

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object. Inside a `with strategy.scope()` block, it returns `strategy`, otherwise it returns the default (single-replica) [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.