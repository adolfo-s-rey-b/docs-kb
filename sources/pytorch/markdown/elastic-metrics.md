Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/metrics.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/metrics.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/metrics.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/metrics.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/metrics.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/metrics.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/metrics.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/metrics.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/metrics.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/metrics.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/metrics.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/metrics.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/metrics.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/metrics.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/metrics.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/metrics.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/metrics.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/metrics.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/metrics.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/metrics.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/metrics.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/metrics.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/metrics.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/metrics.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/metrics.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/metrics.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/metrics.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/metrics.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/metrics.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/metrics.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/metrics.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/metrics.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/metrics.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/metrics.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/metrics.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/metrics.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/metrics.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/metrics.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/metrics.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/metrics.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/metrics.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/metrics.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/metrics.html)

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

Metrics[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#module-torch.distributed.elastic.metrics "Link to this heading")

====================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 07, 2026

Metrics API.

**Overview**:

The metrics API in torchelastic is used to publish telemetry metrics. It is designed to be used by torchelastic’s internal modules to publish metrics for the end user with the goal of increasing visibility and helping with debugging. However you may use the same API in your jobs to publish metrics to the same metrics `sink`.

A `metric` can be thought of as timeseries data and is uniquely identified by the string-valued tuple `(metric_group, metric_name)`.

torchelastic makes no assumptions about what a `metric_group` is and what relationship it has with `metric_name`. It is totally up to the user to use these two fields to uniquely identify a metric.

Note

The metric group `torchelastic` is reserved by torchelastic for platform level metrics that it produces. For instance torchelastic may output the latency (in milliseconds) of a re-rendezvous operation from the agent as `(torchelastic, agent.rendezvous.duration.ms)`

A sensible way to use metric groups is to map them to a stage or module in your job. You may also encode certain high level properties the job such as the region or stage (dev vs prod).

**Publish Metrics**:

Using torchelastic’s metrics API is similar to using python’s logging framework. You first have to configure a metrics handler before trying to add metric data.

The example below measures the latency for the `calculate()` function.

import time
import torch.distributed.elastic.metrics as metrics

\# makes all metrics other than the one from "my\_module" to go /dev/null
metrics.configure(metrics.NullMetricsHandler())
metrics.configure(metrics.ConsoleMetricsHandler(), "my\_module")

def my\_method():
    start \= time.time()
    calculate()
    end \= time.time()
    metrics.put\_metric("calculate\_latency", int(end \- start), "my\_module")

Copy to clipboard

You may also use the torch.distributed.elastic.metrics.prof\` decorator to conveniently and succinctly profile functions

\# -- in module examples.foobar --

import torch.distributed.elastic.metrics as metrics

metrics.configure(metrics.ConsoleMetricsHandler(), "foobar")
metrics.configure(metrics.ConsoleMetricsHandler(), "Bar")

@metrics.prof
def foo():
    pass

class Bar:
    @metrics.prof
    def baz():
        pass

Copy to clipboard

`@metrics.prof` will publish the following metrics

<leaf\_module or classname\>.success \- 1 if the function finished successfully
<leaf\_module or classname\>.failure \- 1 if the function threw an exception
<leaf\_module or classname\>.duration.ms \- function duration in milliseconds

Copy to clipboard

**Configuring Metrics Handler**:

torch.distributed.elastic.metrics.MetricHandler is responsible for emitting the added metric values to a particular destination. Metric groups can be configured with different metric handlers.

By default torchelastic emits all metrics to `/dev/null`. By adding the following configuration metrics, `torchelastic` and `my_app` metric groups will be printed out to console.

import torch.distributed.elastic.metrics as metrics

metrics.configure(metrics.ConsoleMetricHandler(), group\="torchelastic")
metrics.configure(metrics.ConsoleMetricHandler(), group\="my\_app")

Copy to clipboard

**Writing a Custom Metric Handler**:

If you want your metrics to be emitted to a custom location, implement the torch.distributed.elastic.metrics.MetricHandler interface and configure your job to use your custom metric handler.

Below is a toy example that prints the metrics to `stdout`

import torch.distributed.elastic.metrics as metrics

class StdoutMetricHandler(metrics.MetricHandler):
    def emit(self, metric\_data):
        ts \= metric\_data.timestamp
        group \= metric\_data.group\_name
        name \= metric\_data.name
        value \= metric\_data.value
        print(f"\[{ts}\]\[{group}\]: {name}\={value}")

metrics.configure(StdoutMetricHandler(), group\="my\_app")

Copy to clipboard

Now all metrics in the group `my_app` will be printed to stdout as:

\[1574213883.4182858\]\[my\_app\]: my\_metric\=<value\>
\[1574213940.5237644\]\[my\_app\]: my\_metric\=<value\>

Copy to clipboard

Metric Handlers[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#metric-handlers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

Below are the metric handlers that come included with torchelastic.

_class_ torch.distributed.elastic.metrics.api.MetricHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L45)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.api.MetricHandler "Link to this definition")

_class_ torch.distributed.elastic.metrics.api.ConsoleMetricHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L51)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.api.ConsoleMetricHandler "Link to this definition")

_class_ torch.distributed.elastic.metrics.api.NullMetricHandler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L58)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.api.NullMetricHandler "Link to this definition")

Methods[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#methods "Link to this heading")

---------------------------------------------------------------------------------------------------

torch.distributed.elastic.metrics.configure(_handler_, _group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L79)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.configure "Link to this definition")

torch.distributed.elastic.metrics.prof(_fn\=None_, _group\='torchelastic'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L107)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.prof "Link to this definition")

@profile decorator publishes duration.ms, count, success, failure metrics for the function that it decorates.

The metric name defaults to the qualified name (`class_name.def_name`) of the function. If the function does not belong to a class, it uses the leaf module name instead.

Usage

@metrics.prof
def x():
    pass

@metrics.prof(group\="agent")
def y():
    pass

Copy to clipboard

torch.distributed.elastic.metrics.put\_metric(_metric\_name_, _metric\_value_, _metric\_group\='torchelastic'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/metrics/api.py#L190)
[#](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#torch.distributed.elastic.metrics.put_metric "Link to this definition")

Publish a metric data point.

Usage

put\_metric("metric\_name", 1)
put\_metric("metric\_name", 1, "metric\_group\_name")

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/metrics.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/metrics.md.txt)

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