Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CTCLoss.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.CTCLoss.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CTCLoss.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CTCLoss.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.CTCLoss.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.CTCLoss.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.CTCLoss.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.CTCLoss.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.CTCLoss.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.CTCLoss.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.CTCLoss.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.CTCLoss.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.CTCLoss.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.CTCLoss.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.CTCLoss.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.CTCLoss.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.CTCLoss.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.CTCLoss.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.CTCLoss.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.CTCLoss.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.CTCLoss.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.CTCLoss.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.CTCLoss.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.CTCLoss.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.CTCLoss.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.CTCLoss.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.CTCLoss.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.CTCLoss.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.CTCLoss.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.CTCLoss.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.CTCLoss.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.CTCLoss.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.CTCLoss.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.CTCLoss.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.CTCLoss.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.CTCLoss.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.CTCLoss.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.CTCLoss.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.CTCLoss.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.CTCLoss.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.CTCLoss.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.CTCLoss.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.CTCLoss.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.CTCLoss.html)

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

CTCLoss[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CTCLoss.html#ctcloss "Link to this heading")

==============================================================================================================

_class_ torch.nn.CTCLoss(_blank\=0_, _reduction\='mean'_, _zero\_infinity\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/loss.py#L2151)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss "Link to this definition")

The Connectionist Temporal Classification loss.

Calculates loss between a continuous (unsegmented) time series and a target sequence. CTCLoss sums over the probability of possible alignments of input to target, producing a loss value which is differentiable with respect to each input node. The alignment of input to target is assumed to be “many-to-one”, which limits the length of the target sequence such that it must be ≤\\leq≤ the input length.

Parameters:

*   **blank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – blank label. Default 000.
    
*   **reduction** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Specifies the reduction to apply to the output: `'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied, `'mean'`: the output losses will be divided by the target lengths and then the mean over the batch is taken, `'sum'`: the output losses will be summed. Default: `'mean'`
    
*   **zero\_infinity** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to zero infinite losses and the associated gradients. Default: `False` Infinite losses mainly occur when the inputs are too short to be aligned to the targets.
    

Shape:

*   Log\_probs: Tensor of size (T,N,C)(T, N, C)(T,N,C) or (T,C)(T, C)(T,C), where T\=input lengthT = \\text{input length}T\=input length, N\=batch sizeN = \\text{batch size}N\=batch size, and C\=number of classes (including blank)C = \\text{number of classes (including blank)}C\=number of classes (including blank). The logarithmized probabilities of the outputs (e.g. obtained with [`torch.nn.functional.log_softmax()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.log_softmax.html#torch.nn.functional.log_softmax "torch.nn.functional.log_softmax")
    ).
    
*   Targets: Tensor of size (N,S)(N, S)(N,S) or (sum⁡(target\_lengths))(\\operatorname{sum}(\\text{target\\\_lengths}))(sum(target\_lengths)), where N\=batch sizeN = \\text{batch size}N\=batch size and S\=max target length, if shape is (N,S)S = \\text{max target length, if shape is } (N, S)S\=max target length, if shape is (N,S). It represents the target sequences. Each element in the target sequence is a class index. And the target index cannot be blank (default=0). In the (N,S)(N, S)(N,S) form, targets are padded to the length of the longest sequence, and stacked. In the (sum⁡(target\_lengths))(\\operatorname{sum}(\\text{target\\\_lengths}))(sum(target\_lengths)) form, the targets are assumed to be un-padded and concatenated within 1 dimension.
    
*   Input\_lengths: Tuple or tensor of size (N)(N)(N) or ()()(), where N\=batch sizeN = \\text{batch size}N\=batch size. It represents the lengths of the inputs (must each be ≤T\\leq T≤T). And the lengths are specified for each sequence to achieve masking under the assumption that sequences are padded to equal lengths.
    
*   Target\_lengths: Tuple or tensor of size (N)(N)(N) or ()()(), where N\=batch sizeN = \\text{batch size}N\=batch size. It represents lengths of the targets. Lengths are specified for each sequence to achieve masking under the assumption that sequences are padded to equal lengths. If target shape is (N,S)(N,S)(N,S), target\_lengths are effectively the stop index sns\_nsn​ for each target sequence, such that `target_n = targets[n,0:s_n]` for each target in a batch. Lengths must each be ≤S\\leq S≤S If the targets are given as a 1d tensor that is the concatenation of individual targets, the target\_lengths must add up to the total length of the tensor.
    
*   Output: scalar if `reduction` is `'mean'` (default) or `'sum'`. If `reduction` is `'none'`, then (N)(N)(N) if input is batched or ()()() if input is unbatched, where N\=batch sizeN = \\text{batch size}N\=batch size.
    

Examples

\>>> \# Target are to be padded
\>>> T \= 50  \# Input sequence length
\>>> C \= 20  \# Number of classes (including blank)
\>>> N \= 16  \# Batch size
\>>> S \= 30  \# Target sequence length of longest target in batch (padding length)
\>>> S\_min \= 10  \# Minimum target length, for demonstration purposes
\>>>
\>>> \# Initialize random batch of input vectors, for \*size = (T,N,C)
\>>> input \= torch.randn(T, N, C).log\_softmax(2).detach().requires\_grad\_()
\>>>
\>>> \# Initialize random batch of targets (0 = blank, 1:C = classes)
\>>> target \= torch.randint(low\=1, high\=C, size\=(N, S), dtype\=torch.long)
\>>>
\>>> input\_lengths \= torch.full(size\=(N,), fill\_value\=T, dtype\=torch.long)
\>>> target\_lengths \= torch.randint(
...     low\=S\_min,
...     high\=S,
...     size\=(N,),
...     dtype\=torch.long,
... )
\>>> ctc\_loss \= nn.CTCLoss()
\>>> loss \= ctc\_loss(input, target, input\_lengths, target\_lengths)
\>>> loss.backward()
\>>>
\>>>
\>>> \# Target are to be un-padded
\>>> T \= 50  \# Input sequence length
\>>> C \= 20  \# Number of classes (including blank)
\>>> N \= 16  \# Batch size
\>>>
\>>> \# Initialize random batch of input vectors, for \*size = (T,N,C)
\>>> input \= torch.randn(T, N, C).log\_softmax(2).detach().requires\_grad\_()
\>>> input\_lengths \= torch.full(size\=(N,), fill\_value\=T, dtype\=torch.long)
\>>>
\>>> \# Initialize random batch of targets (0 = blank, 1:C = classes)
\>>> target\_lengths \= torch.randint(low\=1, high\=T, size\=(N,), dtype\=torch.long)
\>>> target \= torch.randint(
...     low\=1,
...     high\=C,
...     size\=(sum(target\_lengths),),
...     dtype\=torch.long,
... )
\>>> ctc\_loss \= nn.CTCLoss()
\>>> loss \= ctc\_loss(input, target, input\_lengths, target\_lengths)
\>>> loss.backward()
\>>>
\>>>
\>>> \# Target are to be un-padded and unbatched (effectively N=1)
\>>> T \= 50  \# Input sequence length
\>>> C \= 20  \# Number of classes (including blank)
\>>>
\>>> \# Initialize random batch of input vectors, for \*size = (T,C)
\>>> input \= torch.randn(T, C).log\_softmax(1).detach().requires\_grad\_()
\>>> input\_lengths \= torch.tensor(T, dtype\=torch.long)
\>>>
\>>> \# Initialize random batch of targets (0 = blank, 1:C = classes)
\>>> target\_lengths \= torch.randint(low\=1, high\=T, size\=(), dtype\=torch.long)
\>>> target \= torch.randint(
...     low\=1,
...     high\=C,
...     size\=(target\_lengths,),
...     dtype\=torch.long,
... )
\>>> ctc\_loss \= nn.CTCLoss()
\>>> loss \= ctc\_loss(input, target, input\_lengths, target\_lengths)
\>>> loss.backward()

Copy to clipboard

Reference:

A. Graves et al.: Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks: [https://www.cs.toronto.edu/~graves/icml\_2006.pdf](https://www.cs.toronto.edu/~graves/icml_2006.pdf)

Note

In order to use CuDNN, the following must be satisfied: the `targets` must be in concatenated format, all `input_lengths` must be T. blank\=0blank=0blank\=0, `target_lengths` ≤256\\leq 256≤256, the integer arguments must be of dtype `torch.int32`, and the `log_probs` itself must be of dtype `torch.float32`.

The regular implementation uses the (more common in PyTorch) torch.long dtype.

Note

In some circumstances when using the CUDA backend with CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. Please see the notes on [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for background.

forward(_log\_probs_, _targets_, _input\_lengths_, _target\_lengths_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/loss.py#L2313)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.CTCLoss.rst.txt)

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