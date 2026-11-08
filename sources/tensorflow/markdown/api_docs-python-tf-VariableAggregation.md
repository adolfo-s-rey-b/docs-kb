[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FVariableAggregation&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.VariableAggregation Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L92-L139)

Indicates how a distributed variable will be aggregated.

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 distributes a model by making multiple copies (called "replicas") acting on different elements of the input batch in a data parallel model. When performing some variable-update operation, for example `var.assign_add(x)`, in a model, we need to resolve how to combine the different values for `x` computed in the different replicas.

*   `NONE`: This is the default, giving an error if you use a variable-update operation with multiple replicas.
*   `SUM`: Add the updates across replicas.
*   `MEAN`: Take the arithmetic mean ("average") of the updates across replicas.
*   `ONLY_FIRST_REPLICA`: This is for when every replica is performing the same update, but we only want to perform the update once. Used, e.g., for the global step counter.

#### For example:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| MEAN | `<VariableAggregationV2.MEAN: 2>` |
| NONE | `<VariableAggregationV2.NONE: 0>` |
| ONLY\_FIRST\_REPLICA | `<VariableAggregationV2.ONLY_FIRST_REPLICA: 3>` |
| SUM | `<VariableAggregationV2.SUM: 1>` |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.