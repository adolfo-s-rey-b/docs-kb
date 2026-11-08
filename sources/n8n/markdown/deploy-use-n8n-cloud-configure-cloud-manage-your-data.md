For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data.md)
.

There are two concerns when managing data on n8n Cloud:

*   Memory usage: complex workflows processing large amounts of data can exceed n8n's memory limits. If this happens, the instance can crash and become inaccessible.
    
*   Data storage: depending on your execution settings and volume, your n8n database can grow in size and run out of storage.
    

To avoid these issues, n8n recommends that you build your workflows with memory efficiency in mind, and don't save unnecessary data

Memory limits on each n8n Cloud plan[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#memory-limits-on-each-cloud-plan)

---------------------------------------------------------------------------------------------------------------------------------------------------

Current plans:

*   Trial: 640MiB RAM, 10 millicore CPU burstable
    
*   Starter: 640MiB RAM, 10 millicore CPU burstable
    
*   Pro-1 (10k executions): 640MiB RAM, 20 millicore CPU burstable
    
*   Pro-2 (50k executions): 1280MiB RAM, 80 millicore CPU burstable
    
*   Enterprise: 4096MiB RAM, 80 millicore CPU burstable
    

Legacy plans:

*   Start: 320MiB RAM, 10 millicore CPU burstable
    
*   Power: 1280MiB RAM, 80 millicore CPU burstable
    

n8n gives each instance up to 100GB of data storage.

How to reduce memory consumption in your workflow[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#how-to-reduce-memory-consumption-in-your-workflow)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The way you build workflows affects how much data they consume when executed. Although these guidelines aren't applicable to all cases, they provide a baseline of best practices to avoid exceeding instance memory.

*   Split the data processed into smaller chunks. For example, instead of fetching 10,000 rows with each execution, process 200 rows with each execution.
    
*   Avoid using the Code node where possible.
    
*   Avoid manual executions when processing larger amounts of data.
    
*   Split the workflow up into sub-workflows and ensure each sub-workflow returns a limited amount of data to its parent workflow.
    

Splitting the workflow might seem counter-intuitive at first as it usually requires adding at least two more nodes: the [Loop Over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches)
 node to split up the items into smaller batches and the [Execute Workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow)
 node to start the sub-workflow.

However, as long as your sub-workflow does the heavy lifting for each batch and then returns only a small result set to the main workflow, this reduces memory consumption. This is because the sub-workflow only holds the data for the current batch in memory, after which the memory is free again.

Note that n8n itself consumes memory to run. On average, the software alone uses around 180MiB RAM.

Interactions with the UI also consume memory. Playing around with the workflow UI while it performs heavy executions could also push the memory capacity over the limit.

How to manage execution data on n8n Cloud[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#how-to-manage-execution-data-on-cloud)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Execution data includes node data, parameters, variables, execution context, and binary data references. It's text-based.

Binary data is non-textual data that n8n can't represent as plain text. This is files and media such as images, documents, audio files, and videos. It's much larger than textual data.

If a workflow consumes a large amounts of data and is past testing stage, it's a good option to stop saving the successful executions.

There are two ways you can control how much execution data n8n stores in the database:

In the n8n Cloud console:

1.  Open the [Cloud console](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console)
     and select **Instance settings**.
    
2.  In the **Runtime** section, under **Executions to save**, deselect the execution types you don't want to log: **Manual**, **Failed**, or **Successful**.
    
3.  Select **Save and restart** in the bar at the bottom of the page. Your instance restarts to apply the change.
    

In your workflow settings:

1.  Select the **Options** ![Options menu](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=ad562f34e1096f8739235fce7565185f&sv=3) menu.
    
2.  Select **Settings**. n8n opens the **Workflow settings** modal.
    
3.  Change **Save successful production executions** to **Do not save**.
    

n8n Cloud data pruning and out of memory incident prevention[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#cloud-data-pruning-and-out-of-memory-incident-prevention)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Automatic data pruning[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#automatic-data-pruning)

n8n automatically prunes execution logs after a certain time or once you reach the max storage limit, whichever comes first. The pruning always happens from oldest to newest and the limits depend on your n8n Cloud plan:

*   Start and Starter plans: max 2500 executions saved and 7 days execution log retention;
    
*   Pro plans: max 25000 executions saved and 30 days execution log retention;
    
*   Enterprise plan: max 50000 executions saved and unlimited execution log retention time.
    

You reach the maximum storage limit either by exceeding the maximum number of saved executions or by exceeding the instance's database storage size. If the instance's database reaches this limit, n8n removes only the execution data and keeps the execution record. Pruning based on execution count or retention time, however, removes the record completely.

### Manual data pruning[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#manual-data-pruning)

Heavier executions and use cases can exceed database capacity despite the automatic pruning practices. In cases like this, n8n will manually prune data to protect instance stability.

1.  An alert system warns n8n if an instance is at 85% disk capacity.
    
2.  n8n prunes execution data. n8n does this by running a backup of the instance (workflows, users, credentials and execution data) and restoring it without execution data.
    

Due to the human steps in this process, the alert system isn't perfect. If warnings are triggered after hours or if data consumption rates are high, there might not be time to prune the data before the remaining disk space fills up.

Related resources[](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data#related-resources)

-----------------------------------------------------------------------------------------------------------------

*   [Configure Cloud](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud)
    
*   [Set your timezone](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/set-your-timezone)
    
*   [Find your IP addresses](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses)
    
*   [Change instance ownership or username](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username)
    

[PreviousFind your IP addresses](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses)
[NextChange instance ownership or username](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username)

Last updated 10 days ago

Was this helpful?