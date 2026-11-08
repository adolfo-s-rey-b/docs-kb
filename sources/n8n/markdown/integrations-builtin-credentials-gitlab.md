For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/gitlab.md)
.

You can use these credentials to authenticate the following nodes:

*   [GitLab](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab)
    
*   [GitLab Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/gitlab#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API access token
    
*   OAuth2 (Recommended)
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/gitlab#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [GitLab's API documentation](https://docs.gitlab.com/ee/api/rest/)
 for more information about the service.

Using API access token[](https://docs.n8n.io/integrations/builtin/credentials/gitlab#using-api-access-token)

-------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need a [GitLab](https://gitlab.com/)
 account and:

*   The URL of your **GitLab Server**
    
*   An **Access Token**
    

To set up the credential:

1.  In GitLab, select your avatar, then select **Edit profile**.
    
2.  In the left sidebar, select **Access tokens**.
    
3.  Select **Add new token**.
    
4.  Enter a **Name** for the token, like `n8n integration`.
    
5.  Enter an **expiry date** for the token. If you don't enter an expiry date, GitLab automatically sets it to 365 days later than the current date.
    
    *   The token expires on that expiry date at midnight UTC.
        
    
6.  Select the desired **Scopes**. For the [GitLab](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab)
     node, use the `api` scope to easily grant access for all the node's functionality. Or refer to [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)
     to select scopes for the functions you want to use.
    
7.  Select **Create personal access token**.
    
8.  Copy the access token this creates and enter it in your n8n credential as the **Access Token**.
    
9.  Enter the URL of your **GitLab Server** in your n8n credential.
    

Refer to GitLab's [Create a personal access token documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)
 for more information.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/gitlab#using-oauth2)

-----------------------------------------------------------------------------------------

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you're [self-hosting](https://docs.n8n.io/deploy/host-n8n)
 n8n, you'll need a [GitLab](https://gitlab.com/)
 account. Then create a new GitLab application:

1.  In GitLab, select your avatar, then select **Edit profile**.
    
2.  In the left sidebar, select **Applications**.
    
3.  Select **Add new application**.
    
4.  Enter a **Name** for your application, like `n8n integration`.
    
5.  In n8n, copy the **OAuth Redirect URL**. Enter it as the GitLab **Redirect URI**.
    
6.  Select the desired **Scopes**. For the [GitLab](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab)
     node, use the `api` scope to easily grant access for all the node's functionality. Or refer to [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)
     to select scopes for the functions you want to use.
    
7.  Select **Save application**.
    
8.  Copy the **Application ID** and enter it as the **Client ID** in your n8n credential.
    
9.  Copy the **Secret** and enter it as the **Client Secret** in your n8n credential.
    

Refer to GitLab's [Configure GitLab as an OAuth 2.0 authentication identity provider](https://docs.gitlab.com/ee/integration/oauth_provider.html)
 documentation for more information. Refer to the [GitLab OAuth 2.0 identity provider API documentation](https://docs.gitlab.com/ee/api/oauth2.html)
 for more information on OAuth2 and GitLab.

[PreviousGitHub credentials](https://docs.n8n.io/integrations/builtin/credentials/github)
[NextGong credentials](https://docs.n8n.io/integrations/builtin/credentials/gong)

Last updated 10 days ago

Was this helpful?