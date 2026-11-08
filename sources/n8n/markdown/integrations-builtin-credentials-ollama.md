For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/ollama.md)
.

You can use these credentials to authenticate the following nodes:

*   [Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama)
    
*   [Chat Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama)
    
*   [Embeddings Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/ollama#prerequisites)

-------------------------------------------------------------------------------------------

Create and run an [Ollama](https://ollama.com/)
 instance with one user. Refer to the Ollama [Quick Start](https://github.com/ollama/ollama/blob/main/README.md#quickstart)
 for more information.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/ollama#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   Instance URL
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/ollama#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Ollama's API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using instance URL[](https://docs.n8n.io/integrations/builtin/credentials/ollama#using-instance-url)

-----------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   The **Base URL** of your Ollama instance or remote authenticated Ollama instances.
    
*   (Optional) The **API Key** for Bearer token authentication if connecting to a remote, authenticated proxy.
    

The default **Base URL** is `http://localhost:11434`, but if you've set the `OLLAMA_HOST` environment variable, enter that value. If you have issues connecting to a local n8n server, try `127.0.0.1` instead of `localhost`.

If you're connecting to Ollama through authenticated proxy services (such as [Open WebUI](https://docs.openwebui.com/getting-started/api-endpoints/#-ollama-api-proxy-support)
) you must include an API key. If you don't need authentication, leave this field empty. When provided, the API key is sent as a Bearer token in the `Authorization` header of the request to the Ollama API.

Refer to [How do I configure Ollama server?](https://github.com/ollama/ollama/blob/main/docs/faq.mdx#how-do-i-configure-ollama-server)
 for more information.

### Ollama and self-hosted n8n[](https://docs.n8n.io/integrations/builtin/credentials/ollama#ollama-and-self-hosted-n8n)

If Ollama and n8n run in separate Docker containers, connect both containers to the same user-defined bridge network. Set **Base URL** to `http://<ollama-container>:11434`. Replace `<ollama-container>` with your Ollama container's name. For example, for a container with the name `ollama`, use `http://ollama:11434`.

For the setup steps, refer to [Ollama Chat Model node common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#if-ollama-and-n8n-are-running-in-separate-docker-containers)
.

[PreviousOkta credentials](https://docs.n8n.io/integrations/builtin/credentials/okta)
[NextOne Simple API credentials](https://docs.n8n.io/integrations/builtin/credentials/onesimpleapi)

Last updated 10 days ago

Was this helpful?