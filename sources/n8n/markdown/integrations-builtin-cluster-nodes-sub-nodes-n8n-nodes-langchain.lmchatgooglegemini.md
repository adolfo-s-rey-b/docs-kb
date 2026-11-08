For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md)
.

On n8n Cloud, you can use the Google Gemini Chat Model node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own Google API key. Select **Use Gateway credits** in the node's credential field to run the node without a Google account.

Use the Google Gemini Chat Model node to use Google's Gemini chat models with conversational agents.

On this page, you'll find the node parameters for the Google Gemini Chat Model node, and links to more resources.

**Credentials**

Refer to the [Google Gemini(PaLM) credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/googleai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the completion.
    

n8n dynamically loads models from the Google Gemini API and you'll only see the models available to your account.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Top K**: Enter the number of token choices the model uses to generate the next token.
    
*   **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.
    
*   **Safety Settings**: Gemini supports adjustable safety settings. Refer to Google's [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini)
     for information on the available filters and levels.
    

Limitations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#limitations)

-----------------------------------------------------------------------------------------------------------------------------------

### No proxy support[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#no-proxy-support)

The Google Gemini Chat Model node uses Google's SDK, which doesn't support proxy configuration.

If you need to proxy your connection, as a work around, you can set up a dedicated reverse proxy for Gemini requests and change the **Host** parameter in your [Google Gemini credentials](https://docs.n8n.io/integrations/builtin/credentials/googleai)
 to point to your proxy address:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-b51eec14660518e3ecc3ee6a00f4252f929bbd76%252Fgoogle-gemini-proxy-config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ed6dcfd6299fb50a1424ef8df81e2e64&sv=3)

Google Gemini credentials proxy configuration

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Google Gemini Chat Model node documentation integration templates](https://n8n.io/integrations/google-gemini-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Google Gemini documentation](https://docs.langchain.com/oss/javascript/integrations/chat/google_generative_ai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousDeepSeek Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek)
[NextGoogle Vertex Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex)

Last updated 10 days ago

Was this helpful?