[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/broadcast_to)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/broadcast_to?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.broadcast\_to Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_to#returns)
    

Broadcast an array for a compatible shape.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.broadcast_to`](https://www.tensorflow.org/api_docs/python/tf/broadcast_to)

tf.broadcast_to(
        input: Annotated[Any, TV_BroadcastTo_T],
        shape: Annotated[Any, TV_BroadcastTo_Tidx],
        name=None
    ) -> Annotated[Any, TV_BroadcastTo_T]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor) | *   [Eight schools](https://www.tensorflow.org/probability/examples/Eight_Schools)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification)<br>    <br>*   [FFJORD](https://www.tensorflow.org/probability/examples/FFJORD_Demo)<br>    <br>*   [TFP Release Notes notebook (0.13.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_13_0) |

Broadcasting is the process of making arrays to have compatible shapes for arithmetic operations. Two shapes are compatible if for each dimension pair they are either equal or one of them is one.

#### For example:

    x = tf.constant([[1, 2, 3]])   # Shape (1, 3,)

In the above example, the input Tensor with the shape of `[1, 3]` is broadcasted to output Tensor with shape of `[2, 3]`.

When broadcasting, if a tensor has fewer axes than necessary its shape is padded on the left with ones. So this gives the same result as the previous example:

    x = tf.constant([1, 2, 3])   # Shape (3,)

When doing broadcasted operations such as multiplying a tensor by a scalar, broadcasting (usually) confers some time or space benefit, as the broadcasted tensor is never materialized.

However, `broadcast_to` does not carry with it any such benefits. The newly-created tensor takes the full memory of the broadcasted shape. (In a graph context, `broadcast_to` might be fused to subsequent operation and then be optimized away, however.)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. A Tensor to broadcast. |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. An 1-D `int` Tensor. The shape of the desired output. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.