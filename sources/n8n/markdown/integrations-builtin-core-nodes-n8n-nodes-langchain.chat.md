For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md)
.

Use the Chat node with the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node to send messages into the chat and optionally wait for responses from users. This enables human-in-the-loop (HITL) use cases in chat workflows, allowing you to have multiple chat interactions within a single execution. The Chat node also works as a tool for AI Agents.

**Chat Trigger node**

The Chat node requires a [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node to be present in the workflow, with the [Response Mode](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#response-mode)
 set to 'Using Response Nodes'.

**Embedded mode not supported**

The Chat node isn't supported when the Chat Trigger node is set to **Embedded** mode. In Embedded mode, use the [Respond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
 node instead.

**Previous version**

In previous versions, this node was called "Respond to Chat" and used a single "Wait for User Reply" toggle. The functionality has been reorganized into two distinct actions with additional response types.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#node-parameters)

----------------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

**Human-in-the-loop for AI tool calls**

This node can be used as a human review step for AI Agent tool calls. When configured this way, the AI Agent will pause and request human approval through this service before executing tools that require oversight. Learn more in [Human-in-the-loop for AI tool calls](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
.

Configure this node using the following parameters.

### Operation[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#operation)

The Chat node supports the following operations:

*   **Send Message**: Send a message to the chat. The workflow execution continues immediately after sending.
    
*   **Send and Wait for Response**: Send a message to the chat and wait for a response from the user. This operation pauses the workflow execution until the user submits a response.
    

Choosing **Send and Wait for Response** activates additional parameters and options as discussed in [waiting for a response](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#waiting-for-a-response)
.

### Message[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#message)

The message to send to the chat. This parameter is available for both operations.

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#node-options)

----------------------------------------------------------------------------------------------------------

Use these **Options** to further refine the node's behavior.

### Add Memory Input Connection[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#add-memory-input-connection)

Choose whether you want to commit the messages from the Chat node to a connected memory. Using a shared memory between an agent or chain [root node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes)
 and the Chat node attaches the same session key to these messages and lets you capture the full message history.

Waiting for a response[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#waiting-for-a-response)

------------------------------------------------------------------------------------------------------------------------------

By choosing the **Send and Wait for Response** operation, you can send a message and pause the workflow execution until a person responds. This enables multi-turn conversations and approval workflows within a single execution.

### Response Type[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#response-type)

You can choose between the following types of responses:

*   **Free Text**: Users can type any response in the chat. This is the same behavior as the previous "Wait for User Reply" option.
    
*   **Approval**: Users can approve or disapprove using inline buttons in the message. You can also optionally allow users to type custom responses.
    

Different parameters and options are available depending on which type you choose.

### Free Text parameters and options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#free-text-parameters-and-options)

When using the Free Text response type, the user can type any message as their response.

**Use cases:**

*   Open-ended questions
    
*   Collecting detailed feedback
    
*   Requesting specific information
    

**Options:**

*   **Limit Wait Time**: Whether the workflow automatically resumes execution after a specified time limit. This can be an interval or a specific wall time.
    

### Approval parameters and options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#approval-parameters-and-options)

When using the Approval response type, the message displays inline buttons that users can click to approve or disapprove. This response type follows the same pattern as other human-in-the-loop (HITL) nodes in n8n.

**Use cases:**

*   Simple yes/no decisions
    
*   Approval workflows
    
*   Confirmations
    

When using the Approval response type, the following parameters are available:

*   **Type of Approval**: Whether to present only an approval button or both approval and disapproval buttons.
    
    *   **Approve Only**: Displays a single approval button
        
    *   **Approve and Disapprove**: Displays both buttons (default)
        
    
*   **Approve Button Label**: The text to display on the approval button. Default: `Approve`
    
*   **Disapprove Button Label**: The text to display on the disapproval button (only shown when Type of Approval is "Approve and Disapprove"). Default: `Disapprove`
    
*   **Block User Input**: Whether to prevent users from typing custom messages (enabled) or allow them to type responses (disabled, default).
    
    *   When **disabled** (default): Users can click buttons or type a custom message. Typed messages are treated as disapproval with a custom message.
        
    *   When **enabled**: Users can only interact using the buttons.
        
    

The Approval response type also offers the following option:

*   **Limit Wait Time**: Whether the workflow automatically resumes execution after a specified time limit. This can be an interval or a specific wall time.
    

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#related-resources)

--------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Refer to the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node documentation for information about setting up the chat interface.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse n8n integration templates](https://n8n.io/integrations/)
 or [search all templates](https://n8n.io/workflows/)

Common issues[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat#common-issues)

------------------------------------------------------------------------------------------------------------

*   The Chat node isn't supported when the Chat Trigger node's **Mode** is set to **Embedded**. In Embedded mode, the Chat Trigger node only offers **Respond to Webhook** as a response mode. Use the [Respond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
     node instead.
    
*   The Chat node doesn't work when used as a tool of a sub-agent.
    
*   The Chat node doesn't work when used in a sub-workflow. This includes usage in a sub-workflow that's being used as a tool for an AI Agent.
    
*   Make sure the Chat Trigger node's Response Mode is set to "Using Response Nodes" for the Chat node to function properly.
    

For common questions or issues with the Chat Trigger node, refer to [Common Chat Trigger Node Issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues)
.

[PreviousRename Keys](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys)
[NextRespond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)

Last updated 10 days ago

Was this helpful?