Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/multiprocessing.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/multiprocessing.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/multiprocessing.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/multiprocessing.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/multiprocessing.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/multiprocessing.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/multiprocessing.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/multiprocessing.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/multiprocessing.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/multiprocessing.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/multiprocessing.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/multiprocessing.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/multiprocessing.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/multiprocessing.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/multiprocessing.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/multiprocessing.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/multiprocessing.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/multiprocessing.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/multiprocessing.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/multiprocessing.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/multiprocessing.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/multiprocessing.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/multiprocessing.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/multiprocessing.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/multiprocessing.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/multiprocessing.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/multiprocessing.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/multiprocessing.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/multiprocessing.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/multiprocessing.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/multiprocessing.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/multiprocessing.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/multiprocessing.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/multiprocessing.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/multiprocessing.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/multiprocessing.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/multiprocessing.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/multiprocessing.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/multiprocessing.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/multiprocessing.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/multiprocessing.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/multiprocessing.html)

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

Multiprocessing[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#module-torch.distributed.elastic.multiprocessing "Link to this heading")

============================================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 12, 2026

Library that launches and manages `n` copies of worker subprocesses either specified by a function or a binary.

For functions, it uses `torch.multiprocessing` (and therefore python `multiprocessing`) to spawn/fork worker processes. For binaries it uses python `subprocessing.Popen` to create worker processes.

Usage 1: Launching two trainers as a function

from torch.distributed.elastic.multiprocessing import Std, start\_processes

def trainer(a, b, c):
    pass  \# train

\# runs two trainers
\# LOCAL\_RANK=0 trainer(1,2,3)
\# LOCAL\_RANK=1 trainer(4,5,6)
ctx \= start\_processes(
    name\="trainer",
    entrypoint\=trainer,
    args\={0: (1, 2, 3), 1: (4, 5, 6)},
    envs\={0: {"LOCAL\_RANK": 0}, 1: {"LOCAL\_RANK": 1}},
    log\_dir\="/tmp/foobar",
    redirects\=Std.ALL,  \# write all worker stdout/stderr to a log file
    tee\={0: Std.ERR},  \# tee only local rank 0's stderr to console
)

\# waits for all copies of trainer to finish
ctx.wait()

Copy to clipboard

Usage 2: Launching 2 echo workers as a binary

\# same as invoking
\# echo hello
\# echo world > stdout.log
ctx \= start\_processes(
        name\="echo"
        entrypoint\="echo",
        log\_dir\="/tmp/foobar",
        args\={0: "hello", 1: "world"},
        redirects\={1: Std.OUT},
       )

Copy to clipboard

Just like `torch.multiprocessing`, the return value of the function [`start_processes()`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.start_processes "torch.distributed.elastic.multiprocessing.start_processes")
 is a process context ([`api.PContext`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.PContext "torch.distributed.elastic.multiprocessing.api.PContext")
). If a function was launched, a [`api.MultiprocessContext`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.MultiprocessContext "torch.distributed.elastic.multiprocessing.api.MultiprocessContext")
 is returned and if a binary was launched a [`api.SubprocessContext`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.SubprocessContext "torch.distributed.elastic.multiprocessing.api.SubprocessContext")
 is returned. Both are specific implementations of the parent [`api.PContext`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.PContext "torch.distributed.elastic.multiprocessing.api.PContext")
 class.

Starting Multiple Workers[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#starting-multiple-workers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

torch.distributed.elastic.multiprocessing.start\_processes(_name_, _entrypoint_, _args_, _envs_, _logs\_specs_, _log\_line\_prefixes\=None_, _start\_method\='spawn'_, _numa\_options\=None_, _duplicate\_stdout\_filters\=None_, _duplicate\_stderr\_filters\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/__init__.py#L103)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.start_processes "Link to this definition")

Start `n` copies of `entrypoint` processes with the provided options.

`entrypoint` is either a `Callable` (function) or a `str` (binary). The number of copies is determined by the number of entries for `args` and `envs` arguments, which need to have the same key set.

`args` and `env` parameters are the arguments and environment variables to pass down to the entrypoint mapped by the replica index (local rank). All local ranks must be accounted for. That is, the keyset should be `{0,1,...,(nprocs-1)}`.

Note

When the `entrypoint` is a binary (`str`), `args` can only be strings. If any other type is given, then it is casted to a string representation (e.g. `str(arg1)`). Furthermore, a binary failure will only write an `error.json` error file if the main function is annotated with `torch.distributed.elastic.multiprocessing.errors.record`. For function launches, this is done by default and there is no need to manually annotate with the `@record` annotation.

Inside `logs_specs`, `redirects` and `tee` are bitmasks specifying which std stream(s) to redirect to a log file in the `log_dir`. Valid mask values are defined in `Std`. To redirect/tee only certain local ranks, pass `redirects` as a map with the key as the local rank to specify the redirect behavior for. Any missing local ranks will default to `Std.NONE`.

`duplicate_stdout_filters` and `duplicate_stderr_filters`, if non-empty, duplicate stdouts and stderrs respectively specified in `logs_specs`’s `tee` to a file containing only lines that match \_any\_ of the filter strings. The log file is aggregated across all ranks selected by `tee`.

`tee` acts like the unix “tee” command in that it redirects + prints to console. To avoid worker stdout/stderr from printing to console, use the `redirects` parameter.

For each process, the `log_dir` will contain:

1.  `{local_rank}/error.json`: if the process failed, a file with the error info
    
2.  `{local_rank}/stdout.log`: if `redirect & STDOUT == STDOUT`
    
3.  `{local_rank}/stderr.log`: if `redirect & STDERR == STDERR`
    
4.  `filtered_stdout.log`: if `duplicate_stdout_filters` is non-empty
    
5.  `filtered_stderr.log`: if `duplicate_stderr_filters` is non-empty
    

Note

It is expected that the `log_dir` exists, is empty, and is a directory.

Example:

log\_dir \= "/tmp/test"

\# ok; two copies of foo: foo("bar0"), foo("bar1")
start\_processes(
   name\="trainer",
   entrypoint\=foo,
   args:{0:("bar0",), 1:("bar1",),
   envs:{0:{}, 1:{}},
   log\_dir\=log\_dir
)

\# invalid; envs missing for local rank 1
start\_processes(
   name\="trainer",
   entrypoint\=foo,
   args:{0:("bar0",), 1:("bar1",),
   envs:{0:{}},
   log\_dir\=log\_dir
)

\# ok; two copies of /usr/bin/touch: touch file1, touch file2
start\_processes(
   name\="trainer",
   entrypoint\="/usr/bin/touch",
   args:{0:("file1",), 1:("file2",),
   envs:{0:{}, 1:{}},
   log\_dir\=log\_dir
 )

\# caution; arguments casted to string, runs:
\# echo "1" "2" "3" and echo "\[1, 2, 3\]"
start\_processes(
   name\="trainer",
   entrypoint\="/usr/bin/echo",
   args:{0:(1,2,3), 1:(\[1,2,3\],),
   envs:{0:{}, 1:{}},
   log\_dir\=log\_dir
 )

Copy to clipboard

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a human readable short name that describes what the processes are (used as header when tee’ing stdout/stderr outputs)
    
*   **entrypoint** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – either a `Callable` (function) or `cmd` (binary)
    
*   **args** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\]_) – arguments to each replica
    
*   **envs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__\]_) – env vars to each replica
    
*   **log\_dir** – directory used to write log files
    
*   **start\_method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – multiprocessing start method (spawn, fork, forkserver) ignored for binaries
    
*   **logs\_specs** ([_LogsSpecs_](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsSpecs "torch.distributed.elastic.multiprocessing.api.LogsSpecs")
    ) – defines `log_dir`, `redirects`, and `tee`. inside `logs_specs`: - redirects: which std streams to redirect to a log file - tee: which std streams to redirect + print to console
    
*   **local\_ranks\_filter** – which ranks’ logs to print to console
    
*   **duplicate\_stdout\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – filters for the duplicated stdout logs
    
*   **duplicate\_stderr\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – filters for the duplicated stderr logs
    

Return type:

[_PContext_](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.PContext "torch.distributed.elastic.multiprocessing.api.PContext")

Process Context[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#process-context "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.multiprocessing.api.PContext(_name_, _entrypoint_, _args_, _envs_, _logs\_specs_, _log\_line\_prefixes\=None_, _duplicate\_stdout\_filters\=None_, _duplicate\_stderr\_filters\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L444)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.PContext "Link to this definition")

The base class that standardizes operations over a set of processes that are launched via different mechanisms.

The name `PContext` is intentional to disambiguate with `torch.multiprocessing.ProcessContext`.

Warning

stdouts and stderrs should ALWAYS be a superset of tee\_stdouts and tee\_stderrs (respectively) this is b/c tee is implemented as a redirect + tail -f <stdout/stderr.log>

Parameters:

*   **duplicate\_stdout\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – If non-empty, duplicates stdouts specified in `logs_specs`’s `tee` to a file containing only lines that match \_any\_ of the filter strings. The log file is aggregated across all ranks selected by `tee`.
    
*   **duplicate\_stderr\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – If non-empty, duplicates stderrs specified in `logs_specs`’s `tee` to a file containing only lines that match \_any\_ of the filter strings. The log file is aggregated across all ranks selected by `tee`.
    

_class_ torch.distributed.elastic.multiprocessing.api.MultiprocessContext(_name_, _entrypoint_, _args_, _envs_, _start\_method_, _logs\_specs_, _log\_line\_prefixes\=None_, _numa\_options\=None_, _duplicate\_stdout\_filters\=None_, _duplicate\_stderr\_filters\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L711)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.MultiprocessContext "Link to this definition")

`PContext` holding worker processes invoked as a function.

_class_ torch.distributed.elastic.multiprocessing.api.SubprocessContext(_name_, _entrypoint_, _args_, _envs_, _logs\_specs_, _log\_line\_prefixes\=None_, _numa\_options\=None_, _duplicate\_stdout\_filters\=None_, _duplicate\_stderr\_filters\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L917)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.SubprocessContext "Link to this definition")

`PContext` holding worker processes invoked as a binary.

_class_ torch.distributed.elastic.multiprocessing.api.RunProcsResult(_return\_values=<factory>_, _failures=<factory>_, _stdouts=<factory>_, _stderrs=<factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L421)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.RunProcsResult "Link to this definition")

Results of a completed run of processes started with `start_processes()`. Returned by `PContext`.

Note the following:

1.  All fields are mapped by local rank
    
2.  `return_values` - only populated for functions (not the binaries).
    
3.  `stdouts` - path to stdout.log (empty string if no redirect)
    
4.  `stderrs` - path to stderr.log (empty string if no redirect)
    

_class_ torch.distributed.elastic.multiprocessing.api.DefaultLogsSpecs(_log\_dir\=None_, _redirects\=Std.NONE_, _tee\=Std.NONE_, _local\_ranks\_filter\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L245)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.DefaultLogsSpecs "Link to this definition")

