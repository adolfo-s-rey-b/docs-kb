For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/lemonade.md)
.

You can use these credentials to authenticate the following nodes:

*   [Lemonade Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade)
    
*   [Lemonade Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade)
    
*   [Embeddings Lemonade](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/lemonade#prerequisites)

---------------------------------------------------------------------------------------------

Lemonade runs AI inference locally. These nodes connect directly to a Lemonade server process running on your machine or network. [Install and run Lemonade server](https://lemonade-server.ai/install_options.html)
 before creating credentials in n8n.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/lemonade#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   Lemonade server connection
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/lemonade#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Lemonade's documentation](https://lemonade-server.ai/docs/)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Configuring Lemonade server connection[](https://docs.n8n.io/integrations/builtin/credentials/lemonade#configuring-lemonade-server-connection)

-----------------------------------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   **Base URL**: The URL of your Lemonade server, including the API path. The default for a local installation is `http://localhost:8000/api/v1`. If you're running n8n in Docker, use `http://host.docker.internal:8000/api/v1` instead. If your Lemonade server is on a remote machine, replace `localhost` with the server's address.
    
*   **API key** (optional): Optional API key for Lemonade server authentication. This isn't required for default Lemonade installation.
    

[PreviousLemlist credentials](https://docs.n8n.io/integrations/builtin/credentials/lemlist)
[NextLine credentials](https://docs.n8n.io/integrations/builtin/credentials/line)

Last updated 10 days ago

Was this helpful?