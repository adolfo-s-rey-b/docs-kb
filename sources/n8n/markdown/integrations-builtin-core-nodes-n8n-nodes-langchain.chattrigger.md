For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger.md)
.

Use the Chat Trigger node when building AI workflows for chatbots and other chat interfaces. You can configure how users access the chat, using one of n8n's provided interfaces, or your own. You can add authentication.

You must connect either an agent or chain [root node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes)
.

**Workflow execution usage**

Every message to the Chat Trigger executes your workflow. This means that one conversation where a user sends 10 messages uses 10 executions from your execution allowance. Check your payment plan for details of your allowance.

**Feature availability**

The Chat Trigger node is available from n8n 1.24.0, replacing the Manual Chat Trigger node.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#node-parameters)

-----------------------------------------------------------------------------------------------------------------------

### Make Chat Publicly Available[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#make-chat-publicly-available)

Set whether the chat should be publicly available (turned on) or only available through the manual chat interface (turned off).

Leave this turned off while you're building the workflow. Turn it on when you're ready to publish the workflow and allow users to access the chat.

#### Mode[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#mode)

Choose how users access the chat. Select from:

*   **Hosted Chat**: Use n8n's hosted chat interface. Recommended for most users because you can configure the interface using the [node options](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#node-options)
     and don't have to do any other setup.
    
*   **Embedded Chat**: This option requires you to create your own chat interface. You can use n8n's [chat widget](https://www.npmjs.com/package/@n8n/chat)
     or build your own. Your chat interface must call the webhook URL shown in **Chat URL** in the node.
    

#### Authentication[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#authentication)

Choose whether and how to restrict access to the chat. Select from:

*   **None**: The chat doesn't use authentication. Anyone can use the chat.
    
*   **Basic Auth**: The chat uses basic authentication.
    
    *   Select or create a **Credential for Basic Auth** with a username and password. All users must use the same username and password.
        
    
*   **n8n User Auth**: Only users logged in to an n8n account can use the chat.
    

When you select **n8n User Auth**, a **Require Workflow Execute Permission** toggle appears. Turn it on to require that the triggering user also has permission to execute the workflow in the project it belongs to. Users who are logged in but lack execute permission on the workflow can't use the chat. This is useful with [end-user credentials](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)
, where each user runs the workflow with their own connected account.

#### Initial Message(s)[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#initial-messages)

This parameter's only available if you're using **Hosted Chat**. Use it to configure the message the n8n chat interface displays when the user arrives on the page.

### Make Available in n8n Chat[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#make-available-in-n8n-chat)

Choose whether to make the agent available to Chat Hub.

#### Agent Name[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#agent-name)

The name of the agent on Chat Hub.

#### Agent description[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#agent-description)

The description of the agent on Chat Hub.

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#node-options)

-----------------------------------------------------------------------------------------------------------------

Available options depend on the chat mode.

### Hosted chat options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#hosted-chat-options)

#### Allowed Origin (CORS)[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#allowed-origin-cors)

Set the origins that can access the chat URL. Enter a comma-separated list of URLs allowed for cross-origin non-preflight requests.

Use `*` (default) to allow all origins.

#### Input Placeholder, Title, and Subtitle[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#input-placeholder-title-and-subtitle)

Enter the text for these elements in the chat interface.

View screenshot[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#view-screenshot)

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-e3cc73a9e100d90ffb30c923191c716071f09172%252Fhosted-text-elements.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1baa6b8a7c40a308770cdfb729fd3909&sv=3)

Chat widget preview showing the Input Placeholder, Title, and Subtitle text fields

#### Load Previous Session[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#load-previous-session)

Select whether to load chat messages from a previous chat session.

If you select any option other than **Off**, you must connect the Chat trigger and the Agent you're using to a memory sub-node. The memory connector on the Chat trigger appears when you set **Load Previous Session** to **From Memory**. n8n recommends connecting both the Chat trigger and Agent to the same memory sub-node, as this ensures a single source of truth for both nodes.

View screenshot[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#view-screenshot-1)

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-c0780cc740bbd31bfaa86a8ea9fb96b953df233d%252Fconnect-memory.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=643e741761391edb7f28df63d970e953&sv=3)

Connect nodes to memory

#### Response Mode[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#response-mode)

Use this option when building a workflow with steps after the agent or chain that's handling the chat. Choose from:

*   **When Last Node Finishes**: The Chat Trigger node returns the response code and the data output from the last node executed in the workflow.
    
