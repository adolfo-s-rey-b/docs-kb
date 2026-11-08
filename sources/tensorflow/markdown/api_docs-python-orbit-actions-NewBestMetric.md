[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Forbit%2Factions%2FNewBestMetric&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#methods)
    *   [commit](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#commit)
        
    *   [metric\_value](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#metric_value)
        
    *   [test](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#test)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.actions.NewBestMetric Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#methods)
    *   [commit](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#commit)
        
    *   [metric\_value](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#metric_value)
        
    *   [test](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#test)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L31-L164)

Condition that is satisfied when a new best metric is achieved.

orbit.actions.NewBestMetric(
        metric: Union[str, MetricFn],
        higher_is_better: bool = True,
        filename: Optional[str] = None,
        write_metric=True
    )

This class keeps track of the best metric value seen so far, optionally in a persistent (preemption-safe) way.

Two methods are provided, which each satisfy the `Action` protocol: `test` for only testing whether a new best metric is achieved by a given train/eval output, and `commit`, which both tests and records the new best metric value if it is achieved. These separate methods enable the same `NewBestMetric` instance to be reused as a condition multiple times, and can also provide additional preemption/failure safety. For example, to avoid updating the best metric if a model export fails or is pre-emptied:

new_best_metric = orbit.actions.NewBestMetric(
      'accuracy', filename='/model/dir/best_metric')
    action = orbit.actions.ConditionalAction(
        condition=new_best_metric.test,
        action=[\
          orbit.actions.ExportSavedModel(...),\
          new_best_metric.commit\
        ])

The default `__call__` implementation is equivalent to `commit`.

This class is safe to use in multi-client settings if all clients can be guaranteed to compute the same metric. However when saving metrics it may be helpful to avoid unnecessary writes by setting the `write_value` parameter to `False` for most clients.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `metric` | Either a string key name to use to look up a metric (assuming the train/eval output is a dictionary), or a callable that accepts the train/eval output and returns a metric value. |
| `higher_is_better` | Whether higher metric values are better. If `True`, a new best metric is achieved when the metric value is strictly greater than the previous best metric. If `False`, a new best metric is achieved when the metric value is strictly less than the previous best metric. |
| `filename` | A filename to use for storage of the best metric value seen so far, to allow peristence of the value across preemptions. If `None` (default), values aren't persisted. |
| `write_metric` | If `filename` is set, this controls whether this instance will write new best metric values to the file, or just read from the file to obtain the initial value. Setting this to `False` for most clients in some multi-client setups can avoid unnecessary file writes. Has no effect if `filename` is `None`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `metric` | The metric passed to **init** (may be a string key or a callable that can be applied to train/eval output). |
| `higher_is_better` | Whether higher metric values are better. |
| `best_value` | Returns the best metric value seen so far. |

Methods
-------

### `commit`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L147-L164)

commit(
        output: runner.Output
    ) -> bool

Tests `output` and updates the current best value if necessary.

Unlike `test` above, if `output` does contain a new best metric value, this method _does_ save it (i.e., subsequent calls to this method with the same `output` will return `False`).

|     |     |
| --- | --- |
| Args |     |
| `output` | The train or eval output to test. |

|     |
| --- |
| Returns |     |
| `True` if `output` contains a new best metric value, `False` otherwise. |     |

### `metric_value`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L112-L118)

metric_value(
        output: runner.Output
    ) -> float

Computes the metric value for the given `output`.

### `test`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L125-L145)

test(
        output: runner.Output
    ) -> bool

Tests `output` to see if it contains a new best metric value.

If `output` does contain a new best metric value, this method does _not_ save it (i.e., calling this method multiple times in a row with the same `output` will continue to return `True`).

|     |     |
| --- | --- |
| Args |     |
| `output` | The train or eval output to test. |

|     |
| --- |
| Returns |     |
| `True` if `output` contains a new best metric value, `False` otherwise. |     |

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L99-L110)

__call__(
        output: runner.Output
    ) -> bool

Tests `output` and updates the current best value if necessary.

This is equivalent to `commit` below.

|     |     |
| --- | --- |
| Args |     |
| `output` | The train or eval output to test. |

|     |
| --- |
| Returns |     |
| `True` if `output` contains a new best metric value, `False` otherwise. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.