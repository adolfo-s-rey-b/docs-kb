Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cuda.tunable.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cuda.tunable.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cuda.tunable.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cuda.tunable.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cuda.tunable.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cuda.tunable.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cuda.tunable.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cuda.tunable.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cuda.tunable.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cuda.tunable.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cuda.tunable.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cuda.tunable.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cuda.tunable.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cuda.tunable.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cuda.tunable.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cuda.tunable.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cuda.tunable.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cuda.tunable.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cuda.tunable.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cuda.tunable.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cuda.tunable.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cuda.tunable.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cuda.tunable.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cuda.tunable.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cuda.tunable.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cuda.tunable.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cuda.tunable.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cuda.tunable.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cuda.tunable.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cuda.tunable.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cuda.tunable.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cuda.tunable.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cuda.tunable.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cuda.tunable.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cuda.tunable.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cuda.tunable.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cuda.tunable.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cuda.tunable.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cuda.tunable.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cuda.tunable.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cuda.tunable.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cuda.tunable.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cuda.tunable.html)

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

TunableOp[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#tunableop "Link to this heading")

====================================================================================================

Created On: Jun 03, 2024 | Last Updated On: Aug 25, 2026

Overview[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#module-torch.cuda.tunable "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This module exposes a TunableOp interface.

Some operations, such as GEMMs, could be implemented using more than one library or more than one technique. For example, a GEMM could be implemented for CUDA or ROCm using either the blas or blasLt libraries. Further, ROCm’s rocblas and hipblaslt libraries allow the user to query for all possible algorithms and then choose one. How does one know which implementation is the fastest and should be chosen? That’s what TunableOp provides.

### Enabling TunableOp and Tuning Separately[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#enabling-tunableop-and-tuning-separately "Link to this heading")

The TunableOp feature is enabled separately from enabling the tuning phase itself. Enabling TunableOp means that PyTorch will replace any standard operators with their Tunable implementations. Any call to a TunableOp first checks whether it has already been tuned for the given operator inputs. If so, it will immediately call the tuned operation; no further tuning will take place even when the tuning setting is enabled. Instead if no tuning result is found, and tuning is enabled, the TunableOp will benchmark every registered implementation of that operator for the given set of inputs and select the fastest.

### File Input and Output[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#file-input-and-output "Link to this heading")

The first time any TunableOp is invoked, the internal database of tuned operations will be prepared by attempting to read the results from the given file. The default filename is ‘tunableop\_results.csv’. To support tuning when multiple GPUs are used across multiple processes, the GPU device ordinal is automatically inserted into the filename to avoid multiple processes overwriting the same file.

If tuning is enabled and new tunings are discovered during the course of your workload, it will also write out to this same filename with all tunings, both the ones it read in at startup as well as the new ones found at runtime. This can be used, for example, to build up a tunings file across many workloads by reusing the same file. The output file is automatically created when the application terminates. This behavior can be controlled by the C++ and Python APIs but not the environment variables.

Assuming you specified a filename, you’ll end up with a CSV file with contents like so:

Validator,PT\_VERSION,2.2.0
Validator,ROCM\_VERSION,6.0.0.0\-12969\-1544e39
Validator,HIPBLASLT\_VERSION,0.6.0\-a9c5cc7
Validator,ROCBLAS\_VERSION,4.0.0\-72e57364\-dirty
GemmTunableOp\_float\_NT,nt\_25088\_4096\_64,Gemm\_Hipblaslt\_1219,1.262
GemmTunableOp\_float\_NT,nt\_4096\_4096\_64,Gemm\_Rocblas\_1216,0.033

Copy to clipboard

Note the “Validator” lines. If you change a library version, or ROCm version, or PyTorch version, TunableOp will detect this and reject the tunings file because the prior tunings are likely affected by other software changes.

The remaining lines are the tuned solutions for each TunableOp encountered during your execution. Each line consists of 4 comma-separated fields: operator name, operator parameters, solution name, and average execution time. The execution time is an optional field. The CSV file can be edited, but with caution. For example, the solution name (field 3) can be changed to “Default” and it will fall back to the original PyTorch untuned implementation. Or, in the case of ROCm’s hipBLAS or hipBLASLt libraries, if you know the specific solution index you can override the solution that TunableOp selected by replacing the value. The operator name and parameters (fields 1 and 2) are internally named and should not be modified. In the case of GemmTunableOp, field 1 indicates the datatype and whether the inputs are transposed (T) or not (N) and field 2 indicates the M, N, K input shapes.

There is an option to enable verbose output but it is only recommended for debugging purposes. This will produce a lot of diagnostic messages but may be useful to see if TunableOp is being used at all. Otherwise, TunableOp is completely silent, besides file output, unless there is a warning or error during its use. The verbose option is only available by setting the environment variable PYTORCH\_TUNABLEOP\_VERBOSE=1.

### A Note on Tuning Behavior, Warmup, and Cache Effects[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#a-note-on-tuning-behavior-warmup-and-cache-effects "Link to this heading")

Tuning an operator consists of iterating through the list or registered implementations and profiling each one. The profile is established by running a single implementation in a loop multiple times and taking the average execution time. There is also an optional warmup phase prior to tuning that can help with reaching stable power states by the hardware. During tuning of a workload the various hardware caches will more likely produce hits than when not tuning. There are options for flushing the instruction cache and rotate the input tensors which might help produce a more faithful profile of the tuned operator as if the operator were run within a larger workload instead of in a tight, repetitive loop.

By default, each possible solution for a given operator will be run for either 100 iterations or as many iterations that can be run within 30ms, whichever is smaller, and its average execution will be calculated. The fastest solution among all that were successfully profiled will be chosen. A profile might fail if the given solution doesn’t achieve the same accuracy as the default implementation or if the solution returns an error code.

CUDA cuBLASLt support uses the TunableOp result cache and profiling machinery to time a configurable number of cuBLASLt heuristic candidates.

### Current Tunable Operators[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#current-tunable-operators "Link to this heading")

#### TunableGemm for ROCm[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#tunablegemm-for-rocm "Link to this heading")

Any call to at::cuda::blas::gemm() or ::bgemm() will be routed through TunableOp when enabled. Calling gemm() for a given set of input arguments (transa, transb, m, n, k) on ROCm will attempt to use the fastest available implementation across both rocblas and hipblaslt. On CUDA, TunableGemm registers cuBLASLt heuristic candidates for GEMM paths that already use cuBLASLt.

#### cuBLASLt Heuristic Tuning for CUDA[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#cublaslt-heuristic-tuning-for-cuda "Link to this heading")

The number of cuBLASLt heuristic candidates is controlled by set\_cublaslt\_requested\_algo\_count() or PYTORCH\_TUNABLEOP\_CUBLASLT\_REQUESTED\_ALGO\_COUNT, which defaults to 8. If this count is 1, only the top cuBLASLt heuristic candidate is available.

### Offline Tuning[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#offline-tuning "Link to this heading")

#### Motivation[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#motivation "Link to this heading")

There are several use cases for offline tuning.

One use case involves a workload with a high-memory utilization, where regular tuning might lead to running out of memory.

Another use case is for compute-intensive workloads. In such cases, it is more resource-efficient to collect the GEMMs for the workload once and then tune repeatedly with different tuning parameters or libraries.

#### Workflow[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#workflow "Link to this heading")

There are basically two steps: 1) Set the environment variables to collect the untuned GEMM and this will generate `tunableop_untuned0.csv`:

export PYTORCH\_TUNABLEOP\_ENABLED\=1
export PYTORCH\_TUNABLEOP\_TUNING\=0
export PYTORCH\_TUNABLEOP\_RECORD\_UNTUNED\=1
...

Copy to clipboard

2.  Run a Python script that reads the `tunableop_untuned0.csv` and generates the `tunableop_results0.csv`, like this:
    

import torch.cuda.tunable as tunable
import os

os.putenv("PYTORCH\_TUNABLEOP\_ENABLED", "1")
os.putenv("PYTORCH\_TUNABLEOP\_TUNING", "1")
os.putenv("PYTORCH\_TUNABLEOP\_RECORD\_UNTUNED", "0")
tunable.tune\_gemm\_in\_file("tunableop\_untuned0.csv")

Copy to clipboard

It is also possible to take multiple untuned files and distribute the GEMMs for tuning to multiple GPUs within a single node. In the first step, the GEMMs are first gathered and duplicate GEMMs are eliminated. Next, the GEMMs are distributed to different GPUs for tuning. After all GEMMs are tuned, the results from all the GPUs are then gathered into a single file whose base filename has `_full0` appended to it (for example `tunableop_results_full0.csv`). Finally, this new file, containing the gathered results, will be duplicated N times, once for each GPU as convenience to the user will run the workload with the tuned configuration on N GPUs.

if \_\_name\_\_ \== "\_\_main\_\_":
    num\_gpus \= 8  \# number of GPUs that will be used during the tuning process
    tunable.mgpu\_tune\_gemm\_in\_file("tunableop\_untuned?.csv", num\_gpus)

Copy to clipboard

Note that the usage of the `mgpu_tune_gemm_in_file` API is different from its single GPU counterpart (`tune_gemm_in_file`). The body of the Python script that calls the API must be wrapped in `main()` as shown due to the use of concurrent futures module. The argument to `mgpu_tune_gemm_in_file` must contain a wild card expression (`?` or `*`) to generate the list of untuned files containing the GEMMs to be processed. The `num_gpus` must between 1 and the total number of GPUs available.

### Tuning Context[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#tuning-context "Link to this heading")

The behavior of TunableOp is currently manipulated through environment variables, the C++ interface of at::cuda::tunable::getTuningContext(), or the torch.cuda.tunable python interfaces. The environment variables take precedence over any setting you manipulate using the C++ or Python APIs.

#### Environment Variable Interface[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#environment-variable-interface "Link to this heading")

Environment variables are cached the first time they are read. You cannot use the environment variable interface programmatically since the settings become fixed. Use the C++ or Python APIs instead.

API Reference[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#api-reference "Link to this heading")

------------------------------------------------------------------------------------------------------------

torch.cuda.tunable.enable(_val\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L239)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.enable "Link to this definition")

This is the big on/off switch for all TunableOp implementations.

torch.cuda.tunable.is\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L244)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.is_enabled "Link to this definition")

