[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/cond)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/cond?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.cond Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/cond?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/cond.py#L243-L343)

Return `true_fn()` if the predicate `pred` is true else `false_fn()`.

tf.cond(
        pred, true_fn=None, false_fn=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) | *   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation) |

    @tf.function

    @tf.function

For more information, see [tf.function and AutoGraph guide](https://www.tensorflow.org/guide/function#autograph_transformations)
.

`true_fn` and `false_fn` both return lists of output tensors. `true_fn` and `false_fn` must have the same non-zero number and type of outputs.

Although this behavior is consistent with the dataflow model of TensorFlow, it has frequently surprised users who expected a lazier semantics. Consider the following simple program:

    x, y = tf.constant(2, dtype=tf.int32), tf.constant(4, dtype=tf.int32)

If `x < y`, the `tf.add` operation will be executed and `tf.square` operation will not be executed. Since `z` is needed for at least one branch of the `cond`, the [`tf.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
 operation is always executed, unconditionally.

Note that `cond` calls `true_fn` and `false_fn` _exactly once_ (inside the call to `cond`, and not at all during `Session.run()`). `cond` stitches together the graph fragments created during the `true_fn` and `false_fn` calls with some additional graph nodes to ensure that the right branch gets executed depending on the value of `pred`.

[`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
 supports nested structures as implemented in `tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the same (possibly nested) value structure of lists, tuples, and/or named tuples. Singleton lists and tuples form the only exceptions to this: when returned by `true_fn` and/or `false_fn`, they are implicitly unpacked to single values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pred` | A scalar determining whether to return the result of `true_fn` or `false_fn`. |
| `true_fn` | The callable to be performed if pred is true. |
| `false_fn` | The callable to be performed if pred is false. |
| `name` | Optional name prefix for the returned tensors. |

|     |
| --- |
| Returns<br>------- |     |
| Tensors returned by the call to either `true_fn` or `false_fn`. If the callables return a singleton list, the element is extracted from the list. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `true_fn` or `false_fn` is not callable. |
| `ValueError` | if `true_fn` and `false_fn` do not return the same number of tensors, or return tensors of different types. |

#### Example:

    x = tf.constant(2)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.