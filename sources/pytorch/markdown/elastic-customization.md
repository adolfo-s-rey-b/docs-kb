Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/customization.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/customization.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/customization.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/customization.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/customization.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/customization.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/customization.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/customization.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/customization.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/customization.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/customization.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/customization.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/customization.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/customization.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/customization.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/customization.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/customization.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/customization.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/customization.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/customization.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/customization.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/customization.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/customization.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/customization.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/customization.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/customization.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/customization.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/customization.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/customization.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/customization.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/customization.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/customization.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/customization.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/customization.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/customization.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/customization.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/customization.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/customization.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/customization.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/customization.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/customization.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/customization.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/customization.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/customization.html)

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

Customization[#](https://docs.pytorch.org/docs/2.15/elastic/customization.html#customization "Link to this heading")

=====================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 07, 2026

This section describes how to customize TorchElastic to fit your needs.

Launcher[#](https://docs.pytorch.org/docs/2.15/elastic/customization.html#launcher "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The launcher program that ships with TorchElastic should be sufficient for most use-cases (see [torchrun (Elastic Launch)](https://docs.pytorch.org/docs/2.15/elastic/run.html#launcher-api)
). You can implement a custom launcher by programmatically creating an agent and passing it specs for your workers as shown below.

\# my\_launcher.py

if \_\_name\_\_ \== "\_\_main\_\_":
    args \= parse\_args(sys.argv\[1:\])
    rdzv\_handler \= RendezvousHandler(...)
    spec \= WorkerSpec(
        local\_world\_size\=args.nproc\_per\_node,
        fn\=trainer\_entrypoint\_fn,
        args\=(trainer\_entrypoint\_fn args.fn\_args,...),
        rdzv\_handler\=rdzv\_handler,
        max\_restarts\=args.max\_restarts,
        monitor\_interval\=args.monitor\_interval,
    )

    agent \= LocalElasticAgent(spec, start\_method\="spawn")
    try:
        run\_result \= agent.run()
        if run\_result.is\_failed():
            print(f"worker 0 failed with: run\_result.failures\[0\]")
        else:
            print(f"worker 0 return value is: run\_result.return\_values\[0\]")
    except Exception ex:
        \# handle exception

Copy to clipboard

Rendezvous Handler[#](https://docs.pytorch.org/docs/2.15/elastic/customization.html#rendezvous-handler "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

To implement your own rendezvous, extend `torch.distributed.elastic.rendezvous.RendezvousHandler` and implement its methods.

Warning

Rendezvous handlers are tricky to implement. Before you begin make sure you completely understand the properties of rendezvous. Please refer to [Rendezvous](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#rendezvous-api)
 for more information.

Once implemented you can pass your custom rendezvous handler to the worker spec when creating the agent.

spec \= WorkerSpec(
    rdzv\_handler\=MyRendezvousHandler(params),
    ...
)
elastic\_agent \= LocalElasticAgent(spec, start\_method\=start\_method)
elastic\_agent.run(spec.role)

Copy to clipboard

Metric Handler[#](https://docs.pytorch.org/docs/2.15/elastic/customization.html#metric-handler "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

TorchElastic emits platform level metrics (see [Metrics](https://docs.pytorch.org/docs/2.15/elastic/metrics.html#metrics-api)
). By default metrics are emitted to `/dev/null` so you will not see them. To have the metrics pushed to a metric handling service in your infrastructure, implement a `torch.distributed.elastic.metrics.MetricHandler` and `configure` it in your custom launcher.

\# my\_launcher.py

import torch.distributed.elastic.metrics as metrics

class MyMetricHandler(metrics.MetricHandler):
    def emit(self, metric\_data: metrics.MetricData):
        \# push metric\_data to your metric sink

def main():
    metrics.configure(MyMetricHandler())

    spec \= WorkerSpec(...)
    agent \= LocalElasticAgent(spec)
    agent.run()

Copy to clipboard

Events Handler[#](https://docs.pytorch.org/docs/2.15/elastic/customization.html#events-handler "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

TorchElastic supports events recording (see [Events](https://docs.pytorch.org/docs/2.15/elastic/events.html#events-api)
). The events module defines API that allows you to record events and implement custom EventHandler. EventHandler is used for publishing events produced during torchelastic execution to different sources, e.g. AWS CloudWatch. By default it uses `torch.distributed.elastic.events.NullEventHandler` that ignores events. To configure custom events handler you need to implement `torch.distributed.elastic.events.EventHandler` interface and `configure` it in your custom launcher.

\# my\_launcher.py

import torch.distributed.elastic.events as events

class MyEventHandler(events.EventHandler):
    def record(self, event: events.Event):
        \# process event

def main():
    events.configure(MyEventHandler())

    spec \= WorkerSpec(...)
    agent \= LocalElasticAgent(spec)
    agent.run()

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/customization.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/customization.md.txt)

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