Returns whether the TunableOp feature is enabled.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.cuda.tunable.tuning\_enable(_val\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L249)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.tuning_enable "Link to this definition")

Enable tuning of TunableOp implementations.

When enabled, if a tuned entry isn’t found, run the tuning step and record the entry.

torch.cuda.tunable.tuning\_is\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L258)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.tuning_is_enabled "Link to this definition")

Returns whether TunableOp implementations can be tuned.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.cuda.tunable.record\_untuned\_enable(_val\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L263)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.record_untuned_enable "Link to this definition")

Enable recording untuned TunableOp operations for offline tuning.

When enabled, if a tuned entry isn’t found, write it to the untuned file.

torch.cuda.tunable.record\_untuned\_is\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L271)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.record_untuned_is_enabled "Link to this definition")

Returns whether TunableOp operations are recorded for offline tuning.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.cuda.tunable.set\_max\_tuning\_duration(_duration_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L293)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_max_tuning_duration "Link to this definition")

Set max time in milliseconds to spend tuning a given solution.

If both max tuning duration and iterations are set, the smaller of the two will be honored. At minimum 1 tuning iteration will always be run.

torch.cuda.tunable.get\_max\_tuning\_duration()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L302)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_max_tuning_duration "Link to this definition")

Get max time to spend tuning a given solution.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.cuda.tunable.set\_max\_tuning\_iterations(_iterations_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L307)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_max_tuning_iterations "Link to this definition")

