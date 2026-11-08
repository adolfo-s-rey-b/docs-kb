Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cuda_environment_variables.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cuda_environment_variables.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cuda_environment_variables.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cuda_environment_variables.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cuda_environment_variables.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cuda_environment_variables.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cuda_environment_variables.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cuda_environment_variables.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cuda_environment_variables.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cuda_environment_variables.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cuda_environment_variables.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cuda_environment_variables.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cuda_environment_variables.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cuda_environment_variables.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cuda_environment_variables.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cuda_environment_variables.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cuda_environment_variables.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cuda_environment_variables.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cuda_environment_variables.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cuda_environment_variables.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cuda_environment_variables.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cuda_environment_variables.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cuda_environment_variables.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cuda_environment_variables.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cuda_environment_variables.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cuda_environment_variables.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cuda_environment_variables.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cuda_environment_variables.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cuda_environment_variables.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cuda_environment_variables.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cuda_environment_variables.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cuda_environment_variables.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cuda_environment_variables.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cuda_environment_variables.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cuda_environment_variables.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cuda_environment_variables.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cuda_environment_variables.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cuda_environment_variables.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cuda_environment_variables.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cuda_environment_variables.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cuda_environment_variables.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cuda_environment_variables.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cuda_environment_variables.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cuda_environment_variables.html)

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

CUDA Environment Variables[#](https://docs.pytorch.org/docs/2.15/cuda_environment_variables.html#cuda-environment-variables "Link to this heading")

====================================================================================================================================================

Created On: May 08, 2026 | Last Updated On: Sep 05, 2026

For more information on CUDA runtime environment variables, see [CUDA Environment Variables](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars)
.

**PyTorch Environment Variables**

| Variable | Description |
| --- | --- |
| `PYTORCH_NO_CUDA_MEMORY_CACHING` | If set to `1`, disables caching of memory allocations in CUDA. This can be useful for debugging. |
| `PYTORCH_ALLOC_CONF` | For a more in depth explanation of this environment variable, see [Memory management](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-memory-management)<br>. `PYTORCH_CUDA_ALLOC_CONF` is its alias and is provided only for backward compatibility. |
| `PYTORCH_NVML_BASED_CUDA_CHECK` | If set to `1`, before importing PyTorch modules that check if CUDA is available, PyTorch will use NVML to check if the CUDA driver is functional instead of using the CUDA runtime. This can be helpful if forked processes fail with a CUDA initialization error. |
| `TORCH_CUDNN_V8_API_LRU_CACHE_LIMIT` | The cache limit for the cuDNN v8 API. This is used to limit the memory used by the cuDNN v8 API. The default value is 10000, which roughly corresponds to 2GiB assuming 200KiB per ExecutionPlan. Set to `0` for no limit or a negative value for no caching. |
| `TORCH_CUDNN_V8_API_DISABLED` | If set to `1`, disables the cuDNN v8 API. And will fall back to the cuDNN v7 API. |
| `TORCH_ALLOW_TF32_CUBLAS_OVERRIDE` | If set to `1`, forces TF32 enablement, overrides `set_float32_matmul_precision` setting. |
| `TORCH_CUBLAS_WORKSPACE_CACHE` | If set to `1`, retains ATen’s cuBLAS and cuBLASLt workspaces per handle and stream instead of allocating them for each ATen operation, which is the default. This is separate from the CUDA allocator’s caching of freed device memory. Persistent ATen workspaces should not be used when capturing multiple CUDA graphs on the same stream. Handles returned by `torch.cuda.current_blas_handle()` use cuBLAS’s default workspace when this variable is unset. |
| `TORCH_CUBLASLT_UNIFIED_WORKSPACE` | Controls whether cached cuBLAS and cuBLASLt workspaces share an allocation. This only takes effect when `TORCH_CUBLAS_WORKSPACE_CACHE=1`. |
| `TORCH_NCCL_USE_COMM_NONBLOCKING` | If set to `1`, enables non-blocking error handling in NCCL. |
| `TORCH_CUDNN_V8_API_DEBUG` | If set to `1`, sanity check whether cuDNN V8 is being used. |

**CUDA Runtime and Libraries Environment Variables**

| Variable | Description |
| --- | --- |
| `CUDA_VISIBLE_DEVICES` | Comma-separated list of GPU device IDs that should be made available to CUDA runtime. If set to `-1`, no GPUs are made available. |
| `CUDA_LAUNCH_BLOCKING` | If set to `1`, makes CUDA calls synchronous. This can be useful for debugging. |
| `CUBLAS_WORKSPACE_CONFIG` | This environment variable is used to set the workspace configuration for cuBLAS per allocation. The format is `:[SIZE]:[COUNT]`. For example, `CUBLAS_WORKSPACE_CONFIG=:4096:2:16:8` specifies a total size of `2 * 4096 + 8 * 16 KiB`. To force cuBLAS to avoid using workspaces, set `CUBLAS_WORKSPACE_CONFIG=:0:0`. |
| `CUDNN_CONV_WSCAP_DBG` | Similar to `CUBLAS_WORKSPACE_CONFIG`, this environment variable is used to set the workspace configuration for cuDNN per allocation. |
| `CUBLASLT_WORKSPACE_SIZE` | Similar to `CUBLAS_WORKSPACE_CONFIG`, this environment variable is used to set the workspace size for cuBLASLT. |
| `CUDNN_ERRATA_JSON_FILE` | Can be set to a file path for an errata filter that can be passed to cuDNN to avoid specific engine configs, used primarily for debugging or to hardcode autotuning. |
| `NVIDIA_TF32_OVERRIDE` | If set to `0`, disables TF32 globally across all kernels, overriding all PyTorch settings. |

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cuda_environment_variables.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cuda_environment_variables.md.txt)

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