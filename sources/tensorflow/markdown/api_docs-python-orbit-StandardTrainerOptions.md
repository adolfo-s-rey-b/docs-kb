[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Forbit%2FStandardTrainerOptions&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.StandardTrainerOptions Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L48-L68)

Advanced options for [`orbit.StandardTrainer`](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer)
.

orbit.StandardTrainerOptions(
        use_tf_function: bool = True,
        use_tf_while_loop: bool = True,
        use_tpu_summary_optimization: bool = False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `use_tf_function` | A boolean indicating whether to apply [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> to the training loop. This will only affect the body of the loop (involving `train_step`); `train_loop_begin` and `train_loop_end` will always be run in eager mode. |
| `use_tf_while_loop` | A boolean indicating whether to run the training loop using a [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)<br>. If `True`, `use_tf_function` must also be `True`. |
| `use_tpu_summary_optimization` | A boolean indicating whether to enable a performance optimization for summaries in TPUs. Writing summaries conditionally with outside compilation on TPUs can be extremely slow. If `True`, this optimization creates two [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s with two XLA programs (one with summary calls, and one without). The program with summaries runs only for one step when summaries should be recorded. |

Methods
-------

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| use\_tf\_function | `True` |
| use\_tf\_while\_loop | `True` |
| use\_tpu\_summary\_optimization | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-30 UTC.