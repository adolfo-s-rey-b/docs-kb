[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.saved\_model.experimental.TrackableResource Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/trackable/resource.py#L233-L286)

Holds a Tensor which a tf.function can capture.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.experimental.TrackableResource`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)

tf.saved_model.experimental.TrackableResource(
        device=''
    )

A TrackableResource is most useful for stateful Tensors that require initialization, such as [`tf.lookup.StaticHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticHashTable)
. `TrackableResource`s are discovered by traversing the graph of object attributes, e.g. during [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
.

A TrackableResource has three methods to override:

*   `_create_resource` should create the resource tensor handle.
*   `_initialize` should initialize the resource held at `self.resource_handle`.
*   `_destroy_resource` is called upon a `TrackableResource`'s destruction and should decrement the resource's ref count. For most resources, this should be done with a call to [`tf.raw_ops.DestroyResourceOp`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/DestroyResourceOp)
    .

#### Example usage:

    class DemoResource(tf.saved_model.experimental.TrackableResource):

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | A string indicating a required placement for this resource, e.g. "CPU" if this resource must be created on a CPU device. A blank device allows the user to place resource creation, so generally this should be blank unless the resource only makes sense on one device. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `resource_handle` | Returns the resource handle associated with this Resource. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.