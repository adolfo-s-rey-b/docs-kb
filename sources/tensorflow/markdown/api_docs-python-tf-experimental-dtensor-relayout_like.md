[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout_like#main-content)

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
    

tf.experimental.dtensor.relayout\_like Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L452-L502)

Changes the layout of `tensor` to the same as `layout_tensor`.

tf.experimental.dtensor.relayout_like(
        tensor: tf.Tensor,
        layout_tensor: tf.Tensor,
        name: Optional[str] = None
    ) -> tf.Tensor

`relayout_like` is often used inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, to ensure a tensor is placed to the same mesh and with the same layout as another tensor.

The backward gradient of a `relayout` is a `relayout_like` operation, to ensure the backward tensor has the same layout as the forward input tensor:

@ops.RegisterGradient("Relayout")
    def _relayout_gradient(op, grad):
      return relayout_like(grad, layout_input=op.inputs[0])

Here is another illustrative example:

@tf.function
    def func(x):
      z = tf.ones(x.shape)
      z = dtensor.relayout_like(z, x)
      return x + z
    
    with dtensor.default_mesh(cpu_mesh):
      x = tf.ones((4, 4))
    
    with dtensor.default_mesh(gpu_mesh):
      y = func(x)
    
    # y would be on the cpu mesh, following the mesh of x.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A DTensor to specify a new layout for. |
| `layout_tensor` | A Tensor object whose layout will be used for the layout of result. The shape and type of layout\_tensor are irrelevant. |
| `name` | name of the Op. |

|     |
| --- |
| Returns<br>------- |     |
| A DTensor output from the RelayoutLike op. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.