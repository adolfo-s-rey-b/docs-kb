For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/spotify.md)
.

You can use these credentials to authenticate the following nodes:

*   [Spotify](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/spotify#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/spotify#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Spotify's Web API documentation](https://developer.spotify.com/documentation/web-api)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/spotify#using-oauth2)

------------------------------------------------------------------------------------------

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you're [self-hosting](https://docs.n8n.io/deploy/host-n8n)
 n8n, you'll need a [Spotify Developer](https://developer.spotify.com/)
 account so you can create a Spotify app:

1.  Open the [Spotify developer dashboard](https://developer.spotify.com/dashboard)
    .
    
2.  Select **Create an app**.
    
3.  Enter an **App name**, like `n8n integration`.
    
4.  Enter an **App description**.
    
5.  Copy the **OAuth Redirect URL** from n8n and enter it as the **Redirect URI** in your Spotify app.
    
6.  Check the box to agree to the Spotify Terms of Service and Branding Guidelines.
    
7.  Select **Create**. The **App overview** page opens.
    
8.  Copy the **Client ID** and enter it in your n8n credential.
    
9.  Copy the **Client Secret** and enter it in your n8n credential.
    
10.  Select **Connect my account** and follow the on-screen prompts to finish authorizing the credential.
    

Refer to [Spotify Apps](https://developer.spotify.com/documentation/web-api/concepts/apps)
 for more information.

[PreviousSplunk credentials](https://docs.n8n.io/integrations/builtin/credentials/splunk)
[NextSSH credentials](https://docs.n8n.io/integrations/builtin/credentials/ssh)

Last updated 10 days ago

Was this helpful?