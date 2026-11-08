Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/onnx_testing.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/onnx_testing.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/onnx_testing.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/onnx_testing.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/onnx_testing.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/onnx_testing.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/onnx_testing.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/onnx_testing.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/onnx_testing.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/onnx_testing.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/onnx_testing.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/onnx_testing.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/onnx_testing.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/onnx_testing.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/onnx_testing.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/onnx_testing.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/onnx_testing.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/onnx_testing.html)
[v1.13](https://docs.pytorch.org/docs/1.13/onnx_testing.html)
[v1.12](https://docs.pytorch.org/docs/1.12/onnx_testing.html)
[v1.11](https://docs.pytorch.org/docs/1.11/onnx_testing.html)
[v1.10](https://docs.pytorch.org/docs/1.10/onnx_testing.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/onnx_testing.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/onnx_testing.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/onnx_testing.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/onnx_testing.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/onnx_testing.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/onnx_testing.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/onnx_testing.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/onnx_testing.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/onnx_testing.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/onnx_testing.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/onnx_testing.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/onnx_testing.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/onnx_testing.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/onnx_testing.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/onnx_testing.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/onnx_testing.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/onnx_testing.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/onnx_testing.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/onnx_testing.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/onnx_testing.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/onnx_testing.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/onnx_testing.html)

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

torch.onnx.testing[#](https://docs.pytorch.org/docs/2.15/onnx_testing.html#module-torch.onnx.testing "Link to this heading")

=============================================================================================================================

Created On: Sep 10, 2025 | Last Updated On: Sep 10, 2025

Utilities to aid in testing exported ONNX models.

torch.onnx.testing.assert\_onnx\_program(_program_, _\*_, _rtol\=None_, _atol\=None_, _args\=None_, _kwargs\=None_, _strategy\='TorchExportNonStrictStrategy'_, _backend\='onnxruntime'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_testing.py#L18)
[#](https://docs.pytorch.org/docs/2.15/onnx_testing.html#torch.onnx.testing.assert_onnx_program "Link to this definition")

Assert that the ONNX model produces the same output as the PyTorch ExportedProgram.

Parameters:

*   **program** (_\_onnx\_program.ONNXProgram_) – The `ONNXProgram` to verify.
    
*   **rtol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – Relative tolerance.
    
*   **atol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – Absolute tolerance.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[__Any__,_ _...__\]_ _|_ _None_) – The positional arguments to pass to the program. If None, the default example inputs in the ExportedProgram will be used.
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_ _|_ _None_) – The keyword arguments to pass to the program. If None, the default example inputs in the ExportedProgram will be used.
    
*   **strategy** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – Assert the capture strategy used to export the program. Values can be class names like “TorchExportNonStrictStrategy”. If None, the strategy is not asserted.
    
*   **backend** (_Literal__\[__'onnxruntime'__,_ _'reference'__\]_) – The backend to use for evaluating the ONNX program. Supported values are “onnxruntime” and “reference”.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/onnx_testing.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/onnx_testing.md.txt)

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