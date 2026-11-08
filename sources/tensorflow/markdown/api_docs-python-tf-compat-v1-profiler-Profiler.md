[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fprofiler%2FProfiler&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#methods)
    *   [add\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#add_step)
        
    *   [advise](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#advise)
        
    *   [profile\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_graph)
        
    *   [profile\_name\_scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_name_scope)
        
    *   [profile\_operations](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_operations)
        
    *   [profile\_python](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_python)
        
    *   [serialize\_to\_string](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#serialize_to_string)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.profiler.Profiler Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#methods)
    *   [add\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#add_step)
        
    *   [advise](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#advise)
        
    *   [profile\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_graph)
        
    *   [profile\_name\_scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_name_scope)
        
    *   [profile\_operations](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_operations)
        
    *   [profile\_python](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#profile_python)
        
    *   [serialize\_to\_string](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/Profiler#serialize_to_string)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L121-L307)

TensorFlow multi-step profiler.

tf.compat.v1.profiler.Profiler(
        graph=None, op_log=None
    )

Typical use case:
      # Currently we are only allowed to create 1 profiler per process.
      profiler = Profiler(sess.graph)
    
      for i in range(total_steps):
        if i % 10000 == 0:
          run_meta = tf.compat.v1.RunMetadata()
          _ = sess.run(...,
                       options=tf.compat.v1.RunOptions(
                           trace_level=tf.RunOptions.FULL_TRACE),
                       run_metadata=run_meta)
          profiler.add_step(i, run_meta)
    
          # Profile the parameters of your model.
          profiler.profile_name_scope(options=(option_builder.ProfileOptionBuilder
              .trainable_variables_parameter()))
    
          # Or profile the timing of your model operations.
          opts = option_builder.ProfileOptionBuilder.time_and_memory()
          profiler.profile_operations(options=opts)
    
          # Or you can generate a timeline:
          opts = (option_builder.ProfileOptionBuilder(
                  option_builder.ProfileOptionBuilder.time_and_memory())
                  .with_step(i)
                  .with_timeline_output(filename).build())
          profiler.profile_graph(options=opts)
        else:
          _ = sess.run(...)
      # Auto detect problems and generate advice.
      profiler.advise()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | tf.Graph. If None and eager execution is not enabled, use default graph. |
| `op_log` | optional. tensorflow::tfprof::OpLogProto proto. Used to define extra op types. |

Methods
-------

### `add_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L183-L199)

add_step(
        step, run_meta
    )

Add statistics of a step.

|     |     |
| --- | --- |
| Args |     |
| `step` | int, An id used to group one or more different `run_meta` together. When profiling with the profile\_xxx APIs, user can use the `step` id in the `options` to profile these `run_meta` together. |
| `run_meta` | RunMetadata proto that contains statistics of a session run. |

### `advise`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L279-L292)

advise(
        options
    )

Automatically detect problems and generate reports.

|     |     |
| --- | --- |
| Args |     |
| `options` | A dict of options. See ALL\_ADVICE example above. |

|     |
| --- |
| Returns |     |
| An Advise proto that contains the reports from all checkers. |     |

### `profile_graph`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L261-L277)

profile_graph(
        options
    )

Profile the statistics of graph nodes, organized by dataflow graph.

|     |     |
| --- | --- |
| Args |     |
| `options` | A dict of options. See core/profiler/g3doc/options.md. |

|     |
| --- |
| Returns |     |
| a GraphNodeProto that records the results. |     |

### `profile_name_scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L243-L259)

profile_name_scope(
        options
    )

Profile the statistics of graph nodes, organized by name scope.

|     |     |
| --- | --- |
| Args |     |
| `options` | A dict of options. See core/profiler/g3doc/options.md. |

|     |
| --- |
| Returns |     |
| a GraphNodeProto that records the results. |     |

### `profile_operations`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L223-L241)

profile_operations(
        options
    )

Profile the statistics of the Operation types (e.g.

MatMul, Conv2D).

|     |     |
| --- | --- |
| Args |     |
| `options` | A dict of options. See core/profiler/g3doc/options.md. |

|     |
| --- |
| Returns |     |
| a MultiGraphNodeProto that records the results. |     |

### `profile_python`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L201-L221)

profile_python(
        options
    )

Profile the statistics of the Python codes.

By default, it shows the call stack from root. To avoid redundant output, you may use options to filter as below options\['show\_name\_regexes'\] = \['._my\_code.py._'\]

|     |     |
| --- | --- |
| Args |     |
| `options` | A dict of options. See core/profiler/g3doc/options.md. |

|     |
| --- |
| Returns |     |
| a MultiGraphNodeProto that records the results. |     |

### `serialize_to_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L294-L303)

serialize_to_string()

Serialize the ProfileProto to a binary string.

Users can write it to file for offline analysis by tfprof commandline or graphical interface.

|     |
| --- |
| Returns |     |
| ProfileProto binary string. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.