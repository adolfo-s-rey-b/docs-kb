[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#methods)
    *   [children](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#children)
        
    *   [descendants](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#descendants)
        
    *   [diff](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#diff)
        
    *   [match](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#match)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.CheckpointView Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#methods)
    *   [children](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#children)
        
    *   [descendants](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#descendants)
        
    *   [diff](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#diff)
        
    *   [match](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#match)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_view.py#L28-L301)

Gathers and serializes a checkpoint view.

tf.train.CheckpointView(
        save_path
    )

This is for loading specific portions of a module from a checkpoint, and be able to compare two modules by matching components.

#### Example usage:

    class SimpleModule(tf.Module):

    root = SimpleModule(name="root")

Pass `node_id=0` to [`tf.train.CheckpointView.children()`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#children)
 to get the dictionary of all children directly linked to the checkpoint root.

    for name, node_id in checkpoint_view.children(0).items():

|     |     |
| --- | --- |
| Args<br>---- |     |
| `save_path` | The path to the checkpoint. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the save\_path does not lead to a TF2 checkpoint. |

Methods
-------

### `children`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_view.py#L88-L100)

children(
        node_id
    )

Returns all child trackables attached to obj.

|     |     |
| --- | --- |
| Args |     |
| `node_id` | Id of the node to return its children. |

|     |
| --- |
| Returns |     |
| Dictionary of all children attached to the object with name to node\_id. |     |

### `descendants`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_view.py#L102-L105)

descendants()

Returns a list of trackables by node\_id attached to obj.

### `diff`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_view.py#L216-L301)

diff(
        obj
    )

Returns diff between CheckpointView and Trackable.

This method is intended to be used to compare the object stored in a checkpoint vs a live model in Python. For example, if checkpoint restoration fails the `assert_consumed()` or `assert_existing_objects_matched()` checks, you can use this to list out the objects/checkpoint nodes which were not restored.

#### Example Usage:

    class SimpleModule(tf.Module):

    root = SimpleModule(name="root")

    root2 = SimpleModule(name="root")

Pass `node_id=0` to [`tf.train.CheckpointView.children()`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#children)
 to get the dictionary of all children directly linked to the checkpoint root.

    checkpoint_view_diff = checkpoint_view.diff(root2)

    only_in_checkpoint_view = checkpoint_view_diff[1]

    only_in_trackable = checkpoint_view_diff[2]

|     |     |
| --- | --- |
| Args |     |
| `obj` | `Trackable` root. |

|     |
| --- |
| Returns |     |
| Tuple of (<br><br>*   Overlaps: Dictionary containing all overlapping trackables that maps `node_id` to `Trackable`, same as CheckpointView.match().<br>*   Only in CheckpointView: List of `node_id` that only exist in CheckpointView.<br>*   Only in Trackable: List of `Trackable` that only exist in Trackable. ) |     |

### `match`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_view.py#L130-L214)

match(
        obj
    )

Returns all matching trackables between CheckpointView and Trackable.

Matching trackables represents trackables with the same name and position in graph.

|     |     |
| --- | --- |
| Args |     |
| `obj` | `Trackable` root. |

|     |
| --- |
| Returns |     |
| Dictionary containing all overlapping trackables that maps `node_id` to `Trackable`. |     |

#### Example usage:

    class SimpleModule(tf.Module):

    root = SimpleModule(name="root")

    root2 = SimpleModule(name="root")

Pass `node_id=0` to [`tf.train.CheckpointView.children()`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView#children)
 to get the dictionary of all children directly linked to the checkpoint root.

    checkpoint_view_match = checkpoint_view.match(root2).items()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.