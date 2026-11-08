For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md)
.

On n8n Cloud, you can use the Qwen Cloud Chat Model node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own Qwen Cloud API key. Select **Use Gateway credits** in the node's credential field to run the node without a Qwen Cloud account.

The Qwen Cloud Chat Model node sends chat prompts to conversational models available on Qwen Cloud, for advanced AI chains and LangChain integrations. Use it to generate conversational responses, integrate model outputs into workflows, or run prompts with custom sampling, retry, and timeout settings.

**Credentials**

Refer to the [Qwen Cloud credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/alibaba)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Operations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud#operations)

---------------------------------------------------------------------------------------------------------------------------------

### Generate chat response[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud#generate-chat-response)

Generate a chat-style response from the selected Qwen Cloud model.

**Parameters**

*   **Model** (type: _options_, field: `model`): The model that generates the completion. Learn more about available models on Qwen Cloud: [Choose models](https://docs.qwencloud.com/developer-guides/getting-started/model-selection)
    .
    

**Options**

*   **Frequency Penalty** (type: _number_, field: `frequencyPenalty`): Positive values penalize new tokens based on how often they appear so far, decreasing the model's likelihood to repeat the same line verbatim. Default: `0`.
    
*   **Maximum Number of Tokens** (type: _number_, field: `maxTokens`): The maximum number of tokens to generate in the completion. The limit depends on the selected model. A value of minus one uses the model's default limit. Default: `-1`.
    
*   **Response Format** (type: _options_, field: `responseFormat`): The output format returned by the node, for example plain text or structured formats. Default: text.
    
*   **Presence Penalty** (type: _number_, field: `presencePenalty`): Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to discuss new topics. Default: `0`.
    
*   **Sampling Temperature** (type: _number_, field: `temperature`): Control randomness. Lower values make output less random, near zero is deterministic. Default: `0.7`.
    
*   **Timeout** (type: _number_, field: `timeout`): Maximum time (in milliseconds) allowed for a request before it's aborted. Default: `360000`.
    
*   **Max Retries** (type: _number_, field: `maxRetries`): Maximum number of retry attempts for failed requests. Default: `2`.
    
*   **Top P** (type: _number_, field: `topP`): Nucleus sampling parameter that controls diversity. 0.5 means half of the probability mass is considered. Adjust **Top P** or **Sampling Temperature**, but not both. Default: `1`.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Qwen Cloud Chat Model node documentation integration templates](https://n8n.io/integrations/alibaba-cloud-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Choose models](https://docs.qwencloud.com/developer-guides/getting-started/model-selection)
 for more information about available models and their capabilities.

[PreviousEmbeddings Oracle Database](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb)
[NextAnthropic Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic)

Last updated 10 days ago

Was this helpful?