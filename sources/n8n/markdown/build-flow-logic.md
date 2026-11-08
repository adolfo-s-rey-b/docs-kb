For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic.md)
.

n8n allows you to represent complex logic in your workflows.

In this section[](https://docs.n8n.io/build/flow-logic#in-this-section)

------------------------------------------------------------------------

*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    : route items down different branches with the IF and Switch nodes.
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    : combine multiple data streams back into one.
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    : repeat an action until a condition is met, or until all items are processed.
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    : pause a workflow's execution and resume it later.
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    : learn how n8n decides which branch runs first in a multi-branch workflow.
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    : call one workflow from another to build modular, microservice-like workflows.
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    : turn part of an existing workflow into a reusable sub-workflow.
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    : set up an error workflow to respond to execution failures.
    

Related sections[](https://docs.n8n.io/build/flow-logic#related-sections)

--------------------------------------------------------------------------

You need some understanding of [Data](https://docs.n8n.io/build/work-with-data)
 in n8n, including [Data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
 and [Data flow within nodes](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#how-data-flows-within-nodes)
.

When building your logic, you'll use n8n's [Core nodes](https://docs.n8n.io/integrations/builtin/core-nodes)
, including:

*   Splitting: [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
     and [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
    .
    
*   Merging: [Merge](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge)
    , [Compare Datasets](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets)
    , and [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
    .
    
*   Looping: [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
     and [Loop Over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches)
    .
    
*   Waiting: [Wait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
    .
    
*   Creating sub-workflows: [Execute Workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow)
     and [Execute Workflow Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)
    .
    
*   Error handling: [Stop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror)
     and [Error Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger)
    .
    

Related resources[](https://docs.n8n.io/build/flow-logic#related-resources)

----------------------------------------------------------------------------

*   [Build](https://docs.n8n.io/build)
    
*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Build and manage agents](https://docs.n8n.io/build/build-and-manage-agents)
    
*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Code in n8n](https://docs.n8n.io/build/code-in-n8n)
    
*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [Keyboard shortcuts](https://docs.n8n.io/build/keyboard-shortcuts)
    

[PreviousShare with others](https://docs.n8n.io/build/manage-workflows/share-with-others)
[NextSplit with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)

Last updated 10 days ago

Was this helpful?