For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai.md)
.

On n8n Cloud, you can use the OpenAI Chat Model node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own OpenAI API key. Select **Use Gateway credits** in the node's credential field to run the node without an OpenAI account.

Use the OpenAI Chat Model node to use OpenAI's chat models with conversational agents.

On this page, you'll find the node parameters for the OpenAI Chat Model node and links to more resources.

**Credentials**

Refer to the [OpenAI credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/openai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#model)

Select the model to use to generate the completion.

n8n dynamically loads models from OpenAI, and you'll only see the models available to your account.

### Use Responses API[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#use-responses-api)

OpenAI provides two endpoints for generating output from a model:

*   **Chat Completions**: The Chat Completions API endpoint generates a model response from a list of messages that comprise a conversation. The API requires the user to handle conversation state manually, for example by adding a [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)
     subnode. For new projects, OpenAI recommends to use the Responses API.
    
*   **Responses**: The Responses API is an agentic loop, allowing the model to call multiple built-in tools within the span of one API request. It also supports persistent conversations by passing a `conversation_id`.
    

Toggle to **Use Responses API** if you want the model to generate output using the Responses API. Otherwise, the OpenAI Chat Model node will default to using the Chat Completions API.

Refer to the OpenAI documentation for a [comparison of the Chat Completions and Responses APIs](https://platform.openai.com/docs/guides/migrate-to-responses)
.

### Built-in Tools[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#built-in-tools)

The OpenAI Responses API provides a range of [built-in tools](https://platform.openai.com/docs/guides/tools)
 to enrich the model's response. Toggle to **Use Responses API** if you want the model to have access to the following built-in tools:

*   **Web Search**: Allows models to search the web for the latest information before generating a response.
    
*   **File Search**: Allow models to search your knowledgebase from previously uploaded files for relevant information before generating a response. Refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/tools-file-search)
     for more information.
    
*   **Code Interpreter**: Allows models to write and run Python code in a sandboxed environment.
    

**Use with AI Agent node**

Built-in tools are only supported when using the OpenAI Chat Model node in combination with the AI Agent node. Built-in tools aren't available when using the OpenAI Chat Model node in combination with a Basic LLM Chain node, for example.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#node-options)

-------------------------------------------------------------------------------------------------------------------------------

Use these options to further refine the node's behavior. The following options are available whether you use the Responses API to generate model output or not.

### Frequency Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#frequency-penalty)

Use this option to control the chances of the model repeating itself. Higher values reduce the chance of the model repeating itself.

### Maximum Number of Tokens[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#maximum-number-of-tokens)

Enter the maximum number of tokens used, which sets the completion length.

### Presence Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#presence-penalty)

Use this option to control the chances of the model talking about new topics. Higher values increase the chance of the model talking about new topics.

### Sampling Temperature[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#sampling-temperature)

Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.

### Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#timeout)

Enter the maximum request time in milliseconds.

### Max Retries[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#max-retries)

Enter the maximum number of times to retry a request.

### Top P[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#top-p)

Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.

Additional node options (Responses API only)[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#additional-node-options-responses-api-only)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following, additional options are available when toggling to **Use Responses API**.

### Conversation ID[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#conversation-id)

The conversation that this response belongs to. Input items and output items from this response are automatically added to this conversation after this response completes.

### Prompt Cache Key[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#prompt-cache-key)

Use this key for caching similar requests to optimize cache hit rates.

### Safety Identifier[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#safety-identifier)

Apply an identifier to track users who may violate usage policies.

### Service Tier[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#service-tier)

Select the service tier that fits your needs: Auto, Flex, Default, or Priority.

### Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#metadata)

A set of key-value pairs for storing structured information. You can attach up to 16 pairs to an object, which is useful for adding custom data that can be used for searching by the API or in the dashboard.

### Top Logprobs[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#top-logprobs)

Define an integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability.

### Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#output-format)

Choose a response format: Text, JSON Schema, or JSON Object. Use of JSON Schema is recommended, if you want to receive data in JSON format.

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#prompt)

Configure the prompt filled with a unique ID, its version, and substitutable variables. Prompts are configured through the OpenAI dashboard.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.lmchatopenai integration templates](https://n8n.io/integrations/openai-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's OpenAI documentation](https://docs.langchain.com/oss/javascript/integrations/chat/openai)
 for more information about the service.

Refer to [OpenAI documentation](https://platform.openai.com/docs/api-reference/responses/create)
 for more information about the parameters.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai#common-issues)

---------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues)
.

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues)

Last updated 10 days ago

Was this helpful?