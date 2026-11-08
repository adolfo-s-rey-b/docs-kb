For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md)
.

Use the DeepSeek Chat Model node to use DeepSeek's chat models with conversational agents.

On this page, you'll find the node parameters for the DeepSeek Chat Model node and links to more resources.

**Credentials**

Refer to the [DeepSeek credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/deepseek)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#model)

Select the model to use to generate the completion.

n8n dynamically loads models from DeepSeek and you'll only see the models available to your account.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#node-options)

---------------------------------------------------------------------------------------------------------------------------------

Use these options to further refine the node's behavior.

### Base URL[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#base-url)

Enter a URL here to override the default URL for the API.

### Frequency Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#frequency-penalty)

Use this option to control the chances of the model repeating itself. Higher values reduce the chance of the model repeating itself.

### Maximum Number of Tokens[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#maximum-number-of-tokens)

Enter the maximum number of tokens used, which sets the completion length.

### Response Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#response-format)

Choose **Text** or **JSON**. **JSON** ensures the model returns valid JSON.

### Presence Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#presence-penalty)

Use this option to control the chances of the model talking about new topics. Higher values increase the chance of the model talking about new topics.

### Sampling Temperature[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#sampling-temperature)

Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.

### Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#timeout)

Enter the maximum request time in milliseconds.

### Max Retries[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#max-retries)

Enter the maximum number of times to retry a request.

### Top P[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#top-p)

Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[Browse DeepSeek Chat Model node documentation integration templates](https://n8n.io/integrations/deepseek-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------

As DeepSeek is API-compatible with OpenAI, you can refer to [LangChain's OpenAI documentation](https://docs.langchain.com/oss/javascript/integrations/chat/openai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousDatabricks Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks)
[NextGoogle Gemini Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini)

Last updated 10 days ago

Was this helpful?