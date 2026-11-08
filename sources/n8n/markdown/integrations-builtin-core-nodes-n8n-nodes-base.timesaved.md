For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved.md)
.

Use the Track Time Saved node to record how many minutes a workflow saves, based on the path an execution actually takes. n8n adds up every Track Time Saved node that runs during an execution and reports the total in [Insights](https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights)
.

Use this node when different paths through a workflow save different amounts of time. If every execution saves the same amount, set a fixed value on the workflow instead and you don't need this node.

**Set the workflow to Dynamic first**

This node only counts if the workflow's **Estimated time saved** setting is set to **Dynamic**. See [Setting the time saved by a workflow](https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights#setting-the-time-saved-by-a-workflow)
.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved#node-parameters)

----------------------------------------------------------------------------------------------------------------

*   **Calculation Mode**: Choose how n8n counts the minutes:
    
    *   **Once For All Items**: Counts **Minutes Saved** once, no matter how many items reach the node.
        
    *   **Per Item**: Multiplies **Minutes Saved** by the number of input items.
        
    
*   **Minutes Saved**: The number of minutes this step saves. Whole minutes, zero or more. Defaults to `0`.
    

The node passes every input item through unchanged, recording the time saved as execution metadata.

How n8n calculates the total[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved#how-n8n-calculates-the-total)

------------------------------------------------------------------------------------------------------------------------------------------

n8n adds up every Track Time Saved node that runs during an execution. Nodes on a branch that doesn't run don't count, which is what makes the total reflect the path taken.

You can place more than one Track Time Saved node in the same workflow. n8n sums their values for that execution.

When n8n counts an execution[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved#when-n8n-counts-an-execution)

------------------------------------------------------------------------------------------------------------------------------------------

n8n only records time saved for **successful production executions**. The following runs never contribute, whatever values the node holds:

*   **Manual executions.** Running the workflow from the editor doesn't count. Only production runs do.
    
*   **Failed executions.** If the run ends in an error, n8n records no time saved for it, even for the Track Time Saved nodes that already ran.
    
*   **Sub-workflow executions.** Insights skips them, so a Track Time Saved node inside a sub-workflow adds nothing, either to the sub-workflow or to the parent that called it. n8n records the minutes against the sub-workflow's own execution, and the parent's total never picks them up. To count time a sub-workflow saves, put the Track Time Saved node in the parent, after the Execute Sub-workflow node.
    
*   **Error workflow executions.** n8n treats these as operational rather than productive work.
    
*   **Chat executions.** Messages sent through n8n Chat Hub don't count, even when the run succeeds.
    
*   **Agent executions.** Executions started by an n8n Agent don't count, even when they succeed.
    

If the workflow uses **Fixed** rather than **Dynamic** for **Estimated time saved**, n8n ignores these nodes entirely and uses the fixed value instead.

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved#related-resources)

--------------------------------------------------------------------------------------------------------------------

*   [Track usage with Insights](https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights)
    : the Insights dashboard and the workflow-level time saved setting.
    
*   [Workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
    : where you set **Estimated time saved**.
    

[PreviousTOTP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp)
[NextWait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)

Last updated 10 days ago

Was this helpful?