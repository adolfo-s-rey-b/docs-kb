Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/backends.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/backends.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/backends.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/backends.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/backends.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/backends.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/backends.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/backends.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/backends.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/backends.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/backends.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/backends.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/backends.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/backends.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/backends.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/backends.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/backends.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/backends.html)
[v1.13](https://docs.pytorch.org/docs/1.13/backends.html)
[v1.12](https://docs.pytorch.org/docs/1.12/backends.html)
[v1.11](https://docs.pytorch.org/docs/1.11/backends.html)
[v1.10](https://docs.pytorch.org/docs/1.10/backends.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/backends.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/backends.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/backends.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/backends.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/backends.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/backends.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/backends.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/backends.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/backends.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/backends.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/backends.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/backends.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/backends.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/backends.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/backends.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/backends.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/backends.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/backends.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/backends.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/backends.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/backends.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/backends.html)

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

torch.backends[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends "Link to this heading")

=================================================================================================================

Created On: Sep 16, 2020 | Last Updated On: Sep 02, 2026

`torch.backends` controls the behavior of various backends that PyTorch supports.

These backends include:

*   `torch.backends.cpu`
    
*   `torch.backends.cuda`
    
*   `torch.backends.cudnn`
    
*   `torch.backends.cusparselt`
    
*   `torch.backends.mha`
    
*   `torch.backends.mps`
    
*   `torch.backends.mkl`
    
*   `torch.backends.mkldnn`
    
*   `torch.backends.nnpack`
    
*   `torch.backends.openmp`
    
*   `torch.backends.opt_einsum`
    
*   `torch.backends.python_native`
    
*   `torch.backends.xeon`
    

torch.backends.cpu[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.cpu "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

torch.backends.cpu.get\_cpu\_capability()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cpu/__init__.py#L9)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cpu.get_cpu_capability "Link to this definition")

Return cpu capability as a string value.

Possible values: - “DEFAULT” - “VSX” - “Z VECTOR” - “NO AVX” - “AVX2” - “AVX512” - “SVE256”

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.backends.cuda[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.cuda "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

torch.backends.cuda.is\_built()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L43)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.is_built "Link to this definition")

Return whether PyTorch is built with CUDA support.

Note that this doesn’t necessarily mean CUDA is available; just that if this PyTorch binary were run on a machine with working CUDA drivers and devices, we would be able to use it.

torch.backends.cuda.matmul.fp32\_precision[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.fp32_precision "Link to this definition")

A [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 that controls the internal computation precision of CUDA matrix multiplications with FP32 inputs and outputs. Supported values are `"ieee"`, `"tf32"`, and `"bfx9"`. The `"bfx9"` value allows cuBLAS BF16x9 and requires a PyTorch build with CUDA 12.9 or newer. BF16x9 emulation is available on NVIDIA GPUs with compute capability 10.0 or 10.3; cuBLAS uses native FP32 on other architectures. See [TensorFloat-32 (TF32) on Ampere (and later) devices](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

torch.backends.cuda.matmul.allow\_tf32[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.allow_tf32 "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether TensorFloat-32 tensor cores may be used in matrix multiplications on Ampere or newer GPUs. allow\_tf32 is going to be deprecated. See [TensorFloat-32 (TF32) on Ampere (and later) devices](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

torch.backends.cuda.matmul.allow\_fp16\_reduced\_precision\_reduction[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether reduced precision reductions (e.g., with fp16 accumulation type) are allowed with fp16 GEMMs. For tuple assignment and split-k behavior, see [Reduced Precision Reduction in FP16 GEMMs](https://docs.pytorch.org/docs/2.15/notes/cuda.html#fp16reducedprecision)
.

torch.backends.cuda.matmul.allow\_fp16\_reduced\_precision\_reduction\_split\_k[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction_split_k "Link to this definition")

A readonly [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that reports whether split-K heuristics may be used for fp16 GEMMs when dispatching to cuBLASLt. For how this value is controlled, see [Reduced Precision Reduction in FP16 GEMMs](https://docs.pytorch.org/docs/2.15/notes/cuda.html#fp16reducedprecision)
.

torch.backends.cuda.matmul.prefer\_cublaslt\_grouped\_gemm[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.prefer_cublaslt_grouped_gemm "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether supported grouped GEMMs prefer the cuBLASLt backend.

torch.backends.cuda.matmul.allow\_bf16\_reduced\_precision\_reduction[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether reduced precision reductions are allowed with bf16 GEMMs. For tuple assignment and split-k behavior, see [Reduced Precision Reduction in BF16 GEMMs](https://docs.pytorch.org/docs/2.15/notes/cuda.html#bf16reducedprecision)
.

torch.backends.cuda.matmul.allow\_bf16\_reduced\_precision\_reduction\_split\_k[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction_split_k "Link to this definition")

A readonly [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that reports whether split-K heuristics may be used for bf16 GEMMs when dispatching to cuBLASLt. For how this value is controlled, see [Reduced Precision Reduction in BF16 GEMMs](https://docs.pytorch.org/docs/2.15/notes/cuda.html#bf16reducedprecision)
.

torch.backends.cuda.cufft\_plan\_cache[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cufft_plan_cache "Link to this definition")

`cufft_plan_cache` contains the cuFFT plan caches for each CUDA device. Query a specific device i’s cache via torch.backends.cuda.cufft\_plan\_cache\[i\].

torch.backends.cuda.cufft\_plan\_cache.size[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cufft_plan_cache.size "Link to this definition")

A readonly [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 that shows the number of plans currently in a cuFFT plan cache.

torch.backends.cuda.cufft\_plan\_cache.max\_size[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cufft_plan_cache.max_size "Link to this definition")

A [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 that controls the capacity of a cuFFT plan cache.

torch.backends.cuda.cufft\_plan\_cache.clear()[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cufft_plan_cache.clear "Link to this definition")

Clears a cuFFT plan cache.

torch.backends.cuda.preferred\_blas\_library(_backend\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L296)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.preferred_blas_library "Link to this definition")

Override the library PyTorch uses for BLAS operations. Choose between cuBLAS, cuBLASLt, and CK \[ROCm-only\].

Warning

This flag is experimental and subject to change.

When PyTorch runs a CUDA BLAS operation it defaults to cuBLAS even if both cuBLAS and cuBLASLt are available. For PyTorch built for ROCm, hipBLAS, hipBLASLt, and CK may offer different performance. This flag (a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) allows overriding which BLAS library to use.

*   If “cublas” is set then cuBLAS will be used wherever possible.
    
*   If “cublaslt” is set then cuBLASLt will be used wherever possible.
    
*   If “ck” is set then CK will be used wherever possible.
    
*   If “default” (the default) is set then heuristics will be used to pick between the other options.
    
*   When no input is given, this function returns the currently preferred library.
    
*   User may use the environment variable TORCH\_BLAS\_PREFER\_CUBLASLT=1 to set the preferred library to cuBLASLt globally. This flag only sets the initial value of the preferred library and the preferred library may still be overridden by this function call later in your script.
    

Note: When a library is preferred other libraries may still be used if the preferred library doesn’t implement the operation(s) called. This flag may achieve better performance if PyTorch’s library selection is incorrect for your application’s inputs.

Return type:

_\_BlasBackend_

torch.backends.cuda.cublas\_workspace\_size(_size\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L340)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cublas_workspace_size "Link to this definition")

Query or set the cuBLAS workspace size in bytes.

When called with no arguments, returns the current workspace size. When called with a size argument, sets the workspace size and returns the new value. Setting the workspace size will take precedence over the CUBLAS\_WORKSPACE\_CONFIG environment variable. Changes affect subsequent cuBLAS operations. When workspace caching is enabled, cached allocations are resized lazily as their handle and stream pairs are used.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – workspace size in bytes. Must be non-negative.

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.backends.cuda.cublaslt\_workspace\_size(_size\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L360)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cublaslt_workspace_size "Link to this definition")

Query or set the cuBLASLt workspace size in bytes.

When called with no arguments, returns the current workspace size. When called with a size argument, sets the workspace size and returns the new value. Setting the workspace size will take precedence over the CUBLASLT\_WORKSPACE\_SIZE environment variable. Changes affect subsequent cuBLASLt operations. When workspace caching is enabled, cached allocations are resized lazily as their handle and stream pairs are used.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – workspace size in bytes. Must be non-negative.

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.backends.cuda.blas\_workspace\_size(_size\=None_, _backend\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L380)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.blas_workspace_size "Link to this definition")

Query or set the BLAS workspace size for a given backend.

Convenience wrapper that dispatches to [`cublas_workspace_size()`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cublas_workspace_size "torch.backends.cuda.cublas_workspace_size")
 or [`cublaslt_workspace_size()`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cublaslt_workspace_size "torch.backends.cuda.cublaslt_workspace_size")
 depending on the backend.

When _backend_ is `None` the current [`preferred_blas_library()`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.preferred_blas_library "torch.backends.cuda.preferred_blas_library")
 is used. `Default` is resolved to the platform’s default backend (cuBLAS on NVIDIA, potentially hipBLASLt on supported ROCm architectures).

Note

On CUDA, when workspace caching is enabled with `TORCH_CUBLAS_WORKSPACE_CACHE=1`, `TORCH_CUBLASLT_UNIFIED_WORKSPACE` controls whether the cuBLASLt workspace is capped at the cuBLAS workspace size and physically reuses the same allocation. Unified workspaces are enabled by default on open-source CUDA builds when caching is enabled.

Note

Setting the workspace size for the cublas backend will take precedence over the CUBLAS\_WORKSPACE\_CONFIG environment variable, and setting the workspace size for the cublaslt backend will take precedence over the CUBLASLT\_WORKSPACE\_SIZE environment variable.

Parameters:

*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – workspace size in bytes. Must be non-negative. When omitted the current size is returned without modification.
    
*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _torch.\_C.\_BlasBackend__,_ _optional_) – which backend’s workspace to query/set. Accepts the same strings as [`preferred_blas_library()`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.preferred_blas_library "torch.backends.cuda.preferred_blas_library")
     (e.g. `"cublas"`, `"cublaslt"`).
    

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – if the resolved backend is CK (no workspace concept).

torch.backends.cuda.preferred\_rocm\_fa\_library(_backend\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L457)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.preferred_rocm_fa_library "Link to this definition")

\[ROCm-only\] Override the backend PyTorch uses in ROCm environments for Flash Attention. Choose between AOTriton and CK

Warning

This flag is experimental and subject to change.

When Flash Attention is enabled and desired, PyTorch defaults to using AOTriton as the backend. This flag (a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) allows users to override this backend to use composable\_kernel

*   If “default” is set then the default backend will be used wherever possible. Currently AOTriton.
    
*   If “aotriton” is set then AOTriton will be used wherever possible.
    
*   If “ck” is set then CK will be used wherever possible.
    
*   When no input is given, this function returns the currently preferred library.
    
*   User may use the environment variable TORCH\_ROCM\_FA\_PREFER\_CK=1 to set the preferred library to CK globally.
    

Note: When a library is preferred other libraries may still be used if the preferred library doesn’t implement the operation(s) called. This flag may achieve better performance if PyTorch’s library selection is incorrect for your application’s inputs.

Return type:

_\_ROCmFABackend_

torch.backends.cuda.is\_ck\_sdpa\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L502)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.is_ck_sdpa_available "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether composable\_kernel may be used as the backend for scaled-dot-product-attention.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.cuda.preferred\_linalg\_library(_backend\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L225)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.preferred_linalg_library "Link to this definition")

Override the heuristic PyTorch uses to choose between cuSOLVER and MAGMA for CUDA linear algebra operations.

Warning

This flag is experimental and subject to change.

When PyTorch runs a CUDA linear algebra operation it often uses the cuSOLVER or MAGMA libraries, and if both are available it decides which to use with a heuristic. This flag (a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) allows overriding those heuristics.

*   If “cusolver” is set then cuSOLVER will be used wherever possible.
    
*   If “magma” is set then MAGMA will be used wherever possible.
    
*   If “default” (the default) is set then heuristics will be used to pick between cuSOLVER and MAGMA if both are available.
    
*   When no input is given, this function returns the currently preferred library.
    
*   User may use the environment variable TORCH\_LINALG\_PREFER\_CUSOLVER=1 to set the preferred library to cuSOLVER globally. This flag only sets the initial value of the preferred library and the preferred library may still be overridden by this function call later in your script.
    

Note: When a library is preferred other libraries may still be used if the preferred library doesn’t implement the operation(s) called. This flag may achieve better performance if PyTorch’s heuristic library selection is incorrect for your application’s inputs.

Currently supported linalg operators:

*   [`torch.linalg.inv()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv.html#torch.linalg.inv "torch.linalg.inv")
    
*   [`torch.linalg.inv_ex()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv_ex.html#torch.linalg.inv_ex "torch.linalg.inv_ex")
    
*   [`torch.linalg.cholesky()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cholesky.html#torch.linalg.cholesky "torch.linalg.cholesky")
    
*   [`torch.linalg.cholesky_ex()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cholesky_ex.html#torch.linalg.cholesky_ex "torch.linalg.cholesky_ex")
    
*   [`torch.cholesky_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_solve.html#torch.cholesky_solve "torch.cholesky_solve")
    
*   [`torch.cholesky_inverse()`](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html#torch.cholesky_inverse "torch.cholesky_inverse")
    
*   [`torch.linalg.lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")
    
*   [`torch.linalg.lu()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html#torch.linalg.lu "torch.linalg.lu")
    
*   [`torch.linalg.lu_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_solve.html#torch.linalg.lu_solve "torch.linalg.lu_solve")
    
*   [`torch.linalg.qr()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.qr.html#torch.linalg.qr "torch.linalg.qr")
    
*   [`torch.linalg.eigh()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigh.html#torch.linalg.eigh "torch.linalg.eigh")
    
*   [`torch.linalg.eigvals()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigvals.html#torch.linalg.eigvals "torch.linalg.eigvals")
    
*   [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
    
*   [`torch.linalg.svdvals()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svdvals.html#torch.linalg.svdvals "torch.linalg.svdvals")
    

Return type:

_\_LinalgBackend_

_class_ torch.backends.cuda.SDPAParams[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.SDPAParams "Link to this definition")

torch.backends.cuda.flash\_sdp\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L513)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.flash_sdp_enabled "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether flash scaled dot product attention is enabled or not.

torch.backends.cuda.enable\_mem\_efficient\_sdp(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L540)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.enable_mem_efficient_sdp "Link to this definition")

Warning

This flag is beta and subject to change.

Enables or disables memory efficient scaled dot product attention.

torch.backends.cuda.mem\_efficient\_sdp\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L531)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.mem_efficient_sdp_enabled "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether memory efficient scaled dot product attention is enabled or not.

torch.backends.cuda.enable\_flash\_sdp(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L522)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.enable_flash_sdp "Link to this definition")

Warning

This flag is beta and subject to change.

Enables or disables flash scaled dot product attention.

torch.backends.cuda.math\_sdp\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L549)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.math_sdp_enabled "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether math scaled dot product attention is enabled or not.

torch.backends.cuda.enable\_math\_sdp(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L558)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.enable_math_sdp "Link to this definition")

Warning

This flag is beta and subject to change.

Enables or disables math scaled dot product attention.

torch.backends.cuda.fp16\_bf16\_reduction\_math\_sdp\_allowed()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L576)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.fp16_bf16_reduction_math_sdp_allowed "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether fp16/bf16 reduction in math scaled dot product attention is enabled or not.

torch.backends.cuda.allow\_fp16\_bf16\_reduction\_math\_sdp(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L567)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.allow_fp16_bf16_reduction_math_sdp "Link to this definition")

Warning

This flag is beta and subject to change.

Enables or disables fp16/bf16 reduction in math scaled dot product attention.

torch.backends.cuda.cudnn\_sdp\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L658)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.cudnn_sdp_enabled "Link to this definition")

Warning

This flag is beta and subject to change.

Returns whether cuDNN scaled dot product attention is enabled or not.

torch.backends.cuda.enable\_cudnn\_sdp(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L667)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.enable_cudnn_sdp "Link to this definition")

Warning

This flag is beta and subject to change.

Enables or disables cuDNN scaled dot product attention.

torch.backends.cuda.is\_flash\_attention\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L585)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.is_flash_attention_available "Link to this definition")

Check if PyTorch was built with FlashAttention for scaled\_dot\_product\_attention.

Returns:

True if FlashAttention is built and available; otherwise, False.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False in non-CUDA environments.

torch.backends.cuda.can\_use\_flash\_attention(_params_, _debug\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L598)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.can_use_flash_attention "Link to this definition")

Check if FlashAttention can be utilized in scaled\_dot\_product\_attention.

Parameters:

*   **params** ([_\_SDPAParams_](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.SDPAParams "torch.backends.cuda._SDPAParams")
    ) – An instance of SDPAParams containing the tensors for query, key, value, an optional attention mask, dropout rate, and a flag indicating if the attention is causal.
    
*   **debug** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to logging.warn debug information as to why FlashAttention could not be run. Defaults to False.
    

Returns:

True if FlashAttention can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False in non-CUDA environments.

torch.backends.cuda.can\_use\_efficient\_attention(_params_, _debug\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L618)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.can_use_efficient_attention "Link to this definition")

Check if efficient\_attention can be utilized in scaled\_dot\_product\_attention.

Parameters:

*   **params** ([_\_SDPAParams_](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.SDPAParams "torch.backends.cuda._SDPAParams")
    ) – An instance of SDPAParams containing the tensors for query, key, value, an optional attention mask, dropout rate, and a flag indicating if the attention is causal.
    
*   **debug** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to logging.warn with information as to why efficient\_attention could not be run. Defaults to False.
    

Returns:

True if efficient\_attention can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False in non-CUDA environments.

torch.backends.cuda.can\_use\_cudnn\_attention(_params_, _debug\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L638)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.can_use_cudnn_attention "Link to this definition")

Check if cudnn\_attention can be utilized in scaled\_dot\_product\_attention.

Parameters:

*   **params** ([_\_SDPAParams_](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.SDPAParams "torch.backends.cuda._SDPAParams")
    ) – An instance of SDPAParams containing the tensors for query, key, value, an optional attention mask, dropout rate, and a flag indicating if the attention is causal.
    
*   **debug** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to logging.warn with information as to why cuDNN attention could not be run. Defaults to False.
    

Returns:

True if cuDNN can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False in non-CUDA environments.

torch.backends.cuda.sdp\_kernel(_enable\_flash\=True_, _enable\_math\=True_, _enable\_mem\_efficient\=True_, _enable\_cudnn\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cuda/__init__.py#L676)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.sdp_kernel "Link to this definition")

Warning

This flag is beta and subject to change.

This context manager can be used to temporarily enable or disable any of the three backends for scaled dot product attention. Upon exiting the context manager, the previous state of the flags will be restored.

torch.backends.cudnn[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.cudnn "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

torch.backends.cudnn.version()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cudnn/__init__.py#L110)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.version "Link to this definition")

Return the version of cuDNN.

torch.backends.cudnn.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cudnn/__init__.py#L124)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.is_available "Link to this definition")

Return a bool indicating if CUDNN is currently available.

torch.backends.cudnn.enabled[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.enabled "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether cuDNN is enabled.

torch.backends.cudnn.allow\_tf32[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.allow_tf32 "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls where TensorFloat-32 tensor cores may be used in cuDNN convolutions on Ampere or newer GPUs. allow\_tf32 is going to be deprecated. See [TensorFloat-32 (TF32) on Ampere (and later) devices](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

torch.backends.cudnn.deterministic[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.deterministic "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that, if True, causes cuDNN to only use deterministic convolution algorithms. See also [`torch.are_deterministic_algorithms_enabled()`](https://docs.pytorch.org/docs/2.15/generated/torch.are_deterministic_algorithms_enabled.html#torch.are_deterministic_algorithms_enabled "torch.are_deterministic_algorithms_enabled")
 and [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
.

torch.backends.cudnn.benchmark[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.benchmark "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that, if True, causes cuDNN to benchmark multiple convolution algorithms and select the fastest.

torch.backends.cudnn.benchmark\_limit[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cudnn.benchmark_limit "Link to this definition")

A [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 that specifies the maximum number of cuDNN convolution algorithms to try when torch.backends.cudnn.benchmark is True. Set benchmark\_limit to zero to try every available algorithm. Note that this setting only affects convolutions dispatched via the cuDNN v8 API.

torch.backends.cusparselt[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.cusparselt "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

torch.backends.cusparselt.version()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cusparselt/__init__.py#L42)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cusparselt.version "Link to this definition")

Return the version of cuSPARSELt

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | None

torch.backends.cusparselt.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cusparselt/__init__.py#L49)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cusparselt.is_available "Link to this definition")

Return a bool indicating if cuSPARSELt is currently available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.cusparselt.get\_max\_alg\_id()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/cusparselt/__init__.py#L54)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cusparselt.get_max_alg_id "Link to this definition")

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | None

torch.backends.mha[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.mha "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

torch.backends.mha.get\_fastpath\_enabled()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mha/__init__.py#L9)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mha.get_fastpath_enabled "Link to this definition")

Returns whether fast path for TransformerEncoder and MultiHeadAttention is enabled, or `True` if jit is scripting.

Note

The fastpath might not be run even if `get_fastpath_enabled` returns `True` unless all conditions on inputs are met.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.mha.set\_fastpath\_enabled(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mha/__init__.py#L22)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mha.set_fastpath_enabled "Link to this definition")

Sets whether fast path is enabled

torch.backends.miopen[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.miopen "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

torch.backends.miopen.immediate[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.miopen.immediate "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that, if True, causes MIOpen to use Immediate Mode ([https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html](https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html)
).

torch.backends.mps[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.mps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

torch.backends.mps.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L28)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.is_available "Link to this definition")

Return a bool indicating if MPS is currently available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.mps.is\_built()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L18)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.is_built "Link to this definition")

Return whether PyTorch is built with MPS support.

Note that this doesn’t necessarily mean MPS is available; just that if this PyTorch binary were run on a machine with working MPS drivers and devices, we would be able to use it.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.mps.get\_core\_count()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L52)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.get_core_count "Link to this definition")

Return GPU core count.

According to the documentation, one core is comprised of 16 Execution Units. One execution Unit has 8 ALUs. And one ALU can run 24 threads, i.e. one core is capable of executing 3072 threads concurrently.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.backends.mps.get\_name()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L46)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.get_name "Link to this definition")

Return Metal device name

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.backends.mps.is\_macos13\_or\_newer(_minor\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L40)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.is_macos13_or_newer "Link to this definition")

Return a bool indicating whether MPS is running on MacOS 13 or newer.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.mps.is\_macos\_or\_newer(_major_, _minor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mps/__init__.py#L34)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mps.is_macos_or_newer "Link to this definition")

Return a bool indicating whether MPS is running on given MacOS or newer.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.mkl[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.mkl "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

torch.backends.mkl.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mkl/__init__.py#L5)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mkl.is_available "Link to this definition")

Return whether PyTorch is built with MKL support.

_class_ torch.backends.mkl.verbose(_enable_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mkl/__init__.py#L14)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mkl.verbose "Link to this definition")

On-demand oneMKL verbosing functionality.

To make it easier to debug performance issues, oneMKL can dump verbose messages containing execution information like duration while executing the kernel. The verbosing functionality can be invoked via an environment variable named MKL\_VERBOSE. However, this methodology dumps messages in all steps. Those are a large amount of verbose messages. Moreover, for investigating the performance issues, generally taking verbose messages for one single iteration is enough. This on-demand verbosing functionality makes it possible to control scope for verbose message dumping. In the following example, verbose messages will be dumped out for the second inference only.

import torch

model(data)
with torch.backends.mkl.verbose(torch.backends.mkl.VERBOSE\_ON):
    model(data)

Copy to clipboard

Parameters:

**level** – Verbose level - `VERBOSE_OFF`: Disable verbosing - `VERBOSE_ON`: Enable verbosing

torch.backends.mkldnn[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.mkldnn "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

torch.backends.mkldnn.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mkldnn/__init__.py#L114)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mkldnn.is_available "Link to this definition")

_class_ torch.backends.mkldnn.verbose(_level_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/mkldnn/__init__.py#L33)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.mkldnn.verbose "Link to this definition")

On-demand oneDNN (former MKL-DNN) verbosing functionality.

To make it easier to debug performance issues, oneDNN can dump verbose messages containing information like kernel size, input data size and execution duration while executing the kernel. The verbosing functionality can be invoked via an environment variable named DNNL\_VERBOSE. However, this methodology dumps messages in all steps. Those are a large amount of verbose messages. Moreover, for investigating the performance issues, generally taking verbose messages for one single iteration is enough. This on-demand verbosing functionality makes it possible to control scope for verbose message dumping. In the following example, verbose messages will be dumped out for the second inference only.

import torch

model(data)
with torch.backends.mkldnn.verbose(torch.backends.mkldnn.VERBOSE\_ON):
    model(data)

Copy to clipboard

Parameters:

**level** – Verbose level - `VERBOSE_OFF`: Disable verbosing - `VERBOSE_ON`: Enable verbosing - `VERBOSE_ON_CREATION`: Enable verbosing, including oneDNN kernel creation

torch.backends.nnpack[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.nnpack "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

torch.backends.nnpack.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/nnpack/__init__.py#L11)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.nnpack.is_available "Link to this definition")

Return whether PyTorch is built with NNPACK support.

torch.backends.nnpack.flags(_enabled\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/nnpack/__init__.py#L23)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.nnpack.flags "Link to this definition")

Context manager for setting if nnpack is enabled globally

torch.backends.nnpack.set\_flags(_\_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/nnpack/__init__.py#L16)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.nnpack.set_flags "Link to this definition")

Set if nnpack is enabled globally

torch.backends.openmp[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.openmp "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

torch.backends.openmp.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/openmp/__init__.py#L5)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.openmp.is_available "Link to this definition")

Return whether PyTorch is built with OpenMP support.

torch.backends.kleidiai.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/kleidiai/__init__.py#L5)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.kleidiai.is_available "Link to this definition")

Return whether PyTorch is built with KleidiAI support.

torch.backends.opt\_einsum[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.opt_einsum "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

torch.backends.opt\_einsum.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/opt_einsum/__init__.py#L17)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.opt_einsum.is_available "Link to this definition")

Return a bool indicating if opt\_einsum is currently available.

You must install opt-einsum in order for torch to automatically optimize einsum. To make opt-einsum available, you can install it along with torch: `pip install torch[opt-einsum]` or by itself: `pip install opt-einsum`. If the package is installed, torch will import it automatically and use it accordingly. Use this function to check whether opt-einsum was installed and properly imported by torch.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.backends.opt\_einsum.get\_opt\_einsum()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/opt_einsum/__init__.py#L30)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.opt_einsum.get_opt_einsum "Link to this definition")

Return the opt\_einsum package if opt\_einsum is currently available, else None.

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

torch.backends.opt\_einsum.enabled[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.opt_einsum.enabled "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that controls whether opt\_einsum is enabled (`True` by default). If so, torch.einsum will use opt\_einsum ([https://optimized-einsum.readthedocs.io/en/stable/path\_finding.html](https://optimized-einsum.readthedocs.io/en/stable/path_finding.html)
) if available to calculate an optimal path of contraction for faster performance.

If opt\_einsum is not available, torch.einsum will fall back to the default contraction path of left to right.

torch.backends.opt\_einsum.strategy[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.opt_einsum.strategy "Link to this definition")

A [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 that specifies which strategies to try when `torch.backends.opt_einsum.enabled` is `True`. By default, torch.einsum will try the “auto” strategy, but the “greedy” and “optimal” strategies are also supported. Note that the “optimal” strategy is factorial on the number of inputs as it tries all possible paths. See more details in opt\_einsum’s docs ([https://optimized-einsum.readthedocs.io/en/stable/path\_finding.html](https://optimized-einsum.readthedocs.io/en/stable/path_finding.html)
).

torch.backends.python\_native[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.python_native "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

The `torch.backends.python_native` module provides user control over native operators implemented in python via. DSLs (Domain Specific Languages) that are defined in `torch._native`. This allows users to selectively enable or disable high-performance implementations from various DSLs like Triton and CuteDSL.

### Module-level Functions[#](https://docs.pytorch.org/docs/2.15/backends.html#module-level-functions "Link to this heading")

torch.backends.python\_native.get\_dsl\_operations(_dsl\_name_, _lib\_symbol\='aten'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L232)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.get_dsl_operations "Link to this definition")

Get list of operations registered by a specific DSL in one namespace.

Parameters:

*   **dsl\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the DSL to query (e.g., ‘triton’, ‘cutedsl’).
    
*   **lib\_symbol** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Namespace to report on, `"aten"` by default. One namespace per call: op symbols are unique within a namespace but not across them.
    

Returns:

Sorted list of op symbols the DSL registered on `lib_symbol`.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

Example:

ops \= torch.backends.python\_native.get\_dsl\_operations("triton")
print(ops)  \# \['triton\_to\_mxfp8\_dim0', ...\]

Copy to clipboard

torch.backends.python\_native.disable\_operations(_\*op\_symbols_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L254)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.disable_operations "Link to this definition")

Disable specific operations across all DSLs.

Parameters:

**\*op\_symbols** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Names of operations to disable.

Example:

\# Disable scaled matrix multiply across all DSLs
torch.backends.python\_native.disable\_operations("scaled\_mm")

\# Disable multiple operations
torch.backends.python\_native.disable\_operations(
    "scaled\_mm", "flash\_attention"
)

Copy to clipboard

torch.backends.python\_native.enable\_operations(_\*op\_symbols_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L273)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.enable_operations "Link to this definition")

Re-enable specific operations across all DSLs.

Parameters:

**\*op\_symbols** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Names of operations to re-enable.

Example:

\# Re-enable previously disabled operations
torch.backends.python\_native.enable\_operations(
    "scaled\_mm", "flash\_attention"
)

Copy to clipboard

torch.backends.python\_native.disable\_dispatch\_keys(_\*dispatch\_keys_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L289)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.disable_dispatch_keys "Link to this definition")

Disable operations at specific dispatch keys.

Parameters:

**\*dispatch\_keys** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Dispatch keys to disable (e.g., ‘CUDA’, ‘CPU’).

Example:

\# Disable all native operations on CUDA
torch.backends.python\_native.disable\_dispatch\_keys("CUDA")

Copy to clipboard

torch.backends.python\_native.enable\_dispatch\_keys(_\*dispatch\_keys_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L303)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.enable_dispatch_keys "Link to this definition")

Re-enable operations at specific dispatch keys.

Parameters:

**\*dispatch\_keys** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Dispatch keys to re-enable (e.g., ‘CUDA’, ‘CPU’).

Example:

\# Re-enable native operations on CUDA
torch.backends.python\_native.enable\_dispatch\_keys("CUDA")

Copy to clipboard

torch.backends.python\_native.operations\_disabled(_\*op\_symbols_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/python_native/__init__.py#L317)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.operations_disabled "Link to this definition")

Context manager to temporarily disable operations.

Parameters:

**\*op\_symbols** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Names of operations to temporarily disable.

Example:

with torch.backends.python\_native.operations\_disabled("scaled\_mm"):
    \# scaled\_mm is disabled across all DSLs
    result \= model(input)
\# scaled\_mm is automatically re-enabled here

Copy to clipboard

### Module-level Properties[#](https://docs.pytorch.org/docs/2.15/backends.html#module-level-properties "Link to this heading")

torch.backends.python\_native.available\_dsls[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.available_dsls "Link to this definition")

A [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
 of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 containing the names of DSLs that are available at runtime. This is a subset of [`all_dsls`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.all_dsls "torch.backends.python_native.all_dsls")
 that have their runtime dependencies satisfied.

torch.backends.python\_native.all\_dsls[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.python_native.all_dsls "Link to this definition")

A [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
 of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 containing the names of all registered DSLs, whether available at runtime or not.

### DSL Controllers[#](https://docs.pytorch.org/docs/2.15/backends.html#dsl-controllers "Link to this heading")

For each registered DSL (e.g., `triton`, `cutedsl`), auto-populated controller modules are available:

#### DSL Properties[#](https://docs.pytorch.org/docs/2.15/backends.html#dsl-properties "Link to this heading")

Each DSL controller (e.g., `torch.backends.python_native.triton`) provides the following properties:

| Property | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the DSL |
| `available` | `bool` | Whether the DSL’s runtime dependencies are available |
| `enabled` | `bool` | Controls whether all operations from this DSL are enabled. Setting to `False` disables all operations from the DSL, while `True` re-enables them |
| `version` | `Version` or `None` | The version of the DSL runtime, if available. Returns `None` if the DSL is not available |

#### DSL Methods[#](https://docs.pytorch.org/docs/2.15/backends.html#dsl-methods "Link to this heading")

Each DSL controller provides the following methods:

**disable()** Disable all operations from this DSL.

**enable()** Re-enable all operations from this DSL.

**disabled()** Context manager that temporarily disables all operations from this DSL. Operations are automatically re-enabled when exiting the context.

Example::

    with torch.backends.python\_native.triton.disabled():
        # Triton operations are disabled here
        result = model(input)
    # Triton operations restored here

Copy to clipboard

### Usage Examples[#](https://docs.pytorch.org/docs/2.15/backends.html#usage-examples "Link to this heading")

import torch.backends.python\_native as pn

\# Query available DSLs
print(pn.available\_dsls)  \# \['triton', 'cutedsl'\]

\# Disable all Triton operations
pn.triton.enabled \= False

\# Temporarily disable CuteDSL operations
with pn.cutedsl.disabled():
    result \= model(input)  \# CuteDSL ops disabled

\# Disable specific operations across all DSLs
pn.disable\_operations('scaled\_mm', '\_flash\_attention\_forward')

\# Query operations for a specific DSL
triton\_ops \= pn.get\_dsl\_operations('triton')

Copy to clipboard

torch.backends.xeon[#](https://docs.pytorch.org/docs/2.15/backends.html#module-torch.backends.xeon "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

torch.backends.xeon.run\_cpu.create\_args(_parser\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/backends/xeon/run_cpu.py#L913)
[#](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.xeon.run_cpu.create_args "Link to this definition")

Parse the command line options.

@retval ArgumentParser

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/backends.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/backends.md.txt)

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