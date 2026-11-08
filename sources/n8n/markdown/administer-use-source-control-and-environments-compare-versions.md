For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions.md)
.

Workflow diffs allow you to visually compare changes between the workflow you have on an instance and the most recent version saved in your connected Git repository. This helps you understand the exact changes to the workflow before you decide to either push or pull it across different environments.

**Feature availability**

Workflow diffs are available on:

*   **n8n Cloud:** Enterprise
    
*   **Self-hosted:** Business, Enterprise
    

Workflow diffs are only available when you [enable the environments features](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
 on an instance.

Accessing workflow diffs[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#accessing-workflow-diffs)

-----------------------------------------------------------------------------------------------------------------------------------------

You can access workflow diffs from two locations:

1.  **When pushing changes**: Click the workflow diff icon in the commit modal alongside the workflow you want to review
    
2.  **When pulling changes**: Click the workflow diff icon in the modified changes modal alongside the workflow you want to review
    

Understanding the workflow diff view[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#understanding-the-workflow-diff-view)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

When you open a workflow diff, n8n displays two workflows stacked vertically:

### When pushing[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#when-pushing)

*   **Top panel** (Remote branch): Latest version in your Git repository
    
*   **Bottom panel** (Local): Current locally saved version of the workflow
    

### When pulling[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#when-pulling)

*   **Top panel** (Local): Current version on your n8n instance
    
*   **Bottom panel** (Remote branch): Version you're pulling from the Git repository
    

In both cases, the top panel always displays the workflow that will update with changes.

The diff view highlights three types of changes:

*   **Added nodes and connectors**: New node additions or connectors will show as green along with an "N" icon
    
*   **Modified nodes and connectors**: Modifications to existing nodes or connectors will show as orange along with a "M" icon
    
*   **Deleted nodes and connectors**: Node or connector deletions will show as red along with a "D" icon
    

Reviewing node changes[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#reviewing-node-changes)

-------------------------------------------------------------------------------------------------------------------------------------

For modified nodes, you can also compare the specific changes. Click modified nodes to show a JSON diff of the changes. You can review the exact configuration for that node before and after the given change.

Viewing the summary of changes[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#viewing-the-summary-of-changes)

-----------------------------------------------------------------------------------------------------------------------------------------------------

In the top-right corner, the **changes** button shows the number of changes. This represents the total number of changes across node and node connectors, as well as general workflow settings updates.

Navigating through each change[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#navigating-through-each-change)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the **next** and **previous** arrows in the upper-right corner to cycle through your changes in a logical order. Use the **back** button in the top-left corner to return to the commit or pull modal to select a different workflow to review changes on.

Who can use workflow diffs[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#who-can-use-workflow-diffs)

---------------------------------------------------------------------------------------------------------------------------------------------

Only users who can push or pull commits for an instance can access workflow diffs:

*   instance owners
    
*   instance admins
    
*   project admins
    

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Use Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
    
*   [Choose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
    
*   [Set up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
    
*   [Push and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
    
*   [Move work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousPush and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
[NextMove work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)

Last updated 10 days ago

Was this helpful?