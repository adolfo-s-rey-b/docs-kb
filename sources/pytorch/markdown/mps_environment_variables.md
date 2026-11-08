Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/mps_environment_variables.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/mps_environment_variables.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/mps_environment_variables.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/mps_environment_variables.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/mps_environment_variables.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/mps_environment_variables.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/mps_environment_variables.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/mps_environment_variables.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/mps_environment_variables.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/mps_environment_variables.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/mps_environment_variables.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/mps_environment_variables.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/mps_environment_variables.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/mps_environment_variables.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/mps_environment_variables.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/mps_environment_variables.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/mps_environment_variables.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/mps_environment_variables.html)
[v1.13](https://docs.pytorch.org/docs/1.13/mps_environment_variables.html)
[v1.12](https://docs.pytorch.org/docs/1.12/mps_environment_variables.html)
[v1.11](https://docs.pytorch.org/docs/1.11/mps_environment_variables.html)
[v1.10](https://docs.pytorch.org/docs/1.10/mps_environment_variables.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/mps_environment_variables.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/mps_environment_variables.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/mps_environment_variables.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/mps_environment_variables.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/mps_environment_variables.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/mps_environment_variables.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/mps_environment_variables.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/mps_environment_variables.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/mps_environment_variables.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/mps_environment_variables.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/mps_environment_variables.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/mps_environment_variables.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/mps_environment_variables.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/mps_environment_variables.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/mps_environment_variables.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/mps_environment_variables.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/mps_environment_variables.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/mps_environment_variables.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/mps_environment_variables.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/mps_environment_variables.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/mps_environment_variables.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/mps_environment_variables.html)

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

MPS Environment Variables[#](https://docs.pytorch.org/docs/2.15/mps_environment_variables.html#mps-environment-variables "Link to this heading")

=================================================================================================================================================

Created On: Jun 11, 2025 | Last Updated On: Sep 12, 2026

**PyTorch Environment Variables**

| Variable | Description |
| --- | --- |
| `PYTORCH_DEBUG_MPS_ALLOCATOR` | If set to `1`, set allocator logging level to verbose. |
| `PYTORCH_MPS_LOG_PROFILE_INFO` | Set log options bitmask to `MPSProfiler`. See `LogOptions` enum in `aten/src/ATen/mps/MPSProfiler.h`. |
| `PYTORCH_MPS_TRACE_SIGNPOSTS` | Set profile and signpost bitmasks to `MPSProfiler`. See `ProfileOptions` and `SignpostTypes`. |
| `PYTORCH_MPS_HIGH_WATERMARK_RATIO` | High watermark ratio for MPS allocator. Default is 1.7. |
| `PYTORCH_MPS_LOW_WATERMARK_RATIO` | Low watermark ratio for MPS allocator. Default is 1.4 (unified) or 1.0 (discrete). |
| `PYTORCH_MPS_FAST_MATH` | If `1`, enables fast math for MPS kernels. See section 1.6.3 in the [Metal Shading Language Spec](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)<br>. |
| `PYTORCH_MPS_PREFER_METAL` | If `1`, uses metal kernels instead of MPS Graph APIs. Used for matmul. |
| `PYTORCH_MPS_METAL_VERSION` | Caps the Metal language version used by the MPS backend, given as `major.minor` (e.g. `3.1`). Setting it below `4.0` loads the Metal 3 shader library and disables the MetalPerformancePrimitives kernels, even on macOS 26. |
| `PYTORCH_ENABLE_MPS_FALLBACK` | If `1`, falls back to CPU when MPS ops aren’t supported. |

Note

**high watermark ratio** is a hard limit for the total allowed allocations

*   `0.0` : disables high watermark limit (may cause system failure if system-wide OOM occurs)
    
*   `1.0` : recommended maximum allocation size (i.e., device.recommendedMaxWorkingSetSize)
    
*   `>1.0`: allows limits beyond the device.recommendedMaxWorkingSetSize
    

e.g., value 0.95 means we allocate up to 95% of recommended maximum allocation size; beyond that, the allocations would fail with OOM error.

**low watermark ratio** is a soft limit to attempt limiting memory allocations up to the lower watermark level by garbage collection or committing command buffers more frequently (a.k.a, adaptive commit). Value between 0 to m\_high\_watermark\_ratio (setting 0.0 disables adaptive commit and garbage collection) e.g., value 0.9 means we ‘attempt’ to limit allocations up to 90% of recommended maximum allocation size.

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/mps_environment_variables.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/mps_environment_variables.md.txt)

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