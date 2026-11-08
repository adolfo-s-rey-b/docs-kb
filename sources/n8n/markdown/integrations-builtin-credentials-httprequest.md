For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/httprequest.md)
.

You can use these credentials to authenticate the following nodes:

*   [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#prerequisites)

------------------------------------------------------------------------------------------------

You must use the authentication method required by the app or service you want to query.

If you need to secure the authentication with an SSL certificate, refer to [Provide an SSL certificate](https://docs.n8n.io/integrations/builtin/credentials/httprequest#provide-an-ssl-certificate)
 for the information you'll need.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------------

*   Predefined credential type
    
*   Basic auth (generic credential type)
    
*   Custom auth (generic credential type)
    
*   Digest auth (generic credential type)
    
*   Header auth (generic credential type)
    
*   Bearer auth (generic credential type)
    
*   OAuth1 (generic credential type)
    
*   OAuth2 (generic credential type)
    
*   Query auth (generic credential type)
    
*   Simplified Custom Auth (generic credential type)
    

Refer to [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
 for more information relating to generic credential types.

**Predefined credential types**

n8n recommends using predefined credential types whenever there's a credential type available for the service you want to connect to. It offers an easier way to set up and manage credentials, compared to configuring generic credentials.

You can use [Predefined credential types](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes#predefined-credential-types)
 to perform custom operations with some APIs where n8n has a node for the platform. For example, n8n has an Asana node, and supports using your Asana credentials in the HTTP Request node. Refer to [Custom operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Using predefined credential type[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-predefined-credential-type)

--------------------------------------------------------------------------------------------------------------------------------------

To use a predefined credential type:

1.  Open your HTTP Request or GraphQL node, or add a new one to your workflow.
    
2.  In **Authentication**, select **Predefined Credential Type**.
    
3.  In **Credential Type**, select the API you want to use.
    
4.  In **Credential for** `**<API name>**`, you can:
    
    1.  Select an existing credential for that platform, if available.
        
    2.  Select **Create New** to create a new credential.
        
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

### Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-basic-auth)

Use this generic authentication if your app or service supports basic authentication.

To configure this credential, enter:

*   The **Username** you use to access the app or service your HTTP Request is targeting
    
*   The **Password** that goes with that username
    

### Using digest auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-digest-auth)

Use this generic authentication if your app or service supports digest authentication.

To configure this credential, enter:

*   The **Username** you use to access the app or service your HTTP Request is targeting
    
*   The **Password** that goes with that username
    

### Using header auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-header-auth)

Use this generic authentication if your app or service supports header authentication.

To configure this credential, enter:

*   The header **Name** you need to pass to the app or service your HTTP request is targeting
    
*   The **Value** for the header
    

Read more about [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#authentication)

### Using bearer auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-bearer-auth)

Use this generic authentication if your app or service supports bearer authentication. This authentication type is actually just header authentication with the `Name` set to `Authorization` and the `Value` set to `Bearer <token>`.

To configure this credential, enter:

*   The **Bearer Token** you need to pass to the app or service your HTTP request is targeting
    

Read more about [bearer authentication](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/)
.

Using OAuth1[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-oauth1)

----------------------------------------------------------------------------------------------

Use this generic authentication if your app or service supports OAuth1 authentication.

To configure this credential, enter:

*   An **Authorization URL**: Also known as the Resource Owner Authorization URI. This URL typically ends in `/oauth1/authorize`. n8n sends the temporary credentials here to prompt a user to complete authorization.
    
*   An **Access Token URL**: This is the URI used for the initial request for temporary credentials. This URL typically ends in `/oauth1/request` or `/oauth1/token`.
    
*   A **Consumer Key**: Also known as the client key, like a username. This specifies the `oauth_consumer_key` to use for the call.
    
*   A **Consumer Secret**: Also known as the client secret, like a password.
    
*   A **Request Token URL**: This is the URI used to switch from temporary credentials to long-lived credentials after authorization. This URL typically ends in `/oauth1/access`.
    
*   Select the **Signature Method** the auth handshake uses. This specifies the `oauth_signature_method` to use for the call. Options include:
    
    *   **HMAC-SHA1**
        
    *   **HMAC-SHA256**
        
    *   **HMAC-SHA512**
        
    

For most OAuth1 integrations, you'll need to configure an app, service, or integration to generate the values for most of these fields. Use the **OAuth Redirect URL** in n8n as the redirect URL or redirect URI for such a service.

Read more about [OAuth1](https://oauth.net/1/)
 and the [OAuth1 authorization flow](https://oauth1.wp-api.org/docs/basics/Auth-Flow.html)
.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-oauth2)

----------------------------------------------------------------------------------------------

Use this generic authentication if your app or service supports OAuth2 authentication.

Requirements to configure this credential depend on the **Grant Type** selected. Refer to [OAuth Grant Types](https://oauth.net/2/grant-types/)
 for more information on each grant type.

For most OAuth2 integrations, you'll need to configure an app, service, or integration. Use the **OAuth Redirect URL** in n8n as the redirect URL or redirect URI for such a service.

Read more about [OAuth2](https://oauth.net/2/)
.

### Authorization Code grant type[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#authorization-code-grant-type)

Use Authorization Code grant type to exchange an authorization code for an access token. The auth flow uses the redirect URL to return the user to the client. Then the application gets the authorization code from the URL and uses it to request an access token. Refer to [Authorization Code Request](https://www.oauth.com/oauth2-servers/access-tokens/authorization-code-request/)
 for more information.

To configure this credential, select **Authorization Code** as the **Grant Type**.

Then enter:

*   An **Authorization URL**
    
*   An **Access Token URL**
    
*   A **Client ID**: The ID or username to log in with.
    
*   A **Client Secret**: The secret or password used to log in with.
    
*   _Optional:_ Enter one or more **Scope**s for the credential. If unspecified, the credential will request all scopes available to the client.
    
*   _Optional:_ Some services require more query parameters. If your service does, add them as **Auth URI Query Parameters**.
    
*   An **Authentication** type: Select the option that best suits your use case. Options include:
    
    *   **Header**: Send the credentials as a basic auth header.
        
    *   **Body**: Send the credentials in the body of the request.
        
    
*   _Optional:_ Choose whether to **Ignore SSL Issues**. If turned on, n8n will connect even if SSL validation fails.
    

### Client Credentials grant type[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#client-credentials-grant-type)

Use the Client Credentials grant type when applications request an access token to access their own resources, not on behalf of a user. Refer to [Client Credentials](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)
 for more information.

To configure this credential, select **Client Credentials** as the **Grant Type**.

Then enter:

*   An **Access Token URL**: The URL to hit to begin the OAuth2 flow. Typically this URL ends in `/token`.
    
*   A **Client ID**: The ID or username to use to log in to the client.
    
*   A **Client Secret**: The secret or password used to log in to the client.
    
*   _Optional:_ Enter one or more **Scope**s for the credential. Most services don't support scopes for Client Credentials grant types; only enter scopes here if yours does.
    
*   An **Authentication** type: Select the option that best suits your use case. Options include:
    
    *   **Header**: Send the credentials as a basic auth header.
        
    *   **Body**: Send the credentials in the body of the request.
        
    
*   _Optional:_ Choose whether to **Ignore SSL Issues**. If turned on, n8n will connect even if SSL validation fails.
    

### PKCE grant type[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#pkce-grant-type)

Proof Key for Code Exchange (PKCE) grant type is an extension to the Authorization Code flow to prevent CSRF and authorization code injection attacks.

To configure this credential, select **PKCE** as the **Grant Type**.

Then enter:

*   An **Authorization URL**
    
*   An **Access Token URL**
    
*   A **Client ID**: The ID or username to log in with.
    
*   A **Client Secret**: The secret or password used to log in with.
    
*   _Optional:_ Enter one or more **Scope**s for the credential. If unspecified, the credential will request all scopes available to the client.
    
*   _Optional:_ Some services require more query parameters. If your service does, add them as **Auth URI Query Parameters**.
    
*   An **Authentication** type: Select the option that best suits your use case. Options include:
    
    *   **Header**: Send the credentials as a basic auth header.
        
    *   **Body**: Send the credentials in the body of the request.
        
    
*   _Optional:_ Choose whether to **Ignore SSL Issues**. If turned on, n8n will connect even if SSL validation fails.
    

Using query auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-query-auth)

------------------------------------------------------------------------------------------------------

Use this generic authentication if your app or service supports passing authentication as a single key/value query parameter. (For multiple query parameters, use [Custom Auth](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-custom-auth)
.)

To configure this credential, enter:

*   A query parameter key or **Name**
    
*   A query parameter **Value**
    

Using custom auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-custom-auth)

--------------------------------------------------------------------------------------------------------

Use this generic authentication if your app or service supports passing authentication as multiple key/value query parameters or you need more flexibility than the other generic auth options.

The **Custom Auth** credential expects JSON data to define your credential. You can use `headers`, `qs`, `body` or a mix. Review the examples below to get started.

### Sending two headers[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#sending-two-headers)

Copy

    {
    	"headers": {
    		"X-AUTH-USERNAME": "username",
    		"X-AUTH-PASSWORD": "password"
    	}
    }

### Body[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#body)

Copy

    {
    	 "body" : {
    		"user": "username",
    		"pass": "password"
    	}
    }

### Query string[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#query-string)

Copy

    {
    	"qs": { 
    		"appid": "123456",
    		"apikey": "my-api-key"
    	}
    }

### Sending header and query string[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#sending-header-and-query-string)

Copy

    {
    	"headers": {
    		"api-version": "202404"
    	},
    	"qs": {
    		"apikey": "my-api-key"
    	}
    }

Using Simplified Custom Auth[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-simplified-custom-auth)

------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Simplified Custom Auth is available from n8n 2.35.0. In older versions, use [Custom auth](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-custom-auth)
 instead.

Use this generic authentication if your app or service expects static authentication values in headers, query parameters, or the request body, and you want to keep the secret values separate from the request definition.

Simplified Custom Auth works like [Custom auth](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-custom-auth)
: JSON that n8n merges into every request that uses the credential. The difference is that the JSON is a template containing `{{placeholder}}` markers instead of the secrets themselves. The credential form shows one field per placeholder, and n8n replaces each marker with the field's value when it sends a request.

This split exists so n8n Assistant can prepare the setup part for you. When [n8n Assistant](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant)
 builds a workflow for a service that has no dedicated n8n credential, it creates this credential type: it prepares the template, the fields, and the test URL from the service's API documentation, and you only paste the secret values into the form. It also records the service's API host so that n8n only offers the credential to nodes calling the same service.

You can also set up the credential yourself. Select **Edit setup** in the credential modal and enter:

*   An **Auth template**: The JSON n8n merges into every request that uses this credential. You can use `headers`, `qs`, `body`, or a mix, with a `{{placeholder}}` marker wherever a secret or account-specific value goes. Don't put real values in the template itself.
    
*   The **Fields** settings for each placeholder: a **Label**, whether the value is **Secret** (masked) or **Plain text**, whether it's **Required**, and an optional **Hint** clarifying the expected value, such as its format.
    
*   _Optional:_ A **Test URL**: A GET endpoint n8n calls with the authentication applied to check that the credential works when you save it. Pick a side-effect-free endpoint that never triggers billable work, such as an account or profile endpoint.
    
*   _Optional:_ **Accepted status codes**: Status codes to treat as success alongside 2xx responses when testing the credential, such as `403` for services that return 403 for a valid key with limited scopes.
    
*   _Optional:_ A **Documentation URL**: The provider page where you create or copy the secret. It doesn't appear in the credential form; n8n Assistant uses it to point you to the exact page.
    

Then go back to the form and enter a value for each field. n8n redacts the values after saving.

### Sending an API key in a header[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#sending-an-api-key-in-a-header)

A template that sends a bearer token:

Copy

    {
    	"headers": {
    		"Authorization": "Bearer {{api_key}}"
    	}
    }

The credential form shows one field for `api_key`. When the node sends a request, n8n replaces the marker with the field's value, resulting in the header `Authorization: Bearer <your-api-key>`.

If a required field is empty, requests fail with an error rather than sending the literal marker to the service. If an optional field is empty, n8n removes the template entries that use it from the request.

Provide an SSL certificate[](https://docs.n8n.io/integrations/builtin/credentials/httprequest#provide-an-ssl-certificate)

--------------------------------------------------------------------------------------------------------------------------

You can send an SSL certificate with your HTTP request. Create the SSL certificate as a separate credential for use by the node:

1.  In the HTTP Request node **Settings**, turn on **SSL Certificates**.
    
2.  On the **Parameters** tab, add an existing SSL Certificate credential to **Credential for SSL Certificates** or create a new one.
    

To configure your SSL Certificates credential, you'll need to add:

*   The Certificate Authority **CA** bundle
    
*   The **Certificate** (CRT): May also appear as a Public Key, depending on who your issuing CA was and how they format the cert
    
*   The **Private Key** (KEY)
    
*   _Optional:_ If the **Private Key** is encrypted, enter a **Passphrase** for the private key.
    

If your SSL certificate is in a single file (such as a `.pfx` file), you'll need to open the file to copy details from it to paste into the appropriate fields:

*   Enter the Public Key/CRT as the **Certificate**
    
*   Enter the **Private Key**/KEY in that field
    

[PreviousHome Assistant credentials](https://docs.n8n.io/integrations/builtin/credentials/homeassistant)
[NextHubSpot credentials](https://docs.n8n.io/integrations/builtin/credentials/hubspot)

Last updated 10 days ago

Was this helpful?