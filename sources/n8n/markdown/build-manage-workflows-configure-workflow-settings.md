For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings.md)
.

You can customize workflow behavior for individual workflows using workflow settings.

Access workflow settings[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#access-workflow-settings)

----------------------------------------------------------------------------------------------------------------------------

To open the settings:

1.  Open your workflow.
    
2.  Select the **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=054f3c717b7b07b59bb2cd5fd69cc732&sv=3) in the upper-right corner.
    
3.  Select **Settings**. n8n opens the **Workflow settings** modal.
    

Available settings[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#available-settings)

----------------------------------------------------------------------------------------------------------------

The following settings are available:

### Execution order[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#execution-order)

Choose the execution order for multi-branch workflows:

**v1 (recommended)** executes each branch in turn, completing one branch before starting another. n8n orders the branches based on their position on the canvas, from topmost to bottommost. If two branches are at the same height, the leftmost branch executes first.

**v0 (legacy)** executes the first node of each branch, then the second node of each branch, and so on.

### Error Workflow (to notify when this one errors)[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#error-workflow-to-notify-when-this-one-errors)

Select a workflow to trigger if the current workflow fails. See [error workflows](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
 for more details.

### This workflow can be called by[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#this-workflow-can-be-called-by)

Choose which other workflows can call this workflow.

### Timezone[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#timezone)

Sets the timezone for this workflow. The timezone setting is important for the Schedule Trigger node.

You can set your n8n instance's timezone to configure the default timezone workflows use:

*   [Set a n8n Cloud instance timezone](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/set-your-timezone)
    
*   [Configure the timezone for self-hosted instances](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization)
    

If you don't configure the workflow or instance timezone, n8n defaults to the EDT (New York) timezone.

### Save failed production executions[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#save-failed-production-executions)

Whether n8n should save failed executions for published workflows.

### Save successful production executions[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#save-successful-production-executions)

Whether n8n should save successful executions for published workflows.

### Save manual executions[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#save-manual-executions)

Whether n8n should save executions for workflows started by the user in the editor.

### Save execution progress[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#save-execution-progress)

Whether n8n should save execution data for each node.

If set to **Save**, the workflow resumes from where it stopped in case of an error. This may increase latency.

### Timeout Workflow[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#timeout-workflow)

Whether n8n should cancel the current workflow execution after a certain amount of time elapses.

When enabled, the **Timeout After** option appears. Here, you can set the time (in hours, minutes, and seconds) after which the workflow should timeout. For n8n Cloud users, n8n enforces a maximum available timeout for each plan.

### Redact production execution data[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#redact-production-execution-data)

Controls whether n8n redacts execution data from production (non-manually triggered) executions. When set to **Redact**, n8n hides the input and output data of each node and replaces it with a redacted indicator.

### Redact manual execution data[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#redact-manual-execution-data)

Controls whether n8n redacts execution data from manually triggered executions. When set to **Redact**, n8n hides the input and output data of each node and replaces it with a redacted indicator.

If your instance admin [enforces data redaction instance-wide](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#instance-level-enforcement)
, n8n locks the settings covered by the enforced scope to **Redact**. You can't turn them off here.

Refer to [Execution data redaction](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data)
 for details on redaction policies, revealing data, and permission requirements.

### Estimated time saved[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#estimated-time-saved)

An estimate of the number of minutes each of execution of this workflow saves you.

Setting this lets n8n calculate the amount of time saved for [insights](https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights)
.

### Custom span attributes[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#custom-span-attributes)

Add custom key-value attributes to the workflow's OpenTelemetry span. Refer to [Custom span attributes](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry#custom-span-attributes)
 for details.

Related resources[](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#related-resources)

--------------------------------------------------------------------------------------------------------------

*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Tag workflows](https://docs.n8n.io/build/manage-workflows/tag-workflows)
    
*   [Favorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
    
*   [View change history](https://docs.n8n.io/build/manage-workflows/view-change-history)
    
*   [Review workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
    
*   [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import)
    
*   [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
    
*   [Share with others](https://docs.n8n.io/build/manage-workflows/share-with-others)
    

[PreviousManage workflows](https://docs.n8n.io/build/manage-workflows)
[NextTag workflows](https://docs.n8n.io/build/manage-workflows/tag-workflows)

Last updated 10 days ago

Was this helpful?