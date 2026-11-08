Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/benchmark_utils.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/benchmark_utils.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/benchmark_utils.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/benchmark_utils.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/benchmark_utils.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/benchmark_utils.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/benchmark_utils.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/benchmark_utils.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/benchmark_utils.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/benchmark_utils.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/benchmark_utils.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/benchmark_utils.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/benchmark_utils.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/benchmark_utils.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/benchmark_utils.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/benchmark_utils.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/benchmark_utils.html)
[v1.13](https://docs.pytorch.org/docs/1.13/benchmark_utils.html)
[v1.12](https://docs.pytorch.org/docs/1.12/benchmark_utils.html)
[v1.11](https://docs.pytorch.org/docs/1.11/benchmark_utils.html)
[v1.10](https://docs.pytorch.org/docs/1.10/benchmark_utils.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/benchmark_utils.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/benchmark_utils.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/benchmark_utils.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/benchmark_utils.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/benchmark_utils.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/benchmark_utils.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/benchmark_utils.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/benchmark_utils.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/benchmark_utils.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/benchmark_utils.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/benchmark_utils.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/benchmark_utils.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/benchmark_utils.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/benchmark_utils.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/benchmark_utils.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/benchmark_utils.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/benchmark_utils.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/benchmark_utils.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/benchmark_utils.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/benchmark_utils.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/benchmark_utils.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/benchmark_utils.html)

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

Benchmark Utils - torch.utils.benchmark[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#module-torch.utils.benchmark "Link to this heading")

========================================================================================================================================================

Created On: Nov 02, 2020 | Last Updated On: May 07, 2026

_class_ torch.utils.benchmark.Timer(_stmt='pass'_, _setup='pass'_, _global\_setup=''_, _timer=<function timer>_, _globals=None_, _label=None_, _sub\_label=None_, _description=None_, _env=None_, _num\_threads=1_, _language=Language.PYTHON_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/timer.py#L66)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer "Link to this definition")

Helper class for measuring execution time of PyTorch statements.

For a full tutorial on how to use this class, see: [https://pytorch.org/tutorials/recipes/recipes/benchmark.html](https://pytorch.org/tutorials/recipes/recipes/benchmark.html)

The PyTorch Timer is based on timeit.Timer (and in fact uses timeit.Timer internally), but with several key differences:

1.  Runtime aware:
    
    Timer will perform warmups (important as some elements of PyTorch are lazily initialized), set threadpool size so that comparisons are apples-to-apples, and synchronize asynchronous accelerator functions when necessary.
    
2.  Focus on replicates:
    
    When measuring code, and particularly complex kernels / models, run-to-run variation is a significant confounding factor. It is expected that all measurements should include replicates to quantify noise and allow median computation, which is more robust than mean. To that effect, this class deviates from the timeit API by conceptually merging timeit.Timer.repeat and timeit.Timer.autorange. (Exact algorithms are discussed in method docstrings.) The timeit method is replicated for cases where an adaptive strategy is not desired.
    
3.  Optional metadata:
    
    When defining a Timer, one can optionally specify label, sub\_label, description, and env. (Defined later) These fields are included in the representation of result object and by the Compare class to group and display results for comparison.
    
4.  Instruction counts
    
    In addition to wall times, Timer can run a statement under Callgrind and report instructions executed.
    

Directly analogous to timeit.Timer constructor arguments:

> stmt, setup, timer, globals

PyTorch Timer specific constructor arguments:

> label, sub\_label, description, env, num\_threads

Parameters:

*   **stmt** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Code snippet to be run in a loop and timed.
    
*   **setup** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Optional setup code. Used to define variables used in stmt
    
*   **global\_setup** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – (C++ only) Code which is placed at the top level of the file for things like #include statements.
    
*   **timer** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[__\]__,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Callable which returns the current time. If PyTorch was built without accelerators or there is no accelerator present, this defaults to timeit.default\_timer; otherwise it will synchronize accelerators before measuring the time.
    
*   **globals** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ _None_) – A dict which defines the global variables when stmt is being executed. This is the other method for providing variables which stmt needs.
    
*   **label** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – String which summarizes stmt. For instance, if stmt is “torch.nn.functional.relu(torch.add(x, 1, out=out))” one might set label to “ReLU(x + 1)” to improve readability.
    
*   **sub\_label** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) –
    
    Provide supplemental information to disambiguate measurements with identical stmt or label. For instance, in our example above sub\_label might be “float” or “int”, so that it is easy to differentiate: “ReLU(x + 1): (float)”
    
    ”ReLU(x + 1): (int)” when printing Measurements or summarizing using Compare.
    
*   **description** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) –
    
    String to distinguish measurements with identical label and sub\_label. The principal use of description is to signal to Compare the columns of data. For instance one might set it based on the input size to create a table of the form:
    
                            | n\=1 | n\=4 | ...
                            \------------- ...
    ReLU(x + 1): (float)    | ... | ... | ...
    ReLU(x + 1): (int)      | ... | ... | ...
    
    Copy to clipboard
    
    using Compare. It is also included when printing a Measurement.
    
*   **env** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – This tag indicates that otherwise identical tasks were run in different environments, and are therefore not equivalent, for instance when A/B testing a change to a kernel. Compare will treat Measurements with different env specification as distinct when merging replicate runs.
    
*   **num\_threads** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The size of the PyTorch threadpool when executing stmt. Single threaded performance is important as both a key inference workload and a good indicator of intrinsic algorithmic efficiency, so the default is set to one. This is in contrast to the default PyTorch threadpool size which tries to utilize all cores.
    

adaptive\_autorange(_threshold\=0.1_, _\*_, _min\_run\_time\=0.01_, _max\_run\_time\=10.0_, _callback\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/timer.py#L384)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer.adaptive_autorange "Link to this definition")

Similar to blocked\_autorange but also checks for variability in measurements and repeats until iqr/median is smaller than threshold or max\_run\_time is reached.

At a high level, adaptive\_autorange executes the following pseudo-code:

\`setup\`

times = \[\]
while times.sum < max\_run\_time
    start = timer()
    for \_ in range(block\_size):
        \`stmt\`
    times.append(timer() - start)

    enough\_data = len(times)>3 and times.sum > min\_run\_time
    small\_iqr=times.iqr/times.mean<threshold

    if enough\_data and small\_iqr:
        break

Copy to clipboard

Parameters:

*   **threshold** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – value of iqr/median threshold for stopping
    
*   **min\_run\_time** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – total runtime needed before checking threshold
    
*   **max\_run\_time** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – total runtime for all measurements regardless of threshold
    

Returns:

A Measurement object that contains measured runtimes and repetition counts, and can be used to compute statistics. (mean, median, etc.)

Return type:

[_Measurement_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "torch.utils.benchmark.utils.common.Measurement")

blocked\_autorange(_callback\=None_, _min\_run\_time\=0.2_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/timer.py#L324)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer.blocked_autorange "Link to this definition")

Measure many replicates while keeping timer overhead to a minimum.

At a high level, blocked\_autorange executes the following pseudo-code:

\`setup\`

total\_time = 0
while total\_time < min\_run\_time
    start = timer()
    for \_ in range(block\_size):
        \`stmt\`
    total\_time += (timer() - start)

Copy to clipboard

Note the variable block\_size in the inner loop. The choice of block size is important to measurement quality, and must balance two competing objectives:

> 1.  A small block size results in more replicates and generally better statistics.
>     
> 2.  A large block size better amortizes the cost of timer invocation, and results in a less biased measurement. This is important because accelerator synchronization time is non-trivial (order single to low double digit microseconds) and would otherwise bias the measurement.
>     

blocked\_autorange sets block\_size by running a warmup period, increasing block size until timer overhead is less than 0.1% of the overall computation. This value is then used for the main measurement loop.

Returns:

A Measurement object that contains measured runtimes and repetition counts, and can be used to compute statistics. (mean, median, etc.)

Return type:

[_Measurement_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "torch.utils.benchmark.utils.common.Measurement")

collect\_callgrind(_number: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _\*_, _repeats: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_, _collect\_baseline: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_, _retain\_out\_file: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_) → [CallgrindStats](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.CallgrindStats")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/timer.py#L469)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer.collect_callgrind "Link to this definition")

collect\_callgrind(_number: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _\*_, _repeats: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _collect\_baseline: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_, _retain\_out\_file: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[CallgrindStats](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.CallgrindStats")\
, ...\]

Collect instruction counts using Callgrind.

Unlike wall times, instruction counts are deterministic (modulo non-determinism in the program itself and small amounts of jitter from the Python interpreter.) This makes them ideal for detailed performance analysis. This method runs stmt in a separate process so that Valgrind can instrument the program. Performance is severely degraded due to the instrumentation, however this is ameliorated by the fact that a small number of iterations is generally sufficient to obtain good measurements.

In order to use this method valgrind, callgrind\_control, and callgrind\_annotate must be installed.

Because there is a process boundary between the caller (this process) and the stmt execution, globals cannot contain arbitrary in-memory data structures. (Unlike timing methods) Instead, globals are restricted to builtins, nn.Modules’s, and TorchScripted functions/modules to reduce the surprise factor from serialization and subsequent deserialization. The GlobalsBridge class provides more detail on this subject. Take particular care with nn.Modules: they rely on pickle and you may need to add an import to setup for them to transfer properly.

By default, a profile for an empty statement will be collected and cached to indicate how many instructions are from the Python loop which drives stmt.

Returns:

A CallgrindStats object which provides instruction counts and some basic facilities for analyzing and manipulating results.

timeit(_number\=1000000_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/timer.py#L259)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer.timeit "Link to this definition")

Mirrors the semantics of timeit.Timer.timeit().

Execute the main statement (stmt) number times. [https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit)

Return type:

[_Measurement_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "torch.utils.benchmark.utils.common.Measurement")

_class_ torch.utils.benchmark.Measurement(_number\_per\_run_, _raw\_times_, _task\_spec_, _metadata\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/common.py#L74)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "Link to this definition")

The result of a Timer measurement.

This class stores one or more measurements of a given statement. It is serializable and provides several convenience methods (including a detailed \_\_repr\_\_) for downstream consumers.

_static_ merge(_measurements_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/common.py#L230)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement.merge "Link to this definition")

Convenience method for merging replicates.

Merge will extrapolate times to number\_per\_run=1 and will not transfer any metadata. (Since it might differ between replicates)

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_Measurement_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "torch.utils.benchmark.utils.common.Measurement")\
\]

_property_ significant\_figures_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement.significant_figures "Link to this definition")

Approximate significant figure estimate.

This property is intended to give a convenient way to estimate the precision of a measurement. It only uses the interquartile region to estimate statistics to try to mitigate skew from the tails, and uses a static z value of 1.645 since it is not expected to be used for small values of n, so z can approximate t.

The significant figure estimation used in conjunction with the trim\_sigfig method to provide a more human interpretable data summary. \_\_repr\_\_ does not use this method; it simply displays raw values. Significant figure estimation is intended for Compare.

_class_ torch.utils.benchmark.CallgrindStats(_task\_spec_, _number\_per\_run_, _built\_with\_debug\_symbols_, _baseline\_inclusive\_stats_, _baseline\_exclusive\_stats_, _stmt\_inclusive\_stats_, _stmt\_exclusive\_stats_, _stmt\_callgrind\_out_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L169)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats "Link to this definition")

Top level container for Callgrind results collected by Timer.

Manipulation is generally done using the FunctionCounts class, which is obtained by calling CallgrindStats.stats(…). Several convenience methods are provided as well; the most significant is CallgrindStats.as\_standardized().

as\_standardized()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L244)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats.as_standardized "Link to this definition")

Strip library names and some prefixes from function strings.

When comparing two different sets of instruction counts, on stumbling block can be path prefixes. Callgrind includes the full filepath when reporting a function (as it should). However, this can cause issues when diffing profiles. If a key component such as Python or PyTorch was built in separate locations in the two profiles, which can result in something resembling:

23234231 /tmp/first\_build\_dir/thing.c:foo(...)
 9823794 /tmp/first\_build\_dir/thing.c:bar(...)
  ...
   53453 .../aten/src/Aten/...:function\_that\_actually\_changed(...)
  ...
 \-9823794 /tmp/second\_build\_dir/thing.c:bar(...)
\-23234231 /tmp/second\_build\_dir/thing.c:foo(...)

Copy to clipboard

Stripping prefixes can ameliorate this issue by regularizing the strings and causing better cancellation of equivalent call sites when diffing.

Return type:

[_CallgrindStats_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.CallgrindStats")

counts(_\*_, _denoise\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L218)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats.counts "Link to this definition")

Returns the total number of instructions executed.

See FunctionCounts.denoise() for an explanation of the denoise arg.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

delta(_other_, _inclusive\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L227)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats.delta "Link to this definition")

Diff two sets of counts.

One common reason to collect instruction counts is to determine the effect that a particular change will have on the number of instructions needed to perform some unit of work. If a change increases that number, the next logical question is “why”. This generally involves looking at what part if the code increased in instruction count. This function automates that process so that one can easily diff counts on both an inclusive and exclusive basis.

Return type:

[_FunctionCounts_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.FunctionCounts")

stats(_inclusive\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L204)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.CallgrindStats.stats "Link to this definition")

Returns detailed function counts.

Conceptually, the FunctionCounts returned can be thought of as a tuple of (count, path\_and\_function\_name) tuples.

inclusive matches the semantics of callgrind. If True, the counts include instructions executed by children. inclusive=True is useful for identifying hot spots in code; inclusive=False is useful for reducing noise when diffing counts from two different runs. (See CallgrindStats.delta(…) for more details)

Return type:

[_FunctionCounts_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.FunctionCounts")

_class_ torch.utils.benchmark.FunctionCounts(_\_data_, _inclusive_, _truncate\_rows\=True_, _\_linewidth\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L44)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "Link to this definition")

Container for manipulating Callgrind results.

It supports:

1.  Addition and subtraction to combine or diff results.
    
2.  Tuple-like indexing.
    
3.  A denoise function which strips CPython calls which are known to be non-deterministic and quite noisy.
    
4.  Two higher order methods (filter and transform) for custom manipulation.
    

denoise()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L137)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts.denoise "Link to this definition")

Remove known noisy instructions.

Several instructions in the CPython interpreter are rather noisy. These instructions involve unicode to dictionary lookups which Python uses to map variable names. FunctionCounts is generally a content agnostic container, however this is sufficiently important for obtaining reliable results to warrant an exception.

Return type:

[_FunctionCounts_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "torch.utils.benchmark.utils.valgrind_wrapper.timer_interface.FunctionCounts")

filter(_filter\_fn_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L130)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts.filter "Link to this definition")

Keep only the elements where filter\_fn applied to function name returns True.

Return type:

[FunctionCounts](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "torch.utils.benchmark.FunctionCounts")

transform(_map\_fn_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L117)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts.transform "Link to this definition")

Apply map\_fn to all of the function names.

This can be used to regularize function names (e.g. stripping irrelevant parts of the file path), coalesce entries by mapping multiple functions to the same name (in which case the counts are added together), etc.

Return type:

[FunctionCounts](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.FunctionCounts "torch.utils.benchmark.FunctionCounts")

_class_ torch.utils.benchmark.Compare(_results_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L269)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare "Link to this definition")

Helper class for displaying the results of many measurements in a formatted table.

The table format is based on the information fields provided in [`torch.utils.benchmark.Timer`](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Timer "torch.utils.benchmark.Timer")
 (description, label, sub\_label, num\_threads, etc).

The table can be directly printed using [`print()`](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.print "torch.utils.benchmark.Compare.print")
 or casted as a str.

For a full tutorial on how to use this class, see: [https://pytorch.org/tutorials/recipes/recipes/benchmark.html](https://pytorch.org/tutorials/recipes/recipes/benchmark.html)

Parameters:

**results** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
_\[_[_Measurement_](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Measurement "torch.utils.benchmark.utils.common.Measurement")\
_\]_) – List of Measurement to display.

colorize(_rowwise\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L311)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.colorize "Link to this definition")

Colorize formatted table.

Colorize columnwise by default.

extend\_results(_results_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L295)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.extend_results "Link to this definition")

Append results to already stored ones.

All added results must be instances of `Measurement`.

highlight\_warnings()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L318)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.highlight_warnings "Link to this definition")

Enables warning highlighting when building formatted table.

print()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L322)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.print "Link to this definition")

Print formatted table

trim\_significant\_figures()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compare.py#L307)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.Compare.trim_significant_figures "Link to this definition")

Enables trimming of significant figures when building the formatted table.

torch.utils.benchmark.examples.op\_benchmark.assert\_dicts\_equal(_dict\_0_, _dict\_1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/examples/op_benchmark.py#L19)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.examples.op_benchmark.assert_dicts_equal "Link to this definition")

Builtin dict comparison will not compare numpy arrays.

e.g.:

x \= {"a": np.ones((2, 1))}
x \== x  \# Raises ValueError

Copy to clipboard

torch.utils.benchmark.utils.fuzzer.prod(_values_, _base\=1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/fuzzer.py#L177)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.utils.fuzzer.prod "Link to this definition")

np.prod can overflow, so for sizes the product should be done in Python.

Even though np.prod type promotes to int64, it can still overflow in which case the negative value will pass the size check and OOM when attempting to actually allocate the Tensor.

torch.utils.benchmark.utils.common.select\_unit(_t_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/common.py#L258)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.utils.common.select_unit "Link to this definition")

Determine how to scale times for O(1) magnitude.

This utility is used to format numbers for human consumption.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
\]

torch.utils.benchmark.utils.common.trim\_sigfig(_x_, _n_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/common.py#L277)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.utils.common.trim_sigfig "Link to this definition")

Trim x to n significant figures. (e.g. 3.14159, 2 -> 3.10000)

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")

torch.utils.benchmark.utils.compile.bench\_all(_model_, _sample\_input_, _num\_iters\=5_, _optimizer\=None_, _loss\_fn\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compile.py#L127)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.utils.compile.bench_all "Link to this definition")

This is a simple utility that can be used to benchmark torch.compile In particular it ensures that your GPU is setup to use tensor cores if it supports its It also tries out all the main backends and prints a table of results so you can easily compare them all Many of the backends have their own optional dependencies so please pip install them separately

You will get one table for inference and another for training If you’d like to leverage this utility for training make sure to pass in a torch.optim.Optimizer

The important warnings are Your GPU supports tensor cores we will enable it automatically by setting torch.set\_float32\_matmul\_precision(‘high’)

If a compilation fails for any reason including the dependency not being included then we will print Failed to compile {backend} with mode {mode}

torch.utils.benchmark.utils.compile.benchmark\_compile(_model_, _sample\_input_, _num\_iters\=5_, _backend\=None_, _mode\='default'_, _optimizer\=None_, _loss\_fn\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/benchmark/utils/compile.py#L82)
[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#torch.utils.benchmark.utils.compile.benchmark_compile "Link to this definition")

Use this utility to benchmark torch.compile

torch.utils.benchmark.examples[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#module-torch.utils.benchmark.examples "Link to this heading")

========================================================================================================================================================

torch.utils.benchmark.examples.spectral\_ops\_fuzz\_test[#](https://docs.pytorch.org/docs/2.15/benchmark_utils.html#module-torch.utils.benchmark.examples.spectral_ops_fuzz_test "Link to this heading")

=========================================================================================================================================================================================================

Microbenchmarks for the torch.fft module

|     |     |
| --- | --- |
| [`run_benchmark`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.benchmark.examples.spectral_ops_fuzz_test.run_benchmark.html#torch.utils.benchmark.examples.spectral_ops_fuzz_test.run_benchmark "torch.utils.benchmark.examples.spectral_ops_fuzz_test.run_benchmark") |     |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/benchmark_utils.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/benchmark_utils.md.txt)

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