For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/openai.md)
.

On n8n Cloud, you can skip setting up OpenAI credentials by selecting **Use Gateway credits** in the credential field of nodes that support it. Refer to [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 for details.

You can use these credentials to authenticate the following nodes:

*   [OpenAI](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai)
    
*   [Chat OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai)
    
*   [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai)
    
*   [LM OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/openai#prerequisites)

-------------------------------------------------------------------------------------------

Create an [OpenAI](https://platform.openai.com/signup/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/openai#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/openai#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [OpenAI's API documentation](https://platform.openai.com/docs/introduction)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/openai#using-api-key)

-------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**
    
*   An **Organization ID**: Required if you belong to multiple organizations; otherwise, leave this blank.
    

To generate your API Key:

1.  Log in to your OpenAI account or [create](https://platform.openai.com/signup/)
     an account.
    
2.  Open your [API keys](https://platform.openai.com/api-keys)
     page.
    
3.  Select **Create new secret key** to create an API key, optionally naming the key.
    
4.  Copy your key and add it as the **API Key** in n8n.
    

Refer to the [API Quickstart Account Setup documentation](https://platform.openai.com/docs/quickstart/account-setup)
 for more information.

To find your Organization ID:

1.  Go to your [Organization Settings](https://platform.openai.com/account/organization)
     page.
    
2.  Copy your Organization ID and add it as the **Organization ID** in n8n.
    

Refer to [Setting up your organization](https://platform.openai.com/docs/guides/production-best-practices/setting-up-your-organization)
 for more information. Note that API requests made using an Organization ID will count toward the organization's subscription quota.

[PreviousOnfleet credentials](https://docs.n8n.io/integrations/builtin/credentials/onfleet)
[NextOpenCTI credentials](https://docs.n8n.io/integrations/builtin/credentials/opencti)

Last updated 10 days ago

Was this helpful?