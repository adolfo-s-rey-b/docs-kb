For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/webhook.md)
.

You can use these credentials to authenticate the following nodes:

*   [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/webhook#prerequisites)

--------------------------------------------------------------------------------------------

You must use the authentication method required by the app or service you want to query.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/webhook#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    
*   Header auth
    
*   JWT auth
    
*   None
    

### Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/webhook#using-basic-auth)

Use this generic authentication if your app or service supports basic authentication.

To configure this credential, enter:

*   The **Username** you use to access the app or service your HTTP Request is targeting
    
*   The **Password** that goes with that username
    

### Using header auth[](https://docs.n8n.io/integrations/builtin/credentials/webhook#using-header-auth)

Use this generic authentication if your app or service supports header authentication.

To configure this credential, enter:

*   The header **Name** you need to pass to the app or service your HTTP request is targeting
    
*   The **Value** for the header
    

Read more about [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#authentication)

Using JWT auth[](https://docs.n8n.io/integrations/builtin/credentials/webhook#using-jwt-auth)

----------------------------------------------------------------------------------------------

[**JWT Auth**](https://jwt.io/introduction/)
 is a method of authentication that uses JSON Web Tokens (JWT) to digitally sign data. This authentication method uses the **JWT credential** and can use either a **Passphrase** or **PEM Key** as key type. Refer to [JWT credential](https://docs.n8n.io/integrations/builtin/credentials/jwt)
 for more information.

[PreviousWebflow credentials](https://docs.n8n.io/integrations/builtin/credentials/webflow)
[NextWekan credentials](https://docs.n8n.io/integrations/builtin/credentials/wekan)

Last updated 10 days ago

Was this helpful?