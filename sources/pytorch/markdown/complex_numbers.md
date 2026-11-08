Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/complex_numbers.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/complex_numbers.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/complex_numbers.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/complex_numbers.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/complex_numbers.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/complex_numbers.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/complex_numbers.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/complex_numbers.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/complex_numbers.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/complex_numbers.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/complex_numbers.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/complex_numbers.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/complex_numbers.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/complex_numbers.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/complex_numbers.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/complex_numbers.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/complex_numbers.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/complex_numbers.html)
[v1.13](https://docs.pytorch.org/docs/1.13/complex_numbers.html)
[v1.12](https://docs.pytorch.org/docs/1.12/complex_numbers.html)
[v1.11](https://docs.pytorch.org/docs/1.11/complex_numbers.html)
[v1.10](https://docs.pytorch.org/docs/1.10/complex_numbers.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/complex_numbers.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/complex_numbers.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/complex_numbers.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/complex_numbers.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/complex_numbers.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/complex_numbers.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/complex_numbers.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/complex_numbers.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/complex_numbers.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/complex_numbers.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/complex_numbers.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/complex_numbers.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/complex_numbers.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/complex_numbers.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/complex_numbers.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/complex_numbers.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/complex_numbers.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/complex_numbers.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/complex_numbers.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/complex_numbers.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/complex_numbers.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/complex_numbers.html)

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

Complex Numbers[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#complex-numbers "Link to this heading")

===================================================================================================================

Created On: Jun 16, 2025 | Last Updated On: Nov 05, 2025

Complex numbers are numbers that can be expressed in the form a+bja + bja+bj, where a and b are real numbers, and _j_ is called the imaginary unit, which satisfies the equation j2\=−1j^2 = -1j2\=−1. Complex numbers frequently occur in mathematics and engineering, especially in topics like signal processing. Traditionally many users and libraries (e.g., TorchAudio) have handled complex numbers by representing the data in float tensors with shape (...,2)(..., 2)(...,2) where the last dimension contains the real and imaginary values.

Tensors of complex dtypes provide a more natural user experience while working with complex numbers. Operations on complex tensors (e.g., [`torch.mv()`](https://docs.pytorch.org/docs/2.15/generated/torch.mv.html#torch.mv "torch.mv")
, [`torch.matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul")
) are likely to be faster and more memory efficient than operations on float tensors mimicking them. Operations involving complex numbers in PyTorch are optimized to use vectorized assembly instructions and specialized kernels (e.g. LAPACK, cuBlas).

Note

Spectral operations in the [torch.fft module](https://pytorch.org/docs/stable/fft.html#torch-fft)
 support native complex tensors.

Warning

Complex tensors is a beta feature and subject to change.

Creating Complex Tensors[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#creating-complex-tensors "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

We support two complex dtypes: `torch.cfloat` and `torch.cdouble`

\>>> x \= torch.randn(2,2, dtype\=torch.cfloat)
\>>> x
tensor(\[\[-0.4621-0.0303j, -0.2438-0.5874j\],\
     \[ 0.7706+0.1421j,  1.2110+0.1918j\]\])

Copy to clipboard

Note

The default dtype for complex tensors is determined by the default floating point dtype. If the default floating point dtype is `torch.float64` then complex numbers are inferred to have a dtype of `torch.complex128`, otherwise they are assumed to have a dtype of `torch.complex64`.

All factory functions apart from [`torch.linspace()`](https://docs.pytorch.org/docs/2.15/generated/torch.linspace.html#torch.linspace "torch.linspace")
, [`torch.logspace()`](https://docs.pytorch.org/docs/2.15/generated/torch.logspace.html#torch.logspace "torch.logspace")
, and [`torch.arange()`](https://docs.pytorch.org/docs/2.15/generated/torch.arange.html#torch.arange "torch.arange")
 are supported for complex tensors.

Transition from the old representation[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#transition-from-the-old-representation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Users who currently worked around the lack of complex tensors with real tensors of shape (...,2)(..., 2)(...,2) can easily switch to using the complex tensors in their code using [`torch.view_as_complex()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_complex.html#torch.view_as_complex "torch.view_as_complex")
 and [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")
. Note that these functions don’t perform any copy and return a view of the input tensor.

\>>> x \= torch.randn(3, 2)
\>>> x
tensor(\[\[ 0.6125, -0.1681\],\
     \[-0.3773,  1.3487\],\
     \[-0.0861, -0.7981\]\])
\>>> y \= torch.view\_as\_complex(x)
\>>> y
tensor(\[ 0.6125-0.1681j, -0.3773+1.3487j, -0.0861-0.7981j\])
\>>> torch.view\_as\_real(y)
tensor(\[\[ 0.6125, -0.1681\],\
     \[-0.3773,  1.3487\],\
     \[-0.0861, -0.7981\]\])

Copy to clipboard

Accessing real and imag[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#accessing-real-and-imag "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The real and imaginary values of a complex tensor can be accessed using the `real` and `imag`.

Note

Accessing `real` and `imag` attributes doesn’t allocate any memory, and in-place updates on the `real` and `imag` tensors will update the original complex tensor. Also, the returned `real` and `imag` tensors are not contiguous.

\>>> y.real
tensor(\[ 0.6125, -0.3773, -0.0861\])
\>>> y.imag
tensor(\[-0.1681,  1.3487, -0.7981\])

\>>> y.real.mul\_(2)
tensor(\[ 1.2250, -0.7546, -0.1722\])
\>>> y
tensor(\[ 1.2250-0.1681j, -0.7546+1.3487j, -0.1722-0.7981j\])
\>>> y.real.stride()
(2,)

Copy to clipboard

Angle and abs[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#angle-and-abs "Link to this heading")

---------------------------------------------------------------------------------------------------------------

The angle and absolute values of a complex tensor can be computed using [`torch.angle()`](https://docs.pytorch.org/docs/2.15/generated/torch.angle.html#torch.angle "torch.angle")
 and [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs")
.

\>>> x1\=torch.tensor(\[3j, 4+4j\])
\>>> x1.abs()
tensor(\[3.0000, 5.6569\])
\>>> x1.angle()
tensor(\[1.5708, 0.7854\])

Copy to clipboard

Linear Algebra[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#linear-algebra "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Many linear algebra operations, like [`torch.matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul")
, [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
, [`torch.linalg.solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve.html#torch.linalg.solve "torch.linalg.solve")
 etc., support complex numbers. If you’d like to request an operation we don’t currently support, please [search](https://github.com/pytorch/pytorch/issues?q=is%3Aissue+is%3Aopen+complex)
 if an issue has already been filed and if not, [file one](https://github.com/pytorch/pytorch/issues/new/choose)
.

Serialization[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#serialization "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Complex tensors can be serialized, allowing data to be saved as complex values.

\>>> torch.save(y, 'complex\_tensor.pt')
\>>> torch.load('complex\_tensor.pt')
tensor(\[ 0.6125-0.1681j, -0.3773+1.3487j, -0.0861-0.7981j\])

Copy to clipboard

Autograd[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#autograd "Link to this heading")

-----------------------------------------------------------------------------------------------------

PyTorch supports autograd for complex tensors. The gradient computed is the Conjugate Wirtinger derivative, the negative of which is precisely the direction of steepest descent used in Gradient Descent algorithm. Thus, all the existing optimizers can be implemented to work out of the box with complex parameters. For more details, check out the note [Autograd for Complex Numbers](https://docs.pytorch.org/docs/2.15/notes/autograd.html#complex-autograd-doc)
.

Optimizers[#](https://docs.pytorch.org/docs/2.15/complex_numbers.html#optimizers "Link to this heading")

---------------------------------------------------------------------------------------------------------

Semantically, we define stepping through a PyTorch optimizer with complex parameters as being equivalent to stepping through the same optimizer on the [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")
 equivalent of the complex params. More concretely:

\>>> params \= \[torch.rand(2, 3, dtype\=torch.complex64) for \_ in range(5)\]
\>>> real\_params \= \[torch.view\_as\_real(p) for p in params\]

\>>> complex\_optim \= torch.optim.AdamW(params)
\>>> real\_optim \= torch.optim.AdamW(real\_params)

Copy to clipboard

`real_optim` and `complex_optim` will compute the same updates on the parameters, though there may be slight numerical discrepancies between the two optimizers, similar to numerical discrepancies between foreach vs forloop optimizers and capturable vs default optimizers. For more details, see [numerical accuracy](https://pytorch.org/docs/stable/notes/numerical_accuracy.html)
.

Specifically, while you can think of our optimizer’s handling of complex tensors as the same as optimizing over their `p.real` and `p.imag` pieces separately, the implementation details are not precisely that. Note that the [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")
 equivalent will convert a complex tensor to a real tensor with shape (...,2)(..., 2)(...,2), whereas splitting a complex tensor into two tensors is 2 tensors of size (...)(...)(...). This distinction has no impact on pointwise optimizers (like AdamW) but will cause slight discrepancy in optimizers that do global reductions (like LBFGS). We currently do not have optimizers that do per-Tensor reductions and thus do not yet define this behavior. Open an issue if you have a use case that requires precisely defining this behavior.

We do not fully support the following subsystems:

*   Quantization
    
*   JIT
    
*   Sparse Tensors
    
*   Distributed
    

If any of these would help your use case, please [search](https://github.com/pytorch/pytorch/issues?q=is%3Aissue+is%3Aopen+complex)
 if an issue has already been filed and if not, [file one](https://github.com/pytorch/pytorch/issues/new/choose)
.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/complex_numbers.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/complex_numbers.md.txt)

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