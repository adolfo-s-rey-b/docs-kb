Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/amp.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/amp.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/amp.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/amp.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/amp.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/amp.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/amp.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/amp.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/amp.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/amp.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/amp.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/amp.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/amp.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/amp.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/amp.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/amp.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/amp.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/amp.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/amp.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/amp.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/amp.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/amp.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/amp.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/amp.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/amp.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/amp.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/amp.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/amp.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/amp.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/amp.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/amp.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/amp.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/amp.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/amp.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/amp.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/amp.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/amp.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/amp.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/amp.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/amp.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/amp.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/amp.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/amp.html)

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

Automatic Mixed Precision[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#automatic-mixed-precision "Link to this heading")

=======================================================================================================================================

Created On: Sep 30, 2025 | Last Updated On: Sep 30, 2025

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#background "Link to this heading")

---------------------------------------------------------------------------------------------------------

Automatic Mixed Precision (AMP) enables the use of both single precision (32-bit) and half precision (16-bit) floating point types during training or inference.

Key components include:

*   [**Autocast**](https://docs.pytorch.org/docs/stable/amp.html#autocasting)
    : Automatically casts operations to lower-precision (e.g., float16 or bfloat16) to improve performance while maintaining accuracy.
    
*   [**Gradient Scaling**](https://docs.pytorch.org/docs/stable/amp.html#gradient-scaling)
    : Dynamically scales gradients during backpropagation to prevent underflow when training with mixed precision.
    

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#design "Link to this heading")

-------------------------------------------------------------------------------------------------

### Casting Strategy[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#casting-strategy "Link to this heading")

The [`CastPolicy`](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L416-L438)
 is used to define type conversion rules. Each enum value represents a set of type conversion requirements for a group of operators, ensuring consistent handling of operations that prioritize either precision or performance.

| Policy | Explanation |
| --- | --- |
| **`lower_precision_fp`** | Cast all inputs to `lower_precision_fp` before execute the op. |
| **`fp32`** | Cast all inputs to `at::kFloat` before running the op. |
| **`fp32_set_opt_dtype`** | Execution in `at::kFloat`, while respecting user-specified output dtype if provided. |
| **`fp32_append_dtype`** | Append at::kFloat to the args and redispatch to the type-aware overload |
| **`promote`** | Promote all inputs to the “widest” dtype before execution. |

### Operators Lists[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#operators-lists "Link to this heading")

PyTorch defines a general list of operators for each of casting strategies mentioned above, as a reference for developers of new accelerators.

| Policy | Operators List |
| --- | --- |
| **`lower_precision_fp`** | [List Link](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L819-L852) |
| **`fp32`** | [List Link](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L854-L912) |
| **`fp32_set_opt_dtype`** | [List Link](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L914-L931) |
| **`fp32_append_dtype`** | [List Link](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L933-L958) |
| **`promote`** | [List Link](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/autocast_mode.h#L960-L971) |

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#implementation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

### Python Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#python-integration "Link to this heading")

Implement the `get_amp_supported_dtype` method to return the data types supported by the new accelerator in the AMP context.

1def get\_amp\_supported\_dtype():
2    return \[torch.float16, torch.bfloat16\]
3
4

Copy to clipboard

### C++ Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/amp.html#c-integration "Link to this heading")

This section shows how AMP registers autocast kernels for the `AutocastPrivateUse1` dispatch key.

*   Register a fallback that makes unhandled ops fall through to their normal implementations.
    
*   Register specific aten kernels under `AutocastPrivateUse1` using the `KERNEL_PRIVATEUSEONE` helper macro, which maps an op to the desired precision implementation (with enum `at::autocast::CastPolicy`)
    

1TORCH\_LIBRARY\_IMPL(\_, AutocastPrivateUse1, m) {
2  m.fallback(torch::CppFunction::makeFallthrough());
3}

Copy to clipboard

 1TORCH\_LIBRARY\_IMPL(aten, AutocastPrivateUse1, m) {
 2  // lower\_precision\_fp
 3  KERNEL\_PRIVATEUSEONE(mm, lower\_precision\_fp) 4
 5  // fp32
 6  KERNEL\_PRIVATEUSEONE(asin, fp32) 7
 8  m.impl( 9      TORCH\_SELECTIVE\_NAME("aten::binary\_cross\_entropy"),
10      TORCH\_FN((&binary\_cross\_entropy\_banned)));
11}

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/amp.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/amp.md.txt)

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