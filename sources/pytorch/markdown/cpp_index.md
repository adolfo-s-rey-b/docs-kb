Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cpp_index.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cpp_index.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cpp_index.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cpp_index.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cpp_index.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cpp_index.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cpp_index.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cpp_index.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cpp_index.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cpp_index.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cpp_index.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cpp_index.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cpp_index.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cpp_index.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cpp_index.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cpp_index.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cpp_index.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cpp_index.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cpp_index.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cpp_index.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cpp_index.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cpp_index.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cpp_index.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cpp_index.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cpp_index.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cpp_index.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cpp_index.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cpp_index.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cpp_index.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cpp_index.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cpp_index.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cpp_index.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cpp_index.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cpp_index.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cpp_index.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cpp_index.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cpp_index.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cpp_index.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cpp_index.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cpp_index.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cpp_index.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cpp_index.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cpp_index.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cpp_index.html)

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

C++[#](https://docs.pytorch.org/docs/2.15/cpp_index.html#c "Link to this heading")

===================================================================================

Created On: May 08, 2026 | Last Updated On: May 08, 2026

Note

If you are looking for the PyTorch C++ API docs, directly go [here](https://pytorch.org/cppdocs/)
.

PyTorch provides several features for working with C++, and it’s best to choose from them based on your needs. At a high level, the following support is available:

Tensor and Autograd in C++[#](https://docs.pytorch.org/docs/2.15/cpp_index.html#tensor-and-autograd-in-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Most of the tensor and autograd operations in PyTorch Python API are also available in the C++ API. These include:

*   `torch::Tensor` methods such as `add` / `reshape` / `clone`. For the full list of methods available, please see: [https://pytorch.org/cppdocs/api/classat\_1\_1\_tensor.html](https://pytorch.org/cppdocs/api/classat_1_1_tensor.html)
    
*   C++ tensor indexing API that looks and behaves the same as the Python API. For details on its usage, please see: [https://pytorch.org/cppdocs/notes/tensor\_indexing.html](https://pytorch.org/cppdocs/notes/tensor_indexing.html)
    
*   The tensor autograd APIs and the `torch::autograd` package that are crucial for building dynamic neural networks in C++ frontend. For more details, please see: [https://pytorch.org/tutorials/advanced/cpp\_autograd.html](https://pytorch.org/tutorials/advanced/cpp_autograd.html)
    

Authoring Models in C++[#](https://docs.pytorch.org/docs/2.15/cpp_index.html#authoring-models-in-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

We provide the full capability of authoring and training a neural net model purely in C++, with familiar components such as `torch::nn` / `torch::nn::functional` / `torch::optim` that closely resemble the Python API.

*   For an overview of the PyTorch C++ model authoring and training API, please see: [https://pytorch.org/cppdocs/frontend.html](https://pytorch.org/cppdocs/frontend.html)
    
*   For a detailed tutorial on how to use the API, please see: [https://pytorch.org/tutorials/advanced/cpp\_frontend.html](https://pytorch.org/tutorials/advanced/cpp_frontend.html)
    
*   Docs for components such as `torch::nn` / `torch::nn::functional` / `torch::optim` can be found at: [https://pytorch.org/cppdocs/api/library\_root.html](https://pytorch.org/cppdocs/api/library_root.html)
    

Packaging for C++[#](https://docs.pytorch.org/docs/2.15/cpp_index.html#packaging-for-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------

For guidance on how to install and link with libtorch (the library that contains all of the above C++ APIs), please see: [https://pytorch.org/cppdocs/installing.html](https://pytorch.org/cppdocs/installing.html)
. Note that on Linux there are two types of libtorch binaries provided: one compiled with GCC pre-cxx11 ABI and the other with GCC cxx11 ABI, and you should make the selection based on the GCC ABI your system is using.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cpp_index.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cpp_index.md.txt)

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