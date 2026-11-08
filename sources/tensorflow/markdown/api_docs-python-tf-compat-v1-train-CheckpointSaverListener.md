[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#methods)
    *   [after\_save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#after_save)
        
    *   [before\_save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#before_save)
        
    *   [begin](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#begin)
        
    *   [end](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#end)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.CheckpointSaverListener Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#methods)
    *   [after\_save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#after_save)
        
    *   [before\_save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#before_save)
        
    *   [begin](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#begin)
        
    *   [end](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/CheckpointSaverListener#end)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L456-L520)

Interface for listeners that take action before or after checkpoint save.

`CheckpointSaverListener` triggers only in steps when `CheckpointSaverHook` is triggered, and provides callbacks at the following points:

*   before using the session
*   before each call to `Saver.save()`
*   after each call to `Saver.save()`
*   at the end of session

To use a listener, implement a class and pass the listener to a `CheckpointSaverHook`, as in this example:

class ExampleCheckpointSaverListener(CheckpointSaverListener):
      def begin(self):
        # You can add ops to the graph here.
        print('Starting the session.')
        self.your_tensor = ...
    
      def before_save(self, session, global_step_value):
        print('About to write a checkpoint')
    
      def after_save(self, session, global_step_value):
        print('Done writing checkpoint.')
        if decided_to_stop_training():
          return True
    
      def end(self, session, global_step_value):
        print('Done with the session.')
    
    ...
    listener = ExampleCheckpointSaverListener()
    saver_hook = tf.estimator.CheckpointSaverHook(
        checkpoint_dir, listeners=[listener])
    with
    tf.compat.v1.train.MonitoredTrainingSession(chief_only_hooks=[saver_hook]):
      ...

A `CheckpointSaverListener` may simply take some action after every checkpoint save. It is also possible for the listener to use its own schedule to act less frequently, e.g. based on global\_step\_value. In this case, implementors should implement the `end()` method to handle actions related to the last checkpoint save. But the listener should not act twice if `after_save()` already handled this last checkpoint save.

A `CheckpointSaverListener` can request training to be stopped, by returning True in `after_save`. Please note that, in replicated distributed training setting, only `chief` should use this behavior. Otherwise each worker will do their own evaluation, which may be wasteful of resources.

Methods
-------

### `after_save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L516-L517)

after_save(
        session, global_step_value
    )

### `before_save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L513-L514)

before_save(
        session, global_step_value
    )

### `begin`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L510-L511)

begin()

### `end`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L519-L520)

end(
        session, global_step_value
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.