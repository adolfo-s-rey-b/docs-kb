For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/msg91.md)
.

You can use these credentials to authenticate the following nodes:

*   [MSG91](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.msg91)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/msg91#prerequisites)

------------------------------------------------------------------------------------------

Create a [MSG91](https://msg91.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/msg91#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/msg91#related-resources)

--------------------------------------------------------------------------------------------------

Refer to [MSG91's API documentation](https://docs.msg91.com/overview)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/msg91#using-api-key)

------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **Authentication Key**: To get your Authentication Key, go to the user menu and select **Authkey**. Refer to MSG91's [Where can I find my authentication key? documentation](https://msg91.com/help/api/where-can-i-find-my-authentication-ke)
     for more information.
    

IP Security[](https://docs.n8n.io/integrations/builtin/credentials/msg91#ip-security)

--------------------------------------------------------------------------------------

MSG91 enables [IP Security](https://msg91.com/help/api/what-do-you-mean-by-api-security)
 by default for authkeys.

For the n8n credentials to function with this setting enabled, add all the [n8n IP addresses](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses)
 as whitelisted IPs in MSG91. You can add them in one of two places, depending on your desired security level:

*   To allow any/all authkeys in the account to work with n8n, add the n8n IP addresses in the **Company's whitelisted IPs** section of the **Authkey** page.
    
*   To allow only specific authkeys to work with n8n, add the n8n IP addresses in the **Whitelisted IPs** section of an authkey's details.
    

[PreviousMQTT credentials](https://docs.n8n.io/integrations/builtin/credentials/mqtt)
[NextMySQL credentials](https://docs.n8n.io/integrations/builtin/credentials/mysql)

Last updated 10 days ago

Was this helpful?