For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai.md)
.

On n8n Cloud, you can use the OpenAI node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own OpenAI API key. Select **Use Gateway credits** in the node's credential field to run the node without an OpenAI account.

Use the OpenAI node to automate work in OpenAI and integrate OpenAI with other applications. n8n has built-in support for a wide range of OpenAI features, including creating images and assistants, as well as chatting with models.

On this page, you'll find a list of operations the OpenAI node supports and links to more resources.

**Feature availability**

The OpenAI node V2 is available from n8n 1.117.0. It supports the OpenAI Responses API, and removes support for [the Assistants API, which OpenAI has announced plans to retire](https://platform.openai.com/docs/assistants/migration)
.

From n8n 1.29.0, the OpenAI node replaces the OpenAI assistant node.

**Credentials**

Refer to [OpenAI credentials](https://docs.n8n.io/integrations/builtin/credentials/openai)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#operations)

-------------------------------------------------------------------------------------------------------

*   **Text**
    
    *   [**Generate a Chat Completion**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations#generate-a-chat-completion)
        
    *   [**Generate a Model Response**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations#generate-a-model-response)
        
    *   [**Classify Text for Violations**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations#classify-text-for-violations)
        
    
*   **Image**
    
    *   [**Analyze Image**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations#analyze-image)
        
    *   [**Generate an Image**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations#generate-an-image)
        
    *   [**Edit an Image**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations#edit-an-image)
        
    
*   **Audio**
    
    *   [**Generate Audio**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations#generate-audio)
        
    *   [**Transcribe a Recording**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations#transcribe-a-recording)
        
    *   [**Translate a Recording**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations#translate-a-recording)
        
    
*   **File**
    
    *   [**Delete a File**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations#delete-a-file)
        
    *   [**List Files**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations#list-files)
        
    *   [**Upload a File**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations#upload-a-file)
        
    
*   **Video**
    
    *   [**Generate a Video**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations#generate-video)
        
    
*   **Conversation**
    
    *   [**Create a Conversation**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations#create-a-conversation)
        
    *   [**Get a Conversation**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations#get-a-conversation)
        
    *   [**Update a Conversation**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations#update-a-conversation)
        
    *   [**Remove a Conversation**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations#remove-a-conversation)
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.openai integration templates](https://n8n.io/integrations/openai)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#related-resources)

---------------------------------------------------------------------------------------------------------------------

Refer to [OpenAI's documentation](https://beta.openai.com/docs/introduction)
 for more information about the service.

Refer to [OpenAI's assistants documentation](https://platform.openai.com/docs/assistants/how-it-works/objects)
 for more information about how assistants work.

For help dealing with rate limits, refer to [Handling rate limits](https://docs.n8n.io/integrations/builtin/handle-rate-limits)
.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Using tools with OpenAI assistants[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#using-tools-with-openai-assistants)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Some operations allow you to connect tools. [Tools](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
 act like addons that your AI can use to access extra context or resources.

Select the **Tools** connector to browse the available tools and add them.

Once you add a tool connection, the OpenAI node becomes a root node, allowing it to form a cluster node with the tools sub-nodes. See [Node types](https://docs.n8n.io/integrations/builtin/node-types#cluster-nodes)
 for more information on cluster nodes and root nodes.

### Operations that support tool connectors[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#operations-that-support-tool-connectors)

*   **Text**
    
    *   [**Generate a Chat Completion**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations#generate-a-chat-completion)
        
    *   [**Generate a Model Response**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations#generate-a-model-response)
        
    

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai#common-issues)

-------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues)
.

[PreviousOnfleet](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet)
[NextAssistant operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations)

Last updated 10 days ago

Was this helpful?