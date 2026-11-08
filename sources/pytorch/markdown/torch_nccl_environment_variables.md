Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch_nccl_environment_variables.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch_nccl_environment_variables.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch_nccl_environment_variables.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch_nccl_environment_variables.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch_nccl_environment_variables.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch_nccl_environment_variables.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch_nccl_environment_variables.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch_nccl_environment_variables.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch_nccl_environment_variables.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch_nccl_environment_variables.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch_nccl_environment_variables.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch_nccl_environment_variables.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch_nccl_environment_variables.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch_nccl_environment_variables.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch_nccl_environment_variables.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch_nccl_environment_variables.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch_nccl_environment_variables.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch_nccl_environment_variables.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch_nccl_environment_variables.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch_nccl_environment_variables.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch_nccl_environment_variables.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch_nccl_environment_variables.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch_nccl_environment_variables.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch_nccl_environment_variables.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch_nccl_environment_variables.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch_nccl_environment_variables.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch_nccl_environment_variables.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch_nccl_environment_variables.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch_nccl_environment_variables.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch_nccl_environment_variables.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch_nccl_environment_variables.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch_nccl_environment_variables.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch_nccl_environment_variables.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch_nccl_environment_variables.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch_nccl_environment_variables.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch_nccl_environment_variables.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch_nccl_environment_variables.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch_nccl_environment_variables.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch_nccl_environment_variables.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch_nccl_environment_variables.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch_nccl_environment_variables.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch_nccl_environment_variables.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch_nccl_environment_variables.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch_nccl_environment_variables.html)

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

PYTORCH ProcessGroupNCCL Environment Variables[#](https://docs.pytorch.org/docs/2.15/torch_nccl_environment_variables.html#pytorch-processgroupnccl-environment-variables "Link to this heading")

==================================================================================================================================================================================================

Created On: Jun 10, 2025 | Last Updated On: Jun 10, 2025

For more information on the environment variables, see [ProcessGroupNCCL Environment Variables](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/ProcessGroupNCCL.hpp)
.

| **Variable** | **Description** |
| --- | --- |
| `TORCH_NCCL_ASYNC_ERROR_HANDLING` | Control how we perform Async Error Handling with NCCL when an exception is observed in watchdog. If set to 0, no handling of asynchronous NCCL errors. If set to 1, aborting NCCL communicator and tearing down process upon error. If set to 2, only abort NCCL communicator and if set to 3, tearing down process without aborting NCCL communicator. By default, it is set to 3. |
| `TORCH_NCCL_HIGH_PRIORITY` | Control whether to use high priority stream for the NCCL communicator. |
| `TORCH_NCCL_BLOCKING_WAIT` | Control whether or not wait() is blocking or non-blocking. |
| `TORCH_NCCL_DUMP_ON_TIMEOUT` | Control whether dumping debug info on watchdog timeout or exception is detected. This variable must be set together with TORCH\_NCCL\_TRACE\_BUFFER\_SIZE larger than 0. |
| `TORCH_NCCL_DESYNC_DEBUG` | Control whether Desync Debug is enabled. This is helpful in figuring out the culprit rank of collective desync. |
| `TORCH_NCCL_ENABLE_TIMING` | If set to `1`, enable recording start-events for all ProcessGroupNCCL collectives, and compute accurate collective timing per-collective. |
| `TORCH_NCCL_ENABLE_MONITORING` | If set to `1`,enable monitoring thread which aborts the process when the ProcessGroupNCCL Watchdog thread gets stuck and no heartbeat is detected after TORCH\_NCCL\_HEARTBEAT\_TIMEOUT\_SEC. This can happen due to calling CUDA/NCCL APIs that may hang. It is Useful to prevent jobs being stuck for a prolonged time than necessary tying up cluster resources. |
| `TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC` | Control the watchdog heartbeat timeout period after which the monitoring thread will abort the process. |
| `TORCH_NCCL_TRACE_BUFFER_SIZE` | The maximum number of events we store in the flight recorder’s ring buffer. One event could be the start or end of a collective, for example. Set to 0 to disable the tracebuffer and debugging info dump. |
| `TORCH_NCCL_TRACE_CPP_STACK` | Whether to collect cpp stack traces for flight recorder. Default value is False. |
| `TORCH_NCCL_COORD_CHECK_MILSEC` | Control the interval inside the monitoring thread to check the coordinated signal from other ranks, e.g. to dump the debugging information. Default value is 1000 ms. |
| `TORCH_NCCL_WAIT_TIMEOUT_DUMP_MILSEC` | Control how much extra time we will wait for dumping the debugging info before we exit and throws timeout exception. |
| `TORCH_NCCL_DEBUG_INFO_TEMP_FILE` | The file into which the debugging info would be dumped. |
| `TORCH_NCCL_DEBUG_INFO_PIPE_FILE` | The pipe file to trigger debugging dump manually, write anything into the pipe would trigger the dump. |
| `TORCH_NCCL_NAN_CHECK` | Control whether to enable NAN check for the input, Error would be thrown if NAN is detected. |

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch_nccl_environment_variables.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch_nccl_environment_variables.md.txt)

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