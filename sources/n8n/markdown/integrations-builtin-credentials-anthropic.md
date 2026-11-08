For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/anthropic.md)
.

On n8n Cloud, you can skip setting up Anthropic credentials by selecting **Use Gateway credits** in the credential field of nodes that support it. Refer to [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 for details.

You can use these credentials to authenticate the following nodes:

*   [Anthropic](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic)
    
*   [Anthropic Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/anthropic#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/anthropic#related-resources)

------------------------------------------------------------------------------------------------------

Refer to [Anthropic's documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/anthropic#using-api-key)

----------------------------------------------------------------------------------------------

To configure this credential, you'll need an [Anthropic Console account](https://console.anthropic.com/)
 with access to Claude.

Then:

1.  In the Anthropic Console, open **Settings >** [**API Keys**](https://console.anthropic.com/settings/keys)
    .
    
2.  Select **\+ Create Key**.
    
3.  Give your key a **Name**, like `n8n-integration`.
    
4.  Select **Copy Key** to copy the key.
    
5.  Enter this as the **API Key** in your n8n credential.
    
6.  (Optional) To add custom headers to your API requests:
    
    1.  Enable the **Add Custom Header** toggle.
        
    2.  Enter the **Header Name** for your custom header.
        
    3.  Enter the **Header Value** for your custom header.
        
    

Refer to Anthropic's [Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude)
 and [Quickstart](https://docs.anthropic.com/en/docs/quickstart)
 for more information.

[PreviousAMQP credentials](https://docs.n8n.io/integrations/builtin/credentials/amqp)
[NextAPITemplate.io credentials](https://docs.n8n.io/integrations/builtin/credentials/apitemplateio)

Last updated 10 days ago

Was this helpful?