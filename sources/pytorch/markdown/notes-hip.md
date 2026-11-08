Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/hip.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/hip.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/hip.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/hip.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/hip.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/hip.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/hip.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/hip.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/hip.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/hip.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/hip.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/hip.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/hip.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/hip.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/hip.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/hip.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/hip.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/hip.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/hip.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/hip.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/hip.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/hip.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/hip.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/hip.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/hip.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/hip.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/hip.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/hip.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/hip.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/hip.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/hip.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/hip.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/hip.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/hip.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/hip.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/hip.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/hip.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/hip.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/hip.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/hip.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/hip.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/hip.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/hip.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/hip.html)

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

HIP (ROCm) semantics[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#hip-rocm-semantics "Link to this heading")

=====================================================================================================================

Created On: May 12, 2021 | Last Updated On: Oct 01, 2026

ROCm™ is AMD’s open source software platform for GPU-accelerated high performance computing and machine learning. HIP is ROCm’s C++ dialect designed to ease conversion of CUDA applications to portable C++ code. HIP is used when converting existing CUDA applications like PyTorch to portable C++ and for new projects that require portability between AMD and NVIDIA.

HIP Interfaces Reuse the CUDA Interfaces[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#hip-interfaces-reuse-the-cuda-interfaces "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch for HIP intentionally reuses the existing [`torch.cuda`](https://docs.pytorch.org/docs/2.15/cuda.html#module-torch.cuda "torch.cuda")
 interfaces. This helps to accelerate the porting of existing PyTorch code and models because very few code changes are necessary, if any.

The example from [CUDA semantics](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics)
 will work exactly the same for HIP:

cuda \= torch.device('cuda')     \# Default HIP device
cuda0 \= torch.device('cuda:0')  \# 'rocm' or 'hip' are not valid, use 'cuda'
cuda2 \= torch.device('cuda:2')  \# GPU 2 (these are 0-indexed)

x \= torch.tensor(\[1., 2.\], device\=cuda0)
\# x.device is device(type='cuda', index=0)
y \= torch.tensor(\[1., 2.\]).cuda()
\# y.device is device(type='cuda', index=0)

with torch.cuda.device(1):
    \# allocates a tensor on GPU 1
    a \= torch.tensor(\[1., 2.\], device\=cuda)

    \# transfers a tensor from CPU to GPU 1
    b \= torch.tensor(\[1., 2.\]).cuda()
    \# a.device and b.device are device(type='cuda', index=1)

    \# You can also use \`\`Tensor.to\`\` to transfer a tensor:
    b2 \= torch.tensor(\[1., 2.\]).to(device\=cuda)
    \# b.device and b2.device are device(type='cuda', index=1)

    c \= a + b
    \# c.device is device(type='cuda', index=1)

    z \= x + y
    \# z.device is device(type='cuda', index=0)

    \# even within a context, you can specify the device
    \# (or give a GPU index to the .cuda call)
    d \= torch.randn(2, device\=cuda2)
    e \= torch.randn(2).to(cuda2)
    f \= torch.randn(2).cuda(cuda2)
    \# d.device, e.device, and f.device are all device(type='cuda', index=2)

Copy to clipboard

Checking for HIP[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#checking-for-hip "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Whether you are using PyTorch for CUDA or HIP, the result of calling [`is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_available.html#torch.cuda.is_available "torch.cuda.is_available")
 will be the same. If you are using a PyTorch that has been built with GPU support, it will return True. If you must check which version of PyTorch you are using, refer to this example below:

if torch.cuda.is\_available() and torch.version.hip:
    \# do something specific for HIP
elif torch.cuda.is\_available() and torch.version.cuda:
    \# do something specific for CUDA

Copy to clipboard

TensorFloat-32(TF32) on ROCm[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#tensorfloat-32-tf32-on-rocm "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

TF32 is supported on AMD Instinct MI300 (gfx942, CDNA3) via hipBLASLt. The same `torch.backends.cuda.matmul.fp32_precision` and `torch.backends.cuda.matmul.allow_tf32` controls used on NVIDIA hardware also apply on ROCm, except that the `"bfx9"` precision mode is NVIDIA-only and raises an error on ROCm because rocBLAS and hipBLASLt have no corresponding nine-product compute mode. The TF32 path on MI300 has hardware-level numerical differences from the NVIDIA implementation; see [TensorFloat-32 (TF32) on AMD Instinct MI300 devices](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#tf32-on-mi300)
 for details.

Memory management[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#memory-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

PyTorch uses a caching memory allocator to speed up memory allocations. This allows fast memory deallocation without device synchronizations. However, the unused memory managed by the allocator will still show as if used in `amd-smi`. You can use `memory_allocated()` and `max_memory_allocated()` to monitor memory occupied by tensors, and use `memory_reserved()` and `max_memory_reserved()` to monitor the total amount of memory managed by the caching allocator. Calling `empty_cache()` releases all **unused** cached memory from PyTorch so that those can be used by other GPU applications. However, the occupied GPU memory by tensors will not be freed so it can not increase the amount of GPU memory available for PyTorch.

For more advanced users, we offer more comprehensive memory benchmarking via `memory_stats()`. We also offer the capability to capture a complete snapshot of the memory allocator state via `memory_snapshot()`, which can help you understand the underlying allocation patterns produced by your code.

To debug memory errors, set `PYTORCH_NO_HIP_MEMORY_CACHING=1` in your environment to disable caching. `PYTORCH_NO_CUDA_MEMORY_CACHING=1` is also accepted for ease of porting.

hipBLAS workspaces[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#hipblas-workspaces "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

As on CUDA, ATen allocates a hipBLAS workspace for each operation from the HIP caching allocator and releases it when the operation returns. Set `TORCH_CUBLAS_WORKSPACE_CACHE=1` to instead retain one workspace for each hipBLAS handle and HIP stream, which was the default before PyTorch 2.15. Persistent workspaces must not be used when capturing multiple HIP graphs on the same stream.

When ATen workspace caching is disabled, ATen operations bind their workspaces to handles that `torch.cuda.current_blas_handle()` never returns. That function returns a separate handle for each thread and stream, because a rocBLAS handle’s workspace must not be used by two streams at once. When the handle is created, ATen replaces the workspace rocBLAS allocated for it with a buffer from the HIP caching allocator, so `torch.cuda.memory_allocated()` counts it. The buffer comes from a memory pool reserved for these buffers, never from a pool selected with `torch.cuda.use_mem_pool` or by CUDA graphs, and so never shares a segment with other allocations. The buffer is as large as the workspace rocBLAS allocated (128 MiB on MI355X; the size depends on the GPU, the rocBLAS version and `ROCBLAS_DEVICE_MEMORY_SIZE`), and at least the hipBLAS workspace size described below, so a `ROCBLAS_DEVICE_MEMORY_SIZE` below that size has no effect. rocBLAS never grows a bound workspace: GEMMs that need more fall back to kernels that use less, and other calls that need more fail with `rocblas_status_memory_error`. Handles are never destroyed. When a thread exits, its handles pass to other threads and streams, so the buffer stays allocated for the life of the process, and `torch.cuda.empty_cache()` does not release it. Where rocBLAS runs GEMMs through hipBLASLt, as on MI355X, each rocBLAS handle also holds about 25 MiB that hipBLASLt allocates when the handle is created, outside the caching allocator, and no API replaces it.

A workspace bound with `rocblas_set_workspace` stays bound, even after the buffer is freed, and after the thread exits and the handle passes to another thread. Unbind it with `rocblas_set_workspace(handle, nullptr, 0)` before freeing the buffer. The handle then has no workspace, and ATen does not bind its own buffer again, so GEMMs on it use kernels that need none and other calls make rocBLAS allocate a workspace outside the caching allocator, which is not allowed during capture. A caller that needs its own workspace can create its own rocBLAS handle instead. Synchronize a handle’s stream before its thread exits, and before moving the handle to another stream with `rocblas_set_stream`, as rocBLAS requires.

Call `torch.cuda.current_blas_handle()` on each thread before capture begins. It also creates ATen’s handle for that thread; an ATen warmup operation alone does not create the handle the function returns. `hipblasCreate` initializes hipBLASLt, which allocates device memory that HIP rejects on a capturing stream.

With caching disabled, while the current stream is capturing, `torch.cuda.current_blas_handle()` returns a capture handle instead. There is one per thread, and it serves every stream in the capture: each request points it at the current stream and binds a workspace for that stream allocated from the capture’s memory pool, so a graph shares its rocBLAS scratch memory neither with eager work nor with other graphs. Request the handle inside the capture instead of using one obtained before it, whose workspace eager work on that stream keeps using. When the capture ends, its workspaces return to the pool and the handle is unbound, so do not use it afterwards. Once a device’s handle has been requested, graph capture creates the capturing thread’s capture handle and one spare for another thread, such as an autograd worker, so side streams that first appear inside a capture can use the function too.

hipBLASLt handles are created for each thread and stream on first use, and creating one on a capturing stream raises an error. Graph capture creates the capture stream’s hipBLASLt handle and one spare whenever the device supports hipBLASLt, in both workspace modes, so in a capture that forks two new side streams running hipBLASLt operations such as `torch._scaled_mm`, the second raises. Run a hipBLASLt operation on each such stream before capture begins. TunableOp’s tuning benchmarks must also run outside capture. See [ROCm/rocm-libraries#11838](https://github.com/ROCm/rocm-libraries/issues/11838)
.

Extensions that call hipBLASLt themselves can use the workspace `at::cuda::getCUDABlasLtWorkspace()` returns: a buffer cached for each stream, or, with caching disabled while the stream is capturing, a buffer from the capture’s memory pool, one per stream and capture, which returns to the pool when the capture ends. Fetch it inside the capture: a buffer fetched before the capture must not be used in it.

When caching is enabled, a hipBLAS workspace is allocated for each combination of hipBLAS handle and HIP stream that executes a hipBLAS kernel requiring a workspace. In order to avoid repeatedly allocating workspaces, these workspaces are not deallocated unless `torch._C._cuda_clearCublasWorkspaces()` is called; note that it’s the same function for CUDA or HIP. The workspace size per allocation can be specified via the environment variable `HIPBLAS_WORKSPACE_CONFIG` with the format `:[SIZE]:[COUNT]`. As an example, the environment variable `HIPBLAS_WORKSPACE_CONFIG=:4096:2:16:8` specifies a total size of `2 * 4096 + 8 * 16 KiB` or 8 MIB. The default workspace size is 32 MiB; MI300 and newer defaults to 128 MiB. `HIPBLAS_WORKSPACE_CONFIG=:0:0` makes rocBLAS GEMMs use kernels that need no workspace. Unlike on CUDA, other rocBLAS calls such as `torch.dot` then have rocBLAS allocate a workspace itself, outside the caching allocator, so they cannot be captured. For convenience, `CUBLAS_WORKSPACE_CONFIG` is also accepted.

hipFFT/rocFFT plan cache[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#hipfft-rocfft-plan-cache "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Setting the size of the cache for hipFFT/rocFFT plans is not supported.

hipFile (GPUDirect Storage)[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#hipfile-gpudirect-storage "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The `torch.cuda.gds` APIs are implemented with [hipFile](https://rocm.docs.amd.com/projects/hipFile/en/latest/)
 on ROCm, taking the place of cuFile on CUDA. hipFile ships with ROCm 7.14 and later; on older ROCm the build disables GDS support and [`torch.cuda.gds.is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.is_available.html#torch.cuda.gds.is_available "torch.cuda.gds.is_available")
 returns `False`. As elsewhere in the HIP port, the build option keeps its CUDA name, so `USE_CUFILE=0` is what disables the support in a ROCm build. hipFile is Linux-only, so a Windows ROCm build never has GDS support.

Each wrapper in `torch.cuda.gds` calls the hipFile counterpart of the cuFile function named in its docstring: `hipFileRead`, `hipFileWrite`, `hipFileBufRegister`, `hipFileBufDeregister`, `hipFileHandleRegister` and `hipFileHandleDeregister`. Errors quote the hipFile name, so a failed read raises `hipFileRead failed: ...`. hipFile is close to cuFile but not identical; the known divergences, including that numeric error codes are not guaranteed to match, are listed in [cuFile compatibility](https://rocm.docs.amd.com/projects/hipFile/en/latest/reference/hipFile-cuFile-compatibility.html)
.

Configuring a system for GDS on ROCm differs from CUDA, and the NVIDIA GPUDirect Storage installation and troubleshooting guide does not apply. Refer instead to the hipFile documentation:

*   [Install hipFile](https://rocm.docs.amd.com/projects/hipFile/en/latest/install/install.html)
    
*   [Check for fastpath compatibility](https://rocm.docs.amd.com/projects/hipFile/en/latest/how-to/checking-system-compatibility.html)
    
*   [Set up a local NVMe drive](https://rocm.docs.amd.com/projects/hipFile/en/latest/how-to/setup-local-nvme.html)
    
*   [Troubleshooting](https://rocm.docs.amd.com/projects/hipFile/en/latest/troubleshooting/troubleshooting.html)
    

torch.distributed backends[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#torch-distributed-backends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Currently, only the “nccl” and “gloo” backends for torch.distributed are supported on ROCm.

CUDA API to HIP API mappings in C++[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#cuda-api-to-hip-api-mappings-in-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Please refer: [https://rocm.docs.amd.com/projects/HIP/en/latest/reference/api\_syntax.html](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/api_syntax.html)

NOTE: The CUDA\_VERSION macro, cudaRuntimeGetVersion and cudaDriverGetVersion APIs do not semantically map to the same values as HIP\_VERSION macro, hipRuntimeGetVersion and hipDriverGetVersion APIs. Please do not use them interchangeably when doing version checks.

For example: Instead of using

`#if defined(CUDA_VERSION) && CUDA_VERSION >= 11000` to implicitly exclude ROCm/HIP,

use the following to not take the code path for ROCm/HIP:

`#if defined(CUDA_VERSION) && CUDA_VERSION >= 11000 && !defined(USE_ROCM)`

Alternatively, if it is desired to take the code path for ROCm/HIP:

`#if (defined(CUDA_VERSION) && CUDA_VERSION >= 11000) || defined(USE_ROCM)`

Or if it is desired to take the code path for ROCm/HIP only for specific HIP versions:

`#if (defined(CUDA_VERSION) && CUDA_VERSION >= 11000) || (defined(USE_ROCM) && ROCM_VERSION >= 40300)`

Refer to CUDA Semantics doc[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#refer-to-cuda-semantics-doc "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

For any sections not listed here, please refer to the CUDA semantics doc: [CUDA semantics](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics)

Enabling kernel asserts[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#enabling-kernel-asserts "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

Kernel asserts are supported on ROCm, but they are disabled due to performance overhead. It can be enabled by recompiling the PyTorch from source.

Please add below line as an argument to cmake command parameters:

\-DROCM\_FORCE\_ENABLE\_GPU\_ASSERTS:BOOL\=ON

Copy to clipboard

Enabling/Disabling ROCm Composable Kernel[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#enabling-disabling-rocm-composable-kernel "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Enabling composable\_kernel (CK) for both SDPA and GEMMs is a two-part process. First the user must have built pytorch while setting the corresponding environment variable to ‘1’

SDPA: `USE_ROCM_CK_SDPA=1`

GEMMs: `USE_ROCM_CK_GEMM=1`

Second, the user must explicitly request that CK be used as the backend library via the corresponding python call

SDPA: `setROCmFAPreferredBackend('<choice>')`

GEMMs: `setBlasPreferredBackend('<choice>')`

To enable CK in either scenario, simply pass ‘ck’ to those functions.

In order to set the backend to CK, the user MUST have built with the correct environment variable. If not, PyTorch will print a warning and use the “default” backend. For GEMMs, this will route to hipblas and for SDPA it routes to aotriton.

SDPA input layout on ROCm[#](https://docs.pytorch.org/docs/2.15/notes/hip.html#sdpa-input-layout-on-rocm "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The AOTriton backend for [`scaled_dot_product_attention()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_dot_product_attention.html#torch.nn.functional.scaled_dot_product_attention "torch.nn.functional.scaled_dot_product_attention")
 selects kernel configurations from a tuning database that assumes contiguous BHSD (batch, heads, seqlen, head\_dim) inputs. Inputs that are BHSD-shaped but not contiguous, such as the view produced by `permute(0, 2, 1, 3)` on a BSHD tensor, fall outside the tuned configuration space and may select a suboptimal kernel.

Materializing contiguous inputs first trades a copy for a better kernel choice, so whether it wins depends on device, shape and dtype. It is generally not profitable on discrete GPUs, where the copy overhead tends to outweigh the kernel benefit. It has been observed to be a large win on the AMD gfx1151 iGPU at long sequence lengths (see [#190154](https://github.com/pytorch/pytorch/issues/190154)
 for measurements). Time both forms end to end, including the copies, on the shapes and dtype your model actually uses:

def sdpa\_permute(q, k, v):
    q2, k2, v2 \= (x.permute(0, 2, 1, 3) for x in (q, k, v))
    out \= torch.nn.functional.scaled\_dot\_product\_attention(q2, k2, v2)
    return out.permute(0, 2, 1, 3)

def sdpa\_contiguous(q, k, v):
    q2, k2, v2 \= (x.transpose(1, 2).contiguous() for x in (q, k, v))
    out \= torch.nn.functional.scaled\_dot\_product\_attention(q2, k2, v2)
    return out.transpose(1, 2)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/hip.rst)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/hip.rst.txt)

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