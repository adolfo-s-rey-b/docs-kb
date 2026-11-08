[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2FLooperThread&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#methods)
    *   [getName](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#getName)
        
    *   [isDaemon](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#isDaemon)
        
    *   [is\_alive](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#is_alive)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#join)
        
    *   [loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#loop)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#run)
        
    *   [run\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#run_loop)
        
    *   [setDaemon](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#setDaemon)
        
    *   [setName](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#setName)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#start)
        
    *   [start\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#start_loop)
        
    *   [stop\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#stop_loop)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.LooperThread Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#methods)
    *   [getName](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#getName)
        
    *   [isDaemon](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#isDaemon)
        
    *   [is\_alive](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#is_alive)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#join)
        
    *   [loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#loop)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#run)
        
    *   [run\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#run_loop)
        
    *   [setDaemon](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#setDaemon)
        
    *   [setName](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#setName)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#start)
        
    *   [start\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#start_loop)
        
    *   [stop\_loop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/LooperThread#stop_loop)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L409-L507)

A thread that runs code repeatedly, optionally on a timer.

tf.compat.v1.train.LooperThread(
        coord, timer_interval_secs, target=None, args=None, kwargs=None
    )

This thread class is intended to be used with a `Coordinator`. It repeatedly runs code specified either as `target` and `args` or by the `run_loop()` method.

Before each run the thread checks if the coordinator has requested stop. In that case the looper thread terminates immediately.

If the code being run raises an exception, that exception is reported to the coordinator and the thread terminates. The coordinator will then request all the other threads it coordinates to stop.

You typically pass looper threads to the supervisor `Join()` method.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `coord` | A Coordinator. |
| `timer_interval_secs` | Time boundaries at which to call Run(), or None if it should be called back to back. |
| `target` | Optional callable object that will be executed in the thread. |
| `args` | Optional arguments to pass to `target` when calling it. |
| `kwargs` | Optional keyword arguments to pass to `target` when calling it. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If one of the arguments is invalid. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `daemon` | A boolean value indicating whether this thread is a daemon thread.<br><br>This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.<br><br>The entire Python program exits when only daemon threads are left. |
| `ident` | Thread identifier of this thread or None if it has not been started.<br><br>This is a nonzero integer. See the get\_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited. |
| `name` | A string used for identification purposes only.<br><br>It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor. |
| `native_id` | Native integral thread ID of this thread, or None if it has not been started.<br><br>This is a non-negative integer. See the get\_native\_id() function. This represents the Thread ID as reported by the kernel. |

Methods
-------

### `getName`

getName()

Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.

### `isDaemon`

isDaemon()

Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.

### `is_alive`

is_alive()

Return whether the thread is alive.

This method returns True just before the run() method starts until just after the run() method terminates. See also the module function enumerate().

### `join`

join(
        timeout=None
    )

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is called terminates -- either normally or through an unhandled exception or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As join() always returns None, you must call is\_alive() after join() to decide whether a timeout happened -- if the thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to join() a thread before it has been started and attempts to do so raises the same exception.

### `loop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L457-L479)

@staticmethod

Start a LooperThread that calls a function periodically.

If `timer_interval_secs` is None the thread calls `target(args)` repeatedly. Otherwise `target(args)` is called every `timer_interval_secs` seconds. The thread terminates when a stop of the coordinator is requested.

|     |     |
| --- | --- |
| Args |     |
| `coord` | A Coordinator. |
| `timer_interval_secs` | Number. Time boundaries at which to call `target`. |
| `target` | A callable object. |
| `args` | Optional arguments to pass to `target` when calling it. |
| `kwargs` | Optional keyword arguments to pass to `target` when calling it. |

|     |
| --- |
| Returns |     |
| The started thread. |     |

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L481-L494)

run()

Method representing the thread's activity.

You may override this method in a subclass. The standard run() method invokes the callable object passed to the object's constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

### `run_loop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L504-L507)

run_loop()

Called at 'timer\_interval\_secs' boundaries.

### `setDaemon`

setDaemon(
        daemonic
    )

Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.

### `setName`

setName(
        name
    )

Set the name string for this thread.

This method is deprecated, use the name attribute instead.

### `start`

start()

Start the thread's activity.

It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the same thread object.

### `start_loop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L496-L498)

start_loop()

Called when the thread starts.

### `stop_loop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/coordinator.py#L500-L502)

stop_loop()

Called when the thread stops.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.