For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions.md)
.

To view **all executions** from an n8n instance, navigate to the **Overview** page and then click into the Executions tab. This will show you all executions from the workflows you have access to.

If your n8n instance supports **projects**, you'll also be able to view the executions tab within projects you have access to. This will show you executions only from the workflows within the specified project.

**Deleted workflows**

When you delete a workflow, n8n deletes its execution history as well. This means you can't view executions for deleted workflows.

Filter executions[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions#filter-executions)

--------------------------------------------------------------------------------------------------------------------------------

You can filter the executions list:

1.  Select the **Executions** tab either from within the **Overview** page or a specific **project** to open the list.
    
2.  Select **Filters**.
    
3.  Enter your filters. You can filter by:
    
    *   **Workflows**: choose all workflows, or a specific workflow name.
        
    *   **Status**: choose from **Failed**, **Running**, **Success**, or **Waiting**.
        
    *   **Execution start**: see executions that started in the given time.
        
    *   **Saved custom data**: this is data you create within the workflow using the Code node. Enter the key and value to filter. Refer to [Custom executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
         for information on adding custom data.
        
    

**Feature availability**

Custom executions data is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Registered Community, Enterprise
    

Retry failed workflows[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions#retry-failed-workflows)

------------------------------------------------------------------------------------------------------------------------------------------

If your workflow execution fails, you can retry the execution. To retry a failed workflow:

1.  Select the **Executions** tab from within either the **Overview** page or a specific **project** to open the list.
    
2.  On the execution you want to retry, select **Retry execution** ![Options menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=71816d7d4b7eec8ac467fd97f3d76f22&sv=3).
    
3.  Select either of the following options to retry the execution:
    
    *   **Retry with currently saved workflow**: Once you make changes to your workflow, you can select this option to execute the workflow with the previous execution data.
        
    *   **Retry with original workflow**: If you want to retry the execution without making changes to your workflow, you can select this option to retry the execution with the previous execution data.
        
    

### What a retry runs[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions#what-a-retry-runs)

When a node fails, a retry resumes from the saved execution state instead of starting the workflow again from the trigger:

*   n8n keeps the results of completed node runs. For example, if a workflow adds a row and then fails when sending a message, retrying the failed message node doesn't repeat the earlier row addition.
    
*   The failed node receives its saved input again and processes every item, including items it handled before it failed. For example, a node that sent some messages before it failed sends those messages again. Before you retry, check the target app for items the node already handled. To make retries safe, use operations that update existing records instead of creating new ones, such as **Append or Update Row** in the Google Sheets node or **Insert or Update** in the Postgres node.
    
*   If the failed node is an **Execute Sub-workflow** node, the retry runs the whole sub-workflow again from its start.
    
*   **Retry with original workflow** runs the workflow as it was when the execution ran. If you changed the workflow to fix the failure, choose **Retry with currently saved workflow**. Your changes apply only to nodes that haven't completed: completed nodes keep their saved results. Both options load your credentials when the retry runs, so if you only fixed a credential, **Retry with original workflow** already uses the fix.
    
*   Each retry is a new execution. If a retry fails, both the original execution and the failed retry show the retry option. Retry only one of them: retrying both can repeat work for the same data. To avoid extra failed retries, fix the cause before you retry.
    
*   You can't retry an execution that succeeded, even if it didn't do what you expected. For example, an **If** node may have sent every item to the false branch. Use **Copy to editor** to pin the saved data in the first node of your current workflow, then run the workflow again. That run repeats every node after the first, including actions such as adding rows or sending messages. Refer to [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
     for availability and steps.
    
*   You can retry an execution only while n8n still stores it. n8n doesn't store failed production executions if the workflow's [Save failed production executions](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings#save-failed-production-executions)
     setting is **Do not save**. For how long n8n keeps executions, refer to [Execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
     for self-hosted instances, or [Manage your data](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data)
     for n8n Cloud.
    

Load data from previous executions into your current workflow[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions#load-data-from-previous-executions-into-your-current-workflow)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can load data from a previous workflow back into the canvas. Refer to [Debug executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
 for more information.

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousView executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
[NextCustomize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)

Last updated 10 days ago

Was this helpful?