[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.run\_functions\_eagerly Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/polymorphic_function/eager_function_run.py#L31-L76)

Enables / disables eager execution of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.run_functions_eagerly`](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)

tf.config.run_functions_eagerly(
        run_eagerly
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs) |

Calling [`tf.config.run_functions_eagerly(True)`](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)
 will make all invocations of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 run eagerly instead of running as a traced graph function. This can be useful for debugging. As the code now runs line-by-line, you can add arbitrary `print` messages or pdb breakpoints to monitor the inputs/outputs of each Tensorflow operation. However, you should avoid using this for actual production because it significantly slows down execution.

    def my_func(a):

    # A side effect the first time the function is traced

    # `print` is a python side effect, it won't execute as the traced function

    # Now, switch to eager running

    # Turn this back off

|     |     |
| --- | --- |
| Args<br>---- |     |
| `run_eagerly` | Boolean. Whether to run functions eagerly. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.