[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftpu%2Frewrite&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.rewrite Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L1442-L1501)

Rewrites `computation` for execution on a TPU system.

tf.compat.v1.tpu.rewrite(
        computation: Callable[..., Any],
        inputs: Optional[List[List[Optional[core_types.Tensor]]]] = None,
        infeed_queue: Optional[tpu_feed.InfeedQueue] = None,
        device_assignment: Optional[tf.tpu.experimental.DeviceAssignment] = None,
        name: Optional[Text] = None,
        xla_options: Optional[tf.tpu.XLAOptions] = None
    ) -> Any

|     |     |
| --- | --- |
| Args<br>---- |     |
| `computation` | A Python function that builds a computation to apply to the input. If the function takes n inputs, 'inputs' should be a list of n tensors.<br><br>`computation` may return a list of operations and tensors. Tensors must come before operations in the returned list. The return value of `rewrite` is a list of tensors corresponding to the tensors from the output of `computation`.<br><br>All `Operation`s constructed during `computation` will be executed when evaluating any of the returned output tensors, not just the ones returned. |
| `inputs` | A list of input tensors or `None` (equivalent to an empty list). Each input can be a nested structure containing values that are convertible to tensors. Note that passing an N-dimension list of compatible values will result in a N-dimension list of scalar tensors rather than a single Rank-N tensors. If you need different behavior, convert part of inputs to tensors with [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>. |
| `infeed_queue` | If not `None`, the `InfeedQueue` from which to append a tuple of arguments as inputs to `computation`. |
| `device_assignment` | if not `None`, a `DeviceAssignment` describing the mapping between logical cores in the computation with physical cores in the TPU topology. May be omitted for a single-core computation, in which case the core attached to task 0, TPU device 0 is used. |
| `name` | (Deprecated) Does nothing. |
| `xla_options` | An instance of [`tpu.XLAOptions`](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions)<br> which indicates the options passed to XLA compiler. Use `None` for default options. |

|     |
| --- |
| Returns<br>------- |     |
| Same data structure as if computation(\*inputs) is called directly with some exceptions for correctness. Exceptions include:<br><br>1) None output: a NoOp would be returned which control-depends on computation. 2) Single value output: A tuple containing the value would be returned. 3) Operation-only outputs: a NoOp would be returned which control-depends on computation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.