Set max number of iterations to spend tuning a given solution.

If both max tuning duration and iterations are set, the smaller of the two will be honored. At minimum 1 tuning iteration will always be run.

torch.cuda.tunable.get\_max\_tuning\_iterations()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L316)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_max_tuning_iterations "Link to this definition")

Get max iterations to spend tuning a given solution.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.cuda.tunable.set\_cublaslt\_requested\_algo\_count(_count_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L321)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_cublaslt_requested_algo_count "Link to this definition")

Set the number of cuBLASLt heuristic algorithms to request on CUDA.

Values less than 1 are clamped to 1.

torch.cuda.tunable.get\_cublaslt\_requested\_algo\_count()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L329)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_cublaslt_requested_algo_count "Link to this definition")

Get the number of cuBLASLt heuristic algorithms requested on CUDA.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.cuda.tunable.set\_filename(_filename_, _insert\_device\_ordinal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L406)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_filename "Link to this definition")

Set the filename to use for input/output of tuning results.

If `insert_device_ordinal` is `True` then the current device ordinal will be added to the given filename automatically. This can be used in a 1-process-per-gpu scenario to ensure all processes write to a separate file.

torch.cuda.tunable.get\_filename()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L416)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_filename "Link to this definition")

Get the results filename.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.cuda.tunable.get\_results()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L421)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_results "Link to this definition")

