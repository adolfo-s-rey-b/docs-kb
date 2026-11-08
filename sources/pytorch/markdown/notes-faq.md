Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/faq.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/faq.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/faq.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/faq.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/faq.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/faq.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/faq.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/faq.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/faq.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/faq.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/faq.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/faq.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/faq.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/faq.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/faq.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/faq.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/faq.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/faq.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/faq.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/faq.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/faq.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/faq.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/faq.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/faq.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/faq.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/faq.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/faq.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/faq.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/faq.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/faq.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/faq.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/faq.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/faq.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/faq.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/faq.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/faq.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/faq.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/faq.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/faq.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/faq.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/faq.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/faq.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/faq.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/faq.html)

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

Frequently Asked Questions[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#frequently-asked-questions "Link to this heading")

===================================================================================================================================

Created On: May 08, 2026 | Last Updated On: Aug 14, 2026

My model reports “cuda runtime error(2): out of memory”[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#my-model-reports-cuda-runtime-error-2-out-of-memory "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As the error message suggests, you have run out of memory on your GPU. Since we often deal with large amounts of data in PyTorch, small mistakes can rapidly cause your program to use up all of your GPU; fortunately, the fixes in these cases are often simple. Here are a few common things to check:

**Don’t accumulate history across your training loop.** By default, computations involving variables that require gradients will keep history. This means that you should avoid using such variables in computations which will live beyond your training loops, e.g., when tracking statistics. Instead, you should detach the variable or access its underlying data.

Sometimes, it can be non-obvious when differentiable variables can occur. Consider the following training loop (abridged from [source](https://discuss.pytorch.org/t/high-memory-usage-while-training/162)
):

total\_loss \= 0
for i in range(10000):
    optimizer.zero\_grad()
    output \= model(input)
    loss \= criterion(output)
    loss.backward()
    optimizer.step()
    total\_loss += loss

Copy to clipboard

Here, `total_loss` is accumulating history across your training loop, since `loss` is a differentiable variable with autograd history. You can fix this by writing `total_loss += float(loss)` instead.

Other instances of this problem: [1](https://discuss.pytorch.org/t/resolved-gpu-out-of-memory-error-with-batch-size-1/3719)
.

**Don’t hold onto tensors and variables you don’t need.** If you assign a Tensor or Variable to a local, Python will not deallocate until the local goes out of scope. You can free this reference by using `del x`. Similarly, if you assign a Tensor or Variable to a member variable of an object, it will not deallocate until the object goes out of scope. You will get the best memory usage if you don’t hold onto temporaries you don’t need.

The scopes of locals can be larger than you expect. For example:

for i in range(5):
    intermediate \= f(input\[i\])
    result += g(intermediate)
output \= h(result)
return output

Copy to clipboard

Here, `intermediate` remains live even while `h` is executing, because its scope extrudes past the end of the loop. To free it earlier, you should `del intermediate` when you are done with it.

**Avoid running RNNs on sequences that are too large.** The amount of memory required to backpropagate through an RNN scales linearly with the length of the RNN input; thus, you will run out of memory if you try to feed an RNN a sequence that is too long.

The technical term for this phenomenon is [backpropagation through time](https://en.wikipedia.org/wiki/Backpropagation_through_time)
, and there are plenty of references for how to implement truncated BPTT, including in the [word language model](https://github.com/pytorch/examples/tree/master/word_language_model)
 example; truncation is handled by the `repackage` function as described in [this forum post](https://discuss.pytorch.org/t/help-clarifying-repackage-hidden-in-word-language-model/226)
.

**Don’t use linear layers that are too large.** A linear layer `nn.Linear(m, n)` uses O(nm)O(nm)O(nm) memory: that is to say, the memory requirements of the weights scales quadratically with the number of features. It is very easy to [blow through your memory](https://github.com/pytorch/pytorch/issues/958)
 this way (and remember that you will need at least twice the size of the weights, since you also need to store the gradients.)

**Consider checkpointing.** You can trade-off memory for compute by using [checkpoint](https://pytorch.org/docs/stable/checkpoint.html)
.

My GPU memory isn’t freed properly[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#my-gpu-memory-isn-t-freed-properly "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch uses a caching memory allocator to speed up memory allocations. As a result, the values shown in `nvidia-smi` usually don’t reflect the true memory usage. See [Memory management](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-memory-management)
 for more details about GPU memory management.

If your GPU memory isn’t freed even after Python quits, it is very likely that some Python subprocesses are still alive. You may find them via `ps -elf | grep python` and manually kill them with `kill -9 [pid]`.

My out of memory exception handler can’t allocate memory[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#my-out-of-memory-exception-handler-can-t-allocate-memory "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You may have some code that tries to recover from out of memory errors.

try:
    run\_model(batch\_size)
except RuntimeError: \# Out of memory
    for \_ in range(batch\_size):
        run\_model(1)

Copy to clipboard

But find that when you do run out of memory, your recovery code can’t allocate either. That’s because the python exception object holds a reference to the stack frame where the error was raised. Which prevents the original tensor objects from being freed. The solution is to move your OOM recovery code outside of the `except` clause.

oom \= False
try:
    run\_model(batch\_size)
except RuntimeError: \# Out of memory
    oom \= True

if oom:
    for \_ in range(batch\_size):
        run\_model(1)

Copy to clipboard

My data loader workers return identical random numbers[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#my-data-loader-workers-return-identical-random-numbers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are likely using other libraries to generate random numbers in the dataset and worker subprocesses are started via `fork`. See [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
’s documentation for how to properly set up random seeds in workers with its `worker_init_fn` option.

My recurrent network doesn’t work with data parallelism[#](https://docs.pytorch.org/docs/2.15/notes/faq.html#my-recurrent-network-doesn-t-work-with-data-parallelism "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There is a subtlety in using the `pack sequence -> recurrent network -> unpack sequence` pattern in a [`Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 with [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 or [`data_parallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.torch.nn.parallel.data_parallel.html#torch.nn.parallel.data_parallel "torch.nn.parallel.data_parallel")
. Input to each the `forward()` on each device will only be part of the entire input. Because the unpack operation [`torch.nn.utils.rnn.pad_packed_sequence()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.rnn.pad_packed_sequence.html#torch.nn.utils.rnn.pad_packed_sequence "torch.nn.utils.rnn.pad_packed_sequence")
 by default only pads up to the longest input it sees, i.e., the longest on that particular device, size mismatches will happen when results are gathered together. Therefore, you can instead take advantage of the `total_length` argument of [`pad_packed_sequence()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.rnn.pad_packed_sequence.html#torch.nn.utils.rnn.pad_packed_sequence "torch.nn.utils.rnn.pad_packed_sequence")
 to make sure that the `forward()` calls return sequences of same length. For example, you can write:

from torch.nn.utils.rnn import pack\_padded\_sequence, pad\_packed\_sequence

class MyModule(nn.Module):
    \# ... \_\_init\_\_, other methods, etc.

    \# padded\_input is of shape \[B x T x \*\] (batch\_first mode) and contains
    \# the sequences sorted by lengths
    \#   B is the batch size
    \#   T is max sequence length
    def forward(self, padded\_input, input\_lengths):
        total\_length \= padded\_input.size(1)  \# get the max sequence length
        packed\_input \= pack\_padded\_sequence(padded\_input, input\_lengths,
                                            batch\_first\=True)
        packed\_output, \_ \= self.my\_lstm(packed\_input)
        output, \_ \= pad\_packed\_sequence(packed\_output, batch\_first\=True,
                                        total\_length\=total\_length)
        return output

m \= MyModule().cuda()
dp\_m \= nn.DataParallel(m)

Copy to clipboard

Additionally, extra care needs to be taken when batch dimension is dim `1` (i.e., `batch_first=False`) with data parallelism. In this case, the first argument of pack\_padded\_sequence `padding_input` will be of shape `[T x B x *]` and should be scattered along dim `1`, but the second argument `input_lengths` will be of shape `[B]` and should be scattered along dim `0`. Extra code to manipulate the tensor shapes will be needed.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/faq.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/faq.md.txt)

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