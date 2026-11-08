[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.call\_with\_layout Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L37-L64)

Calls a function in the DTensor device scope if `layout` is not None.

tf.experimental.dtensor.call_with_layout(
        fn: Callable[..., Any],
        layout: Optional[tf.experimental.dtensor.Layout],
        *args,
        **kwargs
    ) -> Any

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

If `layout` is not None, `fn` consumes DTensor(s) as input and produces a DTensor as output; a DTensor is a tf.Tensor with layout-related attributes.

If `layout` is None, `fn` consumes and produces regular tf.Tensors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | A supported TF API function such as tf.zeros. |
| `layout` | Optional, the layout of the output DTensor. |
| `*args` | Arguments given to `fn`. |
| `**kwargs` | Keyword arguments given to `fn`. |

|     |
| --- |
| Returns<br>------- |     |
| The return value of `fn` transformed to a DTensor if requested. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.