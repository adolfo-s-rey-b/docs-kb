Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/hub.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/hub.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/hub.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/hub.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/hub.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/hub.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/hub.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/hub.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/hub.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/hub.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/hub.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/hub.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/hub.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/hub.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/hub.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/hub.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/hub.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/hub.html)
[v1.13](https://docs.pytorch.org/docs/1.13/hub.html)
[v1.12](https://docs.pytorch.org/docs/1.12/hub.html)
[v1.11](https://docs.pytorch.org/docs/1.11/hub.html)
[v1.10](https://docs.pytorch.org/docs/1.10/hub.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/hub.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/hub.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/hub.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/hub.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/hub.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/hub.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/hub.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/hub.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/hub.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/hub.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/hub.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/hub.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/hub.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/hub.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/hub.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/hub.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/hub.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/hub.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/hub.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/hub.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/hub.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/hub.html)

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

torch.hub[#](https://docs.pytorch.org/docs/2.15/hub.html#torch-hub "Link to this heading")

===========================================================================================

Created On: Jun 13, 2025 | Last Updated On: Jul 08, 2026

PyTorch Hub is a pre-trained model repository designed to facilitate research reproducibility.

Publishing models[#](https://docs.pytorch.org/docs/2.15/hub.html#publishing-models "Link to this heading")

-----------------------------------------------------------------------------------------------------------

PyTorch Hub supports publishing pre-trained models(model definitions and pre-trained weights) to a GitHub repository by adding a simple `hubconf.py` file;

`hubconf.py` can have multiple entrypoints. Each entrypoint is defined as a python function (example: a pre-trained model you want to publish).

  def entrypoint\_name(\*args, \*\*kwargs):
      \# args & kwargs are optional, for models which take positional/keyword arguments.
      ...

Copy to clipboard

### How to implement an entrypoint?[#](https://docs.pytorch.org/docs/2.15/hub.html#how-to-implement-an-entrypoint "Link to this heading")

Here is a code snippet specifies an entrypoint for `resnet18` model if we expand the implementation in `pytorch/vision/hubconf.py`. In most case importing the right function in `hubconf.py` is sufficient. Here we just want to use the expanded version as an example to show how it works. You can see the full script in [pytorch/vision repo](https://github.com/pytorch/vision/blob/master/hubconf.py)

  dependencies \= \['torch'\]
  from torchvision.models.resnet import resnet18 as \_resnet18

  \# resnet18 is the name of entrypoint
  def resnet18(pretrained\=False, \*\*kwargs):
      """ # This docstring shows up in hub.help()
      Resnet18 model
      pretrained (bool): kwargs, load pretrained weights into the model
      """
      \# Call the model, load pretrained weights
      model \= \_resnet18(pretrained\=pretrained, \*\*kwargs)
      return model

Copy to clipboard

*   `dependencies` variable is a **list** of package names required to **load** the model. Note this might be slightly different from dependencies required for training a model.
    
*   `args` and `kwargs` are passed along to the real callable function.
    
*   Docstring of the function works as a help message. It explains what does the model do and what are the allowed positional/keyword arguments. It’s highly recommended to add a few examples here.
    
*   Entrypoint function can either return a model(nn.module), or auxiliary tools to make the user workflow smoother, e.g. tokenizers.
    
*   Callables prefixed with underscore are considered as helper functions which won’t show up in [`torch.hub.list()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.list "torch.hub.list")
    .
    
*   Pretrained weights can either be stored locally in the GitHub repo, or loadable by [`torch.hub.load_state_dict_from_url()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.load_state_dict_from_url "torch.hub.load_state_dict_from_url")
    . If less than 2GB, it’s recommended to attach it to a [project release](https://help.github.com/en/articles/distributing-large-binaries)
     and use the url from the release. In the example above `torchvision.models.resnet.resnet18` handles `pretrained`, alternatively you can put the following logic in the entrypoint definition.
    

  if pretrained:
      \# For checkpoint saved in local GitHub repo, e.g. <RELATIVE\_PATH\_TO\_CHECKPOINT>=weights/save.pth
      dirname \= os.path.dirname(\_\_file\_\_)
      checkpoint \= os.path.join(dirname, <RELATIVE\_PATH\_TO\_CHECKPOINT\>)
      state\_dict \= torch.load(checkpoint)
      model.load\_state\_dict(state\_dict)

      \# For checkpoint saved elsewhere
      checkpoint \= 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
      model.load\_state\_dict(torch.hub.load\_state\_dict\_from\_url(checkpoint, progress\=False))

Copy to clipboard

### Important Notice[#](https://docs.pytorch.org/docs/2.15/hub.html#important-notice "Link to this heading")

*   The published models should be at least in a branch/tag. It can’t be a random commit.
    

Loading models from Hub[#](https://docs.pytorch.org/docs/2.15/hub.html#loading-models-from-hub "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

PyTorch Hub provides convenient APIs to explore all available models in hub through [`torch.hub.list()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.list "torch.hub.list")
, show docstring and examples through [`torch.hub.help()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.help "torch.hub.help")
 and load the pre-trained models using [`torch.hub.load()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.load "torch.hub.load")
.

torch.hub.list(_github_, _force\_reload\=False_, _skip\_validation\=False_, _trust\_repo\='check'_, _verbose\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L459)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.list "Link to this definition")

List all callable entrypoints available in the repo specified by `github`.

Parameters:

*   **github** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a string with format “repo\_owner/repo\_name\[:ref\]” with an optional ref (tag or branch). If `ref` is not specified, the default branch is assumed to be `main` if it exists, and otherwise `master`. Example: ‘pytorch/vision:0.10’
    
*   **force\_reload** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to discard the existing cache and force a fresh download. Default is `False`.
    
*   **skip\_validation** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `False`, torchhub will check that the branch or commit specified by the `github` argument properly belongs to the repo owner. This will make requests to the GitHub API; you can specify a non-default GitHub token by setting the `GITHUB_TOKEN` environment variable. Default is `False`.
    
*   **trust\_repo** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) –
    
    `"check"`, `True` or `False`. This parameter was introduced in v1.12 and helps ensuring that users only run code from repos that they trust.
    
    *   If `False`, a prompt will ask the user whether the repo should be trusted.
        
    *   If `True`, the repo will be added to the trusted list and loaded without requiring explicit confirmation.
        
    *   If `"check"`, the repo will be checked against the list of trusted repos in the cache. If it is not present in that list, the behaviour will fall back onto the `trust_repo=False` option.
        
    
    Default is `"check"`.
    
*   **verbose** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, mute messages about hitting local caches. Note that the message about first download cannot be muted. Default is `True`.
    

Returns:

The available callables entrypoint

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")

Example

\>>> entrypoints \= torch.hub.list("pytorch/vision", force\_reload\=True)

Copy to clipboard

torch.hub.help(_github_, _model_, _force\_reload\=False_, _skip\_validation\=False_, _trust\_repo\='check'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L526)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.help "Link to this definition")

Show the docstring of entrypoint `model`.

Parameters:

*   **github** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a string with format <repo\_owner/repo\_name\[:ref\]> with an optional ref (a tag or a branch). If `ref` is not specified, the default branch is assumed to be `main` if it exists, and otherwise `master`. Example: ‘pytorch/vision:0.10’
    
*   **model** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a string of entrypoint name defined in repo’s `hubconf.py`
    
*   **force\_reload** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to discard the existing cache and force a fresh download. Default is `False`.
    
*   **skip\_validation** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `False`, torchhub will check that the ref specified by the `github` argument properly belongs to the repo owner. This will make requests to the GitHub API; you can specify a non-default GitHub token by setting the `GITHUB_TOKEN` environment variable. Default is `False`.
    
*   **trust\_repo** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) –
    
    `"check"`, `True` or `False`. This parameter was introduced in v1.12 and helps ensuring that users only run code from repos that they trust.
    
    *   If `False`, a prompt will ask the user whether the repo should be trusted.
        
    *   If `True`, the repo will be added to the trusted list and loaded without requiring explicit confirmation.
        
    *   If `"check"`, the repo will be checked against the list of trusted repos in the cache. If it is not present in that list, the behaviour will fall back onto the `trust_repo=False` option.
        
    
    Default is `"check"`.
    

Example

\>>> print(torch.hub.help("pytorch/vision", "resnet18", force\_reload\=True))

Copy to clipboard

torch.hub.load(_repo\_or\_dir_, _model_, _\*args_, _source\='github'_, _trust\_repo\='check'_, _force\_reload\=False_, _verbose\=True_, _skip\_validation\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L576)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.load "Link to this definition")

Load a model from a github repo or a local directory.

Note: Loading a model is the typical use case, but this can also be used for loading other objects such as tokenizers, loss functions, etc.

If `source` is ‘github’, `repo_or_dir` is expected to be of the form `repo_owner/repo_name[:ref]` with an optional ref (a tag or a branch).

If `source` is ‘local’, `repo_or_dir` is expected to be a path to a local directory.

Parameters:

*   **repo\_or\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – If `source` is ‘github’, this should correspond to a github repo with format `repo_owner/repo_name[:ref]` with an optional ref (tag or branch), for example ‘pytorch/vision:0.10’. If `ref` is not specified, the default branch is assumed to be `main` if it exists, and otherwise `master`. If `source` is ‘local’ then it should be a path to a local directory.
    
*   **model** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – the name of a callable (entrypoint) defined in the repo/dir’s `hubconf.py`.
    
*   **\*args** (_optional_) – the corresponding args for callable `model`.
    
*   **source** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – ‘github’ or ‘local’. Specifies how `repo_or_dir` is to be interpreted. Default is ‘github’.
    
*   **trust\_repo** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) –
    
    `"check"`, `True` or `False`. This parameter was introduced in v1.12 and helps ensuring that users only run code from repos that they trust.
    
    *   If `False`, a prompt will ask the user whether the repo should be trusted.
        
    *   If `True`, the repo will be added to the trusted list and loaded without requiring explicit confirmation.
        
    *   If `"check"`, the repo will be checked against the list of trusted repos in the cache. If it is not present in that list, the behaviour will fall back onto the `trust_repo=False` option.
        
    
    Default is `"check"`.
    
*   **force\_reload** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to force a fresh download of the github repo unconditionally. Does not have any effect if `source = 'local'`. Default is `False`.
    
*   **verbose** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, mute messages about hitting local caches. Note that the message about first download cannot be muted. Does not have any effect if `source = 'local'`. Default is `True`.
    
*   **skip\_validation** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `False`, torchhub will check that the branch or commit specified by the `github` argument properly belongs to the repo owner. This will make requests to the GitHub API; you can specify a non-default GitHub token by setting the `GITHUB_TOKEN` environment variable. Default is `False`.
    
*   **\*\*kwargs** (_optional_) – the corresponding kwargs for callable `model`.
    

Returns:

The output of the `model` callable when called with the given `*args` and `**kwargs`.

Example

\>>> \# from a github repo
\>>> repo \= "pytorch/vision"
\>>> model \= torch.hub.load(
...     repo, "resnet50", weights\="ResNet50\_Weights.IMAGENET1K\_V1"
... )
\>>> \# from a local directory
\>>> path \= "/some/local/path/pytorch/vision"
\>>> model \= torch.hub.load(path, "resnet50", weights\="ResNet50\_Weights.DEFAULT")

Copy to clipboard

torch.hub.download\_url\_to\_file(_url_, _dst_, _hash\_prefix\=None_, _progress\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L707)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.download_url_to_file "Link to this definition")

Download object at the given URL to a local path.

Parameters:

*   **url** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – URL of the object to download
    
*   **dst** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Full path where object will be saved, e.g. `/tmp/temporary_file`
    
*   **hash\_prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – If not None, the SHA256 downloaded file should start with `hash_prefix`. Default: None
    
*   **progress** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether or not to display a progress bar to stderr Default: True
    

Example

\>>> torch.hub.download\_url\_to\_file(
...     "https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth",
...     "/tmp/temporary\_file",
... )

Copy to clipboard

torch.hub.load\_state\_dict\_from\_url(_url_, _model\_dir\=None_, _map\_location\=None_, _progress\=True_, _check\_hash\=False_, _file\_name\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L829)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.load_state_dict_from_url "Link to this definition")

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

### Running a loaded model:[#](https://docs.pytorch.org/docs/2.15/hub.html#running-a-loaded-model "Link to this heading")

Note that `*args` and `**kwargs` in [`torch.hub.load()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.load "torch.hub.load")
 are used to **instantiate** a model. After you have loaded a model, how can you find out what you can do with the model? A suggested workflow is

*   `dir(model)` to see all available methods of the model.
    
*   `help(model.foo)` to check what arguments `model.foo` takes to run
    

To help users explore without referring to documentation back and forth, we strongly recommend repo owners make function help messages clear and succinct. It’s also helpful to include a minimal working example.

### Where are my downloaded models saved?[#](https://docs.pytorch.org/docs/2.15/hub.html#where-are-my-downloaded-models-saved "Link to this heading")

The locations are used in the order of

*   Calling `hub.set_dir(<PATH_TO_HUB_DIR>)`
    
*   `$TORCH_HOME/hub`, if environment variable `TORCH_HOME` is set.
    
*   `$XDG_CACHE_HOME/torch/hub`, if environment variable `XDG_CACHE_HOME` is set.
    
*   `~/.cache/torch/hub`
    

torch.hub.get\_dir()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L427)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.get_dir "Link to this definition")

Get the Torch Hub cache directory used for storing downloaded models & weights.

If [`set_dir()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.set_dir "torch.hub.set_dir")
 is not called, default path is `$TORCH_HOME/hub` where environment variable `$TORCH_HOME` defaults to `$XDG_CACHE_HOME/torch`. `$XDG_CACHE_HOME` follows the X Design Group specification of the Linux filesystem layout, with a default value `~/.cache` if the environment variable is not set.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.hub.set\_dir(_d_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/hub.py#L448)
[#](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.set_dir "Link to this definition")

Optionally set the Torch Hub directory used to save downloaded models & weights.

Parameters:

**d** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – path to a local folder to save downloaded models & weights.

### Caching logic[#](https://docs.pytorch.org/docs/2.15/hub.html#caching-logic "Link to this heading")

By default, we don’t clean up files after loading it. Hub uses the cache by default if it already exists in the directory returned by [`get_dir()`](https://docs.pytorch.org/docs/2.15/hub.html#torch.hub.get_dir "torch.hub.get_dir")
.

Users can force a reload by calling `hub.load(..., force_reload=True)`. This will delete the existing GitHub folder and downloaded weights, reinitialize a fresh download. This is useful when updates are published to the same branch, users can keep up with the latest release.

### Known limitations:[#](https://docs.pytorch.org/docs/2.15/hub.html#known-limitations "Link to this heading")

Torch hub works by importing the package as if it was installed. There are some side effects introduced by importing in Python. For example, you can see new items in Python caches `sys.modules` and `sys.path_importer_cache` which is normal Python behavior. This also means that you may have import errors when importing different models from different repos, if the repos have the same sub-package names (typically, a `model` subpackage). A workaround for these kinds of import errors is to remove the offending sub-package from the `sys.modules` dict; more details can be found in [this GitHub issue](https://github.com/pytorch/hub/issues/243#issuecomment-942403391)
.

A known limitation that is worth mentioning here: users **CANNOT** load two different branches of the same repo in the **same python process**. It’s just like installing two packages with the same name in Python, which is not good. Cache might join the party and give you surprises if you actually try that. Of course it’s totally fine to load them in separate processes.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/hub.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/hub.md.txt)

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