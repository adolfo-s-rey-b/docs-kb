[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage:](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#methods)
    *   [prepare\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#prepare_session)
        
    *   [recover\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#recover_session)
        
    *   [wait\_for\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#wait_for_session)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SessionManager Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Usage:](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#methods)
    *   [prepare\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#prepare_session)
        
    *   [recover\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#recover_session)
        
    *   [wait\_for\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionManager#wait_for_session)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_manager.py#L74-L552)

Training helper that restores from checkpoint and creates session.

tf.compat.v1.train.SessionManager(
        local_init_op: tf.Operation = None,
        ready_op: tf.Operation = None,
        ready_for_local_init_op: tf.Operation = None,
        graph: tf.Graph = None,
        recovery_wait_secs=30,
        local_init_run_options: 'distribute_lib.RunOptions' = None,
        local_init_feed_dict=None
    )

This class is a small wrapper that takes care of session creation and checkpoint recovery. It also provides functions that to facilitate coordination among multiple training threads or processes.

*   Checkpointing trained variables as the training progresses.
*   Initializing variables on startup, restoring them from the most recent checkpoint after a crash, or wait for checkpoints to become available.

### Usage:

with tf.Graph().as_default():
       ...add operations to the graph...
      # Create a SessionManager that will checkpoint the model in '/tmp/mydir'.
      sm = SessionManager()
      sess = sm.prepare_session(master, init_op, saver, checkpoint_dir)
      # Use the session to train the graph.
      while True:
        sess.run(<my_train_op>)

`prepare_session()` initializes or restores a model. It requires `init_op` and `saver` as an argument.

A second process could wait for the model to be ready by doing the following:

with tf.Graph().as_default():
       ...add operations to the graph...
      # Create a SessionManager that will wait for the model to become ready.
      sm = SessionManager()
      sess = sm.wait_for_session(master)
      # Use the session to train the graph.
      while True:
        sess.run(<my_train_op>)

`wait_for_session()` waits for a model to be initialized by other processes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `local_init_op` | An `Operation` run immediately after session creation. Usually used to initialize tables and local variables. |
| `ready_op` | An `Operation` to check if the model is initialized. |
| `ready_for_local_init_op` | An `Operation` to check if the model is ready to run local\_init\_op. |
| `graph` | The `Graph` that the model will use. |
| `recovery_wait_secs` | Seconds between checks for the model to be ready. |
| `local_init_run_options` | RunOptions to be passed to session.run when executing the local\_init\_op. |
| `local_init_feed_dict` | Optional session feed dictionary to use when running the local\_init\_op. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If ready\_for\_local\_init\_op is not None but local\_init\_op is None |

Methods
-------

### `prepare_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_manager.py#L259-L351)

prepare_session(
        master: str,
        init_op: tf.Operation = None,
        saver: tf.compat.v1.train.Saver = None,
        checkpoint_dir: str = None,
        checkpoint_filename_with_path: str = None,
        wait_for_checkpoint=False,
        max_wait_secs=7200,
        config=None,
        init_feed_dict=None,
        init_fn=None
    ) -> tf.compat.v1.Session

Creates a `Session`. Makes sure the model is ready to be used.

Creates a `Session` on 'master'. If a `saver` object is passed in, and `checkpoint_dir` points to a directory containing valid checkpoint files, then it will try to recover the model from checkpoint. If no checkpoint files are available, and `wait_for_checkpoint` is `True`, then the process would check every `recovery_wait_secs`, up to `max_wait_secs`, for recovery to succeed.

If the model cannot be recovered successfully then it is initialized by running the `init_op` and calling `init_fn` if they are provided. The `local_init_op` is also run after init\_op and init\_fn, regardless of whether the model was recovered successfully, but only if `ready_for_local_init_op` passes.

If the model is recovered from a checkpoint it is assumed that all global variables have been initialized, in particular neither `init_op` nor `init_fn` will be executed.

It is an error if the model cannot be recovered and no `init_op` or `init_fn` or `local_init_op` are passed.

|     |     |
| --- | --- |
| Args |     |
| `master` | `String` representation of the TensorFlow master to use. |
| `init_op` | Optional `Operation` used to initialize the model. |
| `saver` | A `Saver` object used to restore a model. |
| `checkpoint_dir` | Path to the checkpoint files. The latest checkpoint in the dir will be used to restore. |
| `checkpoint_filename_with_path` | Full file name path to the checkpoint file. |
| `wait_for_checkpoint` | Whether to wait for checkpoint to become available. |
| `max_wait_secs` | Maximum time to wait for checkpoints to become available. |
| `config` | Optional `ConfigProto` proto used to configure the session. |
| `init_feed_dict` | Optional dictionary that maps `Tensor` objects to feed values. This feed dictionary is passed to the session `run()` call when running the init op. |
| `init_fn` | Optional callable used to initialize the model. Called after the optional `init_op` is called. The callable must accept one argument, the session being initialized. |

|     |
| --- |
| Returns |     |
| A `Session` object that can be used to drive the model. |     |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If the model cannot be initialized or recovered. |
| `ValueError` | If both checkpoint\_dir and checkpoint\_filename\_with\_path are set. |

### `recover_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_manager.py#L353-L417)

recover_session(
        master: str,
        saver: tf.compat.v1.train.Saver = None,
        checkpoint_dir: str = None,
        checkpoint_filename_with_path: str = None,
        wait_for_checkpoint=False,
        max_wait_secs=7200,
        config=None
    ) -> Tuple[tf.compat.v1.Session, bool]

Creates a `Session`, recovering if possible.

Creates a new session on 'master'. If the session is not initialized and can be recovered from a checkpoint, recover it.

|     |     |
| --- | --- |
| Args |     |
| `master` | `String` representation of the TensorFlow master to use. |
| `saver` | A `Saver` object used to restore a model. |
| `checkpoint_dir` | Path to the checkpoint files. The latest checkpoint in the dir will be used to restore. |
| `checkpoint_filename_with_path` | Full file name path to the checkpoint file. |
| `wait_for_checkpoint` | Whether to wait for checkpoint to become available. |
| `max_wait_secs` | Maximum time to wait for checkpoints to become available. |
| `config` | Optional `ConfigProto` proto used to configure the session. |

|     |
| --- |
| Returns |     |
| A pair (sess, initialized) where 'initialized' is `True` if the session could be recovered and initialized, `False` otherwise. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If both checkpoint\_dir and checkpoint\_filename\_with\_path are set. |

### `wait_for_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_manager.py#L419-L478)

wait_for_session(
        master: str, config=None, max_wait_secs=float('Inf')
    ) -> Optional[tf.compat.v1.Session]

Creates a new `Session` and waits for model to be ready.

Creates a new `Session` on 'master'. Waits for the model to be initialized or recovered from a checkpoint. It's expected that another thread or process will make the model ready, and that this is intended to be used by threads/processes that participate in a distributed training configuration where a different thread/process is responsible for initializing or recovering the model being trained.

|     |     |
| --- | --- |
| Args |     |
| `master` | `String` representation of the TensorFlow master to use. |
| `config` | Optional ConfigProto proto used to configure the session. |
| `max_wait_secs` | Maximum time to wait for the session to become available. |

|     |
| --- |
| Returns |     |
| A `Session`. May be None if the operation exceeds the timeout specified by config.operation\_timeout\_in\_ms. |     |

|     |     |
| --- | --- |
| Raises |     |
| `tf.DeadlineExceededError` | if the session is not available after max\_wait\_secs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.