For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/bitwarden.md)
.

You can use these credentials to authenticate the following node:

*   [Bitwarden](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bitwarden)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/bitwarden#prerequisites)

----------------------------------------------------------------------------------------------

Create a [Bitwarden](https://vault.bitwarden.com/#/register?org=teams)
 Teams organization or Enterprise organization account. (Bitwarden only makes the Bitwarden Public API available for these [organization](https://bitwarden.com/help/about-organizations/)
 plans.)

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/bitwarden#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/bitwarden#related-resources)

------------------------------------------------------------------------------------------------------

Refer to [Bitwarden's Public API documentation](https://bitwarden.com/help/public-api/)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/bitwarden#using-api-key)

----------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Provided when you generate an API key
    
*   A **Client Secret**: Provided when you generate an API key
    
*   The **Environment**:
    
    *   Choose **Cloud-hosted** if you don't self-host Bitwarden. No further configuration required.
        
    *   Choose **Self-hosted** if you host Bitwarden on your own server. Enter your **Self-hosted domain** in the appropriate field.
        
    

The Client ID and Client Secret must be for an **Organization API Key**, not a Personal API Key. Refer to the [Bitwarden Public API Authentication documentation](https://bitwarden.com/help/public-api/#authentication)
 for instructions on generating an Organization API Key.

[PreviousBitly credentials](https://docs.n8n.io/integrations/builtin/credentials/bitly)
[NextBox credentials](https://docs.n8n.io/integrations/builtin/credentials/box)

Last updated 10 days ago

Was this helpful?