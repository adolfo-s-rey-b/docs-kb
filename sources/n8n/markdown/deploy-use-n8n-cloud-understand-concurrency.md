For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency.md)
.

**Only for n8n Cloud**

This document discusses concurrency in n8n Cloud. Read [self-hosted n8n concurrency control](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)
 to learn how concurrency works with self-hosted n8n instances.

Too many concurrent executions can cause performance degradation and unresponsiveness. To prevent this and improve instance stability, n8n sets concurrency limits for production executions in regular mode.

Any executions beyond the limits queue for later processing. These executions remain in the queue until concurrency capacity frees up, and are then processed in FIFO order.

Concurrency limits[](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency#concurrency-limits)

---------------------------------------------------------------------------------------------------------

n8n limits the number of concurrent executions for Cloud instances according to their plan. Refer to [Pricing](https://n8n.io/pricing/)
 for details.

You can view the number of active executions and your plan's concurrency limit at the top of a project's or workflow's executions tab.

Details[](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency#details)

-----------------------------------------------------------------------------------

Some other details about concurrency to keep in mind:

*   Concurrency control applies only to production executions: those started from a webhook or trigger node. It doesn't apply to any other kinds, such as manual executions, sub-workflow executions, or error executions.
    
*   Test evaluations don't count towards production concurrency limits. They use a separate per-plan limit for how many test cases can run in parallel within a single test run: self-hosted Community and n8n Cloud Pro run 1 (sequential), self-hosted Business runs 3, and Enterprise (both n8n Cloud and self-hosted) runs 5. You can adjust the value for a given run from the **Run Test** popover. Refer to [Metric-based evaluations](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality#run-test-cases-in-parallel)
     for details.
    
*   You can't retry queued executions. Cancelling or deleting a queued execution also removes it from the queue.
    
*   On instance startup, n8n resumes queued executions up to the concurrency limit and re-enqueues the rest.
    

Comparison to queue mode[](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency#comparison-to-queue-mode)

---------------------------------------------------------------------------------------------------------------------

**Feature availability**

Queue mode is available for n8n Cloud Enterprise plans. To enable it, [contact n8n](https://n8n-community.typeform.com/to/y9X2YuGa)
.

Concurrency in queue mode is a separate mechanism from concurrency in regular mode. In queue mode, the concurrency settings determine how many jobs each worker can run in parallel. In regular mode, concurrency limits apply to the entire instance.

Related resources[](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency#related-resources)

-------------------------------------------------------------------------------------------------------

*   [Use n8n Cloud](https://docs.n8n.io/deploy/use-n8n-cloud)
    
*   [Try free then choose a plan](https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial)
    
*   [Use the Cloud console](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console)
    
*   [Update your version](https://docs.n8n.io/deploy/use-n8n-cloud/update-your-version)
    
*   [Configure Cloud](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud)
    
*   [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
    
*   [Assistant credits](https://docs.n8n.io/deploy/use-n8n-cloud/assistant-credits)
    
*   [Download workflows](https://docs.n8n.io/deploy/use-n8n-cloud/download-workflows)
    

[PreviousChange instance ownership or username](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username)
[NextGateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)

Last updated 10 days ago

Was this helpful?