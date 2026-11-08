Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/profiler.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/profiler.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/profiler.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/profiler.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/profiler.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/profiler.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/profiler.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/profiler.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/profiler.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/profiler.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/profiler.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/profiler.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/profiler.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/profiler.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/profiler.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/profiler.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/profiler.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/profiler.html)
[v1.13](https://docs.pytorch.org/docs/1.13/profiler.html)
[v1.12](https://docs.pytorch.org/docs/1.12/profiler.html)
[v1.11](https://docs.pytorch.org/docs/1.11/profiler.html)
[v1.10](https://docs.pytorch.org/docs/1.10/profiler.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/profiler.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/profiler.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/profiler.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/profiler.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/profiler.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/profiler.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/profiler.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/profiler.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/profiler.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/profiler.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/profiler.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/profiler.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/profiler.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/profiler.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/profiler.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/profiler.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/profiler.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/profiler.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/profiler.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/profiler.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/profiler.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/profiler.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.profiler[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch-profiler "Link to this heading")

==========================================================================================================

Created On: Dec 18, 2020 | Last Updated On: Sep 04, 2026

Overview[#](https://docs.pytorch.org/docs/2.15/profiler.html#module-torch.profiler "Link to this heading")

-----------------------------------------------------------------------------------------------------------

PyTorch Profiler is a tool that allows the collection of performance metrics during training and inference. Profiler’s context manager API can be used to better understand what model operators are the most expensive, examine their input shapes and stack traces, study device kernel activity and visualize the execution trace.

Note

An earlier version of the API in [`torch.autograd`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd "torch.autograd")
 module is considered legacy and will be deprecated.

torch.profiler.profiler.schedule(_\*_, _wait_, _warmup_, _active_, _repeat\=0_, _skip\_first\=0_, _skip\_first\_wait\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L972)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profiler.schedule "Link to this definition")

Returns a callable that can be used as profiler `schedule` argument. The profiler will skip the first `skip_first` steps, then wait for `wait` steps, then do the warmup for the next `warmup` steps, then do the active recording for the next `active` steps and then repeat the cycle starting with `wait` steps. The optional number of cycles is specified with the `repeat` parameter, the zero value means that the cycles will continue until the profiling is finished.

The `skip_first_wait` parameter controls whether the first `wait` stage should be skipped. This can be useful if a user wants to wait longer than `skip_first` between cycles, but not for the first profile. For example, if `skip_first` is 10 and `wait` is 20, the first cycle will wait 10 + 20 = 30 steps before warmup if `skip_first_wait` is zero, but will wait only 10 steps if `skip_first_wait` is non-zero. All subsequent cycles will then wait 20 steps between the last active and warmup.

Return type:

Callable

torch.profiler.profiler.supported\_activities()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L96)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profiler.supported_activities "Link to this definition")

Returns a set of supported profiler tracing activities.

Note: profiler uses CUPTI library to trace on-device CUDA kernels. In case when CUDA is enabled but CUPTI is not available, passing `ProfilerActivity.CUDA` to profiler results in using the legacy CUDA profiling code (same as in the legacy `torch.autograd.profiler`). This, in turn, results in including CUDA time in the profiler table output, but not in the JSON trace.

torch.profiler.profiler.tensorboard\_trace\_handler(_dir\_name_, _worker\_name\=None_, _use\_gzip\=False_, _use\_python\_export\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L1042)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profiler.tensorboard_trace_handler "Link to this definition")

Outputs tracing files to directory of `dir_name`, then that directory can be directly delivered to tensorboard as logdir. `worker_name` should be unique for each worker in distributed scenario, it will be set to ‘\[hostname\]\_\[pid\]’ by default.

API Reference[#](https://docs.pytorch.org/docs/2.15/profiler.html#api-reference "Link to this heading")

--------------------------------------------------------------------------------------------------------

_class_ torch.profiler.profile(_\*_, _activities\=None_, _schedule\=None_, _on\_trace\_ready\=None_, _record\_shapes\=False_, _profile\_memory\=False_, _with\_stack\=False_, _with\_flops\=False_, _with\_modules\=False_, _experimental\_config\=None_, _execution\_trace\_observer\=None_, _acc\_events\=False_, _custom\_trace\_id\_callback\=None_, _post\_processing\_timeout\_s\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L1078)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile "Link to this definition")

Profiler context manager.

Parameters:

*   **activities** (_iterable_) –
    
    list of activity groups (CPU, CUDA) to use in profiling, supported values: `torch.profiler.ProfilerActivity.CPU`, `torch.profiler.ProfilerActivity.CUDA`, `torch.profiler.ProfilerActivity.XPU`. Default value: ProfilerActivity.CPU and (when available) ProfilerActivity.CUDA or (when available) ProfilerActivity.XPU.
    
    Each item can be a `ProfilerActivity` enum (collects all default activity types for that group) or a `dict` mapping a `ProfilerActivity` to a list of individual activity type names to collect, e.g. `{ProfilerActivity.CUDA: ["GPU_MEMCPY", "CUDA_RUNTIME"]}`. An empty list (e.g. `{ProfilerActivity.CUDA: []}`) means collect nothing for that group. The same activity group must not appear more than once. See [`ProfilerActivity`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.ProfilerActivity "torch.profiler.ProfilerActivity")
     for the valid activity type names and device-specific behavior.
    
*   **schedule** (_Callable_) – callable that takes step (int) as a single parameter and returns `ProfilerAction` value that specifies the profiler action to perform at each step.
    
*   **on\_trace\_ready** (_Callable_) – callable invoked at the end of each profiling cycle (when `schedule` returns `ProfilerAction.RECORD_AND_SAVE`). Receives the [`profile`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile "torch.profiler.profile")
     instance as its only argument, typically used to export the trace (e.g. via [`export_chrome_trace()`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.export_chrome_trace "torch.profiler.profile.export_chrome_trace")
    ) or print a summary.
    
*   **record\_shapes** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – save information about operator’s input shapes.
    
*   **profile\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – track tensor memory allocation/deallocation.
    
*   **with\_stack** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – record source information (file and line number) for the ops.
    
*   **with\_flops** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – use formula to estimate the FLOPs (floating point operations) of specific operators (matrix multiplication and 2D convolution).
    
*   **with\_modules** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) –
    
    record module hierarchy (including function names) corresponding to the callstack of the op. e.g. If module A’s forward call’s module B’s forward which contains an aten::add op, then aten::add’s module hierarchy is A.B
    
    Deprecated since version \`\`with\_modules\`\`: is deprecated and will be removed in a future version. It only collects data for TorchScript models, which are themselves deprecated, and does nothing in eager mode. Use `with_stack=True`, which records `nn.Module` events for eager models.
    
*   **experimental\_config** (_\_ExperimentalConfig_) – A set of experimental options used for Kineto library features. Note, backward compatibility is not guaranteed.
    
*   **execution\_trace\_observer** (_ExecutionTraceObserver_) – A PyTorch Execution Trace Observer object. [PyTorch Execution Traces](https://arxiv.org/pdf/2305.14516.pdf)
     offer a graph based representation of AI/ML workloads and enable replay benchmarks, simulators, and emulators. When this argument is included the observer start() and stop() will be called for the same time window as PyTorch profiler. See the examples section below for a code sample.
    
*   **acc\_events** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable the accumulation of FunctionEvents across multiple profiling cycles
    
*   **post\_processing\_timeout\_s** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional timeout in seconds for post-processing profiler results. If specified, event parsing will stop after this duration and return partial results. Useful for handling large traces that may take too long to process.
    
*   **custom\_trace\_id\_callback** (_Callable__\[__\[__\]__,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _optional_) – User-supplied trace ID generator, invoked once per profiling cycle. Defaults to a random UUID; retrieve via [`get_trace_id()`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.get_trace_id "torch.profiler.profile.get_trace_id")
    .
    

Note

Use `schedule()` to generate the callable schedule. Non-default schedules are useful when profiling long training jobs and allow the user to obtain multiple traces at the different iterations of the training process. The default schedule simply records all the events continuously for the duration of the context manager.

Note

Use `tensorboard_trace_handler()` to generate result files for TensorBoard:

`on_trace_ready=torch.profiler.tensorboard_trace_handler(dir_name)`

After profiling, result files can be found in the specified directory. Use the command:

`tensorboard --logdir dir_name`

to see the results in TensorBoard. For more information, see [PyTorch Profiler TensorBoard Plugin](https://github.com/pytorch/kineto/tree/master/tb_plugin)

Note

Enabling shape and stack tracing results in additional overhead. When record\_shapes=True is specified, profiler will temporarily hold references to the tensors; that may further prevent certain optimizations that depend on the reference count and introduce extra tensor copies.

Examples:

with torch.profiler.profile(
    activities\=\[\
        torch.profiler.ProfilerActivity.CPU,\
        torch.profiler.ProfilerActivity.CUDA,\
    \]
) as p:
    code\_to\_profile()
print(p.key\_averages().table(sort\_by\="self\_cuda\_time\_total", row\_limit\=-1))

Copy to clipboard

Using the profiler’s `schedule`, `on_trace_ready` and `step` functions:

\# Non-default profiler schedule allows user to turn profiler on and off
\# on different iterations of the training loop;
\# trace\_handler is called every time a new trace becomes available
def trace\_handler(prof):
    print(
        prof.key\_averages().table(sort\_by\="self\_cuda\_time\_total", row\_limit\=-1)
    )
    \# prof.export\_chrome\_trace("/tmp/test\_trace\_" + str(prof.step\_num) + ".json")

with torch.profiler.profile(
    activities\=\[\
        torch.profiler.ProfilerActivity.CPU,\
        torch.profiler.ProfilerActivity.CUDA,\
    \],
    \# In this example with wait=1, warmup=1, active=2, repeat=1,
    \# profiler will skip the first step/iteration,
    \# start warming up on the second, record
    \# the third and the fourth iterations,
    \# after which the trace will become available
    \# and on\_trace\_ready (when set) is called;
    \# the cycle repeats starting with the next step
    schedule\=torch.profiler.schedule(wait\=1, warmup\=1, active\=2, repeat\=1),
    on\_trace\_ready\=trace\_handler,
    \# on\_trace\_ready=torch.profiler.tensorboard\_trace\_handler('./log')
    \# used when outputting for tensorboard
) as p:
    for iter in range(N):
        code\_iteration\_to\_profile(iter)
        \# send a signal to the profiler that the next iteration has started
        p.step()

Copy to clipboard

The following sample shows how to setup up an Execution Trace Observer (execution\_trace\_observer)

with torch.profiler.profile(
    ...
    execution\_trace\_observer\=(
        ExecutionTraceObserver().register\_callback("./execution\_trace.json")
    ),
) as p:
    for iter in range(N):
        code\_iteration\_to\_profile(iter)
        p.step()

Copy to clipboard

You can also refer to test\_execution\_trace\_with\_kineto() in tests/profiler/test\_profiler.py. Note: One can also pass any object satisfying the \_ITraceObserver interface.

add\_metadata(_key_, _value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L834)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.add_metadata "Link to this definition")

Adds a user defined metadata with a string key and a string value into the trace file

add\_metadata\_json(_key_, _value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L843)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.add_metadata_json "Link to this definition")

Adds a user defined metadata with a string key and a valid json value into the trace file

events()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L820)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.events "Link to this definition")

Return the list of unaggregated [`FunctionEvent`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent "torch.autograd.profiler_util.FunctionEvent")
 objects, for use in the trace callback or after profiling has finished.

export\_chrome\_trace(_path_, _use\_python\_export\=False_, _cuda\_graph\_annotations\=None_, _graph\_lanes\='none'_, _default\_stream\=7_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L637)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.export_chrome_trace "Link to this definition")

Exports the collected trace in Chrome JSON format. If kineto is enabled, only last cycle in schedule is exported.

`cuda_graph_annotations` bakes CUDA-graph kernel annotations into the trace: matching graphed work carries its annotation’s fields in `args`. Pass [`torch.cuda.graph_annotations.get_kernel_annotations()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.get_kernel_annotations.html#torch.cuda.graph_annotations.get_kernel_annotations "torch.cuda.graph_annotations.get_kernel_annotations")
 to use what [`mark_kernels()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels "torch.cuda.graph_annotations.mark_kernels")
 recorded, or any mapping in that shape – a filtered or edited copy, or one unpickled from an earlier run. An empty mapping is treated as no annotations at all. Passing it implies `use_python_export`, the export path able to inject (the `cuspy` backend does its own injection and ignores this argument).

`graph_lanes` decides whether graphed events are moved onto display lanes. `"none"` (default) leaves the trace’s stream layout alone, reporting a recorded lane as `args["annotated_stream"]` instead of acting on it. `"all"` moves each graphed event to the lane its annotation names (as `mark_stream()` records) and the rest onto `default_stream` – what a replay scattered over many hardware streams needs, at the cost of piling everything onto one lane when no annotation names a stream. A moved event keeps the stream it ran on as `args["original_stream"]`. `"all"` requires `cuda_graph_annotations` and raises without them, since on its own it would only do the collapsing half.

export\_memory\_timeline(_path_, _device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L891)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.export_memory_timeline "Link to this definition")

Export memory event information from the profiler collected tree for a given device, and export a timeline plot. There are 3 exportable files using `export_memory_timeline`, each controlled by the `path`’s suffix.

*   For an HTML compatible plot, use the suffix `.html`, and a memory timeline plot will be embedded as a PNG file in the HTML file.
    
*   For plot points consisting of `[times, [sizes by category]]`, where `times` are timestamps and `sizes` are memory usage for each category. The memory timeline plot will be saved a JSON (`.json`) or gzipped JSON (`.json.gz`) depending on the suffix.
    
*   For raw memory points, use the suffix `.raw.json.gz`. Each raw memory event will consist of `(timestamp, action, numbytes, category)`, where `action` is one of `[PREEXISTING, CREATE, INCREMENT_VERSION, DESTROY]`, and `category` is one of the enums from `torch.profiler._memory_profiler.Category`.
    

Output: Memory timeline written as gzipped JSON, JSON, or HTML.

Deprecated since version \`\`export\_memory\_timeline\`\`: is deprecated and will be removed in a future version. Please use `torch.cuda.memory._record_memory_history` and `torch.cuda.memory._export_memory_snapshot` instead.

export\_stacks(_path_, _metric\='self\_cpu\_time\_total'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L746)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.export_stacks "Link to this definition")

Save stack traces to a file

Parameters:

*   **path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – save stacks file to this location;
    
*   **metric** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – metric to use: “self\_cpu\_time\_total” or “self\_cuda\_time\_total”
    

get\_trace\_id()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L1539)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.get_trace_id "Link to this definition")

Returns the current trace ID.

key\_averages(_group\_by\_input\_shape\=False_, _group\_by\_stack\_n\=0_, _group\_by\_overload\_name\=False_, _include\_python\_functions\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L793)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.key_averages "Link to this definition")

Averages events, grouping them by operator name and (optionally) input shapes, stack and overload name.

Returns an [`EventList`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList "torch.autograd.profiler_util.EventList")
 of the aggregated events.

Note

To use shape/stack functionality make sure to set record\_shapes/with\_stack when creating profiler context manager.

preset\_metadata\_json(_key_, _value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L851)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.preset_metadata_json "Link to this definition")

Preset a user defined metadata when the profiler is not started and added into the trace file later. Metadata is in the format of a string key and a valid json value

set\_custom\_trace\_id\_callback(_callback_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L1532)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.set_custom_trace_id_callback "Link to this definition")

Set the trace ID generator. Called at the start of each cycle, so updating it between cycles yields distinct IDs per cycle.

step()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L1443)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.step "Link to this definition")

Signals the profiler that the next profiling step has started.

take\_pending\_cuspy\_export()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L735)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.take_pending_cuspy_export "Link to this definition")

Detach this cycle’s cuspy ProfilerObserver (with its unwritten window) so the deferred export can be finalized OFF the training thread (call `obs.join(force=False)` on a worker). None for non-cuspy backends.

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

toggle\_collection\_dynamic(_enable_, _activities_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L757)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.toggle_collection_dynamic "Link to this definition")

Toggle collection of activities on/off at any point of collection. Currently supports toggling Torch Ops (CPU) and CUDA activity supported in Kineto

Parameters:

**activities** (_iterable_) – list of activity groups to use in profiling, supported values: `torch.profiler.ProfilerActivity.CPU`, `torch.profiler.ProfilerActivity.CUDA`

Examples:

with torch.profiler.profile(
    activities\=\[\
        torch.profiler.ProfilerActivity.CPU,\
        torch.profiler.ProfilerActivity.CUDA,\
    \]
) as p:
    code\_to\_profile\_0()
    \# turn off collection of all CUDA activity
    p.toggle\_collection\_dynamic(
        False, \[torch.profiler.ProfilerActivity.CUDA\]
    )
    code\_to\_profile\_1()
    \# turn on collection of all CUDA activity
    p.toggle\_collection\_dynamic(
        True, \[torch.profiler.ProfilerActivity.CUDA\]
    )
    code\_to\_profile\_2()
print(p.key\_averages().table(sort\_by\="self\_cuda\_time\_total", row\_limit\=-1))

Copy to clipboard

wait\_for\_exports()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L726)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile.wait_for_exports "Link to this definition")

Block until every deferred cuspy export is written, then unregister. No-op unless the cuspy backend is active. Call on the training thread when you need the file(s) on disk; the finalize force-flushes CUPTI (safe here).

_class_ torch.profiler.ProfilerAction(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L949)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.ProfilerAction "Link to this definition")

Profiler actions that can be taken at the specified intervals.

NONE, WARMUP, RECORD, and RECORD\_AND\_SAVE are user-facing values that may be returned from a user-provided schedule. DEVICE\_STOPPED is set internally by the profiler when device collection stops early due to errors; it must not be returned from a user-provided schedule.

_class_ torch.profiler.ProfilerActivity[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.ProfilerActivity "Link to this definition")

Device kinds that the profiler supports.

Members:

> CPU : CPU events (operators, runtime, …).
> 
> XPU : Intel XPU device activity. In a fine-grained activity dict (`{ProfilerActivity.XPU: [...]}`), names that are not XPU activity types are interpreted as Intel XPU hardware metric names and enable the per-kernel scope profiler, e.g. `{ProfilerActivity.XPU: ["GpuTime", "GpuCoreClocks"]}`. The metric values are attached to each kernel as Perfetto counters. Hardware metric collection requires `ZET_ENABLE_METRICS=1` and access to the GPU performance counters (`perf_stream_paranoid`/`observation_paranoid` set to `0`). Metric names are device-specific and defined by the driver, not by PyTorch. Because a dict entry collects exactly what it lists, requesting only metrics (e.g. `{ProfilerActivity.XPU: ["GpuTime"]}`) does not also collect the default XPU activities; list the desired activity type names alongside the metrics to keep tracing them, e.g. `{ProfilerActivity.XPU: ["CONCURRENT_KERNEL", "XPU_RUNTIME", "GpuTime"]}`.
> 
> MTIA : MTIA device activity.
> 
> CUDA : CUDA kernels and runtime. To sample CUDA hardware performance counters, use `ProfilerActivityConfig` with a `PerformanceMetricsConfig` in the activity dict, e.g. `{ProfilerActivity.CUDA: ProfilerActivityConfig(profiler_configs=[PerformanceMetricsConfig(metric_names=["sm__cycles_active.avg"])])}`. Metric names are CUPTI PM sampling metrics supported by the current CUDA device. Hardware counter collection requires a Kineto build with CUPTI PM sampling support.
> 
> HPU : HPU device activity.
> 
> PrivateUse1 : PrivateUse1 backend activity.

_property_ name[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.ProfilerActivity.name "Link to this definition")

_class_ torch.profiler.CuspyConfig(_enable\_cuda\_sync\_events\=False_, _enable\_environment\_counters\=False_, _enable\_graph\_dependencies\=False_, _enable\_event\_node\_ids\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L138)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.CuspyConfig "Link to this definition")

Configure Cuspy CUDA activity collection.

CPU activity is currently required because Cuspy merges its trace with the CPU trace.

Parameters:

*   **enable\_cuda\_sync\_events** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Collect CUDA synchronization activities.
    
*   **enable\_environment\_counters** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Collect GPU environment counters.
    
*   **enable\_graph\_dependencies** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Record CUDA graph dependency edges.
    
*   **enable\_event\_node\_ids** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Associate CUDA events with CUDA graph event-record nodes.
    

_class_ torch.profiler.ProfilerActivityConfig(_activity\_types=None_, _profiler\_configs=<factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L200)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.ProfilerActivityConfig "Link to this definition")

Configure collection for an activity group.

Parameters:

*   **activity\_types** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _optional_) – Fine-grained activity types to collect. `None` collects the group’s default activity types, while an empty list collects none.
    
*   **profiler\_configs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    ) – Additional profiler configurations associated with this activity group, such as [`PerformanceMetricsConfig`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.PerformanceMetricsConfig "torch.profiler.PerformanceMetricsConfig")
     and [`CuspyConfig`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.CuspyConfig "torch.profiler.CuspyConfig")
    .
    

_class_ torch.profiler.PerformanceMetricsConfig(_metric\_names_, _sampling\_interval\_ms\=None_, _lookback\_window\_ms\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/profiler.py#L165)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.PerformanceMetricsConfig "Link to this definition")

Configure hardware performance-counter metric collection.

This configuration collects hardware counters.

Parameters:

*   **metric\_names** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – Backend-specific hardware metric names to collect.
    
*   **sampling\_interval\_ms** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – CUDA PM-sampling interval in milliseconds. Defaults to 1 millisecond.
    
*   **lookback\_window\_ms** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – CUDA PM-sampling look-back window in milliseconds. This bounds the recent sample history retained for decoding; the capacity is the look-back window divided by the sampling interval. Defaults to 10 seconds.
    

CUDA PM sampling uses the current CUDA device.

Intel Instrumentation and Tracing Technology APIs[#](https://docs.pytorch.org/docs/2.15/profiler.html#intel-instrumentation-and-tracing-technology-apis "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

torch.profiler.itt.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/itt.py#L31)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.itt.is_available "Link to this definition")

Check if ITT feature is available or not

torch.profiler.itt.mark(_msg_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/itt.py#L57)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.itt.mark "Link to this definition")

Describe an instantaneous event that occurred at some point.

Parameters:

**msg** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – ASCII message to associate with the event.

torch.profiler.itt.range\_push(_msg_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/itt.py#L38)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.itt.range_push "Link to this definition")

Pushes a range onto a stack of nested range span. Returns zero-based depth of the range that is started.

Parameters:

**msg** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – ASCII message to associate with range

torch.profiler.itt.range\_pop()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/itt.py#L49)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.itt.range_pop "Link to this definition")

Pops a range off of a stack of nested range spans. Returns the zero-based depth of the range that is ended.

torch.profiler.itt.range(_msg_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/profiler/itt.py#L67)
[#](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.itt.range "Link to this definition")

Context manager / decorator that pushes an ITT range at the beginning of its scope, and pops it at the end. If extra arguments are given, they are passed as arguments to msg.format().

Parameters:

**msg** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – message to associate with the range

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/profiler.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/profiler.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |