Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/broadcasting.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/broadcasting.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/broadcasting.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/broadcasting.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/broadcasting.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/broadcasting.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/broadcasting.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/broadcasting.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/broadcasting.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/broadcasting.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/broadcasting.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/broadcasting.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/broadcasting.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/broadcasting.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/broadcasting.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/broadcasting.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/broadcasting.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/broadcasting.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/broadcasting.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/broadcasting.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/broadcasting.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/broadcasting.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/broadcasting.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/broadcasting.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/broadcasting.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/broadcasting.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/broadcasting.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/broadcasting.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/broadcasting.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/broadcasting.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/broadcasting.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/broadcasting.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/broadcasting.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/broadcasting.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/broadcasting.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/broadcasting.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/broadcasting.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/broadcasting.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/broadcasting.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/broadcasting.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/broadcasting.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/broadcasting.html)

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

Broadcasting semantics[#](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics "Link to this heading")

====================================================================================================================================

Created On: May 08, 2026 | Last Updated On: May 08, 2026

Many PyTorch operations support NumPy’s broadcasting semantics. See [Numpy Documentation](https://numpy.org/doc/stable/user/basics.broadcasting.html)
 for details.

In short, if a PyTorch operation supports broadcast, then its Tensor arguments can be automatically expanded to be of equal sizes (without making copies of the data).

General semantics[#](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#general-semantics "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Two tensors are “broadcastable” if the following rules hold:

*   When iterating over the dimension sizes, starting at the trailing dimension, the dimension sizes must either be equal, one of them is 1, or one of them does not exist.
    

For Example:

\>>> x\=torch.empty(5,7,3)
\>>> y\=torch.empty(5,7,3)
\# same shapes are always broadcastable (i.e. the above rules always hold)

\>>> x\=torch.empty((0,))
\>>> y\=torch.empty(2,2)
\# x and y are not broadcastable, because the 0-sized dimension of x
\# does not match the 2-sized dimension of y.

\# can line up trailing dimensions
\>>> x\=torch.empty(5,3,4,1)
\>>> y\=torch.empty(  3,1,1)
\# x and y are broadcastable.
\# 1st trailing dimension: both have size 1
\# 2nd trailing dimension: y has size 1
\# 3rd trailing dimension: x size == y size
\# 4th trailing dimension: y dimension doesn't exist

\# but:
\>>> x\=torch.empty(5,2,4,1)
\>>> y\=torch.empty(  3,1,1)
\# x and y are not broadcastable, because in the 3rd trailing dimension 2 != 3

Copy to clipboard

If two tensors `x`, `y` are “broadcastable”, the resulting tensor size is calculated as follows:

*   If the number of dimensions of `x` and `y` are not equal, prepend 1 to the dimensions of the tensor with fewer dimensions to make them equal length.
    
*   Then, for each dimension size, the resulting dimension size is the max of the sizes of `x` and `y` along that dimension.
    

For Example:

\# can line up trailing dimensions to make reading easier
\>>> x\=torch.empty(5,1,4,1)
\>>> y\=torch.empty(  3,1,1)
\>>> (x+y).size()
torch.Size(\[5, 3, 4, 1\])

\# but not necessary:
\>>> x\=torch.empty(1)
\>>> y\=torch.empty(3,1,7)
\>>> (x+y).size()
torch.Size(\[3, 1, 7\])

\>>> x\=torch.empty(5,2,4,1)
\>>> y\=torch.empty(3,1,1)
\>>> (x+y).size()
RuntimeError: The size of tensor a (2) must match the size of tensor b (3) at non\-singleton dimension 1

Copy to clipboard

In-place semantics[#](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#in-place-semantics "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

One complication is that in-place operations do not allow the in-place tensor to change shape as a result of the broadcast.

For Example:

\>>> x\=torch.empty(5,3,4,1)
\>>> y\=torch.empty(3,1,1)
\>>> (x.add\_(y)).size()
torch.Size(\[5, 3, 4, 1\])

\# but:
\>>> x\=torch.empty(1,3,1)
\>>> y\=torch.empty(3,1,7)
\>>> (x.add\_(y)).size()
RuntimeError: The expanded size of the tensor (1) must match the existing size (7) at non-singleton dimension 2.

Copy to clipboard

Backwards compatibility[#](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#backwards-compatibility "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Prior versions of PyTorch allowed certain pointwise functions to execute on tensors with different shapes, as long as the number of elements in each tensor was equal. The pointwise operation would then be carried out by viewing each tensor as 1-dimensional. PyTorch now supports broadcasting and the “1-dimensional” pointwise behavior is considered deprecated and will generate a Python warning in cases where tensors are not broadcastable, but have the same number of elements.

Note that the introduction of broadcasting can cause backwards incompatible changes in the case where two tensors do not have the same shape, but are broadcastable and have the same number of elements. For Example:

\>>> torch.add(torch.ones(4,1), torch.randn(4))

Copy to clipboard

would previously produce a Tensor with size: torch.Size(\[4,1\]), but now produces a Tensor with size: torch.Size(\[4,4\]). In order to help identify cases in your code where backwards incompatibilities introduced by broadcasting may exist, you may set `torch.utils.backcompat.broadcast_warning.enabled` to `True`, which will generate a python warning in such cases.

For Example:

\>>> torch.utils.backcompat.broadcast\_warning.enabled\=True
\>>> torch.add(torch.ones(4,1), torch.ones(4))
\_\_main\_\_:1: UserWarning: self and other do not have the same shape, but are broadcastable, and have the same number of elements.
Changing behavior in a backwards incompatible manner to broadcasting rather than viewing as 1-dimensional.

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/broadcasting.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/broadcasting.md.txt)

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