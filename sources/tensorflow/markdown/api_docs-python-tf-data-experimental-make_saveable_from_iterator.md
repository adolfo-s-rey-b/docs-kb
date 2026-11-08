[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.make\_saveable\_from\_iterator Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/iterator_ops.py#L38-L97)

Returns a SaveableObject for saving/restoring iterator state using Saver. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.make_saveable_from_iterator`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator)

tf.data.experimental.make_saveable_from_iterator(
        iterator, external_state_policy=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `iterator` | Iterator. |
| `external_state_policy` | A string that identifies how to handle input pipelines that depend on external state. Possible values are 'ignore': The external state is silently ignored. 'warn': The external state is ignored, logging a warning. 'fail': The operation fails upon encountering external state. By default we set it to 'fail'. |

|     |
| --- |
| Returns<br>------- |     |
| A SaveableObject for saving/restoring iterator state using Saver. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If iterator does not support checkpointing. |
| `ValueError` | If `external_state_policy` is not one of 'warn', 'ignore' or 'fail'. |

#### For example:

with tf.Graph().as_default():
      ds = tf.data.Dataset.range(10)
      iterator = ds.make_initializable_iterator()
      # Build the iterator SaveableObject.
      saveable_obj = tf.data.experimental.make_saveable_from_iterator(iterator)
      # Add the SaveableObject to the SAVEABLE_OBJECTS collection so
      # it can be automatically saved using Saver.
      tf.compat.v1.add_to_collection(tf.GraphKeys.SAVEABLE_OBJECTS, saveable_obj)
      saver = tf.compat.v1.train.Saver()
    
      while continue_training:
        ... Perform training ...
        if should_save_checkpoint:
          saver.save()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.