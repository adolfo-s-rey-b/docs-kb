For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md)
.

Use the Basic LLM Chain node to set the prompt that the model will use along with setting an optional parser for the response.

On this page, you'll find the node parameters for the Basic LLM Chain node and links to more resources.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Basic LLM Chain integrations](https://n8n.io/integrations/basic-llm-chain/)
 page.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#prompt)

Select how you want the node to construct the prompt (also known as the user's query or input from the chat).

Choose from:

*   **Take from previous node automatically**: If you select this option, the node expects an input from a previous node called `chatInput`.
    
*   **Define below**: If you select this option, provide either static text or an expression for dynamic content to serve as the prompt in the **Prompt (User Message)** field.
    

### Require Specific Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#require-specific-output-format)

This parameter controls whether you want the node to require a specific output format. When turned on, n8n prompts you to connect one of these output parsers to the node:

*   [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
    
*   [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
    
*   [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
    

Chat Messages[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#chat-messages)

------------------------------------------------------------------------------------------------------------------------------

Use **Chat Messages** when you're using a chat model to set a message.

n8n ignores these options if you don't connect a chat model. Select the **Type Name or ID** you want the node to use:

#### AI[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#ai)

Enter a sample expected response in the **Message** field. The model will try to respond in the same way in its messages.

#### System[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#system)

Enter a system **Message** to include with the user input to help guide the model in what it should do.

Use this option for things like defining tone, for example: `Always respond talking like a pirate`.

#### User[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#user)

Enter a sample user input. Using this with the AI option can help improve the output of the agent. Using both together provides a sample of an input and expected response (the **AI Message**) for the model to follow.

Select one of these input types:

*   **Text**: Enter a sample user input as a text **Message**.
    
*   **Image (Binary)**: Select a binary input from a previous node. Enter the **Image Data Field Name** to identify which binary field from the previous node contains the image data.
    
*   **Image (URL)**: Use this option to feed an image in from a URL. Enter the **Image URL**.
    

For both the **Image** types, select the **Image Details** to control how the model processes the image and generates its textual understanding. Choose from:

*   **Auto**: The model uses the auto setting, which looks at the image input size and decide if it should use the Low or High setting.
    
*   **Low**: The model receives a low-resolution 512px x 512px version of the image and represents the image with a budget of 65 tokens. This allows the API to return faster responses and consume fewer input tokens. Use this option for use cases that don't require high detail.
    
*   **High**: The model can access the low-resolution image and then creates detailed crops of input images as 512px squares based on the input image size. Each of the detailed crops uses twice the token budget (65 tokens) for a total of 129 tokens. Use this option for use cases that require high detail.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Basic LLM Chain node documentation integration templates](https://n8n.io/integrations/basic-llm-chain)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's models documentation](https://docs.langchain.com/oss/javascript/langchain/models)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#common-issues)

------------------------------------------------------------------------------------------------------------------------------

Here are some common errors and issues with the Basic LLM Chain node and steps to resolve or troubleshoot them.

### No prompt specified error[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm#no-prompt-specified-error)

This error displays when the **Prompt** is empty or invalid.

You might see this error in one of two scenarios:

1.  When you've set the **Prompt** to **Define below** and haven't entered anything in the **Text** field.
    
    *   To resolve, enter a valid prompt in the **Text** field.
        
    
2.  When you've set the **Prompt** to **Connected Chat Trigger Node** and the incoming data has no field called `chatInput`.
    
    *   The node expects the `chatInput` field. If your previous node doesn't have this field, add an [Edit Fields (Set)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         node to edit an incoming field name to `chatInput`.
        
    

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
[NextQuestion and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)

Last updated 10 days ago

Was this helpful?