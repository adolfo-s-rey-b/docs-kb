[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.relayout Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L411-L449)

Changes the layout of `tensor`.

tf.experimental.dtensor.relayout(
        tensor: tf.Tensor,
        layout: tf.experimental.dtensor.Layout,
        name: Optional[str] = None
    ) -> tf.Tensor

### Used in the notebooks

| Used in the guide |
| --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) |

Changes the layout of `tensor` to `layout`. This is used to fine-tune the behavior of ops following/connected to `tensor`, such as choosing one SPMD expansion pattern over another. This works by forward propagating `layout` to connected TensorFlow computation graphs during layout propagation.

Currently, only converting layouts from replicated to sharded or sharded to replicated per mesh dimension is supported. That is, "x, y" -> "unsharded, y" is supported, while "x, y" -> "z, y" is not supported.

We also support a special "match" sharding spec, which instructs the relayout to act as an identity operation with respect to any sharding on these mesh dimensions.

Relayout is internally lowered to a set of Split and/or AllToAll ops. When tensor layouts are converted from replicated to sharded, the cost is comparatively low because we only insert Split ops and no cross-device communication is needed. However, when tensor layouts are converted from sharded to replicated, cross-device communication may occur, causing potential performance impact.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A DTensor to specify a new layout for. |
| `layout` | A Layout object specifying a new sharding spec. |
| `name` | name of the Op. |

|     |
| --- |
| Returns<br>------- |     |
| A DTensor output from the Relayout op. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.