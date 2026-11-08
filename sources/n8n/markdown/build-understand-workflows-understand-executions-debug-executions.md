For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions.md)
.

**Feature availability**

Debugging and re-running past executions is available on:

*   **n8n Cloud:** All plans
    
*   **Self-hosted:** Registered Community, Business, Enterprise
    

You can load data from a previous execution into your current workflow. This is useful for debugging data from failed production executions: you can see a failed execution, make changes to your workflow to fix it, then re-run it with the previous execution data.

Load data[](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions#load-data)

-------------------------------------------------------------------------------------------------------------

To load data from a previous execution:

1.  In your workflow, select the **Executions** tab to view the **Executions** list.
    
2.  Select the execution you want to debug. n8n displays options depending on whether the workflow was successful or failed:
    
    *   For failed executions: select **Debug in editor**.
        
    *   For successful executions: select **Copy to editor**.
        
    
3.  n8n copies the execution data into your current workflow, and [pins the data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
     in the first node in the workflow.
    

**Check which executions you save**

The executions available on the **Executions** list depends on your [Workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
.

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions#related-resources)

-----------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousUnderstand dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
[NextView executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)

Last updated 10 days ago

Was this helpful?