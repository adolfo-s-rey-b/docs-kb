[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.import\_meta\_graph Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1477-L1589)

Recreates a Graph saved in a `MetaGraphDef` proto.

tf.compat.v1.train.import_meta_graph(
        meta_graph_or_file, clear_devices=False, import_scope=None, **kwargs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

This function takes a `MetaGraphDef` protocol buffer as input. If the argument is a file containing a `MetaGraphDef` protocol buffer , it constructs a protocol buffer from the file content. The function then adds all the nodes from the `graph_def` field to the current graph, recreates all the collections, and returns a saver constructed from the `saver_def` field.

In combination with `export_meta_graph()`, this function can be used to

*   Serialize a graph along with other Python objects such as `QueueRunner`, `Variable` into a `MetaGraphDef`.
    
*   Restart training from a saved graph and checkpoints.
    
*   Run inference from a saved graph and checkpoints.
    

...
    # Create a saver.
    saver = tf.compat.v1.train.Saver(...variables...)
    # Remember the training_op we want to run by adding it to a collection.
    tf.compat.v1.add_to_collection('train_op', train_op)
    sess = tf.compat.v1.Session()
    for step in range(1000000):
        sess.run(train_op)
        if step % 1000 == 0:
            # Saves checkpoint, which by default also exports a meta_graph
            # named 'my-model-global_step.meta'.
            saver.save(sess, 'my-model', global_step=step)

Later we can continue training from this saved `meta_graph` without building the model from scratch.

with tf.Session() as sess:
      new_saver =
      tf.train.import_meta_graph('my-save-dir/my-model-10000.meta')
      new_saver.restore(sess, 'my-save-dir/my-model-10000')
      # tf.get_collection() returns a list. In this example we only want
      # the first one.
      train_op = tf.get_collection('train_op')[0]
      for step in range(1000000):
        sess.run(train_op)

#### Example:

Variables, placeholders, and independent operations can also be stored, as shown in the following example.

# Saving contents and operations.
    v1 = tf.placeholder(tf.float32, name="v1")
    v2 = tf.placeholder(tf.float32, name="v2")
    v3 = tf.math.multiply(v1, v2)
    vx = tf.Variable(10.0, name="vx")
    v4 = tf.add(v3, vx, name="v4")
    saver = tf.train.Saver([vx])
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    sess.run(vx.assign(tf.add(vx, vx)))
    result = sess.run(v4, feed_dict={v1:12.0, v2:3.3})
    print(result)
    saver.save(sess, "./model_ex1")

Later this model can be restored and contents loaded.

# Restoring variables and running operations.
    saver = tf.train.import_meta_graph("./model_ex1.meta")
    sess = tf.Session()
    saver.restore(sess, "./model_ex1")
    result = sess.run("v4:0", feed_dict={"v1:0": 12.0, "v2:0": 3.3})
    print(result)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `meta_graph_or_file` | `MetaGraphDef` protocol buffer or filename (including the path) containing a `MetaGraphDef`. |
| `clear_devices` | Whether or not to clear the device field for an `Operation` or `Tensor` during import. |
| `import_scope` | Optional `string`. Name scope to add. Only used when initializing from protocol buffer. |
| `**kwargs` | Optional keyed arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A saver constructed from `saver_def` in `MetaGraphDef` or None.<br><br>A None value is returned if no variables exist in the `MetaGraphDef` (i.e., there are no variables to restore). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If called with eager execution enabled. |

eager compatibility
-------------------

Exporting/importing meta graphs is not supported. No graph exists when eager execution is enabled.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.