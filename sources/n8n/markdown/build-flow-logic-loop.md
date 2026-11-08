For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/loop.md)
.

Looping is useful when you want to process multiple items or perform an action repeatedly, such as sending a message to every contact in your address book. n8n handles this repetitive processing automatically, meaning you don't need to specifically build loops into your workflows. There are [some nodes](https://docs.n8n.io/build/flow-logic/loop#node-exceptions)
 where this isn't true.

Looping is one part of n8n's [flow logic](https://docs.n8n.io/build/flow-logic)
, alongside [splitting](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
 and [merging](https://docs.n8n.io/build/flow-logic/merge-data)
 data streams, and [waiting](https://docs.n8n.io/build/flow-logic/wait)
 between executions.

Using loops in n8n[](https://docs.n8n.io/build/flow-logic/loop#using-loops-in-n8n)

-----------------------------------------------------------------------------------

n8n nodes take any number of items as input, process these items, and output the results. You can think of each item as a single data point, or a single row in the output table of a node.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-e342ab56b034d8e3af917d885a18477e49ff592b%252Fcustomer_datastore_node.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d4d7d4ef5610f295e247e72866b4a062&sv=3)

The Customer Datastore node output

Nodes usually run once for each item. For example, if you wanted to send the name and notes of the customers in the Customer Datastore node as a message on Slack, you would:

1.  Connect the Slack node to the Customer Datastore node.
    
2.  Configure the parameters.
    
3.  Execute the node.
    

You would receive five messages: one for each item.

This is how you can process multiple items without having to explicitly connect nodes in a loop.

### Executing nodes once[](https://docs.n8n.io/build/flow-logic/loop#executing-nodes-once)

For situations where you don't want a node to process all received items, for example sending a Slack message only to the first customer, you can do so by toggling the **Execute Once** parameter in the **Settings** tab of that node This setting is helpful when the incoming data contains multiple items and you want to only process the first one.

Creating loops[](https://docs.n8n.io/build/flow-logic/loop#creating-loops)

---------------------------------------------------------------------------

n8n typically handles the iteration for all incoming items. However, there are certain scenarios where you will have to create a loop to iterate through all items. Refer to [Node exceptions](https://docs.n8n.io/build/flow-logic/loop#node-exceptions)
 for a list of nodes that don't automatically iterate over all incoming items.

### Loop until a condition is met[](https://docs.n8n.io/build/flow-logic/loop#loop-until-a-condition-is-met)

To create a loop in an n8n workflow, connect the output of one node to the input of a previous node. Add an [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
 node to check when to stop the loop.

Here is an [example workflow](https://n8n.io/workflows/1130)
 that implements a loop with an `IF` node:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-64f61a75cdfa6113c1e340cc9de7b93d3f91d971%252Fexample_workflow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=09c7a4f1720f7ef2c2b2ed160e86d75d&sv=3)

Workflow canvas showing an IF node connected back to a previous node to form a loop, checking a condition to stop it

### Loop until all items are processed[](https://docs.n8n.io/build/flow-logic/loop#loop-until-all-items-are-processed)

Use the [Loop Over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches)
 node when you want to loop until all items are processed. To process each item individually, set **Batch Size** to `1`.

You can batch the data in groups and process these batches. This approach is useful for avoiding API rate limits when processing large incoming data or when you want to process a specific group of returned items. Combine batching with a [Wait](https://docs.n8n.io/build/flow-logic/wait)
 node between batches to slow down processing further.

The Loop Over Items node stops executing after all the incoming items get divided into batches and passed on to the next node in the workflow so it's not necessary to add an IF node to stop the loop.

Node exceptions[](https://docs.n8n.io/build/flow-logic/loop#node-exceptions)

-----------------------------------------------------------------------------

Nodes and operations where you need to design a loop into your workflow:

*   [CrateDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb)
     executes once for `insert` and `update`.
    
*   [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
     node in **Run Once for All Items** mode: processes all the items based on the entered code snippet.
    
*   [Execute Workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow)
     node in **Run Once for All Items** mode.
    
*   [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
    : you must handle pagination yourself. If your API call returns paginated results you must create a loop to fetch one page at a time.
    
*   [Microsoft SQL](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql)
     executes once for `insert`, `update`, and `delete`.
    
*   [MongoDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mongodb)
     executes once for `insert` and `update`.
    
*   [QuestDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb)
     executes once for `insert`.
    
*   [Redis](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis)
    :
    
    *   Info: this operation executes only once, regardless of the number of items in the incoming data.
        
    
*   [RSS Read](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread)
     executes once for the requested URL.
    
*   [TimescaleDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb)
     executes once for `insert` and `update`.
    

Related resources[](https://docs.n8n.io/build/flow-logic/loop#related-resources)

---------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    

[PreviousMerge data](https://docs.n8n.io/build/flow-logic/merge-data)
[NextWait](https://docs.n8n.io/build/flow-logic/wait)

Last updated 10 days ago

Was this helpful?