For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/wait.md)
.

Waiting allows you to pause a workflow mid-execution, then resume where the workflow left off, with the same data. This is useful if you need to rate limit your calls to a service, or wait for an external event to complete. You can wait for a specified duration, or until a webhook fires. Waiting is one part of n8n's [flow logic](https://docs.n8n.io/build/flow-logic)
, and works well alongside [loops](https://docs.n8n.io/build/flow-logic/loop)
 when you need to slow down batch processing, or as part of a [merge](https://docs.n8n.io/build/flow-logic/merge-data)
 across multiple node executions.

Making a workflow wait uses the [Wait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
 node. Refer to the node documentation for usage details.

n8n provides a workflow template with a basic example of [Rate limiting and waiting for external events](https://n8n.io/workflows/1749-rate-limiting-and-waiting-for-external-events/)
.

Related resources[](https://docs.n8n.io/build/flow-logic/wait#related-resources)

---------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    

[PreviousLoop](https://docs.n8n.io/build/flow-logic/loop)
[NextBreak workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)

Last updated 10 days ago

Was this helpful?