Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/rendezvous.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/rendezvous.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/rendezvous.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/rendezvous.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/rendezvous.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/rendezvous.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/rendezvous.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/rendezvous.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/rendezvous.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/rendezvous.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/rendezvous.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/rendezvous.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/rendezvous.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/rendezvous.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/rendezvous.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/rendezvous.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/rendezvous.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/rendezvous.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/rendezvous.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/rendezvous.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/rendezvous.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/rendezvous.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/rendezvous.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/rendezvous.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/rendezvous.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/rendezvous.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/rendezvous.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/rendezvous.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/rendezvous.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/rendezvous.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/rendezvous.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/rendezvous.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/rendezvous.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/rendezvous.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/rendezvous.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/rendezvous.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/rendezvous.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/rendezvous.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/rendezvous.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/rendezvous.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/rendezvous.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/rendezvous.html)

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

Rendezvous[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#module-torch.distributed.elastic.rendezvous "Link to this heading")

=============================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 11, 2026

In the context of Torch Distributed Elastic we use the term _rendezvous_ to refer to a particular functionality that combines a **distributed synchronization** primitive with **peer discovery**.

It is used by Torch Distributed Elastic to gather participants of a training job (i.e. nodes) such that they all agree on the same list of participants and everyone’s roles, as well as make a consistent collective decision on when training can begin/resume.

Torch Distributed Elastic rendezvous provides the following critical functionalities:

**Barrier**:

Nodes performing rendezvous will all block until the rendezvous is considered complete - this happens when at least `min` total number of nodes have joined the rendezvous barrier (for the same job). This also implies the barrier is not necessarily of fixed size.

There’s an additional small waiting time after reaching `min` number of nodes - this is used to ensure the rendezvous is not completed “too quickly” (which could potentially exclude additional nodes attempting to join at approximately the same time).

If `max` number of nodes is gathered at the barrier, the rendezvous is completed immediately.

There’s also an overall timeout which causes the rendezvous to fail if `min` number of nodes is never reached - this is meant to be a simple fail-safe to help release partially allocated job resources, in case there’s a problem with the resource manager, and is meant to be interpreted as non-retryable.

**Exclusivity**:

A simple distributed barrier would not be sufficient, as we also need to ensure that only one group of nodes exists at any given time (for a given job). In other words, new nodes (i.e. joining late) should not be able to form a parallel independent group of workers for the same job.

Torch Distributed Elastic rendezvous ensures that if a group of nodes has already completed a rendezvous (and hence might already be training), then additional “late” nodes attempting to rendezvous will only announce themselves as waiting, and will have to wait until the (previously completed) existing rendezvous is destroyed first.

**Consistency**:

When a rendezvous is completed, all its members will agree on the job membership and everyone’s role in it. This role is represented using an integer, called rank, that is between 0 and world size.

Note that ranks are _not stable_, in the sense that the same node can be assigned a different rank in the next (re-)rendezvous.

**Fault-tolerance**:

Torch Distributed Elastic rendezvous is designed to tolerate node failures during the rendezvous process. Should a process crash (or lose network connectivity, etc), between joining the rendezvous and it being completed, then a re-rendezvous with remaining healthy nodes will happen automatically.

A node can also fail _after_ it has completed (or _has been observed_ by other nodes to have completed) the rendezvous - this scenario will be handled by the Torch Distributed Elastic `train_loop` instead (where it will also trigger a re-rendezvous).

**Shared key-value store**:

When the rendezvous is completed, a shared key-value store is created and returned. This store implements a `torch.distributed.Store` API (see [distributed communication docs](https://pytorch.org/docs/stable/distributed.html)
).

This store is only shared by the members of the completed rendezvous. It is intended to be used by Torch Distributed Elastic to exchange information necessary to initialize job control and data-planes.

**Waiting workers and rendezvous closing**:

Torch Distributed Elastic rendezvous handler object provides additional functionalities, which are technically not part of the rendezvous process:

1.  Querying how many workers arrived late at the barrier, who can participate in _next_ rendezvous.
    
2.  Setting the rendezvous _closed_ to signal all nodes not to participate in next rendezvous.
    

**DynamicRendezvousHandler**:

Torch Distributed Elastic comes with the [`DynamicRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler")
 class that implements the rendezvous mechanism described above. It is a backend- agnostic type that expects a particular [`RendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend "torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend")
 instance to be specified during construction.

Torch distributed users can either implement their own backend type or use one of the following implementations that come with PyTorch:

*   [`C10dRendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend "torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend")
    : Uses a C10d store (by default `TCPStore`) as the rendezvous backend. The main advantage of using a C10d store is that it requires no 3rd-party dependency (such as etcd) to establish a rendezvous.
    
*   [`EtcdRendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend "torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend")
    : Supersedes the legacy [`EtcdRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvousHandler "torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvousHandler")
     class. Passing an [`EtcdRendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend "torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend")
     instance to [`DynamicRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler")
     is functionally equivalent to instantiating an [`EtcdRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvousHandler "torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvousHandler")
    .
    
    store \= TCPStore("localhost")
    
    backend \= C10dRendezvousBackend(store, "my\_run\_id")
    
    rdzv\_handler \= DynamicRendezvousHandler.from\_backend(
        run\_id\="my\_run\_id", store\=store, backend\=backend, min\_nodes\=2, max\_nodes\=4
    )
    
    Copy to clipboard
    

Below is a state diagram describing how rendezvous works.

![Rendezvous state diagram](https://docs.pytorch.org/docs/2.15/_images/etcd_rdzv_diagram.png)

Registry[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#registry "Link to this heading")

--------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.rendezvous.RendezvousParameters(_backend_, _endpoint_, _run\_id_, _min\_nodes_, _max\_nodes_, _local\_addr\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L241)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousParameters "Link to this definition")

Hold the parameters to construct a [`RendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.RendezvousHandler")
.

Parameters:

*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of the backend to use to handle the rendezvous.
    
*   **endpoint** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The endpoint of the rendezvous, usually in form <hostname>\[:<port>\].
    
*   **run\_id** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The id of the rendezvous.
    
*   **min\_nodes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The minimum number of nodes to admit to the rendezvous.
    
*   **max\_nodes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The maximum number of nodes to admit to the rendezvous.
    
*   **local\_addr** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – The address of the local node.
    
*   **\*\*kwargs** – Additional parameters for the specified backend.
    

get(_key_, _default\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L292)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousParameters.get "Link to this definition")

Return the value for `key` if `key` exists, else `default`.

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

get\_as\_bool(_key_, _default\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L296)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousParameters.get_as_bool "Link to this definition")

Return the value for `key` as a `bool`.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | None

get\_as\_int(_key_, _default\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L315)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousParameters.get_as_int "Link to this definition")

Return the value for `key` as an `int`.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | None

_class_ torch.distributed.elastic.rendezvous.RendezvousHandlerRegistry[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L332)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandlerRegistry "Link to this definition")

Represent a registry of [`RendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.RendezvousHandler")
 backends.

torch.distributed.elastic.rendezvous.registry.get\_rendezvous\_handler(_params_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/registry.py#L74)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.registry.get_rendezvous_handler "Link to this definition")

Obtain a reference to a :py:class\`RendezvousHandler\`.

Custom rendezvous handlers can be registered by

from torch.distributed.elastic.rendezvous import rendezvous\_handler\_registry
from torch.distributed.elastic.rendezvous.registry import get\_rendezvous\_handler

def create\_my\_rdzv(params: RendezvousParameters):
    return MyCustomRdzv(params)

rendezvous\_handler\_registry.register("my\_rdzv\_backend\_name", create\_my\_rdzv)

my\_rdzv\_handler \= get\_rendezvous\_handler(
    "my\_rdzv\_backend\_name", RendezvousParameters
)

Copy to clipboard

Return type:

[_RendezvousHandler_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.api.RendezvousHandler")

Handler[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#handler "Link to this heading")

------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.rendezvous.RendezvousHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L145)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "Link to this definition")

Main rendezvous interface.

Note

Distributed Torch users normally **do not** need to implement their own `RendezvousHandler`. An implementation based on C10d Store is already provided, and is recommended for most users.

_abstract_ get\_backend()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L154)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.get_backend "Link to this definition")

Return the name of the rendezvous backend.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

_abstract_ get\_run\_id()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L218)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.get_run_id "Link to this definition")

Return the run id of the rendezvous.

The run id is a user-defined id that uniquely identifies an instance of a distributed application. It typically maps to a job id and is used to allow nodes to join the correct distributed application.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

_abstract_ is\_closed()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L190)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.is_closed "Link to this definition")

Check whether the rendezvous has been closed.

A closed rendezvous means all future attempts to re-rendezvous within same job will fail.

`is_closed()` and [`set_closed()`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.set_closed "torch.distributed.elastic.rendezvous.RendezvousHandler.set_closed")
 have semantics of eventual propagation and should not be used for synchronization. The intention is that if at least one node decides the job is finished, it will close the rendezvous, and other nodes will soon observe this and stop running as well.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_abstract_ next\_rendezvous()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L168)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.next_rendezvous "Link to this definition")

Main entry-point into the rendezvous barrier.

Blocks until the rendezvous is complete and the current process is included in the formed worker group, or a timeout occurs, or the rendezvous was marked closed.

Returns:

Instance of [`RendezvousInfo`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousInfo "torch.distributed.elastic.rendezvous.RendezvousInfo")
.

Raises:

*   [**RendezvousClosedError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousClosedError "torch.distributed.elastic.rendezvous.api.RendezvousClosedError")
     – The rendezvous is closed.
    
*   [**RendezvousConnectionError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousConnectionError "torch.distributed.elastic.rendezvous.api.RendezvousConnectionError")
     – The connection to the rendezvous backend has failed.
    
*   [**RendezvousStateError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStateError "torch.distributed.elastic.rendezvous.api.RendezvousStateError")
     – The rendezvous state is corrupt.
    
*   [**RendezvousTimeoutError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousTimeoutError "torch.distributed.elastic.rendezvous.api.RendezvousTimeoutError")
     – The rendezvous did not complete on time.
    

Return type:

[_RendezvousInfo_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousInfo "torch.distributed.elastic.rendezvous.api.RendezvousInfo")

_abstract_ num\_nodes\_waiting()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L208)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.num_nodes_waiting "Link to this definition")

Return the number of nodes who arrived late at the rendezvous barrier, hence were not included in the current worker group.

Callers should periodically call this method to check whether new nodes are waiting to join the job and if so admit them by calling [`next_rendezvous()`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.next_rendezvous "torch.distributed.elastic.rendezvous.RendezvousHandler.next_rendezvous")
 (re-rendezvous).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

_abstract_ set\_closed()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L204)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.set_closed "Link to this definition")

Mark the rendezvous as closed.

_abstract_ shutdown()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L227)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.shutdown "Link to this definition")

Close all resources that were open for the rendezvous.

Example:

rdzv\_handler \= ...
try:
    store, rank, world\_size \= rdzv\_handler.next\_rendezvous()
finally:
    rdzv\_handler.shutdown()

Copy to clipboard

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_property_ use\_agent\_store_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.use_agent_store "Link to this definition")

Indicates that store reference returned by [`next_rendezvous()`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler.next_rendezvous "torch.distributed.elastic.rendezvous.RendezvousHandler.next_rendezvous")
 can be shared with user applications and will be available during application lifecycle.

Rendezvous handler impl will share store details as instance of `RendezvousStoreInfo`. Applications as a convention use MASTER\_ADDR/MASTER\_PORT env variables to lookup the store.

Dataclasses[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#dataclasses "Link to this heading")

--------------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.rendezvous.RendezvousInfo(_store_, _rank_, _world\_size_, _bootstrap\_store\_info_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L109)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousInfo "Link to this definition")

Holds the information about the rendezvous.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousStoreInfo(_master\_addr_, _master\_port_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L62)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStoreInfo "Link to this definition")

Store address and port that can be used to bootstrap trainer distributed comms

_static_ build(_rank_, _store_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L71)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStoreInfo.build "Link to this definition")

Factory method, finds unused new port on rank0 host and addr/port info with all ranks.

If master\_addr/master\_port is known (useful when sharing existing tcp store server) use the constructor.

Parameters:

*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – rank of the current node
    
*   **store** ([_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")
    ) – store to use for rendezvous
    
*   **local\_addr** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – address of the current node, if not provided will be resolved from hostname
    
*   **server\_port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – port of the TCPStore server, when the TCPStore is shared.
    

Return type:

[_RendezvousStoreInfo_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStoreInfo "torch.distributed.elastic.rendezvous.api.RendezvousStoreInfo")

Exceptions[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#exceptions "Link to this heading")

------------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.rendezvous.api.RendezvousError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L35)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousError "Link to this definition")

Represents the base type for rendezvous errors.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousClosedError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L39)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousClosedError "Link to this definition")

Raised when a rendezvous is closed.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousTimeoutError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L43)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousTimeoutError "Link to this definition")

Raised when a rendezvous did not complete on time.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousConnectionError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L47)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousConnectionError "Link to this definition")

Raised when the connection to a rendezvous backend has failed.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousStateError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L51)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStateError "Link to this definition")

Raised when the state of a rendezvous is corrupt.

_class_ torch.distributed.elastic.rendezvous.api.RendezvousGracefulExitError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/api.py#L55)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousGracefulExitError "Link to this definition")

Raised when node wasn’t included in rendezvous and gracefully exits.

Exception is a mechanism to exit the stack, however does not mean a failure.

Implementations[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#implementations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

### Dynamic Rendezvous[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#dynamic-rendezvous "Link to this heading")

torch.distributed.elastic.rendezvous.dynamic\_rendezvous.create\_handler(_store_, _backend_, _params_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L1407)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.create_handler "Link to this definition")

Create a new [`DynamicRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler")
 from the specified parameters.

Parameters:

*   **store** ([_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")
    ) – The C10d store to return as part of the rendezvous.
    
*   **backend** ([_RendezvousBackend_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend "torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend")
    ) – The backend to use to hold the rendezvous state.
    

Return type:

[_DynamicRendezvousHandler_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler")

| Parameter | Description |
| --- | --- |
| join\_timeout | The total time, in seconds, within which the rendezvous is expected to complete. Defaults to 600 seconds. |
| last\_call\_timeout | An additional wait amount, in seconds, before completing the rendezvous once the minimum number of nodes has been reached. Defaults to 30 seconds. |
| close\_timeout | The time, in seconds, within which the rendezvous is expected to close after a call to `RendezvousHandler.set_closed()` or `RendezvousHandler.shutdown()`. Defaults to 30 seconds. |
| heartbeat | The time, in seconds, within which a keep-alive heartbeat is expected to complete |
| cas\_backoff\_max\_seconds | Maximum random delay after a failed state write, in seconds. Defaults to 0.0, which disables backoff. Must be finite and non-negative. |

_class_ torch.distributed.elastic.rendezvous.dynamic\_rendezvous.DynamicRendezvousHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L1002)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "Link to this definition")

Represent a handler that sets up a rendezvous among a set of nodes.

_classmethod_ from\_backend(_run\_id_, _store_, _backend_, _min\_nodes_, _max\_nodes_, _local\_addr\=None_, _timeout\=None_, _keep\_alive\_interval\=5_, _keep\_alive\_max\_attempt\=3_, _cas\_backoff\_max\_seconds\=0.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L1017)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler.from_backend "Link to this definition")

Create a new [`DynamicRendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler "torch.distributed.elastic.rendezvous.dynamic_rendezvous.DynamicRendezvousHandler")
.

Parameters:

*   **run\_id** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The run id of the rendezvous.
    
*   **store** ([_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")
    ) – The C10d store to return as part of the rendezvous.
    
*   **backend** ([_RendezvousBackend_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend "torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend")
    ) – The backend to use to hold the rendezvous state.
    
*   **min\_nodes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The minimum number of nodes to admit to the rendezvous.
    
*   **max\_nodes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The maximum number of nodes to admit to the rendezvous.
    
*   **local\_addr** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – The local node address.
    
*   **timeout** ([_RendezvousTimeout_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout "torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout")
     _|_ _None_) – The timeout configuration of the rendezvous.
    
*   **keep\_alive\_interval** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The amount of time a node waits before sending a heartbeat to keep it alive in the rendezvous.
    
*   **keep\_alive\_max\_attempt** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The maximum number of failed heartbeat attempts after which a node is considered dead.
    
*   **cas\_backoff\_max\_seconds** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – The maximum random delay in seconds after a failed state write.
    

_class_ torch.distributed.elastic.rendezvous.dynamic\_rendezvous.RendezvousBackend[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L63)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend "Link to this definition")

Represent a backend that holds the rendezvous state.

_abstract_ get\_state()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L71)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend.get_state "Link to this definition")

Get the rendezvous state.

Returns:

A tuple of the encoded rendezvous state and its fencing token or `None` if no state is found in the backend.

Raises:

*   [**RendezvousConnectionError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousConnectionError "torch.distributed.elastic.rendezvous.api.RendezvousConnectionError")
     – The connection to the backend has failed.
    
*   [**RendezvousStateError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStateError "torch.distributed.elastic.rendezvous.api.RendezvousStateError")
     – The rendezvous state is corrupt.
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | None

_abstract property_ name_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend.name "Link to this definition")

Get the name of the backend.

_abstract_ set\_state(_state_, _token\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L86)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend.set_state "Link to this definition")

Set the rendezvous state.

The new rendezvous state is set conditionally:

> *   If the specified `token` matches the fencing token stored in the backend, the state will be updated. The new state will be returned to the caller along with its fencing token.
>     
> *   If the specified `token` does not match the fencing token stored in the backend, the state won’t be updated; instead the existing state along with its fencing token will be returned to the caller.
>     
> *   If the specified `token` is `None`, the new state will be set only if there is no existing state in the backend. Either the new state or the existing state along with its fencing token will be returned to the caller.
>     

Parameters:

*   **state** ([_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")
    ) – The encoded rendezvous state.
    
*   **token** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
     _|_ _None_) – An optional fencing token that was retrieved by a previous call to [`get_state()`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend.get_state "torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousBackend.get_state")
     or `set_state()`.
    

Returns:

A tuple of the serialized rendezvous state, its fencing token, and a boolean value indicating whether our set attempt succeeded.

Raises:

*   [**RendezvousConnectionError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousConnectionError "torch.distributed.elastic.rendezvous.api.RendezvousConnectionError")
     – The connection to the backend has failed.
    
*   [**RendezvousStateError**](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.api.RendezvousStateError "torch.distributed.elastic.rendezvous.api.RendezvousStateError")
     – The rendezvous state is corrupt.
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\] | None

_class_ torch.distributed.elastic.rendezvous.dynamic\_rendezvous.RendezvousTimeout(_join\=None_, _last\_call\=None_, _close\=None_, _heartbeat\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py#L124)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout "Link to this definition")

Hold the timeout configuration of a rendezvous.

Parameters:

*   **join** ([_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
     _|_ _None_) – The time within which the rendezvous is expected to complete.
    
*   **last\_call** ([_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
     _|_ _None_) – An additional wait amount before completing the rendezvous once the rendezvous has the minimum number of required participants.
    
*   **close** ([_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
     _|_ _None_) – The time within which the rendezvous is expected to close after a call to `RendezvousHandler.set_closed()` or `RendezvousHandler.shutdown()`.
    
*   **heartbeat** ([_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
     _|_ _None_) – The time within which a keep-alive heartbeat is expected to complete.
    

_property_ close_: [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout.close "Link to this definition")

Get the close timeout.

_property_ heartbeat_: [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout.heartbeat "Link to this definition")

Get the keep-alive heartbeat timeout.

_property_ join_: [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout.join "Link to this definition")

Get the join timeout.

_property_ last\_call_: [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.dynamic_rendezvous.RendezvousTimeout.last_call "Link to this definition")

Get the last call timeout.

#### C10d Backend[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#c10d-backend "Link to this heading")

torch.distributed.elastic.rendezvous.c10d\_rendezvous\_backend.create\_backend(_params_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/c10d_rendezvous_backend.py#L213)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.create_backend "Link to this definition")

Create a new [`C10dRendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend "torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend")
 from the specified parameters.

| Parameter | Description |
| --- | --- |
| store\_type | The type of the C10d store. The currently supported types are “tcp” and “file” which correspond to [`torch.distributed.TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")<br> and [`torch.distributed.FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")<br>, respectively. Defaults to “tcp”. |
| read\_timeout | The read timeout, in seconds, for store operations. Defaults to 60 seconds.<br><br>Note this only applies to [`torch.distributed.TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")<br>. It is not relevant to [`torch.distributed.FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")<br> which does not take in timeout as a parameter. |
| is\_host | A boolean value indicating whether this backend instance will host the C10d store. If not specified it will be inferred heuristically by matching the hostname or the IP address of this machine against the specified rendezvous endpoint. Defaults to `None`.<br><br>Note that this configuration option only applies to [`torch.distributed.TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")<br>. In normal circumstances you can safely skip it; the only time when it is needed is if its value cannot be correctly determined (e.g. the rendezvous endpoint has a CNAME as the hostname or does not match the FQDN of the machine). |

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_C10dRendezvousBackend_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend "torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend")\
, [_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")\
\]

_class_ torch.distributed.elastic.rendezvous.c10d\_rendezvous\_backend.C10dRendezvousBackend(_store_, _run\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/c10d_rendezvous_backend.py#L35)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend "Link to this definition")

Represents a C10d-backed rendezvous backend.

Parameters:

*   **store** ([_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")
    ) – The [`torch.distributed.Store`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.Store")
     instance to use to communicate with the C10d store.
    
*   **run\_id** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The run id of the rendezvous.
    

get\_state()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/c10d_rendezvous_backend.py#L73)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend.get_state "Link to this definition")

See base class.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | None

_property_ name_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend.name "Link to this definition")

See base class.

set\_state(_state_, _token\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/c10d_rendezvous_backend.py#L79)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.c10d_rendezvous_backend.C10dRendezvousBackend.set_state "Link to this definition")

See base class.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\] | None

#### Etcd Backend[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#etcd-backend "Link to this heading")

torch.distributed.elastic.rendezvous.etcd\_rendezvous\_backend.create\_backend(_params_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py#L184)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.create_backend "Link to this definition")

Create a new [`EtcdRendezvousBackend`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend "torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend")
 from the specified parameters.

| Parameter | Description |
| --- | --- |
| read\_timeout | The read timeout, in seconds, for etcd operations. Defaults to 60 seconds. |
| protocol | The protocol to use to communicate with etcd. Valid values are “http” and “https”. Defaults to “http”. |
| ssl\_cert | The path to the SSL client certificate to use along with HTTPS. Defaults to `None`. |
| ssl\_cert\_key | The path to the private key of the SSL client certificate to use along with HTTPS. Defaults to `None`. |
| ca\_cert | The path to the root SSL authority certificate. Defaults to `None`. |

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_EtcdRendezvousBackend_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend "torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend")\
, [_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.distributed_c10d.Store")\
\]

_class_ torch.distributed.elastic.rendezvous.etcd\_rendezvous\_backend.EtcdRendezvousBackend(_client_, _run\_id_, _key\_prefix\=None_, _ttl\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py#L28)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend "Link to this definition")

Represents an etcd-based rendezvous backend.

Parameters:

*   **client** (_Client_) – The `etcd.Client` instance to use to communicate with etcd.
    
*   **run\_id** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The run id of the rendezvous.
    
*   **key\_prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – The path under which to store the rendezvous state in etcd.
    
*   **ttl** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – The TTL of the rendezvous state. If not specified, defaults to two hours.
    

get\_state()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py#L75)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend.get_state "Link to this definition")

See base class.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | None

_property_ name_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend.name "Link to this definition")

See base class.

set\_state(_state_, _token\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py#L88)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend.set_state "Link to this definition")

See base class.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\] | None

### Etcd Rendezvous (Legacy)[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#etcd-rendezvous-legacy "Link to this heading")

Warning

The `DynamicRendezvousHandler` class supersedes the `EtcdRendezvousHandler` class, and is recommended for most users. `EtcdRendezvousHandler` is in maintenance mode and will be deprecated in the future.

_class_ torch.distributed.elastic.rendezvous.etcd\_rendezvous.EtcdRendezvousHandler(_rdzv\_impl_, _local\_addr_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_rendezvous.py#L91)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvousHandler "Link to this definition")

Implements a [`torch.distributed.elastic.rendezvous.RendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.RendezvousHandler")
 interface backed by `torch.distributed.elastic.rendezvous.etcd_rendezvous.EtcdRendezvous`. `EtcdRendezvousHandler` uses a URL to configure the type of rendezvous to use and to pass implementation specific configurations to the rendezvous module. The basic etcd rendezvous configuration URL looks like the following

etcd://<etcd\_address>:<port>/<job\_id>?min\_workers=<min\_workers>&max\_workers=<max\_workers>  # noqa: W605

-- example --

etcd://localhost:2379/1234?min\_workers=1&max\_workers=3

Copy to clipboard

The URL above is interpreted as follows:

1.  Use the rendezvous handler that is registered with the `etcd` scheme
    
2.  The `etcd` endpoint to use is `localhost:2379`
    
3.  `job_id == 1234` is used as the prefix in etcd (this allows one to share a common etcd server for multiple jobs so long as the `job_ids` are guaranteed to be unique). Note that the job id can be any string (e.g. does not need to be a number) as long as it is unique.
    
4.  `min_workers=1` and `max_workers=3` specifies a range for membership size - Torch Distributed Elastic starts running the job as long as the cluster size is greater than or equal to `min_workers` and admits up to `max_workers` into the cluster.
    

Below are a full list of the parameters that can be passed to etcd rendezvous:

| Parameter | Description |
| --- | --- |
| min\_workers | minimum number of workers for the rendezvous to be valid |
| max\_workers | maximum number of workers to admit |
| timeout | total timeout within which next\_rendezvous is expected to succeed (default 600s) |
| last\_call\_timeout | additional wait amount (“last call”) after min number of workers has been reached (defaults to 30s) |
| etcd\_prefix | path prefix (from etcd root), inside which all etcd nodes will be created (defaults to `/torchelastic/p2p`) |

### Etcd Store[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#etcd-store "Link to this heading")

The `EtcdStore` is the C10d `Store` instance type returned by `next_rendezvous()` when etcd is used as the rendezvous backend.

_class_ torch.distributed.elastic.rendezvous.etcd\_store.EtcdStore(_etcd\_client_, _etcd\_store\_prefix_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L30)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore "Link to this definition")

Implement a c10 Store interface by piggybacking on the rendezvous etcd instance.

This is the store object returned by `EtcdRendezvous`.

add(_key_, _num_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L85)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore.add "Link to this definition")

Atomically increment a value by an integer amount.

The integer is represented as a string using base 10. If key is not present, a default value of `0` will be assumed.

Returns:

the new (incremented) value

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

check(_keys_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L137)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore.check "Link to this definition")

Check if all of the keys are immediately present (without waiting).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

get(_key_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L63)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore.get "Link to this definition")

Get a value by key, possibly doing a blocking wait.

If key is not immediately present, will do a blocking wait for at most `timeout` duration or until the key is published.

Returns:

value `(bytes)`

Raises:

**LookupError - If key still not published after timeout** –

Return type:

[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")

set(_key_, _value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L55)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore.set "Link to this definition")

Write a key/value pair into `EtcdStore`.

Both key and value may be either Python `str` or `bytes`.

wait(_keys_, _override\_timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_store.py#L124)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_store.EtcdStore.wait "Link to this definition")

Wait until all of the keys are published, or until timeout.

Raises:

**LookupError - if timeout occurs** –

### Etcd Server[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#etcd-server "Link to this heading")

The `EtcdServer` is a convenience class that makes it easy for you to start and stop an etcd server on a subprocess. This is useful for testing or single-node (multi-worker) deployments where manually setting up an etcd server on the side is cumbersome.

Warning

For production and multi-node deployments please consider properly deploying a highly available etcd server as this is the single point of failure for your distributed jobs.

_class_ torch.distributed.elastic.rendezvous.etcd\_server.EtcdServer(_data\_dir\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/rendezvous/etcd_server.py#L80)
[#](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.etcd_server.EtcdServer "Link to this definition")

Note

tested on etcd server v3.4.3.

Starts and stops a local standalone etcd server on a random free port. Useful for single node, multi-worker launches or testing, where a sidecar etcd server is more convenient than having to separately setup an etcd server.

This class registers a termination handler to shutdown the etcd subprocess on exit. This termination handler is NOT a substitute for calling the `stop()` method.

The following fallback mechanism is used to find the etcd binary:

1.  Uses env var TORCHELASTIC\_ETCD\_BINARY\_PATH
    
2.  Uses `<this file root>/bin/etcd` if one exists
    
3.  Uses `etcd` from `PATH`
    

Usage

server \= EtcdServer()
server.start()
client \= server.get\_client()
\# use client
server.stop()

Copy to clipboard

Parameters:

**data\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _|_ _None_) – directory for the etcd server data. If not provided, a temporary directory is created with `tempfile.mkdtemp()` and deleted when the server stops (or on process exit).

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/rendezvous.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/rendezvous.md.txt)

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