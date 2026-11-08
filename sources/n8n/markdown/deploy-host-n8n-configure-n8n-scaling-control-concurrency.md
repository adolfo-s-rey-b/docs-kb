For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency.md)
.

**Only for self-hosted n8n**

This document is for self-hosted concurrency control. Read [Cloud concurrency](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency)
 to learn how concurrency works with n8n Cloud accounts.

In regular mode, n8n doesn't limit how many production executions may run at the same time. This can lead to a scenario where too many concurrent executions thrash the event loop, causing performance degradation and unresponsiveness.

To prevent this, you can set a concurrency limit for production executions in regular mode. Use this to control how many production executions run concurrently, and queue up any concurrent production executions over the limit. These executions remain in the queue until concurrency capacity frees up, and are then processed in FIFO order.

Concurrency control is disabled by default. To enable it:

Copy

    export N8N_CONCURRENCY_PRODUCTION_LIMIT=20

Keep in mind:

*   Concurrency control applies only to production executions: those started from a webhook or trigger node. It doesn't apply to any other kinds, such as manual executions, sub-workflow executions, error executions, or started from CLI.
    
*   You can't retry queued executions. Cancelling or deleting a queued execution also removes it from the queue.
    
*   On instance startup, n8n resumes queued executions up to the concurrency limit and re-enqueues the rest.
    
*   To monitor concurrency control, watch logs for executions being added to the queue and released. In a future version, n8n will show concurrency control in the UI.
    

When you enable concurrency control, you can view the number of active executions and the configured limit at the top of a project's or workflow's executions tab.

Comparison to queue mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency#comparison-to-queue-mode)

-----------------------------------------------------------------------------------------------------------------------------------

In queue mode, you can control how many jobs a worker may run concurrently using the [`--concurrency` flag](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configure-worker-concurrency)
.

Concurrency control in queue mode is a separate mechanism from concurrency control in regular mode, but the environment variable `N8N_CONCURRENCY_PRODUCTION_LIMIT` controls both of them. In queue mode, n8n takes the limit from this variable if set to a value other than `-1`, falling back to the `--concurrency` flag or its default.

Evaluation concurrency[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency#evaluation-concurrency)

-------------------------------------------------------------------------------------------------------------------------------

Evaluation test runs use a separate concurrency limit from production executions. By default, the limit follows the instance's license tier (Community/Pro 1, Business 3, Enterprise 5). Override it with [`N8N_CONCURRENCY_EVALUATION_LIMIT`](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions)
. Refer to [Metric-based evaluations](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality#run-test-cases-in-parallel)
 for how the slider behaves in the UI.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
    
*   [Measure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)
    
*   [Enable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    
*   [Manage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
    
*   [Handle binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data)
    
*   [Use external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    
*   [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues)
    

[PreviousEnable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
[NextManage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)

Last updated 10 days ago

Was this helpful?