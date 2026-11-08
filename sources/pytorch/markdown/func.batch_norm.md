Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.batch_norm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.batch_norm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.batch_norm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.batch_norm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.batch_norm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.batch_norm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.batch_norm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.batch_norm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.batch_norm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.batch_norm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.batch_norm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.batch_norm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.batch_norm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.batch_norm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.batch_norm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.batch_norm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.batch_norm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.batch_norm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.batch_norm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.batch_norm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.batch_norm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.batch_norm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.batch_norm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.batch_norm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.batch_norm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.batch_norm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.batch_norm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.batch_norm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.batch_norm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.batch_norm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.batch_norm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.batch_norm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.batch_norm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.batch_norm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.batch_norm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.batch_norm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.batch_norm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.batch_norm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.batch_norm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.batch_norm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.batch_norm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.batch_norm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.batch_norm.html)

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

Patching Batch Norm[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#patching-batch-norm "Link to this heading")

===========================================================================================================================

Created On: Jan 03, 2023 | Last Updated On: Jun 11, 2025

What’s happening?[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#what-s-happening "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Batch Norm requires in-place updates to running\_mean and running\_var of the same size as the input. Functorch does not support inplace update to a regular tensor that takes in a batched tensor (i.e. `regular.add_(batched)` is not allowed). So when vmapping over a batch of inputs to a single module, we end up with this error

How to fix[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#how-to-fix "Link to this heading")

---------------------------------------------------------------------------------------------------------

One of the best supported ways is to switch BatchNorm for GroupNorm. Options 1 and 2 support this

All of these options assume that you don’t need running stats. If you’re using a module this means that it’s assumed you won’t use batch norm in evaluation mode. If you have a use case that involves running batch norm with vmap in evaluation mode, please file an issue

### Option 1: Change the BatchNorm[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#option-1-change-the-batchnorm "Link to this heading")

If you want to change for GroupNorm, anywhere that you have BatchNorm, replace it with:

BatchNorm2d(C, G, track\_running\_stats\=False)

Copy to clipboard

Here `C` is the same `C` as in the original BatchNorm. `G` is the number of groups to break `C` into. As such, `C % G == 0` and as a fallback, you can set `C == G`, meaning each channel will be treated separately.

If you must use BatchNorm and you’ve built the module yourself, you can change the module to not use running stats. In other words, anywhere that there’s a BatchNorm module, set the `track_running_stats` flag to be False

BatchNorm2d(64, track\_running\_stats\=False)

Copy to clipboard

### Option 2: torchvision parameter[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#option-2-torchvision-parameter "Link to this heading")

Some torchvision models, like resnet and regnet, can take in a `norm_layer` parameter. These are often defaulted to be BatchNorm2d if they’ve been defaulted.

Instead you can set it to be GroupNorm.

import torchvision
from functools import partial
torchvision.models.resnet18(norm\_layer\=lambda c: GroupNorm(num\_groups\=g, c))

Copy to clipboard

Here, once again, `c % g == 0` so as a fallback, set `g = c`.

If you are attached to BatchNorm, be sure to use a version that doesn’t use running stats

import torchvision
from functools import partial
torchvision.models.resnet18(norm\_layer\=partial(BatchNorm2d, track\_running\_stats\=False))

Copy to clipboard

### Option 3: functorch’s patching[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#option-3-functorch-s-patching "Link to this heading")

functorch has added some functionality to allow for quick, in-place patching of the module to not use running stats. Changing the norm layer is more fragile, so we have not offered that. If you have a net where you want the BatchNorm to not use running stats, you can run `replace_all_batch_norm_modules_` to update the module in-place to not use running stats

from torch.func import replace\_all\_batch\_norm\_modules\_
replace\_all\_batch\_norm\_modules\_(net)

Copy to clipboard

### Option 4: eval mode[#](https://docs.pytorch.org/docs/2.15/func.batch_norm.html#option-4-eval-mode "Link to this heading")

When run under eval mode, the running\_mean and running\_var will not be updated. Therefore, vmap can support this mode

model.eval()
vmap(model)(x)
model.train()

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.batch_norm.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.batch_norm.md.txt)

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