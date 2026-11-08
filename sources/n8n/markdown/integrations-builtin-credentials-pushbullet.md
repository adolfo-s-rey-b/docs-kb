For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/pushbullet.md)
.

You can use these credentials to authenticate the following nodes:

*   [Pushbullet](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/pushbullet#prerequisites)

-----------------------------------------------------------------------------------------------

Create a [Pushbullet](https://www.pushbullet.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/pushbullet#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/pushbullet#related-resources)

-------------------------------------------------------------------------------------------------------

Refer to [Pushbullet's API documentation](https://docs.pushbullet.com/)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/pushbullet#using-oauth2)

---------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated when you create a Pushbullet app, also known as an OAuth client.
    
*   A **Client Secret**: Generated when you create a Pushbullet app, also known as an OAuth client.
    

To generate the **Client ID** and **Client Secret**, go to the [create client](https://www.pushbullet.com/create-client)
 page. Copy the **OAuth Redirect URL** from n8n and add this as your **redirect\_uri** for the app/client. Use the **client\_id** and **client\_secret** from the OAuth Client in your n8n credential.

Refer to Pushbullet's [OAuth2 Guide](https://docs.pushbullet.com/#oauth2)
 for more information.

**Pushbullet OAuth test link**

Pushbullet offers a test link during the client creation process described above. This link isn't compatible with n8n. To verify the authentication works, use the **Connect my account** button in n8n.

[PreviousProfitWell credentials](https://docs.n8n.io/integrations/builtin/credentials/profitwell)
[NextPushcut credentials](https://docs.n8n.io/integrations/builtin/credentials/pushcut)

Last updated 10 days ago

Was this helpful?