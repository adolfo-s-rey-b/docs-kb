[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.merge Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L611-L690)

Merges summaries.

tf.compat.v1.summary.merge(
        inputs, collections=None, name=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, this API can be omitted entirely, because in TF2 individual summary ops, like [`tf.summary.scalar()`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
, write directly to the default summary writer if one is active. Thus, it's not necessary to merge summaries or to manually add the resulting merged summary output to the writer. See the usage example shown below.

For a comprehensive [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary)
 migration guide, please follow [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
.

#### TF1 & TF2 Usage Example

TF1:

dist = tf.compat.v1.placeholder(tf.float32, [100])
    tf.compat.v1.summary.histogram(name="distribution", values=dist)
    writer = tf.compat.v1.summary.FileWriter("/tmp/tf1_summary_example")
    summaries = tf.compat.v1.summary.merge_all()
    
    sess = tf.compat.v1.Session()
    for step in range(100):
      mean_moving_normal = np.random.normal(loc=step, scale=1, size=[100])
      summ = sess.run(summaries, feed_dict={dist: mean_moving_normal})
      writer.add_summary(summ, global_step=step)

TF2:

writer = tf.summary.create_file_writer("/tmp/tf2_summary_example")
    for step in range(100):
      mean_moving_normal = np.random.normal(loc=step, scale=1, size=[100])
      with writer.as_default(step=step):
        tf.summary.histogram(name='distribution', data=mean_moving_normal)

Description
-----------

This op creates a [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
 protocol buffer that contains the union of all the values in the input summaries.

When the Op is run, it reports an `InvalidArgument` error if multiple values in the summaries to merge use the same tag.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of `string` `Tensor` objects containing serialized `Summary` protocol buffers. |
| `collections` | Optional list of graph collections keys. The new summary op is added to these collections. Defaults to `[]`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of type `string`. The serialized `Summary` protocol buffer resulting from the merging. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If called with eager mode enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.