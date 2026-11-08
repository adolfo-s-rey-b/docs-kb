For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/paddle.md)
.

You can use these credentials to authenticate the following nodes:

*   [Paddle](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.paddle)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/paddle#prerequisites)

-------------------------------------------------------------------------------------------

Create a [Paddle](https://paddle.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/paddle#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API access token (Classic)
    

**Paddle Classic API**

This credential works with Paddle Classic's API. If you joined Paddle after August 2023, you're using the [Paddle Billing API](https://developer.paddle.com/api-reference/overview)
 and this credential may not work for you.

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/paddle#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Paddle Classic's API documentation](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference)
 for more information about the service.

Using API access token (Classic)[](https://docs.n8n.io/integrations/builtin/credentials/paddle#using-api-access-token-classic)

-------------------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Vendor Auth Code**: Created when you generate an API key.
    
*   A **Vendor ID**: Displayed when you generate an API key.
    
*   **Use Sandbox Environment API**: When turned on, nodes using this credential will hit the Sandbox API endpoint instead of the live API endpoint.
    

To generate an auth code and view your Vendor ID, go to **Paddle > Developer Tools > Authentication > Generate Auth Code**. Select **Reveal Auth Code** to display the Auth Code. Refer to [API Authentication](https://developer.paddle.com/api-reference/about/authentication)
 for more information.

[PreviousOura credentials](https://docs.n8n.io/integrations/builtin/credentials/oura)
[NextPagerDuty credentials](https://docs.n8n.io/integrations/builtin/credentials/pagerduty)

Last updated 10 days ago

Was this helpful?