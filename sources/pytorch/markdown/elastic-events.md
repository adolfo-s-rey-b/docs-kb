Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/events.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/events.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/events.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/events.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/events.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/events.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/events.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/events.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/events.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/events.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/events.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/events.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/events.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/events.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/events.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/events.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/events.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/events.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/events.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/events.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/events.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/events.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/events.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/events.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/events.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/events.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/events.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/events.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/events.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/events.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/events.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/events.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/events.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/events.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/events.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/events.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/events.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/events.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/events.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/events.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/events.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/events.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/events.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/events.html)

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

Events[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#module-torch.distributed.elastic.events "Link to this heading")

=================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 11, 2026

Module contains events processing mechanisms that are integrated with the standard python logging.

Example of usage:

from torch.distributed.elastic import events

event \= events.Event(
    name\="test\_event", source\=events.EventSource.WORKER, metadata\={...}
)
events.get\_logging\_handler(destination\="console").info(event)

Copy to clipboard

API Methods[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#api-methods "Link to this heading")

----------------------------------------------------------------------------------------------------------

torch.distributed.elastic.events.record(_event_, _destination\='null'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/__init__.py#L69)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.record "Link to this definition")

torch.distributed.elastic.events.construct\_and\_record\_rdzv\_event(_run\_id_, _message_, _node\_state_, _name\=''_, _hostname\=''_, _pid\=None_, _master\_endpoint\=''_, _local\_id\=None_, _rank\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/__init__.py#L77)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.construct_and_record_rdzv_event "Link to this definition")

Initialize rendezvous event object and record its operations.

Parameters:

*   **run\_id** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The run id of the rendezvous.
    
*   **message** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The message describing the event.
    
*   **node\_state** ([_NodeState_](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.NodeState "torch.distributed.elastic.events.api.NodeState")
    ) – The state of the node (INIT, RUNNING, SUCCEEDED, FAILED).
    
*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Event name. (E.g. Current action being performed).
    
*   **hostname** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Hostname of the node.
    
*   **pid** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The process id of the node.
    
*   **master\_endpoint** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The master endpoint for the rendezvous store, if known.
    
*   **local\_id** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The local\_id of the node, if defined in dynamic\_rendezvous.py
    
*   **rank** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The rank of the node, if known.
    

Returns:

None

Return type:

None

Example

\>>> \# See DynamicRendezvousHandler class
\>>> def \_record(
...     self,
...     message: str,
...     node\_state: NodeState \= NodeState.RUNNING,
...     rank: Optional\[int\] \= None,
... ) \-> None:
...     construct\_and\_record\_rdzv\_event(
...         name\=f"{self.\_\_class\_\_.\_\_name\_\_}.{get\_method\_name()}",
...         run\_id\=self.\_settings.run\_id,
...         message\=message,
...         node\_state\=node\_state,
...         hostname\=self.\_this\_node.addr,
...         pid\=self.\_this\_node.pid,
...         local\_id\=self.\_this\_node.local\_id,
...         rank\=rank,
...     )

Copy to clipboard

torch.distributed.elastic.events.get\_logging\_handler(_destination\='null'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/handlers.py#L19)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.get_logging_handler "Link to this definition")

Return type:

[_Handler_](https://docs.python.org/3/library/logging.html#logging.Handler "(in Python v3.15)")

torch.distributed.elastic.events.record\_rdzv\_event(_event_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/__init__.py#L73)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.record_rdzv_event "Link to this definition")

Event Objects[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#event-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.events.api.Event(_name_, _source_, _timestamp=0_, _metadata=<factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/api.py#L28)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.Event "Link to this definition")

The class represents the generic event that occurs during the torchelastic job execution.

The event can be any kind of meaningful action.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – event name.
    
*   **source** ([_EventSource_](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.EventSource "torch.distributed.elastic.events.api.EventSource")
    ) – the event producer, e.g. agent or worker
    
*   **timestamp** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – timestamp in milliseconds when event occurred.
    
*   **metadata** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
     _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _|_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
     _|_ _None__\]_) – additional data that is associated with the event.
    

_class_ torch.distributed.elastic.events.api.EventSource(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/api.py#L21)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.EventSource "Link to this definition")

Known identifiers of the event producers.

torch.distributed.elastic.events.api.EventMetadataValue[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.EventMetadataValue "Link to this definition")

alias of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | [`float`](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [`None`](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")

_class_ torch.distributed.elastic.events.api.NodeState(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/events/api.py#L64)
[#](https://docs.pytorch.org/docs/2.15/elastic/events.html#torch.distributed.elastic.events.api.NodeState "Link to this definition")

The states that a node can be in rendezvous.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/events.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/events.md.txt)

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