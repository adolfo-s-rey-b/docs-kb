Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/monitor.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/monitor.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/monitor.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/monitor.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/monitor.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/monitor.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/monitor.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/monitor.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/monitor.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/monitor.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/monitor.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/monitor.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/monitor.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/monitor.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/monitor.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/monitor.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/monitor.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/monitor.html)
[v1.13](https://docs.pytorch.org/docs/1.13/monitor.html)
[v1.12](https://docs.pytorch.org/docs/1.12/monitor.html)
[v1.11](https://docs.pytorch.org/docs/1.11/monitor.html)
[v1.10](https://docs.pytorch.org/docs/1.10/monitor.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/monitor.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/monitor.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/monitor.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/monitor.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/monitor.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/monitor.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/monitor.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/monitor.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/monitor.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/monitor.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/monitor.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/monitor.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/monitor.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/monitor.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/monitor.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/monitor.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/monitor.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/monitor.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/monitor.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/monitor.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/monitor.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/monitor.html)

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

torch.monitor[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch-monitor "Link to this heading")

=======================================================================================================

Created On: Jan 12, 2022 | Last Updated On: Jun 11, 2025

Warning

This module is a prototype release, and its interfaces and functionality may change without warning in future PyTorch releases.

`torch.monitor` provides an interface for logging events and counters from PyTorch.

The stat interfaces are designed to be used for tracking high level metrics that are periodically logged out to be used for monitoring system performance. Since the stats aggregate with a specific window size you can log to them from critical loops with minimal performance impact.

For more infrequent events or values such as loss, accuracy, usage tracking the event interface can be directly used.

Event handlers can be registered to handle the events and pass them to an external event sink.

API Reference[#](https://docs.pytorch.org/docs/2.15/monitor.html#module-torch.monitor "Link to this heading")

--------------------------------------------------------------------------------------------------------------

_class_ torch.monitor.Aggregation[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Aggregation "Link to this definition")

> These are types of aggregations that can be used to accumulate stats.

Members:

> VALUE :
> 
> VALUE returns the last value to be added.
> 
> MEAN :
> 
> MEAN computes the arithmetic mean of all the added values.
> 
> COUNT :
> 
> COUNT returns the total number of added values.
> 
> SUM :
> 
> SUM returns the sum of the added values.
> 
> MAX :
> 
> MAX returns the max of the added values.
> 
> MIN :
> 
> MIN returns the min of the added values.

_property_ name[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Aggregation.name "Link to this definition")

_class_ torch.monitor.Stat[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat "Link to this definition")

Stat is used to compute summary statistics in a performant way over fixed intervals. Stat logs the statistics as an Event once every `window_size` duration. When the window closes the stats are logged via the event handlers as a `torch.monitor.Stat` event.

`window_size` should be set to something relatively high to avoid a huge number of events being logged. Ex: 60s. Stat uses millisecond precision.

If `max_samples` is set, the stat will cap the number of samples per window by discarding add calls once `max_samples` adds have occurred. If it’s not set, all `add` calls during the window will be included. This is an optional field to make aggregations more directly comparable across windows when the number of samples might vary.

When the Stat is destructed it will log any remaining data even if the window hasn’t elapsed.

\_\_init\_\_(_self: [torch.\_C.\_monitor.Stat](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat "torch._C._monitor.Stat")
_, _name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _aggregations: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
\[[torch.\_C.\_monitor.Aggregation](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Aggregation "torch._C._monitor.Aggregation")\
\]_, _window\_size: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
_, _max\_samples: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= 9223372036854775807_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat.__init__ "Link to this definition")

Constructs the `Stat`.

add(_self: [torch.\_C.\_monitor.Stat](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat "torch._C._monitor.Stat")
_, _v: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat.add "Link to this definition")

Adds a value to the stat to be aggregated according to the configured stat type and aggregations.

_property_ count[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat.count "Link to this definition")

Number of data points that have currently been collected. Resets once the event has been logged.

get(_self: [torch.\_C.\_monitor.Stat](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat "torch._C._monitor.Stat")
_) → [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[torch.\_C.\_monitor.Aggregation](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Aggregation "torch._C._monitor.Aggregation")\
, [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
\][#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat.get "Link to this definition")

Returns the current value of the stat, primarily for testing purposes. If the stat has logged and no additional values have been added this will be zero.

_property_ name[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Stat.name "Link to this definition")

The name of the stat that was set during creation.

_class_ torch.monitor.data\_value\_t[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.data_value_t "Link to this definition")

data\_value\_t is one of `str`, `float`, `int`, `bool`.

_class_ torch.monitor.Event[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event "Link to this definition")

Event represents a specific typed event to be logged. This can represent high-level data points such as loss or accuracy per epoch or more low-level aggregations such as through the Stats provided through this library.

All Events of the same type should have the same name so downstream handlers can correctly process them.

\_\_init\_\_(_self: [torch.\_C.\_monitor.Event](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event "torch._C._monitor.Event")
_, _name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _timestamp: [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
_, _data: [collections.abc.Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [data\_value\_t](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.data_value_t "torch.monitor.data_value_t")\
\]_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event.__init__ "Link to this definition")

Constructs the `Event`.

_property_ data[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event.data "Link to this definition")

The structured data contained within the `Event`.

_property_ name[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event.name "Link to this definition")

The name of the `Event`.

_property_ timestamp[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event.timestamp "Link to this definition")

The timestamp when the `Event` happened.

_class_ torch.monitor.EventHandlerHandle[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.EventHandlerHandle "Link to this definition")

EventHandlerHandle is a wrapper type returned by `register_event_handler` used to unregister the handler via `unregister_event_handler`. This cannot be directly initialized.

torch.monitor.log\_event(_event: [torch.\_C.\_monitor.Event](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event "torch._C._monitor.Event")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.log_event "Link to this definition")

log\_event logs the specified event to all of the registered event handlers. It’s up to the event handlers to log the event out to the corresponding event sink.

If there are no event handlers registered this method is a no-op.

torch.monitor.register\_event\_handler(_callback: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[torch.\_C.\_monitor.Event](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.Event "torch._C._monitor.Event")\
\], [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\]_) → [torch.\_C.\_monitor.EventHandlerHandle](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.EventHandlerHandle "torch._C._monitor.EventHandlerHandle")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.register_event_handler "Link to this definition")

register\_event\_handler registers a callback to be called whenever an event is logged via `log_event`. These handlers should avoid blocking the main thread since that may interfere with training as they run during the `log_event` call.

torch.monitor.unregister\_event\_handler(_handler: [torch.\_C.\_monitor.EventHandlerHandle](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.EventHandlerHandle "torch._C._monitor.EventHandlerHandle")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.unregister_event_handler "Link to this definition")

unregister\_event\_handler unregisters the `EventHandlerHandle` returned after calling `register_event_handler`. After this returns the event handler will no longer receive events.

_class_ torch.monitor.TensorboardEventHandler(_writer_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/monitor/__init__.py#L13)
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.TensorboardEventHandler "Link to this definition")

TensorboardEventHandler is an event handler that will write known events to the provided SummaryWriter.

This currently only supports `torch.monitor.Stat` events which are logged as scalars.

Example

\>>> from torch.utils.tensorboard import SummaryWriter
\>>> from torch.monitor import TensorboardEventHandler, register\_event\_handler
\>>> writer \= SummaryWriter("log\_dir")
\>>> register\_event\_handler(TensorboardEventHandler(writer))

Copy to clipboard

\_\_init\_\_(_writer_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/monitor/__init__.py#L30)
[#](https://docs.pytorch.org/docs/2.15/monitor.html#torch.monitor.TensorboardEventHandler.__init__ "Link to this definition")

Constructs the `TensorboardEventHandler`.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/monitor.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/monitor.md.txt)

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