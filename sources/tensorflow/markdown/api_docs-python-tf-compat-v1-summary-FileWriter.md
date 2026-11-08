[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#methods)
    *   [add\_event](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_event)
        
    *   [add\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_graph)
        
    *   [add\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_meta_graph)
        
    *   [add\_run\_metadata](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_run_metadata)
        
    *   [add\_session\_log](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_session_log)
        
    *   [add\_summary](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_summary)
        
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#flush)
        
    *   [get\_logdir](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#get_logdir)
        
    *   [reopen](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#reopen)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.FileWriter Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#methods)
    *   [add\_event](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_event)
        
    *   [add\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_graph)
        
    *   [add\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_meta_graph)
        
    *   [add\_run\_metadata](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_run_metadata)
        
    *   [add\_session\_log](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_session_log)
        
    *   [add\_summary](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#add_summary)
        
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#close)
        
    *   [flush](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#flush)
        
    *   [get\_logdir](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#get_logdir)
        
    *   [reopen](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#reopen)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/FileWriter#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L278-L483)

Writes `Summary` protocol buffers to event files.

tf.compat.v1.summary.FileWriter(
        logdir,
        graph=None,
        max_queue=10,
        flush_secs=120,
        graph_def=None,
        filename_suffix=None,
        session=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, please use [`tf.summary.create_file_writer`](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer)
 instead for summary management. To specify the summary step, you can manage the context with [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
, which is returned by [`tf.summary.create_file_writer()`](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer)
. Or, you can also use the `step` argument of summary functions such as [`tf.summary.histogram`](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
. See the usage example shown below.

For a comprehensive [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary)
 migration guide, please follow [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `logdir` | `logdir` | \-  |
| `graph` | Not supported | \-  |
| `max_queue` | `max_queue` | \-  |
| `flush_secs` | `flush_millis` | The unit of time is changed from seconds to milliseconds. |
| `graph_def` | Not supported | \-  |
| `filename_suffix` | `filename_suffix` | \-  |
| `name` | `name` | \-  |

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

The `FileWriter` class provides a mechanism to create an event file in a given directory and add summaries and events to it. The class updates the file contents asynchronously. This allows a training program to call methods to add data to the file directly from the training loop, without slowing down training.

When constructed with a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 parameter, a `FileWriter` instead forms a compatibility layer over new graph-based summaries to facilitate the use of new summary writing with pre-existing code that expects a `FileWriter` instance.

This class is not thread-safe.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logdir` | A string. Directory where event file will be written. |
| `graph` | A `Graph` object, such as `sess.graph`. |
| `max_queue` | Integer. Size of the queue for pending events and summaries. |
| `flush_secs` | Number. How often, in seconds, to flush the pending events and summaries to disk. |
| `graph_def` | DEPRECATED: Use the `graph` argument instead. |
| `filename_suffix` | A string. Every event file's name is suffixed with `suffix`. |
| `session` | A [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br> object. See details above. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If called with eager execution enabled. |

Methods
-------

### `add_event`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L446-L453)

add_event(
        event
    )

Adds an event to the event file.

|     |     |
| --- | --- |
| Args |     |
| `event` | An `Event` protocol buffer. |

### `add_graph`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L159-L210)

add_graph(
        graph, global_step=None, graph_def=None
    )

Adds a `Graph` to the event file.

The graph described by the protocol buffer will be displayed by TensorBoard. Most users pass a graph in the constructor instead.

|     |     |
| --- | --- |
| Args |     |
| `graph` | A `Graph` object, such as `sess.graph`. |
| `global_step` | Number. Optional global step counter to record with the graph. |
| `graph_def` | DEPRECATED. Use the `graph` parameter instead. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If both graph and graph\_def are passed to the method. |

### `add_meta_graph`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L225-L245)

add_meta_graph(
        meta_graph_def, global_step=None
    )

Adds a `MetaGraphDef` to the event file.

The `MetaGraphDef` allows running the given graph via `saver.import_meta_graph()`.

|     |     |
| --- | --- |
| Args |     |
| `meta_graph_def` | A `MetaGraphDef` object, often as returned by `saver.export_meta_graph()`. |
| `global_step` | Number. Optional global step counter to record with the graph. |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If both `meta_graph_def` is not an instance of `MetaGraphDef`. |

### `add_run_metadata`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L247-L269)

add_run_metadata(
        run_metadata, tag, global_step=None
    )

Adds a metadata information for a single session.run() call.

|     |     |
| --- | --- |
| Args |     |
| `run_metadata` | A `RunMetadata` protobuf object. |
| `tag` | The tag name for this metadata. |
| `global_step` | Number. Optional global step counter to record with the StepStats. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the provided tag was already used for this type of event. |

### `add_session_log`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L140-L152)

add_session_log(
        session_log, global_step=None
    )

Adds a `SessionLog` protocol buffer to the event file.

This method wraps the provided session in an `Event` protocol buffer and adds it to the event file.

|     |     |
| --- | --- |
| Args |     |
| `session_log` | A `SessionLog` protocol buffer. |
| `global_step` | Number. Optional global step value to record with the summary. |

### `add_summary`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L97-L138)

add_summary(
        summary, global_step=None
    )

Adds a `Summary` protocol buffer to the event file.

This method wraps the provided summary in an `Event` protocol buffer and adds it to the event file.

You can pass the result of evaluating any summary op, using `tf.Session.run` or [`tf.Tensor.eval`](https://www.tensorflow.org/api_docs/python/tf/Tensor#eval)
, to this function. Alternatively, you can pass a [`tf.compat.v1.Summary`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Summary)
 protocol buffer that you populate with your own data. The latter is commonly done to report evaluation results in event files.

|     |     |
| --- | --- |
| Args |     |
| `summary` | A `Summary` protocol buffer, optionally serialized as a string. |
| `global_step` | Number. Optional global step value to record with the summary. |

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L466-L472)

close()

Flushes the event file to disk and close the file.

Call this method when you do not need the summary writer anymore.

### `flush`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L455-L464)

flush()

Flushes the event file to disk.

Call this method to make sure that all pending events have been written to disk.

### `get_logdir`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L432-L434)

get_logdir()

Returns the directory where event file will be written.

### `reopen`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L474-L483)

reopen()

Reopens the EventFileWriter.

Can be called after `close()` to add more events in the same directory. The events will go into a new events file.

Does nothing if the EventFileWriter was not closed.

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L424-L426)

__enter__()

Make usable with "with" statement.

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/writer/writer.py#L428-L430)

__exit__(
        unused_type, unused_value, unused_traceback
    )

Make usable with "with" statement.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.