For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes.md)
.

Nodes are the key building blocks of a workflow. They perform a range of actions, including:

*   Starting the workflow.
    
*   Fetching and sending data.
    
*   Processing and manipulating data.
    

n8n provides a collection of built-in nodes, as well as the ability to create your own nodes. Refer to:

*   [Built-in integrations](https://docs.n8n.io/integrations/builtin/node-types)
     to browse the node library.
    
*   [Community nodes](https://docs.n8n.io/integrations/community-nodes/installation-and-management)
     for guidance on finding and installing community-created nodes.
    
*   [Creating nodes](https://docs.n8n.io/connect/create-nodes/overview)
     to start building your own nodes.
    

Add a node to your workflow[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#add-a-node-to-your-workflow)

----------------------------------------------------------------------------------------------------------------------------------------------

### Add a node to an empty workflow[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#add-a-node-to-an-empty-workflow)

1.  Select **Add first step**. n8n opens the nodes panel, where you can search or browse trigger nodes.
    
2.  Select the trigger you want to use.
    
    **Choose the correct app event**
    
    If you select **On App Event**, n8n shows a list of all the supported services. Use this list to browse n8n's integrations and trigger a workflow in response to an event in your chosen service. Not all integrations have triggers. To see which ones you can use as a trigger, select the node. If a trigger is available, you'll see it at the top of the available operations list.
    
    For example, this is the trigger for Asana:
    
    ![Screenshot of the Asana node operations list, showing the Recommended section at the top of the list](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-6a5204b612729bae4abebc5fa80c041b4fec8d51%252Frecommended-trigger.png%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=e1756dc0e97e6d5a0ffa58a16c0f5b3f&sv=3)
    

### Add a node to an existing workflow[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#add-a-node-to-an-existing-workflow)

Select the **Add node** ![Add node icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-73e6ba16c5921db1159055c997764094715b508e%252Fadd-node-small.png%3Falt%3Dmedia&width=40&dpr=3&quality=100&sign=b0d68592e1e36e94c9f6e4f46843819b&sv=3) connector. n8n opens the nodes panel, where you can search or browse all nodes.

### Node operations: Triggers and Actions[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#node-operations-triggers-and-actions)

When you add a node to a workflow, n8n displays a list of available operations. An operation is something a node does, such as getting or sending data.

There are two types of operation:

*   Triggers start a workflow in response to specific events or conditions in your services. When you select a Trigger, n8n adds a trigger node to your workflow, with the Trigger operation you chose pre-selected. When you search for a node in n8n, Trigger operations have a bolt icon ![Trigger icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-4829d6f9de935beb784ab8cce7a682aaaf30432c%252Ftrigger.png%3Falt%3Dmedia&width=26&dpr=3&quality=100&sign=654467905ab06631af4e1f5367be046d&sv=3).
    
*   Actions are operations that represent specific tasks within a workflow, which you can use to manipulate data, perform operations on external systems, and trigger events in other systems as part of your workflows. When you select an Action, n8n adds a node to your workflow, with the Action operation you chose pre-selected.
    

Node controls[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#node-controls)

------------------------------------------------------------------------------------------------------------------

To view node controls, hover over the node on the canvas:

*   **Execute step** ![Execute step icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1e58ea54f01bc7bb2cc230fab8236edde4b292ff%252Fplay-node.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=9938d4201ed7d899e2db6f7ac8943512&sv=3): Run the node.
    
*   **Deactivate** ![Deactivate node icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-58748b386a57474a063a8e55b29adf1e5e1e51c2%252Fpower-off.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=f1e74cfb40af9be5a70f495f4badad4f&sv=3): Deactivate the node.
    
*   **Delete** ![Delete node icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-3e59223f23216d4a14726e8ab618776bf6dd61ab%252Fdelete-node.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=544d2a26a8327701b4c0a9006cde3a72&sv=3): Delete the node.
    
*   **Node context menu** ![Node context menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-d32a8d59c9322093771e1e567f5ad2cf0a916558%252Fnode-context-menu.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=d026c5aad4711704bc1edd9014b6969a&sv=3): Select node actions. Available actions:
    
    *   Open node
        
    *   Execute step
        
    *   Rename node
        
    *   Deactivate node
        
    *   Pin node
        
    *   Copy node
        
    *   Duplicate node
        
    *   Tidy up workflow
        
    *   Convert node to sub-workflow
        
    *   Select all
        
    *   Clear selection
        
    *   Delete node
        
    

Node settings[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#node-settings)

------------------------------------------------------------------------------------------------------------------

The node settings under the **Settings** tab allow you to control node behaviors and add node notes.

When active or set, they do the following:

*   **Always Output Data**: The node returns an empty item even if the node returns no data during execution. Be careful setting this on IF nodes, as it could cause an infinite loop.
    
*   **Execute Once**: The node executes once, with data from the first item it receives. It doesn't process any extra items.
    
*   **Retry On Fail**: When an execution fails, the node reruns until it succeeds.
    
*   **On Error**:
    
    *   **Stop Workflow**: Halts the entire workflow when an error occurs, preventing further node execution.
        
    *   **Continue**: Proceeds to the next node despite the error, using the last valid data.
        
    *   **Continue (using error output)**: Continues workflow execution, passing error information to the next node for potential handling.
        
    
*   **Custom Span Attributes**: Add custom key-value attributes to a node's OpenTelemetry span. Keys are plain text, and values support expressions. This setting only appears if you enable OpenTelemetry tracing and have a self-hosted Enterprise license. Refer to [Custom span attributes](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry#custom-span-attributes)
     for details.
    

You can document your workflow using node notes:

*   **Notes**: Note to save with the node.
    
*   **Display note in flow**: If active, n8n displays the note in the workflow as a subtitle.
    

Related resources[](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes#related-resources)

--------------------------------------------------------------------------------------------------------------------------

*   [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
    
*   [Connect nodes together](https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together)
    
*   [Add notes and documentation](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation)
    
*   [Canvas Groups](https://docs.n8n.io/build/understand-workflows/workflow-components/canvas-groups)
    
*   [Find your workflow ID](https://docs.n8n.io/build/understand-workflows/workflow-components/find-your-workflow-id)
    

[PreviousWorkflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
[NextConnect nodes together](https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together)

Last updated 10 days ago

Was this helpful?