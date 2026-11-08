Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/model_zoo.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/model_zoo.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/model_zoo.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/model_zoo.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/model_zoo.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/model_zoo.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/model_zoo.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/model_zoo.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/model_zoo.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/model_zoo.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/model_zoo.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/model_zoo.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/model_zoo.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/model_zoo.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/model_zoo.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/model_zoo.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/model_zoo.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/model_zoo.html)
[v1.13](https://docs.pytorch.org/docs/1.13/model_zoo.html)
[v1.12](https://docs.pytorch.org/docs/1.12/model_zoo.html)
[v1.11](https://docs.pytorch.org/docs/1.11/model_zoo.html)
[v1.10](https://docs.pytorch.org/docs/1.10/model_zoo.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/model_zoo.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/model_zoo.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/model_zoo.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/model_zoo.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/model_zoo.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/model_zoo.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/model_zoo.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/model_zoo.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/model_zoo.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/model_zoo.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/model_zoo.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/model_zoo.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/model_zoo.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/model_zoo.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/model_zoo.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/model_zoo.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/model_zoo.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/model_zoo.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/model_zoo.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/model_zoo.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/model_zoo.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/model_zoo.html)

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

torch.utils.model\_zoo[#](https://docs.pytorch.org/docs/2.15/model_zoo.html#torch-utils-model-zoo "Link to this heading")

==========================================================================================================================

Created On: Jan 09, 2017 | Last Updated On: Jun 11, 2025

Moved to `torch.hub`.

torch.utils.model\_zoo.load\_url(_url_, _model\_dir\=None_, _map\_location\=None_, _progress\=True_, _check\_hash\=False_, _file\_name\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L829)
[#](https://docs.pytorch.org/docs/2.15/model_zoo.html#torch.utils.model_zoo.load_url "Link to this definition")

Loads the Torch serialized object at the given URL.

If downloaded file is a zip file, it will be automatically decompressed.

If the object is already present in model\_dir, it’s deserialized and returned. The default value of `model_dir` is `<hub_dir>/checkpoints` where `hub_dir` is the directory returned by [`get_dir()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.get_dir "torch.hub.get_dir")
.

Parameters:

*   **url** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – URL of the object to download
    
*   **model\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – directory in which to save the object
    
*   **map\_location** (_optional_) – a function or a dict specifying how to remap storage locations (see torch.load)
    
*   **progress** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether or not to display a progress bar to stderr. Default: True
    
*   **check\_hash** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, the filename part of the URL should follow the naming convention `filename-<sha256>.ext` where `<sha256>` is the first eight or more digits of the SHA256 hash of the contents of the file. The hash is used to ensure unique names and to verify the contents of the file. Default: False
    
*   **file\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – name for the downloaded file. Filename from `url` will be used if not set.
    
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, only weights will be loaded and no complex pickled objects. Recommended for untrusted sources. See [`load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
     for more details.
    

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

Example

\>>> state\_dict \= torch.hub.load\_state\_dict\_from\_url(
...     "https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth"
... )

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/model_zoo.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/model_zoo.md.txt)

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