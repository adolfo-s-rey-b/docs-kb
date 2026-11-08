For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow.md)
.

The **Executions** list in a workflow shows all executions for that workflow.

**Deleted workflows**

When you delete a workflow, n8n deletes its execution history as well. This means you can't view executions for deleted workflows.

**Execution history and workflow history**

Don't confuse the execution list with [Workflow history](https://docs.n8n.io/build/manage-workflows/view-change-history)
.

Executions are workflow runs. With the executions list, you can see previous runs of the current version of the workflow. You can copy previous executions into the editor to [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
 in your current workflow.

Workflow history is previous versions of the workflow: for example, a version with a different node, or different parameters set.

View executions for a single workflow[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow#view-executions-for-a-single-workflow)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the workflow, select the **Executions** tab in the top menu. You can preview all executions of that workflow.

**Executions using end-user credentials**

When an execution uses an [end-user credential](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)
, only the user whose connected account ran the node can see that node's data. For everyone else, including admins, the output is redacted.

Filter executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow#filter-executions)

--------------------------------------------------------------------------------------------------------------------------------------------------

You can filter the executions list.

1.  In your workflow, select **Executions**.
    
2.  Select **Filters**.
    
3.  Enter your filters. You can filter by:
    
    *   **Status**: choose from **Failed**, **Running**, **Success**, or **Waiting**.
        
    *   **Execution start**: see executions that started in the given time.
        
    *   **Saved custom data**: this is data you create within the workflow using the Code node. Enter the key and value to filter. Refer to [Custom executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
         for information on adding custom data.
        
    

**Feature availability**

Custom executions data is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Registered Community, Enterprise
    

Retry failed workflows[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow#retry-failed-workflows)

------------------------------------------------------------------------------------------------------------------------------------------------------------

If your workflow execution fails, you can retry the execution. To retry a failed workflow:

1.  Open the **Executions** list.
    
2.  For the workflow execution you want to retry, select **Refresh** ![Refresh icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f422242e07871bf736b704bb4a47df45b43dbd70%252Frefresh.png%3Falt%3Dmedia&width=42&dpr=3&quality=100&sign=27d3acecd702275f800e41fe9db3f501&sv=3).
    
3.  Select either of the following options to retry the execution:
    
    *   **Retry with currently saved workflow**: Once you make changes to your workflow, you can select this option to execute the workflow with the previous execution data.
        
    *   **Retry with original workflow**: If you want to retry the execution without making changes to your workflow, you can select this option to retry the execution with the previous execution data.
        
    

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousDebug executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
[NextView all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)

Last updated 10 days ago

Was this helpful?