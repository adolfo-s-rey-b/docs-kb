[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.enable\_eager\_execution Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/enable_eager_execution#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4917-L4992)

Enables eager execution for the lifetime of this program.

tf.compat.v1.enable_eager_execution(
        config=None, device_policy=None, execution_mode=None
    ) -> None

Migrate to TF2
--------------

This function is not necessary if you are using TF2. Eager execution is enabled by default.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow Constrained Optimization Example Using CelebA Dataset](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)<br>    <br>*   [TensorFlow Distributions: A Gentle Introduction](https://www.tensorflow.org/probability/examples/TensorFlow_Distributions_Tutorial) |

Eager execution provides an imperative interface to TensorFlow. With eager execution enabled, TensorFlow functions execute operations immediately (as opposed to adding to a graph to be executed later in a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
) and return concrete values (as opposed to symbolic references to a node in a computational graph).

#### For example:

tf.compat.v1.enable_eager_execution()
    
    # After eager execution is enabled, operations are executed as they are
    # defined and Tensor objects hold concrete values, which can be accessed as
    # numpy.ndarray`s through the numpy() method.
    assert tf.multiply(6, 7).numpy() == 42

Eager execution cannot be enabled after TensorFlow APIs have been used to create or execute graphs. It is typically recommended to invoke this function at program startup and not in a library (as most libraries should be usable both with and without eager execution).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | (Optional.) A [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> to use to configure the environment in which operations are executed. Note that [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> is also used to configure graph execution (via [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br>) and many options within [`tf.compat.v1.ConfigProto`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)<br> are not implemented (or are irrelevant) when eager execution is enabled. |
| `device_policy` | (Optional.) Policy controlling how operations requiring inputs on a specific device (e.g., a GPU 0) handle inputs on a different device (e.g. GPU 1 or CPU). When set to None, an appropriate value will be picked automatically. The value picked may change between TensorFlow releases. Valid values:<br><br>*   DEVICE\_PLACEMENT\_EXPLICIT: raises an error if the placement is not correct.<br>*   DEVICE\_PLACEMENT\_WARN: copies the tensors which are not on the right device but logs a warning.<br>*   DEVICE\_PLACEMENT\_SILENT: silently copies the tensors. Note that this may hide performance problems as there is no notification provided when operations are blocked on the tensor being copied between devices.<br>*   DEVICE\_PLACEMENT\_SILENT\_FOR\_INT32: silently copies int32 tensors, raising errors on the other ones. |
| `execution_mode` | (Optional.) Policy controlling how operations dispatched are actually executed. When set to None, an appropriate value will be picked automatically. The value picked may change between TensorFlow releases. Valid values:*   SYNC: executes each operation synchronously.<br>*   ASYNC: executes each operation asynchronously. These operations may return "non-ready" handles. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If eager execution is enabled after creating/executing a TensorFlow graph, or if options provided conflict with a previous call to this function. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.