Return all TunableOp results.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
\]

torch.cuda.tunable.get\_validators()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L426)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_validators "Link to this definition")

Return the TunableOp validators.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

torch.cuda.tunable.read\_file(_filename\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L431)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.read_file "Link to this definition")

Read results from a TunableOp CSV file.

If `filename` is not given, `get_filename()` is called.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.cuda.tunable.tune\_gemm\_in\_file(_filename_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L467)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.tune_gemm_in_file "Link to this definition")

tune GEMM in file.

torch.cuda.tunable.mgpu\_tune\_gemm\_in\_file(_filename\_pattern_, _num\_gpus_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L1065)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.mgpu_tune_gemm_in_file "Link to this definition")

Process one or more files and distribute work over one or more GPUs.

torch.cuda.tunable.set\_rotating\_buffer\_size(_buffer\_size_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L441)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_rotating_buffer_size "Link to this definition")

Set rotating buffer size to this value in MB, if the buffer size is greater than zero.

If less than zero, query L2 cache size. If equal to zero, means deactivate rotating buffer.

torch.cuda.tunable.get\_rotating\_buffer\_size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L449)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.get_rotating_buffer_size "Link to this definition")

Get the rotating buffer size in kilobytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.cuda.tunable.set\_numerical\_check\_tolerances(_enable_, _atol\=1e-05_, _rtol\=1e-05_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L454)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.set_numerical_check_tolerances "Link to this definition")

Set the atol and rtol values in numeric check

torch.cuda.tunable.dynamic\_dims\_mask(_M\=False_, _N\=False_, _K\=False_, _BATCH\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L386)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.dynamic_dims_mask "Link to this definition")

Context manager that wraps a scope with a per-call dynamic-dims mask.

Each TunableOp GEMM call inside the scope uses the given mask when computing its wildcard signature; outside the scope the legacy concrete-only behavior applies.

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[None\]

torch.cuda.tunable.wildcard\_fallback\_enable(_val\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L276)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.wildcard_fallback_enable "Link to this definition")

Enable wildcard fallback for TunableOp runtime dispatch.

When enabled and a concrete signature misses, the runtime scans persisted wildcard entries for a token-pattern match. When disabled (the default), only exact concrete lookups are performed, matching pre-wildcard behavior.

Also settable via `PYTORCH_TUNABLEOP_WILDCARD_FALLBACK=1`.

torch.cuda.tunable.wildcard\_fallback\_is\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/tunable.py#L288)
[#](https://docs.pytorch.org/docs/2.15/cuda.tunable.html#torch.cuda.tunable.wildcard_fallback_is_enabled "Link to this definition")

Returns whether wildcard fallback is enabled for TunableOp dispatch.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cuda.tunable.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cuda.tunable.md.txt)

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