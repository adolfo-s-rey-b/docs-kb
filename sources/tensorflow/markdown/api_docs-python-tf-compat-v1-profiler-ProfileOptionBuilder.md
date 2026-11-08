[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#methods)
    *   [account\_displayed\_op\_only](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#account_displayed_op_only)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#build)
        
    *   [float\_operation](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#float_operation)
        
    *   [order\_by](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#order_by)
        
    *   [select](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#select)
        
    *   [time\_and\_memory](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#time_and_memory)
        
    *   [trainable\_variables\_parameter](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#trainable_variables_parameter)
        
    *   [with\_accounted\_types](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_accounted_types)
        
    *   [with\_empty\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_empty_output)
        
    *   [with\_file\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_file_output)
        
    *   [with\_max\_depth](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_max_depth)
        
    *   [with\_min\_execution\_time](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_execution_time)
        
    *   [with\_min\_float\_operations](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_float_operations)
        
    *   [with\_min\_memory](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_memory)
        
    *   [with\_min\_occurrence](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_occurrence)
        
    *   [with\_min\_parameters](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_parameters)
        
    *   [with\_node\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_node_names)
        
    *   [with\_pprof\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_pprof_output)
        
    *   [with\_stdout\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_stdout_output)
        
    *   [with\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_step)
        
    *   [with\_timeline\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_timeline_output)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.profiler.ProfileOptionBuilder Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#methods)
    *   [account\_displayed\_op\_only](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#account_displayed_op_only)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#build)
        
    *   [float\_operation](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#float_operation)
        
    *   [order\_by](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#order_by)
        
    *   [select](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#select)
        
    *   [time\_and\_memory](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#time_and_memory)
        
    *   [trainable\_variables\_parameter](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#trainable_variables_parameter)
        
    *   [with\_accounted\_types](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_accounted_types)
        
    *   [with\_empty\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_empty_output)
        
    *   [with\_file\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_file_output)
        
    *   [with\_max\_depth](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_max_depth)
        
    *   [with\_min\_execution\_time](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_execution_time)
        
    *   [with\_min\_float\_operations](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_float_operations)
        
    *   [with\_min\_memory](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_memory)
        
    *   [with\_min\_occurrence](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_occurrence)
        
    *   [with\_min\_parameters](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_min_parameters)
        
    *   [with\_node\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_node_names)
        
    *   [with\_pprof\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_pprof_output)
        
    *   [with\_stdout\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_stdout_output)
        
    *   [with\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_step)
        
    *   [with\_timeline\_output](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/ProfileOptionBuilder#with_timeline_output)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L22-L461)

Option Builder for Profiling API.

tf.compat.v1.profiler.ProfileOptionBuilder(
        options=None
    )

For tutorial on the options, see [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md)

# Users can use pre-built options:
    opts = (
        tf.profiler.ProfileOptionBuilder.trainable_variables_parameter())
    
    # Or, build your own options:
    opts = (tf.compat.v1.profiler.ProfileOptionBuilder()
        .with_max_depth(10)
        .with_min_micros(1000)
        .select(['accelerator_micros'])
        .with_stdout_output()
        .build()
    
    # Or customize the pre-built options:
    opts = (tf.compat.v1.profiler.ProfileOptionBuilder(
        tf.profiler.ProfileOptionBuilder.time_and_memory())
        .with_displaying_options(show_name_regexes=['.*rnn.*'])
        .build())
    
    # Finally, profiling with the options:
    _ = tf.compat.v1.profiler.profile(tf.compat.v1.get_default_graph(),
                            run_meta=run_meta,
                            cmd='scope',
                            options=opts)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `options` | Optional initial option dict to start with. |

Methods
-------

### `account_displayed_op_only`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L368-L381)

account_displayed_op_only(
        is_true
    )

Whether only account the statistics of displayed profiler nodes.

|     |     |
| --- | --- |
| Args |     |
| `is_true` | If true, only account statistics of nodes eventually displayed by the outputs. Otherwise, a node's statistics are accounted by its parents as long as it's types match 'account\_type\_regexes', even if it is hidden from the output, say, by hide\_name\_regexes. |

|     |
| --- |
| Returns |     |
| self |     |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L189-L195)

build()

Build a profiling option.

|     |
| --- |
| Returns |     |
| A dict of profiling options. |     |

### `float_operation`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L110-L137)

@staticmethod

Options used to profile float operations.

Please see [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile\_model\_architecture.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile_model_architecture.md)
 on the caveats of calculating float operations.

|     |
| --- |
| Returns |     |
| A dict of profiling options. |     |

### `order_by`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L417-L431)

order_by(
        attribute
    )

Order the displayed profiler nodes based on a attribute.

Supported attribute includes micros, bytes, occurrence, params, etc. [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md)

|     |     |
| --- | --- |
| Args |     |
| `attribute` | An attribute the profiler node has. |

|     |
| --- |
| Returns |     |
| self |     |

### `select`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L433-L447)

select(
        attributes
    )

Select the attributes to display.

See [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md)
 for supported attributes.

|     |     |
| --- | --- |
| Args |     |
| `attributes` | A list of attribute the profiler node has. |

|     |
| --- |
| Returns |     |
| self |     |

### `time_and_memory`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L139-L187)

@staticmethod

Show operation time and memory consumptions.

|     |     |
| --- | --- |
| Args |     |
| `min_micros` | Only show profiler nodes with execution time no less than this. It sums accelerator and cpu times. |
| `min_bytes` | Only show profiler nodes requested to allocate no less bytes than this. |
| `min_accelerator_micros` | Only show profiler nodes spend no less than this time on accelerator (e.g. GPU). |
| `min_cpu_micros` | Only show profiler nodes spend no less than this time on cpu. |
| `min_peak_bytes` | Only show profiler nodes using no less than this bytes at peak (high watermark). For profiler nodes consist of multiple graph nodes, it sums the graph nodes' peak\_bytes. |
| `min_residual_bytes` | Only show profiler nodes have no less than this bytes not being de-allocated after Compute() ends. For profiler nodes consist of multiple graph nodes, it sums the graph nodes' residual\_bytes. |
| `min_output_bytes` | Only show profiler nodes have no less than this bytes output. The output are not necessarily allocated by this profiler nodes. |

|     |
| --- |
| Returns |     |
| A dict of profiling options. |     |

### `trainable_variables_parameter`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L84-L108)

@staticmethod

Options used to profile trainable variable parameters.

Normally used together with 'scope' view.

|     |
| --- |
| Returns |     |
| A dict of profiling options. |     |

### `with_accounted_types`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L312-L332)

with_accounted_types(
        account_type_regexes
    )

Selectively counting statistics based on node types.

Here, 'types' means the profiler nodes' properties. Profiler by default consider device name (e.g. /job:xx/.../device:GPU:0) and operation type (e.g. MatMul) as profiler nodes' properties. User can also associate customized 'types' to profiler nodes through OpLogProto proto.

For example, user can select profiler nodes placed on gpu:0 with: `account_type_regexes=['.*gpu:0.*']`

If none of a node's properties match the specified regexes, the node is not displayed nor accounted.

|     |     |
| --- | --- |
| Args |     |
| `account_type_regexes` | A list of regexes specifying the types. |

|     |
| --- |
| Returns |     |
| self. |     |

### `with_empty_output`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L383-L386)

with_empty_output()

Do not generate side-effect outputs.

### `with_file_output`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L393-L396)

with_file_output(
        outfile
    )

Print the result to a file.

### `with_max_depth`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L197-L210)

with_max_depth(
        max_depth
    )

Set the maximum depth of display.

The depth depends on profiling view. For 'scope' view, it's the depth of name scope hierarchy (tree), for 'op' view, it's the number of operation types (list), etc.

|     |     |
| --- | --- |
| Args |     |
| `max_depth` | Maximum depth of the data structure to display. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_min_execution_time`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L241-L260)

with_min_execution_time(
        min_micros=0, min_accelerator_micros=0, min_cpu_micros=0
    )

Only show profiler nodes consuming no less than 'min\_micros'.

|     |     |
| --- | --- |
| Args |     |
| `min_micros` | Only show profiler nodes with execution time no less than this. It sums accelerator and cpu times. |
| `min_accelerator_micros` | Only show profiler nodes spend no less than this time on accelerator (e.g. GPU). |
| `min_cpu_micros` | Only show profiler nodes spend no less than this time on cpu. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_min_float_operations`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L295-L310)

with_min_float_operations(
        min_float_ops
    )

Only show profiler nodes consuming no less than 'min\_float\_ops'.

Please see [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile\_model\_architecture.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile_model_architecture.md)
 on the caveats of calculating float operations.

|     |     |
| --- | --- |
| Args |     |
| `min_float_ops` | Only show profiler nodes with float operations no less than this. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_min_memory`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L212-L239)

with_min_memory(
        min_bytes=0, min_peak_bytes=0, min_residual_bytes=0, min_output_bytes=0
    )

Only show profiler nodes consuming no less than 'min\_bytes'.

|     |     |
| --- | --- |
| Args |     |
| `min_bytes` | Only show profiler nodes requested to allocate no less bytes than this. |
| `min_peak_bytes` | Only show profiler nodes using no less than this bytes at peak (high watermark). For profiler nodes consist of multiple graph nodes, it sums the graph nodes' peak\_bytes. |
| `min_residual_bytes` | Only show profiler nodes have no less than this bytes not being de-allocated after Compute() ends. For profiler nodes consist of multiple graph nodes, it sums the graph nodes' residual\_bytes. |
| `min_output_bytes` | Only show profiler nodes have no less than this bytes output. The output are not necessarily allocated by this profiler nodes. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_min_occurrence`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L277-L293)

with_min_occurrence(
        min_occurrence
    )

Only show profiler nodes including no less than 'min\_occurrence' graph nodes.

A "node" means a profiler output node, which can be a python line (code view), an operation type (op view), or a graph node (graph/scope view). A python line includes all graph nodes created by that line, while an operation type includes all graph nodes of that type.

|     |     |
| --- | --- |
| Args |     |
| `min_occurrence` | Only show nodes including no less than this. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_min_parameters`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L262-L275)

with_min_parameters(
        min_params
    )

Only show profiler nodes holding no less than 'min\_params' parameters.

'Parameters' normally refers the weights of in TensorFlow variables. It reflects the 'capacity' of models.

|     |     |
| --- | --- |
| Args |     |
| `min_params` | Only show profiler nodes holding number parameters no less than this. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_node_names`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L334-L366)

with_node_names(
        start_name_regexes=None,
        show_name_regexes=None,
        hide_name_regexes=None,
        trim_name_regexes=None
    )

Regular expressions used to select profiler nodes to display.

After 'with\_accounted\_types' is evaluated, 'with\_node\_names' are evaluated as follows:

For a profile data structure, profiler first finds the profiler nodes matching 'start\_name\_regexes', and starts displaying profiler nodes from there. Then, if a node matches 'show\_name\_regexes' and doesn't match 'hide\_name\_regexes', it's displayed. If a node matches 'trim\_name\_regexes', profiler stops further searching that branch.

|     |     |
| --- | --- |
| Args |     |
| `start_name_regexes` | list of node name regexes to start displaying. |
| `show_name_regexes` | list of node names regexes to display. |
| `hide_name_regexes` | list of node\_names regexes that should be hidden. |
| `trim_name_regexes` | list of node name regexes from where to stop. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_pprof_output`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L403-L415)

with_pprof_output(
        pprof_file
    )

Generate a pprof profile gzip file.

|     |
| --- |
| To use the pprof file |     |
| pprof -png --nodecount=100 --sample\_index=1 |     |

|     |     |
| --- | --- |
| Args |     |
| `pprof_file` | filename for output, usually suffixed with .pb.gz. |

|     |
| --- |
| Returns |     |
| self. |     |

### `with_stdout_output`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L388-L391)

with_stdout_output()

Print the result to stdout.

### `with_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L449-L461)

with_step(
        step
    )

Which profile step to use for profiling.

The 'step' here refers to the step defined by `Profiler.add_step()` API.

|     |     |
| --- | --- |
| Args |     |
| `step` | When multiple steps of profiles are available, select which step's profile to use. If -1, use average of all available steps. |

|     |
| --- |
| Returns |     |
| self |     |

### `with_timeline_output`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/option_builder.py#L398-L401)

with_timeline_output(
        timeline_file
    )

Generate a timeline json file.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.