[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/control_dependencies?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.control\_dependencies Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/control_dependencies#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4554-L4626)

Wrapper for [`Graph.control_dependencies()`](https://www.tensorflow.org/api_docs/python/tf/Graph#control_dependencies)
 using the default graph.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)

tf.control_dependencies(
        control_inputs
    ) -> Graph._ControlDependenciesController

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution)<br>    <br>*   [TensorFlow Probability Case Study: Covariance Estimation](https://www.tensorflow.org/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) |

See [`tf.Graph.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/Graph#control_dependencies)
 for more details.

In TensorFlow 2 with eager and/or Autograph, you should not need this method most of the times, as ops execute in the expected order thanks to automatic control dependencies. Only use it to manually control ordering, for example as a workaround to known issues such as [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 with `tf.debugging.assert*` and [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
. For example:

    @tf.function(

    # Error raised in either `add` or `assert`

    @tf.function(

    # Error raised in `assert`

When eager execution is enabled, any callable object in the `control_inputs` list will be called.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `control_inputs` | A list of `Operation` or `Tensor` objects which must be executed or computed before running the operations defined in the context. Can also be `None` to clear the control dependencies. If eager execution is enabled, any callable object in the `control_inputs` list will be called. |

|     |
| --- |
| Returns<br>------- |     |
| A context manager that specifies control dependencies for all operations constructed within the context. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.