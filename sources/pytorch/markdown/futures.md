Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/futures.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/futures.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/futures.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/futures.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/futures.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/futures.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/futures.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/futures.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/futures.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/futures.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/futures.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/futures.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/futures.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/futures.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/futures.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/futures.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/futures.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/futures.html)
[v1.13](https://docs.pytorch.org/docs/1.13/futures.html)
[v1.12](https://docs.pytorch.org/docs/1.12/futures.html)
[v1.11](https://docs.pytorch.org/docs/1.11/futures.html)
[v1.10](https://docs.pytorch.org/docs/1.10/futures.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/futures.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/futures.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/futures.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/futures.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/futures.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/futures.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/futures.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/futures.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/futures.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/futures.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/futures.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/futures.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/futures.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/futures.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/futures.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/futures.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/futures.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/futures.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/futures.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/futures.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/futures.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/futures.html)

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

torch.futures[#](https://docs.pytorch.org/docs/2.15/futures.html#torch-futures "Link to this heading")

=======================================================================================================

Created On: Jun 12, 2025 | Last Updated On: Jun 12, 2025

This package provides a [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 type that encapsulates an asynchronous execution and a set of utility functions to simplify operations on [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 objects. Currently, the [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 type is primarily used by the [Distributed RPC Framework](https://docs.pytorch.org/docs/2.15/rpc.html#distributed-rpc-framework)
.

_class_ torch.futures.Future(_\*_, _devices\=None_)[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "Link to this definition")

Wrapper around a `torch._C.Future` which encapsulates an asynchronous execution of a callable, e.g. [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
. It also exposes a set of APIs to add callback functions and set results.

Warning

GPU support is a beta feature, subject to changes.

add\_done\_callback(_callback_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L168)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.add_done_callback "Link to this definition")

Append the given callback function to this `Future`, which will be run when the `Future` is completed. Multiple callbacks can be added to the same `Future`, but the order in which they will be executed cannot be guaranteed. The callback must take one argument, which is the reference to this `Future`. The callback function can use the [`value()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.value "torch.futures.Future.value")
 method to get the value. Note that if this `Future` is already completed, the given callback will be run inline.

We recommend that you use the [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
 method as it provides a way to synchronize after your callback has completed. `add_done_callback` can be cheaper if your callback does not return anything. But both [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
 and `add_done_callback` use the same callback registration API under the hood.

With respect to GPU tensors, this method behaves in the same way as [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
.

Parameters:

**callback** (`Future`) – a `Callable` that takes in one argument, which is the reference to this `Future`.

Note

Note that if the callback function throws, either through the original future being completed with an exception and calling `fut.wait()`, or through other code in the callback, error handling must be carefully taken care of. For example, if this callback later completes additional futures, those futures are not marked as completed with an error and the user is responsible for handling completion/waiting on those futures independently.

Example:

\>>> def callback(fut):
...     print("This will run after the future has finished.")
...     print(fut.wait())
\>>> fut \= torch.futures.Future()
\>>> fut.add\_done\_callback(callback)
\>>> fut.set\_result(5)
This will run after the future has finished.
5

Copy to clipboard

done()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L48)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.done "Link to this definition")

Return `True` if this `Future` is done. A `Future` is done if it has a result or an exception.

If the value contains tensors that reside on GPUs, `Future.done()` will return `True` even if the asynchronous kernels that are populating those tensors haven’t yet completed running on the device, because at such stage the result is already usable, provided one performs the appropriate synchronizations (see [`wait()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.wait "torch.futures.Future.wait")
).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

set\_exception(_result_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L253)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.set_exception "Link to this definition")

Set an exception for this `Future`, which will mark this `Future` as completed with an error and trigger all attached callbacks. Note that when calling wait()/value() on this `Future`, the exception set here will be raised inline.

Parameters:

**result** ([_BaseException_](https://docs.python.org/3/builtins/exceptions.html#BaseException "(in Python v3.15)")
) – the exception for this `Future`.

Example:

\>>> fut \= torch.futures.Future()
\>>> fut.set\_exception(ValueError("foo"))
\>>> fut.wait()
Traceback (most recent call last):
...
ValueError: foo

Copy to clipboard

set\_result(_result_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L213)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.set_result "Link to this definition")

Set the result for this `Future`, which will mark this `Future` as completed and trigger all attached callbacks. Note that a `Future` cannot be marked completed twice.

If the result contains tensors that reside on GPUs, this method can be called even if the asynchronous kernels that are populating those tensors haven’t yet completed running on the device, provided that the streams on which those kernels were enqueued are set as the current ones when this method is called. Put simply, it’s safe to call this method immediately after launching those kernels, without any additional synchronization, as long as one doesn’t change streams in between. This method will record events on all the relevant current streams and will use them to ensure proper scheduling for all the consumers of this `Future`.

Parameters:

**result** ([_object_](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
) – the result object of this `Future`.

Example:

\>>> import threading
\>>> import time
\>>> def slow\_set\_future(fut, value):
...     time.sleep(0.5)
...     fut.set\_result(value)
\>>> fut \= torch.futures.Future()
\>>> t \= threading.Thread(
...     target\=slow\_set\_future,
...     args\=(fut, torch.ones(2) \* 3)
... )
\>>> t.start()
\>>> print(fut.wait())
tensor(\[3., 3.\])
\>>> t.join()

Copy to clipboard

then(_callback_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L103)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "Link to this definition")

Append the given callback function to this `Future`, which will be run when the `Future` is completed. Multiple callbacks can be added to the same `Future`, but the order in which they will be executed cannot be guaranteed (to enforce a certain order consider chaining: `fut.then(cb1).then(cb2)`). The callback must take one argument, which is the reference to this `Future`. The callback function can use the [`value()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.value "torch.futures.Future.value")
 method to get the value. Note that if this `Future` is already completed, the given callback will be run immediately inline.

If the `Future`’s value contains tensors that reside on GPUs, the callback might be invoked while the async kernels that are populating those tensors haven’t yet finished executing on the device. However, the callback will be invoked with some dedicated streams set as current (fetched from a global pool) which will be synchronized with those kernels. Hence any operation performed by the callback on these tensors will be scheduled on the device after the kernels complete. In other words, as long as the callback doesn’t switch streams, it can safely manipulate the result without any additional synchronization. This is similar to the non-blocking behavior of [`wait()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.wait "torch.futures.Future.wait")
.

Similarly, if the callback returns a value that contains tensors that reside on a GPU, it can do so even if the kernels that are producing these tensors are still running on the device, as long as the callback didn’t change streams during its execution. If one wants to change streams, one must be careful to re-synchronize them with the original streams, that is, those that were current when the callback was invoked.

Parameters:

**callback** (`Callable`) – a `Callable` that takes this `Future` as the only argument.

Returns:

A new `Future` object that holds the return value of the `callback` and will be marked as completed when the given `callback` finishes.

Return type:

[Future](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
\[S\]

Note

Note that if the callback function throws, either through the original future being completed with an exception and calling `fut.wait()`, or through other code in the callback, the future returned by `then` will be marked appropriately with the encountered error. However, if this callback later completes additional futures, those futures are not marked as completed with an error and the user is responsible for handling completion/waiting on those futures independently.

Example:

\>>> def callback(fut):
...     print(f"RPC return value is {fut.wait()}.")
\>>> fut \= torch.futures.Future()
\>>> \# The inserted callback will print the return value when
\>>> \# receiving the response from "worker1"
\>>> cb\_fut \= fut.then(callback)
\>>> chain\_cb\_fut \= cb\_fut.then(
...     lambda x : print(f"Chained cb done. {x.wait()}")
... )
\>>> fut.set\_result(5)
RPC return value is 5.
Chained cb done. None

Copy to clipboard

value()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L82)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.value "Link to this definition")

Obtain the value of an already-completed future.

This method should only be called after a call to [`wait()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.wait "torch.futures.Future.wait")
 has completed, or inside a callback function passed to [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
. In other cases this `Future` may not yet hold a value and calling `value()` could fail.

If the value contains tensors that reside on GPUs, then this method will _not_ perform any additional synchronization. This should be done beforehand, separately, through a call to [`wait()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.wait "torch.futures.Future.wait")
 (except within callbacks, for which it’s already being taken care of by [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
).

Returns:

The value held by this `Future`. If the function (callback or RPC) creating the value has thrown an error, this `value()` method will also throw an error.

Return type:

_T_

wait()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L61)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.wait "Link to this definition")

Block until the value of this `Future` is ready.

If the value contains tensors that reside on GPUs, then an additional synchronization is performed with the kernels (executing on the device) which may be asynchronously populating those tensors. Such sync is non-blocking, which means that `wait()` will insert the necessary instructions in the current streams to ensure that further operations enqueued on those streams will be properly scheduled after the async kernels but, once that is done, `wait()` will return, even if those kernels are still running. No further synchronization is required when accessing and using the values, as long as one doesn’t change streams.

Returns:

The value held by this `Future`. If the function (callback or RPC) creating the value has thrown an error, this `wait` method will also throw an error.

Return type:

_T_

torch.futures.collect\_all(_futures_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L285)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.collect_all "Link to this definition")

Collects the provided [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 objects into a single combined [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 that is completed when all of the sub-futures are completed.

Parameters:

**futures** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
) – a list of [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 objects.

Returns:

Returns a [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object to a list of the passed in Futures.

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")\
\]\]

Example::

\>>> fut0 \= torch.futures.Future()
\>>> fut1 \= torch.futures.Future()
\>>> fut \= torch.futures.collect\_all(\[fut0, fut1\])
\>>> fut0.set\_result(0)
\>>> fut1.set\_result(1)
\>>> fut\_list \= fut.wait()
\>>> print(f"fut0 result = {fut\_list\[0\].wait()}")
fut0 result = 0
\>>> print(f"fut1 result = {fut\_list\[1\].wait()}")
fut1 result = 1

Copy to clipboard

torch.futures.wait\_all(_futures_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/futures/__init__.py#L317)
[#](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.wait_all "Link to this definition")

Waits for all provided futures to be complete, and returns the list of completed values. If any of the futures encounters an error, the method will exit early and report the error not waiting for other futures to complete.

Parameters:

**futures** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
) – a list of [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object.

Returns:

A list of the completed [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 results. This method will throw an error if `wait` on any [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 throws.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/futures.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/futures.md.txt)

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