For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/misp.md)
.

You can use these credentials to authenticate the following nodes:

*   [MISP](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/misp#prerequisites)

-----------------------------------------------------------------------------------------

Install and run a [MISP](https://misp.github.io/MISP/)
 instance.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/misp#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/misp#related-resources)

-------------------------------------------------------------------------------------------------

Refer to [MISP's Automation API documentation](https://www.circl.lu/doc/misp/automation)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/misp#using-api-key)

-----------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: In MISP, these are called Automation keys. Get an automation key from **Event Actions > Automation**. Refer to [MISP's automation keys documentation](https://www.circl.lu/doc/misp/automation/#automation-key)
     for instructions on generating more keys.
    
*   A **Base URL**: Your MISP URL.
    
*   Select whether to **Allow Unauthorized Certificates**: If turned on, the credential will connect even if SSL certificate validation fails.
    

[PreviousMiro credentials](https://docs.n8n.io/integrations/builtin/credentials/miro)
[NextMist credentials](https://docs.n8n.io/integrations/builtin/credentials/mist)

Last updated 10 days ago

Was this helpful?