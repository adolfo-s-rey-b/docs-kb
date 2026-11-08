Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/errors.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/errors.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/errors.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/errors.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/errors.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/errors.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/errors.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/errors.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/errors.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/errors.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/errors.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/errors.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/errors.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/errors.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/errors.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/errors.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/errors.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/errors.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/errors.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/errors.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/errors.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/errors.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/errors.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/errors.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/errors.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/errors.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/errors.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/errors.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/errors.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/errors.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/errors.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/errors.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/errors.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/errors.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/errors.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/errors.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/errors.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/errors.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/errors.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/errors.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/errors.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/errors.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/errors.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/errors.html)

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

Error Propagation[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#module-torch.distributed.elastic.multiprocessing.errors "Link to this heading")

============================================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 08, 2026

Each host in a distributed PyTorch job runs with a single TorchElastic agent, and multiple workers (as children processes of the TorchElastic agent). Since the workers are user-provided (your PyTorch script/job), TorchElastic has a way to propagate errors on the trainers through the agent and up to the scheduler, which ultimately informs the end-user about the state of the job and applies any retry policies.

TorchElastic categorizes errors into 3 categories:

| Category | Sub-Category | Description |
| --- | --- | --- |
| User Error | Input Error | invalid inputs to TorchElastic APIs (e.g. min > max nodes) |
| Worker Failure | any failures on the worker child process |
| Platform Error | n/a | failures caused by the agent |
| Infra Error | n/a | failures outside the domain of the agent and workers (e.g. host failures) |

All errors other than “Worker Failure” are either raised canonically from the agent process or implicitly or explicitly crash the agent process. So the standard language (python) provided exception handling strategies apply.

Worker Failures are special because the exception/failure originates on a different process from the agent so the error needs to be propagated inter-process (e.g. the agent cannot simply `try-catch` an exception raised on the worker process).

TorchElastic agents use [`torch.distributed.elastic.multiprocessing.start_processes()`](https://docs.pytorch.org/docs/2.15/elastic/multiprocessing.html#torch.distributed.elastic.multiprocessing.start_processes "torch.distributed.elastic.multiprocessing.start_processes")
 to launch the workers which has a simple file based inter-process error propagation built-in.

Any function or binary entrypoint decorated with [`record()`](https://docs.pytorch.org/docs/2.15/elastic/errors.html#torch.distributed.elastic.multiprocessing.errors.record "torch.distributed.elastic.multiprocessing.errors.record")
 will write uncaught exceptions (with the trace information) to a file specified by the environment variable `TORCHELASTIC_ERROR_FILE`. The parent process (e.g. agent) sets this env var on each child it launches, then aggregates the error files for all children, and propagates the one with the **smallest** timestamp (e.g. the **first** error).

Methods and Classes[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#methods-and-classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

torch.distributed.elastic.multiprocessing.errors.record(_fn_, _error\_handler\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/errors/__init__.py#L331)
[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#torch.distributed.elastic.multiprocessing.errors.record "Link to this definition")

Syntactic sugar to record errors/exceptions that happened in the decorated function using the provided `error_handler`.

Using this decorator is equivalent to:

error\_handler \= get\_error\_handler()
error\_handler.set\_entrypoint\_fn\_name(foobar.\_\_qualname\_\_)
error\_handler.initialize()
try:
    foobar()
except ChildFailedError as e:
    \_, failure \= e.get\_first\_failure()
    error\_handler.dump\_error\_file(failure.error\_file, failure.exitcode)
    raise
except Exception as e:
    error\_handler.record\_exception(e)
    raise

Copy to clipboard

Important

use this decorator once per process at the top level method, typically this is the main method.

Example

@record
def main():
    pass

if \_\_name\_\_ \== "\_\_main\_\_":
    main()

Copy to clipboard

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[~\_P\], _\_R_ | None\]

_class_ torch.distributed.elastic.multiprocessing.errors.ChildFailedError(_name_, _failures_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/errors/__init__.py#L205)
[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#torch.distributed.elastic.multiprocessing.errors.ChildFailedError "Link to this definition")

Special exception type that can be raised from a function annotated with the `@record` decorator to have the child process’ (root exception) propagate up the stack as-is (e.g. without being wrapped in the parent’s traceback).

Useful in cases where the parent is a simple nanny process and the child (worker) processes are actually doing meaningful compute. In this case, errors typically occur on the child process as the parent is not doing anything non-trivial, and child errors should be propagated to the scheduler for accurate root cause diagnostics.

Note

The propagation relies on error files rather than exception handling to support both function and binary launches.

Example:

\# process tree on a host (container)
0: scheduler\-init\-process:
           |- 1: torchelastic\_agent:
                    |- 2: trainer\_0 (ok)
                    |- 3: trainer\_1 (fail) \-> error.json
                    |- ...
                    |- n+2: trainer\_n (ok)
           |- n+3: other processes
           |- ...

Copy to clipboard

In the example above, trainer 1’s failure (written into error.json) is the root cause and should be reported to the scheduler’s init process. The torchelastic agent raises a `ChildFailedError("trainer", {1: "trainer_1/error.json"})` upon detecting trainer 1’s failure which would propagate the contents of trainer 1’s error file to the scheduler’s init process.

_class_ torch.distributed.elastic.multiprocessing.errors.ErrorHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/errors/error_handler.py#L24)
[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#torch.distributed.elastic.multiprocessing.errors.ErrorHandler "Link to this definition")

Write the provided exception object along with some other metadata about the error in a structured way in JSON format to an error file specified by the environment variable: `TORCHELASTIC_ERROR_FILE`. If this environment variable is not set, then simply logs the contents of what would have been written to the error file.

This handler may be subclassed to customize the handling of the error. Subclasses should override `initialize()` and `record_exception()`.

_class_ torch.distributed.elastic.multiprocessing.errors.ProcessFailure(_local\_rank_, _pid_, _exitcode_, _error\_file_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/errors/__init__.py#L91)
[#](https://docs.pytorch.org/docs/2.15/elastic/errors.html#torch.distributed.elastic.multiprocessing.errors.ProcessFailure "Link to this definition")

Represent the failed process result. When the worker process fails, it may record failure root cause into the file.

Tries to read the failure timestamp from the provided `error_file`, if the `error_file` does not exist, the timestamp is the current timestamp (seconds since epoch).

The `message` field is a concise explanation of the failure. If the error file exists then the message is obtained from the error file. Otherwise one is generated based on the failure signature.

Note

It is assumed that the `error_file` is written by `torch.distributed.elastic.multiprocessing.errors.error_handler.ErrorHandler`. Otherwise the behavior is undefined.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/errors.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/errors.md.txt)

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