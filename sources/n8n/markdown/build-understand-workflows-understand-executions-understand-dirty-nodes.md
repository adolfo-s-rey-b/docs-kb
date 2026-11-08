For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes.md)
.

A **dirty node** is a node that executed successfully in the past, but whose output n8n now considers stale or unreliable. They're labeled like this to indicate that if the node executes again, the output may be different. It may also be the point where a [partial execution](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#partial-executions)
 starts from.

How to recognize dirty node data[](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes#how-to-recognize-dirty-node-data)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In the canvas of the workflow editor, you can identify dirty notes by their different-colored border and a yellow triangle in place of the previous green tick symbol. For example:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-79a2e3c2065a74d394df91cdeb4a53497994742e%252Fdirty-node-canvas.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e5f2f8dd1e9d3f61cd48bf1d31b2596&sv=3)

A node on the canvas with a yellow border and a yellow triangle icon instead of the usual green success tick

In the node editor view, the output panel also displays a yellow triangle on the output panel. If you hover over the triangle, a tooltip appears with more information about why n8n considers the data stale:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-b0283659b6d5f12514f2cdbca09e842bff0b043c%252Fdirty-node-editor.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b5a9d98af42ae83f175fe1b3a87678be&sv=3)

Node editor's output panel showing a yellow triangle icon with a tooltip explaining why the data is stale

Why n8n marks nodes dirty[](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes#why-n8n-marks-nodes-dirty)

---------------------------------------------------------------------------------------------------------------------------------------------------

There are several reasons why n8n might flag execution data as stale. For example:

*   Inserting or deleting a node: labels the first node that follows the inserted node dirty.
    
*   Modifying node parameters: labels the modified node dirty.
    
*   Adding a connector: labels the destination node of the new connector dirty.
    
*   Deactivating a node: labels the first node that follows the deactivated node dirty.
    

Other reasons n8n marks nodes dirty[](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes#other-reasons-n8n-marks-nodes-dirty)

*   Unpinning a node: labels the unpinned node dirty.
    
*   Modifying pinned data: labels the node that comes after the pinned data dirty.
    
*   If any of the above actions occur inside a loop, also labels the first node of the loop dirty.
    

For sub-nodes, also labels any executed parent nodes (up to and including the root) when:

*   Editing an executed sub-node
    
*   Adding a new sub-node
    
*   Disconnecting or deleting a sub-node
    
*   Deactivating a sub-node
    
*   Activating a sub-node
    

*   When deleting a connected node in a workflow:
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-bb27d61f43d06f2cd04d6fff3068a2b4a51b62e6%252Fdirty-before.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b89db86196b60aa03c07759360fefc79&sv=3)
    
    Workflow canvas before you delete a connected node, with all nodes showing green success ticks
    
*   The next node in the sequence becomes dirty:
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-74070bff3346466d20a0983b5f1c7676828727b5%252Fdirty-after.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=434334b1b49312b6d3e916a145ed3bda&sv=3)
    
    Workflow canvas after you delete the node, with the next node in the sequence now marked dirty with a yellow border
    

When using loops (with the [Loop over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches)
 node), when any node within the loop is dirty, the initial node of the loop is also considered dirty:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-7c7d67bac862a5dc53d2bf5150ccfb2f595f5569%252Fdirty-loop.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=442b4373dab7301f831160ad5e271726&sv=3)

Loop Over Items node marked dirty because a node inside its loop is dirty

Resolving dirty nodes[](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes#resolving-dirty-nodes)

-------------------------------------------------------------------------------------------------------------------------------------------

Executing a node again clears its dirty status. You can do this manually by triggering the whole workflow, or by running a [partial execution](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions#partial-executions)
 with **Execute step** on the individual node or any node which follows it.

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    

[PreviousTypes of executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
[NextDebug executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)

Last updated 10 days ago

Was this helpful?