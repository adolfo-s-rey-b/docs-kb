Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.get_capabilities.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cpu.get_capabilities.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.get_capabilities.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cpu.get_capabilities.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cpu.get_capabilities.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cpu.get_capabilities.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cpu.get_capabilities.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cpu.get_capabilities.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cpu.get_capabilities.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cpu.get_capabilities.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cpu.get_capabilities.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cpu.get_capabilities.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cpu.get_capabilities.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cpu.get_capabilities.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cpu.get_capabilities.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cpu.get_capabilities.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cpu.get_capabilities.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cpu.get_capabilities.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cpu.get_capabilities.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cpu.get_capabilities.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cpu.get_capabilities.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cpu.get_capabilities.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cpu.get_capabilities.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cpu.get_capabilities.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cpu.get_capabilities.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cpu.get_capabilities.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cpu.get_capabilities.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cpu.get_capabilities.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cpu.get_capabilities.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cpu.get_capabilities.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cpu.get_capabilities.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cpu.get_capabilities.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cpu.get_capabilities.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cpu.get_capabilities.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cpu.get_capabilities.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cpu.get_capabilities.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cpu.get_capabilities.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cpu.get_capabilities.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cpu.get_capabilities.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cpu.get_capabilities.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cpu.get_capabilities.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cpu.get_capabilities.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cpu.get_capabilities.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cpu.get_capabilities.html)

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

torch.cpu.get\_capabilities[#](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.get_capabilities.html#torch-cpu-get-capabilities "Link to this heading")

===============================================================================================================================================================

torch.cpu.get\_capabilities()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cpu/__init__.py#L35)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.get_capabilities.html#torch.cpu.get_capabilities "Link to this definition")

Returns an immutable mapping of CPU capabilities detected at runtime.

This function queries the CPU for supported instruction sets and features using cpuinfo. The result is cached after the first call for efficiency.

The returned mapping contains architecture-specific capabilities:

For x86/x86\_64:

*   SSE family: sse, sse2, sse3, ssse3, sse4\_1, sse4\_2, sse4a
    
*   AVX family: avx, avx2, avx\_vnni
    
*   AVX-512 family: avx512\_f, avx512\_cd, avx512\_dq, avx512\_bw, avx512\_vl, avx512\_ifma, avx512\_vbmi, avx512\_vbmi2, avx512\_bitalg, avx512\_vpopcntdq, avx512\_vnni, avx512\_bf16, avx512\_fp16, avx512\_vp2intersect, avx512\_4vnniw, avx512\_4fmaps
    
*   AVX10 family: avx10\_1, avx10\_2
    
*   AVX-VNNI-INT: avx\_vnni\_int8, avx\_vnni\_int16, avx\_ne\_convert
    
*   AMX: amx\_bf16, amx\_tile, amx\_int8, amx\_fp16
    
*   FMA: fma3, fma4
    
*   Other: f16c, bmi, bmi2, popcnt, lzcnt, aes, sha, clflush, clflushopt, clwb
    

For ARM64:

*   SIMD: neon, fp16\_arith, bf16, i8mm, dot
    
*   SVE: sve, sve2, sve\_bf16, sve\_max\_length (when supported)
    
*   SME: sme, sme2, sme\_max\_length (when supported)
    
*   Other: atomics, fhm, rdm, crc32, aes, sha1, sha2, pmull
    

Common to all architectures:

*   architecture: string identifying the CPU architecture
    

Returns:

An immutable mapping where keys are capability names (e.g., ‘avx2’, ‘sve’) and values are booleans indicating support, or integers for properties like vector lengths.

Return type:

MappingProxyType

Example

\>>> caps \= torch.cpu.get\_capabilities()
\>>> if caps.get("avx2", False):
...     print("AVX2 is supported")
\>>> print(f"Architecture: {caps\['architecture'\]}")

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cpu.get_capabilities.rst.txt)

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