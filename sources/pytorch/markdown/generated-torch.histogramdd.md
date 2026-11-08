Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.histogramdd.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.histogramdd.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.histogramdd.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.histogramdd.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.histogramdd.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.histogramdd.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.histogramdd.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.histogramdd.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.histogramdd.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.histogramdd.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.histogramdd.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.histogramdd.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.histogramdd.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.histogramdd.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.histogramdd.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.histogramdd.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.histogramdd.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.histogramdd.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.histogramdd.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.histogramdd.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.histogramdd.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.histogramdd.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.histogramdd.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.histogramdd.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.histogramdd.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.histogramdd.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.histogramdd.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.histogramdd.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.histogramdd.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.histogramdd.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.histogramdd.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.histogramdd.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.histogramdd.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.histogramdd.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.histogramdd.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.histogramdd.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.histogramdd.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.histogramdd.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.histogramdd.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.histogramdd.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.histogramdd.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.histogramdd.html)

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

torch.histogramdd[#](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html#torch-histogramdd "Link to this heading")

===================================================================================================================================

torch.histogramdd(_input_, _bins_, _\*_, _range=None_, _weight=None_, _density=False_, _out=None) \-> (Tensor_, _Tensor\[\]_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html#torch.histogramdd "Link to this definition")

Computes a multi-dimensional histogram of the values in a tensor.

Interprets the elements of an input tensor whose innermost dimension has size N as a collection of N-dimensional points. Maps each of the points into a set of N-dimensional bins and returns the number of points (or total weight) in each bin.

`input` must be a tensor with at least 2 dimensions. If input has shape (M, N), each of its M rows defines a point in N-dimensional space. If input has three or more dimensions, all but the last dimension are flattened.

Each dimension is independently associated with its own strictly increasing sequence of bin edges. Bin edges may be specified explicitly by passing a sequence of 1D tensors. Alternatively, bin edges may be constructed automatically by passing a sequence of integers specifying the number of equal-width bins in each dimension.

For each N-dimensional point in input:

*   Each of its coordinates is binned independently among the bin edges
    
    corresponding to its dimension
    
*   Binning results are combined to identify the N-dimensional bin (if any)
    
    into which the point falls
    
*   If the point falls into a bin, the bin’s count (or total weight) is incremented
    
*   Points which do not fall into any bin do not contribute to the output
    

`bins` can be a sequence of N 1D tensors, a sequence of N ints, or a single int.

If `bins` is a sequence of N 1D tensors, it explicitly specifies the N sequences of bin edges. Each 1D tensor should contain a strictly increasing sequence with at least one element. A sequence of K bin edges defines K-1 bins, explicitly specifying the left and right edges of all bins. Every bin is inclusive of its left edge. Only the rightmost bin is inclusive of its right edge.

If `bins` is a sequence of N ints, it specifies the number of equal-width bins in each dimension. By default, the leftmost and rightmost bin edges in each dimension are determined by the minimum and maximum elements of the input tensor in the corresponding dimension. The [`range`](https://docs.pytorch.org/docs/2.15/generated/torch.range.html#torch.range "torch.range")
 argument can be provided to manually specify the leftmost and rightmost bin edges in each dimension.

If `bins` is an int, it specifies the number of equal-width bins for all dimensions.

Note

See also [`torch.histogram()`](https://docs.pytorch.org/docs/2.15/generated/torch.histogram.html#torch.histogram "torch.histogram")
, which specifically computes 1D histograms. While [`torch.histogramdd()`](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html#torch.histogramdd "torch.histogramdd")
 infers the dimensionality of its bins and binned values from the shape of `input`, [`torch.histogram()`](https://docs.pytorch.org/docs/2.15/generated/torch.histogram.html#torch.histogram "torch.histogram")
 accepts and flattens `input` of any shape.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **bins** – Tensor\[\], int\[\], or int. If Tensor\[\], defines the sequences of bin edges. If int\[\], defines the number of equal-width bins in each dimension. If int, defines the number of equal-width bins for all dimensions.
    

Keyword Arguments:

*   **range** (_sequence_ _of_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Defines the leftmost and rightmost bin edges in each dimension.
    
*   **weight** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – By default, each value in the input has weight 1. If a weight tensor is passed, each N-dimensional coordinate in input contributes its associated weight towards its bin’s result. The weight tensor should have the same shape as the `input` tensor excluding its innermost dimension N.
    
*   **density** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If False (default), the result will contain the count (or total weight) in each bin. If True, each count (weight) is divided by the total count (total weight), then divided by the volume of its associated bin.
    

Returns:

N-dimensional Tensor containing the values of the histogram. bin\_edges(Tensor\[\]): sequence of N 1D Tensors containing the bin edges.

Return type:

hist ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

Example:

\>>> torch.histogramdd(torch.tensor(\[\[0., 1.\], \[1., 0.\], \[2., 0.\], \[2., 2.\]\]), bins\=\[3, 3\],
...                   weight\=torch.tensor(\[1., 2., 4., 8.\]))
    torch.return\_types.histogramdd(
        hist=tensor(\[\[0., 1., 0.\],\
                     \[2., 0., 0.\],\
                     \[4., 0., 8.\]\]),
        bin\_edges=(tensor(\[0.0000, 0.6667, 1.3333, 2.0000\]),
                   tensor(\[0.0000, 0.6667, 1.3333, 2.0000\])))

\>>> torch.histogramdd(torch.tensor(\[\[0., 0.\], \[1., 1.\], \[2., 2.\]\]), bins\=\[2, 2\],
...                   range\=\[0., 1., 0., 1.\], density\=True)
    torch.return\_types.histogramdd(
       hist=tensor(\[\[2., 0.\],\
                    \[0., 2.\]\]),
       bin\_edges=(tensor(\[0.0000, 0.5000, 1.0000\]),
                  tensor(\[0.0000, 0.5000, 1.0000\])))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.histogramdd.rst.txt)

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