*   **Using Response Nodes**: The Chat Trigger node responds as defined in a [Chat](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat)
     node or [Respond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
     node. In this response mode, the Chat Trigger will solely show messages as defined in these nodes and not output the data from the last node executed in the workflow. This mode replaces the 'Using Respond to Webhook Node' mode from Chat Trigger node version 1.2.
    
*   **Streaming response**: Enables real-time data streaming back to the user as the workflow processes. Requires nodes with streaming support in the workflow (for example, the [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
     node).
    

#### Require Button Click to Start Chat[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#require-button-click-to-start-chat)

Set whether to display a **New Conversation** button on the chat interface (turned on) or not (turned off).

View screenshot[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#view-screenshot-2)

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-97585362b226ac60053ac6166f794f51bd107cc3%252Fnew-conversation-button.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=85f29012fc4313f232736a9b47b1127e&sv=3)

New Conversation button

### Embedded chat options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#embedded-chat-options)

#### Allowed Origin (CORS)[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#allowed-origin-cors-1)

Set the origins that can access the chat URL. Enter a comma-separated list of URLs allowed for cross-origin non-preflight requests.

Use `*` (default) to allow all origins.

#### Load Previous Session[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#load-previous-session-1)

Select whether to load chat messages from a previous chat session.

If you select any option other than **Off**, you must connect the Chat trigger and the Agent you're using to a memory sub-node. The memory connector on the Chat trigger appears when you set **Load Previous Session** to **From Memory**. n8n recommends connecting both the Chat trigger and Agent to the same memory sub-node, as this ensures a single source of truth for both nodes.

View screenshot[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#view-screenshot-3)

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-c0780cc740bbd31bfaa86a8ea9fb96b953df233d%252Fconnect-memory.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=643e741761391edb7f28df63d970e953&sv=3)

Connect nodes to memory

#### Response Mode[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#response-mode-1)

Use this option when building a workflow with steps after the agent or chain that's handling the chat. Choose from:

*   **When Last Node Finishes**: The Chat Trigger node returns the response code and the data output from the last node executed in the workflow.
    
*   **Using Response Nodes**: The Chat Trigger node responds as defined in a [Chat](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat)
     node or [Respond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
     node. In this response mode, the Chat Trigger will solely show messages as defined in these nodes and not output the data from the last node executed in the workflow. This mode replaces the 'Using Respond to Webhook Node' mode from Chat Trigger node version 1.2.
    
*   **Streaming response**: Enables real-time data streaming back to the user as the workflow processes. Requires nodes with streaming support enabled.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.compression integration templates](https://n8n.io/integrations/chat-trigger)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#related-resources)

---------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Set the chat response manually[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#set-the-chat-response-manually)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You need to manually set the chat response when you don't want to directly send the output of an Agent or Chain node to the user. Instead, you want to take the output of an Agent or Chain node and modify it or do something else with it before sending it back to the user.

In a basic workflow, the Agent and Chain nodes output a parameter named either `output` or `text`, and the Chat trigger sends the value of this parameter to the user as the chat response.

If you need to manually create the response sent to the user, you must create a parameter named either `text` or `output`. If you use a different parameter name, the Chat trigger sends the entire object as its response, not just the value.

**Chat node**

When you are using a [Chat](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat)
 node to manually create the response sent to the user, you must set the Chat Trigger response mode to 'Using Response Nodes'.

FAQ[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#faq)

-----------------------------------------------------------------------------------------------

### How do I connect a chat interface to an n8n workflow?[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#how-do-i-connect-a-chat-interface-to-an-n8n-workflow)

Add the Chat Trigger node as the workflow's trigger, then connect an agent or chain root node to it. Every message a user sends runs the workflow, so your backend logic processes each message.

### How do I make the chat public or embed it on my site?[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#how-do-i-make-the-chat-public-or-embed-it-on-my-site)

Turn on [Make Chat Publicly Available](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#make-chat-publicly-available)
, then choose a **Mode**. **Hosted Chat** uses n8n's hosted interface with no extra setup. **Embedded Chat** lets you use n8n's [chat widget](https://www.npmjs.com/package/@n8n/chat)
 or your own interface, which calls the **Chat URL** webhook shown in the node.

### How do I set the chatbot's response from my workflow?[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#how-do-i-set-the-chatbots-response-from-my-workflow)

In a basic workflow, the Chat Trigger sends the Agent or Chain node's `output` or `text` value to the user. To customize the response, create a parameter named `text` or `output`. See [Set the chat response manually](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#set-the-chat-response-manually)
. If you use a Chat node, set **Response Mode** to **Using Response Nodes**.

Common issues[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger#common-issues)

-------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues)
.

[PreviousCompression](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues)

Last updated 10 days ago

Was this helpful?