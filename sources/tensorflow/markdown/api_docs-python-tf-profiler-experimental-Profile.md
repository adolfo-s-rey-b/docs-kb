[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.Profile Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/Profile#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_v2.py#L183-L212)

Context-manager profile API.

tf.profiler.experimental.Profile(
        logdir, options=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFF simulations with accelerators](https://www.tensorflow.org/federated/tutorials/simulations_with_accelerators) |

Profiling will start when entering the scope, and stop and save the results to the logdir when exits the scope. Open TensorBoard profile tab to view results.

#### Example usage:

with tf.profiler.experimental.Profile("/path/to/logdir"):
      # do some work

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logdir` | profile data will save to this directory. |
| `options` | An optional [`tf.profiler.experimental.ProfilerOptions`](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions)<br> can be provided to fine tune the profiler's behavior. |

Methods
-------

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_v2.py#L208-L209)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_v2.py#L211-L212)

__exit__(
        typ, value, tb
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.