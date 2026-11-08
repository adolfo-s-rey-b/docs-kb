For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions.md)
.

There are some important differences in how n8n executes workflows manually (by clicking the **Execute Workflow** button) and automatically (when the workflow is **published** and triggered by an event or schedule).

Manual executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#manual-executions)

--------------------------------------------------------------------------------------------------------------------------------

Manual executions allow you to run workflows directly from the canvas to test your workflow logic. These executions are "ad-hoc": they run only when you manually select the **Execute workflow** button.

Manual executions make building workflows easier by allowing you to iteratively test as you go, following the flow logic and seeing data transformations. You can test conditional branching, data formatting changes, and loop behavior by providing different input items and modifying node options.

**Pinning execution data**

When performing manual executions, you can use [data pinning](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
 to "pin" or "freeze" the output data of a node. You can optionally edit the pinned data as well.

On future runs, instead of executing the pinned node, n8n will substitute the pinned data and continue following the flow logic. This allows you to iterate without operating on variable data or repeating queries to external services. Production executions ignore all pinned data.

Partial executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#partial-executions)

----------------------------------------------------------------------------------------------------------------------------------

Clicking the **Execute workflow** button at the bottom of the workflow in the **Editor** tab manually runs the entire workflow. You can also perform partial executions to run specific steps in your workflow. Partial executions are manual executions that only run a subset of your workflow nodes.

To perform a partial execution, select a node, open its detail view, and select **Execute step**. This executes the specific node and any preceding nodes required to fill in its input data. You can also temporarily disable specific nodes in the workflow chain to avoid interacting with those services while building.

In particular, partial executions are useful when updating the logic of a specific node since they allow you to re-execute the node with the same input data.

### Troubleshooting partial executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#troubleshooting-partial-executions)

Some common issues you might come across when running partial executions include the following:

> The destination node is not connected to any trigger. Partial executions need a trigger.

This error message appears when you try to perform a partial execution without connecting the workflow to a trigger. Manual executions, including partial executions, attempt to mimic production executions when possible. Part of this includes requiring a trigger node to describe when the workflow logic should execute.

To work around this, connect a trigger node to the workflow with the node you're trying to execute. Most often, a [manual trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger)
 is the simplest option.

> Please execute the whole workflow, rather than just the node. (Existing execution data is too large.)

This error can appear when performing partial executions on workflows with large numbers of branches. Partial executions involve sending data and workflow logic to the n8n backend in a way that isn't required for full executions. This error occurs when your workflow exceeds the maximum size allowed for these messages.

To work around this, consider using the [limit node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit)
 to limit node output while running partial executions. Once the workflow is running as intended, you can disable or delete the limit node before enabling production execution.

Production executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#production-executions)

----------------------------------------------------------------------------------------------------------------------------------------

Production executions occur when a triggering event or schedule automatically runs a workflow. On [paid plans](https://n8n.io/pricing/)
, production executions count towards your execution quota. For details on what does and doesn't count, refer to [How executions count towards quotas](https://docs.n8n.io/build/understand-workflows/understand-executions#how-executions-count-towards-quotas)
.

To configure production executions, you must attach a trigger node (any trigger other than the [manual trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger)
 works) and [publish the workflow](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows)
 using the **Publish** button. Once published, the workflow automatically executes whenever the trigger condition occurs.

The execution flow for production executions doesn't display in the Editor tab of the workflow as with manual executions. Instead, you can see executions in the workflow's **Executions** tab according to your [workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
. From there, you can explore and troubleshoot problems using the [debug in editor feature](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
.

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousUnderstand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
[NextUnderstand dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)

Last updated 10 days ago

Was this helpful?