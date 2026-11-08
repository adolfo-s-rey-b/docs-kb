For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling.md)
.

When running n8n at scale, with a large number of users, workflows, or executions, you need to change your n8n configuration to ensure good performance.

n8n can run in different [modes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
 depending on your needs. The `queue` mode provides the best scalability. Refer to [Queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
 for configuration details.

You can configure data saving and pruning to improve database performance. Refer to [Execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
 for details.

In this section[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling#in-this-section)

---------------------------------------------------------------------------------------------

*   [Measure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)
    : benchmark n8n's performance and resource consumption.
    
*   [Enable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    : run n8n across multiple worker processes for the best scalability.
    
*   [Control concurrency](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)
    : limit how many executions run at once.
    
*   [Manage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
    : configure data saving and pruning to improve database performance.
    
*   [Handle binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data)
    : handle large files without degrading n8n's performance.
    
*   [Use external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    : store binary data and execution data externally.
    
*   [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues)
    : identify and avoid memory-related errors.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling#related-resources)

-------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousRedact execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data)
[NextMeasure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)

Last updated 10 days ago

Was this helpful?