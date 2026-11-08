For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/matrix.md)
.

You can use these credentials to authenticate the following nodes:

*   [Matrix](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/matrix#prerequisites)

-------------------------------------------------------------------------------------------

Create an account on a [Matrix](https://matrix.org/)
 server. Refer to [Creating an account](https://matrix.org/docs/chat_basics/matrix-for-im/#creating-a-matrix-account)
 for more information.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/matrix#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API access token
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/matrix#related-resources)

---------------------------------------------------------------------------------------------------

Refer to the [Matrix Specification](https://spec.matrix.org/latest/)
 for more information about the service.

Refer to the documentation for the specific client you're using to access the Matrix server.

Using API access token[](https://docs.n8n.io/integrations/builtin/credentials/matrix#using-api-access-token)

-------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **Access Token**: This token is tied to the account you use to log into Matrix with.
    
*   A **Homeserver URL**: This is the URL of the [homeserver](https://matrix.org/docs/matrix-concepts/elements-of-matrix/#homeserver)
     you entered when you created your account. n8n prepopulates this with matrix.org's own server; adjust this if you're using a server hosted elsewhere.
    

Instructions for getting these details vary depending on the client you're using to access the server. Both the **Access Token** and the **Homeserver URL** can most commonly be found in **Settings > Help & About > Advanced**, but refer to your client's documentation for more details.

[PreviousMarketstack credentials](https://docs.n8n.io/integrations/builtin/credentials/marketstack)
[NextMattermost credentials](https://docs.n8n.io/integrations/builtin/credentials/mattermost)

Last updated 10 days ago

Was this helpful?