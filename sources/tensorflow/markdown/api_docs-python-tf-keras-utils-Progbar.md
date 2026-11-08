[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Progbar#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.Progbar Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/progbar.py#L12-L298)

Displays a progress bar.

tf.keras.utils.Progbar(
        target,
        width=20,
        verbose=1,
        interval=0.05,
        stateful_metrics=None,
        stateless_metrics=None,
        unit_name='step'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial) |

If neither of `stateful_metrics` and `stateless_metrics` is provided, all metrics are assumed to be stateless (averaged by the progress bar before display).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target` | Total number of steps expected, None if unknown. |
| `width` | Progress bar width on screen. |
| `verbose` | Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose) |
| `stateful_metrics` | Iterable of string names of metrics that should _not_ be averaged over time. Metrics in this list will be displayed as-is. If provided, do not provide `stateless_metrics`. |
| `stateless_metrics` | Iterable of string names of metrics that _should_ be averaged over time. Metrics in this list will be averaged by the progbar before display. If provided, do not provide `stateful_metrics`. |
| `interval` | Minimum visual progress update interval (in seconds). |
| `unit_name` | Display name for step counts (usually "step" or "sample"). |

Methods
-------

### `add`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/progbar.py#L239-L240)

add(
        n, values=None
    )

### `update`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/progbar.py#L85-L237)

update(
        current, values=None, finalize=None
    )

Updates the progress bar.

|     |     |
| --- | --- |
| Args |     |
| `current` | Index of current step. |
| `values` | List of tuples: `(name, value_for_last_step)`. If `name` is in `stateful_metrics`, `value_for_last_step` will be displayed as-is. Else, an average of the metric over time will be displayed. |
| `finalize` | Whether this is the last update for the progress bar. If `None`, defaults to `current >= self.target`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.