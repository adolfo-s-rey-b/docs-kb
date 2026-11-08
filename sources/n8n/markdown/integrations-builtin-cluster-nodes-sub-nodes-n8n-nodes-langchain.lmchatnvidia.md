For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md)
.

Use the NVIDIA Nemotron Chat Model node to access [NVIDIA Nemotron](https://build.nvidia.com/models)
 models with conversational agents. The node works with Nemotron models hosted on [build.nvidia.com](https://build.nvidia.com/)
 and with self-hosted NVIDIA Inference Microservices (NIM).

On this page, you'll find the node parameters for the NVIDIA Nemotron Chat Model node and links to more resources.

**Credentials**

Refer to the [NVIDIA Nemotron credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/nvidia)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#model)

Select the Nemotron model to use to generate the completion.

n8n dynamically loads Nemotron models from the endpoint configured in your credential. If n8n can't reach the endpoint, it falls back to a curated list of well-known Nemotron model IDs.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#node-options)

-------------------------------------------------------------------------------------------------------------------------------

Use these options to further refine the node's behavior.

### Frequency Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#frequency-penalty)

Use this option to control the chances of the model repeating itself. Higher values reduce the chance of the model repeating itself.

### Maximum Number of Tokens[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#maximum-number-of-tokens)

Enter the maximum number of tokens used, which sets the completion length. Use `-1` for the model default.

### Response Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#response-format)

Choose **Text** or **JSON**. **JSON** ensures the model returns valid JSON. When you choose **JSON**, include the word `json` in your prompt in the chain or agent.

### Presence Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#presence-penalty)

Use this option to control the chances of the model talking about new topics. Higher values increase the chance of the model talking about new topics.

### Sampling Temperature[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#sampling-temperature)

Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.

### Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#timeout)

Enter the maximum request time in milliseconds.

### Max Retries[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#max-retries)

Enter the maximum number of times to retry a request.

### Top P[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#top-p)

Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------

[Browse NVIDIA Nemotron Chat Model node documentation integration templates](https://n8n.io/integrations/nvidia-nemotron-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

Refer to [NVIDIA's build catalogue](https://build.nvidia.com/models)
 for the list of Nemotron models and to the [NIM documentation](https://docs.nvidia.com/nim/)
 for guidance on self-hosting. As the NVIDIA API is OpenAI-spec compatible, you can refer to [LangChain's OpenAI documentation](https://docs.langchain.com/oss/javascript/integrations/chat/openai)
 for more information about the underlying client.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMoonshot Kimi Chat Model node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot)
[NextOllama Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama)

Last updated 10 days ago

Was this helpful?