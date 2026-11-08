For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/alibaba.md)
.

On n8n Cloud, you can skip setting up Qwen Cloud credentials by selecting **Use Gateway credits** in the credential field of nodes that support it. Refer to [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 for details.

You can use these credentials to authenticate the following nodes:

*   [Qwen Cloud](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud)
    
*   [Qwen Cloud Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/alibaba#prerequisites)

--------------------------------------------------------------------------------------------

Create a [Qwen Cloud](https://qwencloud.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/alibaba#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/alibaba#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Qwen Cloud API key documentation](https://docs.qwencloud.com/developer-guides/administration/api-keys)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/alibaba#using-api-key)

--------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**
    

1.  Sign in to [Qwen Cloud](https://qwencloud.com/)
    .
    
2.  Go to **API Keys**.
    
3.  Use the workspace switcher at the bottom of the sidebar to select the workspace where you want to create the key.
    
4.  Select **Create API key**.
    
5.  Enter a description, then select **Generate Key**.
    
6.  Copy the API key. It displays only once.
    
7.  Enter the API key in your n8n credential.
    
8.  For Qwen Cloud accounts, set **Region** to **Singapore**. Select another region only if you're using Alibaba Cloud Model Studio.
    

Refer to [Qwen Cloud API key documentation](https://docs.qwencloud.com/developer-guides/administration/api-keys)
 for more information.

[PreviousAirtop credentials](https://docs.n8n.io/integrations/builtin/credentials/airtop)
[NextAlienVault credentials](https://docs.n8n.io/integrations/builtin/credentials/alienvault)

Last updated 10 days ago

Was this helpful?