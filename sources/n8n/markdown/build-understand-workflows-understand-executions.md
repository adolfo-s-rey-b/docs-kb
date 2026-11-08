For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions.md)
.

An execution is a single run of a workflow.

In this section[](https://docs.n8n.io/build/understand-workflows/understand-executions#in-this-section)

--------------------------------------------------------------------------------------------------------

*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    : how manual, partial, and production executions differ.
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    : view and filter all executions across all your workflows.
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    : view and filter executions for the workflow currently open on the canvas.
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    : copy data from a previous execution into your current workflow to debug it.
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    : add custom data to your workflow executions using the Code node.
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    : send data back to users as an AI Agent node generates it.
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    : what dirty nodes are and how they affect workflow execution.
    

Execution modes[](https://docs.n8n.io/build/understand-workflows/understand-executions#execution-modes)

--------------------------------------------------------------------------------------------------------

There are two execution modes:

*   **Manual:** Run workflows manually by clicking **Execute Workflow**. Unpublish workflows while testing through manual runs.
    
*   **Production:** Production workflows run automatically. Publish a version of the workflow to put it into production.
    

How executions count towards quotas:[](https://docs.n8n.io/build/understand-workflows/understand-executions#how-executions-count-towards-quotas)

-------------------------------------------------------------------------------------------------------------------------------------------------

[Paid plans](https://n8n.io/pricing/)
, whether cloud or self-hosted, have an execution limit quota. Only production executions count towards this quota. These are executions started automatically by triggers, schedules, or polling. This distinction applies regardless of the instance environment, such as development or production.

### Execution count by trigger type[](https://docs.n8n.io/build/understand-workflows/understand-executions#execution-count-by-trigger-type)

The way executions are counted depends on the type of trigger node used:

*   **Schedule Trigger nodes:** Count one execution every time the node fires, regardless of outcome.
    
*   **Polling nodes (like Google Drive Trigger):** Count one execution only when new data is found. Polls that return no results don't count as an execution.
    
*   **Webhook Trigger nodes:** Count one execution for every inbound request that activates the trigger. This includes requests with an empty body (such as `{}`). Malformed requests that fail before the workflow starts don't count as an execution.
    

### Triggers and runs that don't count[](https://docs.n8n.io/build/understand-workflows/understand-executions#triggers-and-runs-that-dont-count)

The following don't count towards your execution quota:

*   **Manual executions:** Running a workflow from the editor while building or testing.
    
*   **Sub-workflow executions:** When a workflow calls another workflow with the Execute Sub-workflow node, only the parent (top-level) execution counts.
    
*   **Error workflow executions:** Runs of a workflow set as an [error workflow](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    .
    
*   **Polls that return no data:** A polling trigger only counts when it finds new data.
    
*   **Malformed or rejected requests:** Webhook requests that fail before the workflow starts.
    

Execution lists[](https://docs.n8n.io/build/understand-workflows/understand-executions#execution-lists)

--------------------------------------------------------------------------------------------------------

n8n provides two execution lists:

*   [Workflow-level executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    : this execution list shows the executions for a single workflow.
    
*   [All executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    : this list shows all executions for all your workflows.
    

n8n supports [adding custom data to executions](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
.

Execution data redaction[](https://docs.n8n.io/build/understand-workflows/understand-executions#execution-data-redaction)

--------------------------------------------------------------------------------------------------------------------------

You can redact execution data to protect sensitive information. Redaction hides the input and output data of workflow executions while preserving execution metadata like status, timing, and node names. Refer to [Execution data redaction](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data)
 for details.

Execution data from credentials you can't use[](https://docs.n8n.io/build/understand-workflows/understand-executions#execution-data-from-credentials-you-cant-use)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

If an execution used a credential you can't use, n8n hides its data from you. You still see the execution's status and timing. This includes data that came back from a sub-workflow that used the credential, even when the parent workflow doesn't use it itself. The same rules apply to executions you read through the public API or the n8n MCP server.

Refer to [Use personal credentials in projects](https://docs.n8n.io/administer/manage-credentials/use-personal-credentials-in-projects#execution-data-from-credentials-you-cant-use)
 for details.

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions#related-resources)

------------------------------------------------------------------------------------------------------------

*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Create and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)
    
*   [Save and publish workflows](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows)
    
*   [Create and edit credentials](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials)
    
*   [Use Gateway credits](https://docs.n8n.io/build/understand-workflows/use-gateway-credits)
    
*   [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
    

[PreviousFind your workflow ID](https://docs.n8n.io/build/understand-workflows/workflow-components/find-your-workflow-id)
[NextTypes of executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)

Last updated 10 days ago

Was this helpful?