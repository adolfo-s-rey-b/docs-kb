Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/numa.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/numa.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/numa.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/numa.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/numa.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/numa.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/numa.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/numa.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/numa.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/numa.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/numa.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/numa.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/numa.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/numa.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/numa.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/numa.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/numa.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/numa.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/numa.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/numa.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/numa.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/numa.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/numa.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/numa.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/numa.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/numa.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/numa.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/numa.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/numa.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/numa.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/numa.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/numa.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/numa.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/numa.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/numa.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/numa.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/numa.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/numa.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/numa.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/numa.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/numa.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/numa.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/numa.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/numa.html)

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

NUMA Binding[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#module-torch.numa "Link to this heading")

===============================================================================================================

Created On: Jul 25, 2025 | Last Updated On: May 06, 2026

In NUMA (Non-Uniform Memory Access) systems, accessing memory on remote NUMA nodes incurs additional latency. PyTorch provides NUMA binding utilities to promote memory locality by binding worker processes to CPUs near their assigned accelerator devices.

In practice, NUMA binding typically results in 1-10% overall performance improvements, but some workloads may obtain much greater benefits or none at all.

To enable NUMA binding, use the `--numa-binding` flag with [torchrun](https://docs.pytorch.org/docs/2.15/elastic/run.html#launcher-api)
, e.g.:

torchrun \--numa-binding\=node \--nproc\_per\_node\=8 train.py

Copy to clipboard

Alternatively, pass [`NumaOptions`](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.NumaOptions "torch.numa.binding.NumaOptions")
 to `LaunchConfig` when using `elastic_launch`.

See [`AffinityMode`](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode "torch.numa.binding.AffinityMode")
 for available binding modes.

_class_ torch.numa.binding.AffinityMode(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/numa/binding.py#L44)
[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode "Link to this definition")

NODE _\= 'node'_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode.NODE "Link to this definition")

Each worker process and its threads will be bound to all the CPUs on the NUMA node containing the accelerator device whose local index equals the worker’s local rank. If in doubt, use this option rather than the others.

**Ex.:** If device 3 lives on NUMA node 1, then the worker whose local rank is 3 will only be able to run on the CPUs of NUMA node 1.

SOCKET _\= 'socket'_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode.SOCKET "Link to this definition")

Each worker process and its threads will be bound to all the CPUs on all the NUMA nodes of the socket containing the accelerator device whose local index equals the worker’s local rank.

**Ex.:** If socket 0 contains device 3 and NUMA nodes 0-1, then the worker whose local rank is 3 will be bound to the CPUs of NUMA nodes 0-1.

For cases where there is only one NUMA node per socket anyway, this is equivalent to NODE.

EXCLUSIVE _\= 'exclusive'_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode.EXCLUSIVE "Link to this definition")

Each worker process and its threads will be bound to an exclusive subset of CPUs on the NUMA node containing the accelerator device whose local index equals the worker’s local rank. The CPUs on the NUMA node are divided evenly among all devices on that node, so no two workers share the same CPU cores.

**Ex.:** If NUMA node 1 has 16 physical cores and devices 2 and 3, then the worker whose local rank is 2 will be bound to cores 0-7, and the worker whose local rank is 3 will be bound to cores 8-15.

CORE\_COMPLEX _\= 'core-complex'_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode.CORE_COMPLEX "Link to this definition")

Each worker process and its threads will be bound to a single core complex (a group of cores sharing the same L3 cache) on the NUMA node containing the accelerator device whose local index equals the worker’s local rank. Each worker is bound to a different core complex when possible.

**Ex.:** If NUMA node 1 has two core complexes (cores 0-7 sharing one L3 cache, cores 8-15 sharing another) and devices 2 and 3, then the worker whose local rank is 2 will be bound to cores 0-7, and the worker whose local rank is 3 will be bound to cores 8-15.

_class_ torch.numa.binding.NumaOptions(_affinity\_mode: [torch.numa.binding.AffinityMode](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode "torch.numa.binding.AffinityMode")
_, _should\_fall\_back\_if\_binding\_fails: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/numa/binding.py#L91)
[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.NumaOptions "Link to this definition")

affinity\_mode_: [AffinityMode](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.AffinityMode "torch.numa.binding.AffinityMode")
_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.NumaOptions.affinity_mode "Link to this definition")

should\_fall\_back\_if\_binding\_fails_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_ _\= False_[#](https://docs.pytorch.org/docs/2.15/elastic/numa.html#torch.numa.binding.NumaOptions.should_fall_back_if_binding_fails "Link to this definition")

If `True`, we will silence any exceptions that occur during NUMA binding itself rather than raising them.

There are no expected exceptions, so avoid using this option. Its purpose is simply to mitigate crash risk while conducting mass rollouts of NUMA binding.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/numa.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/numa.md.txt)

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