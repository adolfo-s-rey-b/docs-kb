[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.TerminationConfig Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/failure_handling.py#L74-L173)

Customization of `PreemptionCheckpointHandler` for various platforms.

tf.distribute.experimental.TerminationConfig(
        termination_watcher_fn=None, exit_fn=None, grace_period=None, save_fn=None
    )

A `TerminationConfig` can be created and passed to a [`tf.distribute.experimental.PreemptionCheckpointHandler`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler)
 to provide customization based on the platform. It can deliver three pieces of information:

*   How to decide if there is a termination event soon

The form of termination notification and how to fetch it vary across platforms. Thus `PreemptionCheckpointHandler` may take a user-defined function, `termination_watcher_fn`, and execute it repeatedly to check for termination notification. `termination_watcher_fn` should be a function that returns `True` if a termination notification is available and `False` otherwise. The function should be lightweight and non-blocking so that resources can be cleaned up properly if no termination signal is ever raised until training finishes.

*   How to exit the program

A user can configure this through the `exit_fn`, which `PreemptionCheckpointHandler` executes after saving the checkpoint to exit the training program gracefully. For [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
, a restart is necessary to reset the program's state. However, having a customized `exit_fn` may facilitate the restart and smoothen the training experience. How so? Maybe the platform has an agreement to a `RESTART_CODE` recognized as a program auto-restart signal, or maybe the user has a coordinating script that starts up the training, in which they can configure the program to auto-restart if it ever exits with this `RESTART_CODE`. In both cases, configuring the `exit_fn` to be `sys.exit(RESTART_CODE)` makes the training seamless.

*   How long does `PreemptionCheckpointHandler` have from receiving a termination event notice till the actual termination

Some platforms have a gap time as long as one hour or so. In these cases, there is the option to utilize this gap time for training as much as possible before saving a checkpoint and exiting. This can be achieved by passing the `grace_period` argument a nonzero value. Note, for a user with a grace period that is not multiple times longer than their checkpoint writing time (e.g., three times or more), we advise not to configure this argument, in which case `PreemptionCheckpointHandler` will directly save a checkpoint and exit.

**The default behavior**:

*   For Google Borg Platform:
    
    *   Automatically know how to detect preemption signal
    *   Exit with a platform-recognized restart code
    *   Save a checkpoint and exit immediately
*   For Google Cloud Platform:
    
    *   Automatically know how to detect maintenance signal.
    *   Exit with a code (User may configure this)
    *   Automatically utilized the extended training period before save and exit
*   For Other platform:
    
    *   If `termination_watcher_fn` is `None`, we will treat `signal.SIGTERM` as a termination signal.
    *   If `exit_fn` is not configured, we exit the program with an arbitrary code.
    *   If `grace_period` is not configured, we will wrap up the current training step, save a checkpoint, and exit the program as soon as we receive the termination signal.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `termination_watcher_fn` | a function to execute repeatedly that returns `True` if a preemption signal is available and False otherwise. The function cannot block until a preemption signal is available, which prevents proper cleanup of the program. A change is **NOT** recommended for users on Google Borg or Google Cloud Platform. |
| `exit_fn` | a function to execute after a checkpoint is saved and before the preemption happens. Usually, it should be in the form of `lambda: sys.exit(RESTART_CODE)`, where `RESTART_CODE` varies by platform. A change is **NOT** recommended for users on Google Borg. Users on Google Cloud Platform may configure it to use a customized `RESTART_CODE`. |
| `grace_period` | the length of time between receiving a preemption signal and the actual preemption. A change is **NOT** recommended for users on Google Borg, Google Cloud Platform, or users with a short grace period. |
| `save_fn` | an optional function letting you configure how to save a checkpoint. This is useful if you'd like to pass extra argument to [`tf.train.CheckpointManager.save`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#save)<br> or [`tf.train.Checkpoint.save`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)<br>. By default, if not configured, the API will save checkpoint without extra arguments. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.