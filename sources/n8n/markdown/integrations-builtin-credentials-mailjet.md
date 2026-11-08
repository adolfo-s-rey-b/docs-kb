For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/mailjet.md)
.

You can use these credentials to authenticate the following nodes:

*   [Mailjet](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailjet)
    
*   [Mailjet Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/mailjet#prerequisites)

--------------------------------------------------------------------------------------------

Create a [Mailjet](https://www.mailjet.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/mailjet#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   Email API key: For use with Mailjet's Email API
    
*   SMS token: For use with Mailjet's SMS API
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/mailjet#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Mailjet's Email API documentation](https://dev.mailjet.com/email/guides/)
 and [Mailjet's SMS API documentation](https://dev.mailjet.com/guides-sms/)
 for more information about each service.

Using Email API key[](https://docs.n8n.io/integrations/builtin/credentials/mailjet#using-email-api-key)

--------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: View and generate API keys in your Mailjet [API Key Management](https://app.mailjet.com/signin)
     page.
    
*   A **Secret Key**: View your API Secret Keys in your Mailjet [API Key Management](https://app.mailjet.com/signin)
     page.
    
*   _Optional:_ Select whether to use **Sandbox Mode** for calls made using this credential. When turned on, all API calls use Sandbox mode: the API will still validate the payloads but won't deliver the actual messages. This can be useful to troubleshoot any payload error messages without actually sending messages. Refer to Mailjet's [Sandbox Mode documentation](https://dev.mailjet.com/email/guides/send-api-v31/#sandbox-mode)
     for more information.
    

For this credential, you can use either:

*   Mailjet's primary API key and secret key
    
*   A subaccount API key and secret key
    

Refer to Mailjet's [How to create a subaccount (or additional API key) documentation](https://documentation.mailjet.com/hc/en-us/articles/360042561974-How-to-create-a-subaccount-or-additional-API-Key)
 for detailed instructions on creating more API keys. Refer to [What are subaccounts and how does it help me?](https://documentation.mailjet.com/hc/en-us/articles/360042561854-What-are-subaccounts-and-how-does-it-help-me)
 page for more information on Mailjet subaccounts and when you might want to use one.

Using SMS Token[](https://docs.n8n.io/integrations/builtin/credentials/mailjet#using-sms-token)

------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An access **Token**: Generate a new token from Mailjet's [SMS Dashboard](https://app.mailjet.com/sms)
    .
    

[PreviousMailgun credentials](https://docs.n8n.io/integrations/builtin/credentials/mailgun)
[NextMalcore credentials](https://docs.n8n.io/integrations/builtin/credentials/malcore)

Last updated 10 days ago

Was this helpful?