Default LogsSpecs implementation:

*   log\_dir will be created if it doesn’t exist
    
*   Generates nested folders for each attempt and rank.
    

reify(_envs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L283)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.DefaultLogsSpecs.reify "Link to this definition")

Uses following scheme to build log destination paths:

*   <log\_dir>/<rdzv\_run\_id>/attempt\_<attempt>/<rank>/stdout.log
    
*   <log\_dir>/<rdzv\_run\_id>/attempt\_<attempt>/<rank>/stderr.log
    
*   <log\_dir>/<rdzv\_run\_id>/attempt\_<attempt>/<rank>/error.json
    
*   <log\_dir>/<rdzv\_run\_id>/attempt\_<attempt>/filtered\_stdout.log
    
*   <log\_dir>/<rdzv\_run\_id>/attempt\_<attempt>/filtered\_stderr.log
    

Return type:

[_LogsDest_](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsDest "torch.distributed.elastic.multiprocessing.api.LogsDest")

_class_ torch.distributed.elastic.multiprocessing.api.LogsDest(_stdouts=<factory>_, _stderrs=<factory>_, _tee\_stdouts=<factory>_, _tee\_stderrs=<factory>_, _error\_files=<factory>_, _filtered\_stdout=<factory>_, _filtered\_stderr=<factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L183)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsDest "Link to this definition")

