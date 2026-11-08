[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.StandardEvaluatorOptions Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/standard_runner.py#L214-L235)

Advanced options for the [`orbit.StandardEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator)
.

orbit.StandardEvaluatorOptions(
        use_tf_function: bool = True,
        use_tf_while_loop: bool = False,
        recreate_iterator_for_each_eval: bool = True
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `use_tf_function` | A boolean indicating whether to apply [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> to the evaluation loop. This will only affect the body of the loop (involving `eval_step`); `eval_loop_begin` and `eval_loop_end` will always be run in eager mode. |
| `use_tf_while_loop` | A boolean indicating whether to run the evaluation loop using a [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)<br>. If `True`, `use_tf_function` must also be `True`. |
| `recreate_iterator_for_each_eval` | A boolean indicating whether to recreate a new iterator for the evaluation dataset before each round of evaluation, which implies each round of evaluation starts from the beginning of the evaluation dataset. For example, the evaluation dataset is `[1, 2, 3, 4]`, batch size is 1 and evaluation steps is 2. If `True`, the data to be evaluated is \[1, 2\] every time. If `False`, the iterator state is maintained between calls to [`StandardEvaluator.evaluate()`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator#evaluate)<br>. |

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
| recreate\_iterator\_for\_each\_eval | `True` |
| use\_tf\_function | `True` |
| use\_tf\_while\_loop | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-30 UTC.