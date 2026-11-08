[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#methods)
    *   [children](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#children)
        
    *   [descendants](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#descendants)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.TrackableView Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#methods)
    *   [children](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#children)
        
    *   [descendants](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView#descendants)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/trackable_view.py#L25-L117)

Gathers and serializes a trackable view.

tf.train.TrackableView(
        root
    )

#### Example usage:

    class SimpleModule(tf.Module):

    root = SimpleModule(name="root")

Pass root to tf.train.TrackableView.children() to get the dictionary of all children directly linked to root by name.

>>> trackable_view_children = trackable_view.children(root)
    >>> for item in trackable_view_children.items():
    ...   print(item)
    ('a_var', <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=5.0>)
    ('b_var', <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=4.0>)
    ('vars', ListWrapper([<tf.Variable 'Variable:0' shape=() dtype=float32,\
    numpy=1.0>, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>]))
    ('leaf', ...)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `root` | A `Trackable` object whose variables (including the variables of dependencies, recursively) should be saved. May be a weak reference. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `root` |     |

Methods
-------

### `children`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/trackable_view.py#L69-L87)

@classmethod

Returns all child trackables attached to obj.

|     |     |
| --- | --- |
| Args |     |
| `obj` | A `Trackable` object. |
| `save_type` | A string, can be 'savedmodel' or 'checkpoint'. |
| `**kwargs` | kwargs to use when retrieving the object's children. |

|     |
| --- |
| Returns |     |
| Dictionary of all children attached to the object with name to trackable. |     |

### `descendants`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/trackable_view.py#L98-L100)

descendants()

Returns a list of all nodes from self.root using a breadth first traversal.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.