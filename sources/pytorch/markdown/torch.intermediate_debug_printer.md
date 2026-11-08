Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch.intermediate_debug_printer.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch.intermediate_debug_printer.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch.intermediate_debug_printer.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch.intermediate_debug_printer.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch.intermediate_debug_printer.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch.intermediate_debug_printer.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch.intermediate_debug_printer.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch.intermediate_debug_printer.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch.intermediate_debug_printer.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch.intermediate_debug_printer.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch.intermediate_debug_printer.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch.intermediate_debug_printer.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch.intermediate_debug_printer.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch.intermediate_debug_printer.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch.intermediate_debug_printer.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch.intermediate_debug_printer.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch.intermediate_debug_printer.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch.intermediate_debug_printer.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch.intermediate_debug_printer.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch.intermediate_debug_printer.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch.intermediate_debug_printer.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch.intermediate_debug_printer.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch.intermediate_debug_printer.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch.intermediate_debug_printer.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch.intermediate_debug_printer.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch.intermediate_debug_printer.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch.intermediate_debug_printer.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch.intermediate_debug_printer.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch.intermediate_debug_printer.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch.intermediate_debug_printer.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch.intermediate_debug_printer.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch.intermediate_debug_printer.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch.intermediate_debug_printer.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch.intermediate_debug_printer.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch.intermediate_debug_printer.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch.intermediate_debug_printer.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch.intermediate_debug_printer.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch.intermediate_debug_printer.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch.intermediate_debug_printer.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch.intermediate_debug_printer.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch.intermediate_debug_printer.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch.intermediate_debug_printer.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch.intermediate_debug_printer.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch.intermediate_debug_printer.html)

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

AOTInductor Intermediate Value Debug Printer[#](https://docs.pytorch.org/docs/2.15/torch.intermediate_debug_printer.html#aotinductor-intermediate-value-debug-printer "Link to this heading")

==============================================================================================================================================================================================

Created On: Sep 30, 2025 | Last Updated On: Sep 30, 2025

This is a user manual on how to use AOT Inductor Intermediate Value Debug Printer tool which is a utility tool that can help pinpoint CUDA IMA kernels / numerical discrepancies when uses AOT Inductor to compile a PyTorch model.

The main functionality of this tool is to automatically print out / or dump the value info of all intermediate tensor arguments before and after each kernel launch call in AOT Inductor.

How to use[#](https://docs.pytorch.org/docs/2.15/torch.intermediate_debug_printer.html#how-to-use "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The debug printer can be configured via environment variable. The following flags are both supported to run with internal fbcode buck commands and OSS.

All configurations are defined here: [torch/\_inductor/config.py](https://github.com/pytorch/pytorch/blob/768361e67f0eb36491d7b763ef38d7c928ebefe6/torch/_inductor/config.py#L1493-L1505)

    \# options for debug printing/saving for intermediate tensor values for aot inductor

    0: disable debug dumping
    1: enable saving intermediate tensor values
    2: enable printing intermediate tensor values
    3: enable printing kernel names only (useful for pinpointing troublesome kernels)

Copy to clipboard

1.  To enable **default** mode debug printing:
    
    *   Add flag `AOT_INDUCTOR_DEBUG_INTERMEDIATE_VALUE_PRINTER=2` (PRINT\_ONLY mode) for default printing all supported kernel tensor arg values.
        
    *   Add flag `AOT_INDUCTOR_FILTERED_KERNELS_TO_PRINT={kernel_name_1, kernel_name_2,...}` for selectively printing tensor values associated with the specified kernels. (suggest to do a run with generating full printing logs first)
        
    
    Sample command:
    
    AOT\_INDUCTOR\_FILTERED\_KERNELS\_TO\_PRINT\="aoti\_torch\_cuda\_addmm\_out" AOT\_INDUCTOR\_DEBUG\_INTERMEDIATE\_VALUE\_PRINTER\=2 TORCH\_LOGS\="+inductor, output\_code" python test/inductor/test\_aot\_inductor.py \-k test\_addmm\_cuda
    
    Copy to clipboard
    
2.  To enable **pinpoint** the problematic kernel name only: (Especially useful in CUDA IMA debugging)
    
    *   Add flag `AOT_INDUCTOR_DEBUG_INTERMEDIATE_VALUE_PRINTER=3` (PRINT\_KERNEL\_NAME\_ONLY mode) no tensor numerical values will be dumped.
        
    
    Sample command:
    
    AOT\_INDUCTOR\_DEBUG\_INTERMEDIATE\_VALUE\_PRINTER\=3 TORCH\_LOGS\="+inductor, output\_code" python test/inductor/test\_aot\_inductor.py \-k test\_addmm\_cuda
    
    Copy to clipboard
    
3.  To enable **save** the intermediate tensor values:
    
    *   Useful when you want to repro the error in a standalone kernel debugging repro. The saved intermediate tensor values can be used as debugging inputs to the problematic kernel.
        
    *   Set `AOT_INDUCTOR_DEBUG_INTERMEDIATE_VALUE_PRINTER=1` (SAVE\_ONLY mode) for default saving all supported kernel tensor arg values to `.pt` in a tmp folder.
        
    *   Similarly, add `AOT_INDUCTOR_FILTERED_KERNELS_TO_PRINT={kernel_name_1, kernel_name_2,...}` for selectively saving tensor values associated with the specified kernels.
        
    
    Sample command:
    
    AOT\_INDUCTOR\_FILTERED\_KERNELS\_TO\_PRINT\="triton\_poi\_fused\_0" AOT\_INDUCTOR\_DEBUG\_INTERMEDIATE\_VALUE\_PRINTER\=1 TORCH\_LOGS\="+inductor, output\_code" python test/inductor/test\_aot\_inductor.py \-k test\_addmm\_cuda
    
    Copy to clipboard
    
    The saved tensor values will be dumped in a format: `<before/after_launch>_<kernel_name>_<arg_name>_<device>.pt`
    
    The dumped `.pt` tensors can be further loaded and used like this:
    
        def \_load\_tensor(path):
            return torch.load(path, weights\_only\=True)
        tensor \= \_load\_tensor("../tmp/aoti\_torch/before\_launch\_aoti\_torch\_cuda\_addmm\_out\_buf1\_cuda:0.pt")
    
        \# Simply print tensor to view the full value
        print(tensor)
    
    Copy to clipboard
    

Example Outputs[#](https://docs.pytorch.org/docs/2.15/torch.intermediate_debug_printer.html#example-outputs "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Before launch tensor stats:

![Sample image 1](https://docs.pytorch.org/docs/2.15/_images/before_launch.png)

After launch tensor stats:

![Sample image 2](https://docs.pytorch.org/docs/2.15/_images/after_launch.png)

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch.intermediate_debug_printer.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch.intermediate_debug_printer.md.txt)

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