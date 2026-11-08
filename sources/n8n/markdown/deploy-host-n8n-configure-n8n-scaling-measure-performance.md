For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance.md)
.

n8n can handle up to 220 workflow executions per second on a single instance, with the ability to scale up further by adding more instances.

This document outlines n8n's performance benchmarking. It describes the factors that affect performance, and includes two example benchmarks.

Performance factors[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance#performance-factors)

-------------------------------------------------------------------------------------------------------------------------

The performance of n8n depends on factors including:

*   The workflow type
    
*   The resources available to n8n
    
*   How you configure n8n's scaling options
    

Run your own benchmarking[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance#run-your-own-benchmarking)

-------------------------------------------------------------------------------------------------------------------------------------

To get an accurate estimate for your use case, run n8n's [benchmarking framework](https://github.com/n8n-io/n8n/tree/master/packages/quality/efficiency/scale/benchmark)
. The repository contains more information about the benchmarking.

Example: Single instance performance[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance#example-single-instance-performance)

----------------------------------------------------------------------------------------------------------------------------------------------------------

This test measures how response time increases as requests per second increase. It looks at the response time when calling the Webhook Trigger node.

Setup:

*   Hardware: ECS c5a.large instance (4GB RAM)
    
*   n8n setup: Single n8n instance (running in main mode, with Postgres database)
    
*   Workflow: Webhook Trigger node, Edit Fields node
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-7006d3f0eff56e0b8421eb714bcfda8802e6d057%252Fbenchmarking-single-instance-100-250.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=06514d29003af62ced3a6997a9589ca6&sv=3)

This graph shows the percentage of requests to the Webhook Trigger node getting a response within 100 seconds, and how that varies with load. Under higher loads n8n usually still processes the data, but takes over 100s to respond.

Example: Multi-instance performance[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance#example-multi-instance-performance)

--------------------------------------------------------------------------------------------------------------------------------------------------------

This test measures how response time increases as requests per second increase. It looks at the response time when calling the Webhook Trigger node.

Setup:

*   Hardware: seven ECS c5a.4xlarge instances (8GB RAM each)
    
*   n8n setup: two webhook instances, four worker instances, one database instance (MySQL), one main instance running n8n and Redis
    
*   Workflow: Webhook Trigger node, Edit Fields node
    
*   Multi-instance setups use [Queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-d931a447da356364a78bdc3ead8585ca139d8dc1%252Fbenchmarking-multi-instance-500-2500.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4e24029ee4a7f3ec37b63815d6ef39b0&sv=3)

This graph shows the percentage of requests to the Webhook Trigger node getting a response within 100 seconds, and how that varies with load. Under higher loads n8n usually still processes the data, but takes over 100s to respond.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
    
*   [Enable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    
*   [Control concurrency](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)
    
*   [Manage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
    
*   [Handle binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data)
    
*   [Use external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    
*   [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues)
    

[PreviousScaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
[NextEnable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)

Last updated 10 days ago

Was this helpful?