For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data.md)
.

Binary data is any file-type data, such as image files or documents generated or processed during the execution of a workflow.

In queue mode, binary data storage also backs webhook responses too large to send through the queue. Refer to [Large webhook responses](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#large-webhook-responses)
 for details.

Enable filesystem mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data#enable-filesystem-mode)

------------------------------------------------------------------------------------------------------------------------------

When handling binary data, n8n keeps the data in memory by default. This can cause crashes when working with large files.

To avoid this, change the `N8N_DEFAULT_BINARY_DATA_MODE` [environment variable](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data)
 to `filesystem`. This causes n8n to save data to disk, instead of using memory.

If you're using queue mode, switch this to `database`. n8n doesn't support `filesystem` mode with queue mode.

Binary data pruning[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data#binary-data-pruning)

------------------------------------------------------------------------------------------------------------------------

n8n executes binary data pruning as part of execution data pruning. Refer to [Execution data | Enable executions pruning](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data#enable-executions-pruning)
 for details.

If you configure multiple binary data modes, binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. Refer to [External storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage#usage)
 for details.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data#related-resources)

--------------------------------------------------------------------------------------------------------------------

*   [Scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
    
*   [Measure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)
    
*   [Enable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    
*   [Control concurrency](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)
    
*   [Manage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
    
*   [Use external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    
*   [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues)
    

[PreviousManage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
[NextUse external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)

Last updated 10 days ago

Was this helpful?