For each log type, holds mapping of local rank ids to file paths.

_class_ torch.distributed.elastic.multiprocessing.api.LogsSpecs(_log\_dir\=None_, _redirects\=Std.NONE_, _tee\=Std.NONE_, _local\_ranks\_filter\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L198)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsSpecs "Link to this definition")

Defines logs processing and redirection for each worker process.

Parameters:

*   **log\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – Base directory where logs will be written.
    
*   **redirects** (_Std_ _|_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _Std__\]_) – Streams to redirect to files. Pass a single `Std` enum to redirect for all workers, or a mapping keyed by local\_rank to selectively redirect.
    
*   **tee** (_Std_ _|_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _Std__\]_) – Streams to duplicate to stdout/stderr. Pass a single `Std` enum to duplicate streams for all workers, or a mapping keyed by local\_rank to selectively duplicate.
    

_abstract_ reify(_envs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/api.py#L227)
[#](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsSpecs.reify "Link to this definition")

Given the environment variables, builds destination of log files for each of the local ranks.

Envs parameter contains env variables dict for each of the local ranks, where entries are defined in: `_start_workers()`.

Return type:

[_LogsDest_](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.api.LogsDest "torch.distributed.elastic.multiprocessing.api.LogsDest")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/multiprocessing.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/multiprocessing.md.txt)

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