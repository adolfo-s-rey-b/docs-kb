[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#update_state)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.metrics.sliced\_metric.SlicedMetric Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/sliced_metric/SlicedMetric#update_state)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/sliced_metric.py#L22-L215)

A metric sliced by integer, boolean, or string features.

tfm.uplift.metrics.sliced_metric.SlicedMetric(
        metric: tf_keras.metrics.Metric,
        slicing_spec: (dict[str, str] | dict[str, int]),
        slicing_feature_dtype: (tf.DType | None) = None,
        name: (str | None) = None
    )

A metric wrapper that computes a metric for different slices of an arbitrary feature. The slicing is specified via a slicing spec, which is a dictionary from a slice name to the unique value to be sliced on. For each pair of `slice_name`, `slicing_value` passed, the suffix `/slice_name` will be appended to the name of the result of the corresponding slice. An overall result is also computed without any slicing applied.

In order for this to work correctly, the given metric must support passing `sample_weight` to its `update_state()` method. Additionally, the slicing feature must also be passed to `update_state()` method of this class and must be of a broadcastable shape to the metric inputs. This wrapper creates a deep copy of the metric passed to it for each slice. At every call to `update_state()`, the wrapper will call the `update_state()` method of the metric for each slice with the `sample_weights` set to zero where the slicing feature is not equal to the corresponding slicing value.

If the given metric returns a tensor, the result of this metric will be a dictionary mapping from the sliced metric's name to the result for that slice. If the given metric returns a dictionary of tensors, the result of this metric will be a flattened dictionary consisting of each of the sliced metrics' results for every slice.

#### Example usage:

    sliced_metric = SlicedMetric(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `metric` | A `tf_keras.metrics.Metric` instance. |
| `slicing_spec` | A dictionary that maps from string slice names, to one of integer, boolean, or string slicing values. |
| `slicing_feature_dtype` | The expected dtype of the slicing feature. The values in the slicing spec are casted to this type if passed. If None, the dtype of the slicing feature is inferred based on the values in the slicing spec. |
| `name` | The name of the wrapper metric. Defaults to `sliced_{metric.name}`. |

|     |
| --- |
| Raises<br>------ |     |
| A ValueError if `slicing_spec` is empty, contains duplicate slicing values, or has slicing values of different types. |     |

Methods
-------

### `call`

call(
        inputs, *args, **kwargs
    )

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

### `merge_state`

merge_state(
        metrics
    )

Merges the state from one or more metrics.

This method can be used by distributed systems to merge the state computed by different metric instances. Typically the state will be stored in the form of the metric's weights. For example, a tf.keras.metrics.Mean metric contains a list of two weight values: a total and a count. If there were two instances of a tf.keras.metrics.Accuracy that each independently aggregated partial state for an overall accuracy calculation, these two metric's states could be combined as follows:

    m1 = tf.keras.metrics.Accuracy()

    m2 = tf.keras.metrics.Accuracy()

    m2.merge_state([m1])

|     |     |
| --- | --- |
| Args |     |
| `metrics` | an iterable of metrics. The metrics must have compatible state. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the provided iterable does not contain metrics matching the metric's required specifications. |

### `reset_state`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/sliced_metric.py#L196-L199)

reset_state()

Resets all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/sliced_metric.py#L168-L194)

result() -> dict[str, tf.Tensor]

Aggregates all the metrics' results into a flattened dictionary.

### `update_state`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/sliced_metric.py#L123-L166)

update_state(
        *args,
        sample_weight: (tf.Tensor | None) = None,
        slicing_feature: tf.Tensor,
        **kwargs
    )

Updates the state of the metrics for each slice.

|     |     |
| --- | --- |
| Args |     |
| `*args` | A variable amount of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> instances that will be passed to the `update_state` method of each metric. |
| `sample_weight` | An optional [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> used to weight the sample. Its dimensions must be broadcastable to the shape(s) of \*args. |
| `slicing_feature` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> consisting of the feature to be sliced on. Its dimensions must be broadcastable to the shape(s) of \*args. |
| `**kwargs` | Keyword arguments that will be passed to the `update_state` method of each metric. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.