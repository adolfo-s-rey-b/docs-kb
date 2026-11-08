For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/slack.md)
.

You can use these credentials to authenticate the following nodes:

*   [Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack)
    
*   [Slack Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/slack#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------

*   API access token:
    
    *   Required for the [Slack Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger)
         node.
        
    *   Works with the [Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack)
         node, but not recommended.
        
    
*   OAuth2:
    
    *   Recommended method for the [Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack)
         node.
        
    *   Doesn't work with the [Slack Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger)
         node.
        
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/slack#related-resources)

--------------------------------------------------------------------------------------------------

Refer to [Slack's API documentation](https://api.slack.com/apis)
 for more information about the service.

Using API access token[](https://docs.n8n.io/integrations/builtin/credentials/slack#using-api-access-token)

------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Slack](https://slack.com/)
 account and:

*   An **Access Token**
    

To generate an access token, create a Slack app. n8n recommends creating the app from a manifest, which configures all the scopes in one step:

### Create the app from a manifest for API access token[](https://docs.n8n.io/integrations/builtin/credentials/slack#create-the-app-from-a-manifest-for-api-access-token)

1.  Open your [Slack API Apps](https://api.slack.com/apps)
     page.
    
2.  Select **Create New App > From a manifest**.
    
3.  Select the **Workspace** where you'll be developing your app, then select **Next**.
    
4.  Select the **JSON** tab and replace the default manifest with the JSON below. Adjust the [scopes](https://docs.n8n.io/integrations/builtin/credentials/slack#scopes)
     if needed.
    
5.  Select **Next**.
    
6.  Review the summary and select **Create**. The app details open.
    

Copy

    {
    	"display_information": {
    		"name": "n8n integration"
    	},
    	"features": {
    		"bot_user": {
    			"display_name": "n8n integration"
    		}
    	},
    	"oauth_config": {
    		"scopes": {
    			"bot": [\
    				"channels:read",\
    				"channels:history",\
    				"chat:write",\
    				"files:read",\
    				"files:write",\
    				"groups:read",\
    				"groups:history",\
    				"im:read",\
    				"im:history",\
    				"mpim:read",\
    				"mpim:history",\
    				"reactions:read",\
    				"reactions:write",\
    				"usergroups:read",\
    				"usergroups:write",\
    				"users.profile:read",\
    				"users:read"\
    			]
    		}
    	},
    	"settings": {
    		"org_deploy_enabled": false,
    		"socket_mode_enabled": false,
    		"token_rotation_enabled": false
    	}
    }

### Create the app from scratch for API access token[](https://docs.n8n.io/integrations/builtin/credentials/slack#create-the-app-from-scratch-for-api-access-token)

1.  Open your [Slack API Apps](https://api.slack.com/apps)
     page.
    
2.  Select **Create New App > From scratch**.
    
3.  Enter an **App Name**.
    
4.  Select the **Workspace** where you'll be developing your app.
    
5.  Select **Create App**. The app details open.
    
6.  In the left menu under **Features**, select **OAuth & Permissions**.
    
7.  In the **Scopes** section, select appropriate scopes for your app. Refer to [Scopes](https://docs.n8n.io/integrations/builtin/credentials/slack#scopes)
     for a list of recommended scopes.
    

Then install the app and copy the token:

1.  In the left menu under **Features**, select **OAuth & Permissions**.
    
2.  In the **OAuth Tokens** section, select **Install to Workspace**. You must be a Slack workspace admin to complete this action.
    
3.  Select **Allow**.
    
4.  Copy the **Bot User OAuth Token** and enter it as the **Access Token** in your n8n credential.
    
5.  If you're using this credential for the [Slack Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger)
    , follow the steps in [Slack Trigger configuration](https://docs.n8n.io/integrations/builtin/credentials/slack#slack-trigger-configuration)
     to finish setting up your app.
    

Refer to the Slack API [Quickstart](https://api.slack.com/quickstart)
 for more information.

### Slack Trigger configuration[](https://docs.n8n.io/integrations/builtin/credentials/slack#slack-trigger-configuration)

To use your Slack app with the [Slack Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger)
 node:

1.  Go to [Your Apps](https://api.slack.com/apps/)
     in Slack and select the app you want to use.
    
2.  Go to **Features** > **Event Subscriptions**.
    
3.  Turn on the **Enable Events** control.
    
4.  In n8n, copy the **Webhook URL** and enter it as the **Request URL** in your Slack app.
    
    **Request URL**
    
    Slack only allows one request URL per app. If you want to test your workflow, you'll need to do one of the following:
    
    *   Test with your **Test URL** first, then change your Slack app to use the **Production URL** once you've verified everything's working
        
    *   Use the **Production URL** with execution logging.
        
    
5.  Once verified, select the bot events to subscribe to. Use the **Trigger on** field in n8n to filter these requests.
    
    *   To use an event not in the list, add it as a bot event and select **Any Event** in the n8n node.
        
    

Refer to [Quickstart | Configuring the app for event listening](https://api.slack.com/quickstart#listening)
 for more information.

After Slack verifies the **Request URL**, you can also manage the event subscription in your app's manifest: go to **Settings** > **App Manifest** and edit the `settings.event_subscriptions` block.

n8n recommends enabling request signature verification for your Slack Trigger for additional security:

1.  Go to [Your Apps](https://api.slack.com/apps/)
     in Slack and select the app you want to use.
    
2.  Go to **Settings** > **Basic Information**.
    
3.  Copy the value of **Signing Secret**.
    
4.  In n8n, Paste this value into the **Signature Secret** field for the credential.
    

The **Signature Secret** field is also required for [Approvals in Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals)
.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/slack#using-oauth2)

----------------------------------------------------------------------------------------

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you're [self-hosting n8n](https://docs.n8n.io/deploy/host-n8n)
 and need to configure OAuth2 from scratch, you'll need a [Slack](https://slack.com/)
 account and:

*   A **Client ID**
    
*   A **Client Secret**
    

To get both, create a Slack app. n8n recommends creating the app from a manifest, which configures the scopes and redirect URL in one step:

### Create the app from a manifest for OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/slack#create-the-app-from-a-manifest-for-oauth2)

1.  In n8n, copy the **OAuth Callback URL** from your Slack credential.
    
2.  Open your [Slack API Apps](https://api.slack.com/apps)
     page.
    
3.  Select **Create New App > From a manifest**.
    
4.  Select the **Workspace** where you'll be developing your app, then select **Next**.
    
5.  Select the **JSON** tab and replace the default manifest with the JSON below. Replace `<your-oauth-callback-url>` with the URL you copied from n8n and adjust the [scopes](https://docs.n8n.io/integrations/builtin/credentials/slack#scopes)
     if needed.
    
6.  Select **Next**.
    
7.  Review the summary and select **Create**. The app details open.
    

Copy

    {
    	"display_information": {
    		"name": "n8n integration"
    	},
    	"features": {
    		"bot_user": {
    			"display_name": "n8n integration"
    		}
    	},
    	"oauth_config": {
    		"redirect_urls": [\
    			"<your-oauth-callback-url>"\
    		],
    		"scopes": {
    			"bot": [\
    				"channels:read",\
    				"channels:history",\
    				"chat:write",\
    				"files:read",\
    				"files:write",\
    				"groups:read",\
    				"groups:history",\
    				"im:read",\
    				"im:history",\
    				"mpim:read",\
    				"mpim:history",\
    				"reactions:read",\
    				"reactions:write",\
    				"usergroups:read",\
    				"usergroups:write",\
    				"users.profile:read",\
    				"users:read"\
    			],
    			"user": [\
    				"channels:write",\
    				"groups:write",\
    				"search:read",\
    				"search:read.public",\
    				"search:read.private",\
    				"search:read.im",\
    				"search:read.mpim",\
    				"stars:read",\
    				"stars:write",\
    				"users.profile:write"\
    			]
    		}
    	},
    	"settings": {
    		"org_deploy_enabled": false,
    		"socket_mode_enabled": false,
    		"token_rotation_enabled": false
    	}
    }

Manifest with user scopes only[](https://docs.n8n.io/integrations/builtin/credentials/slack#manifest-with-user-scopes-only)

Some Slack API endpoints, including Slack's MCP endpoints, only work with user tokens and not bot tokens. If you need a user token, use this manifest instead. It requests all scopes as user scopes:

Copy

    {
    	"display_information": {
    		"name": "n8n integration"
    	},
    	"oauth_config": {
    		"redirect_urls": [\
    			"<your-oauth-callback-url>"\
    		],
    		"scopes": {
    			"user": [\
    				"channels:read",\
    				"channels:write",\
    				"channels:history",\
    				"chat:write",\
    				"files:read",\
    				"files:write",\
    				"groups:read",\
    				"groups:write",\
    				"groups:history",\
    				"im:read",\
    				"im:history",\
    				"mpim:read",\
    				"mpim:history",\
    				"reactions:read",\
    				"reactions:write",\
    				"stars:read",\
    				"stars:write",\
    				"usergroups:read",\
    				"usergroups:write",\
    				"users.profile:read",\
    				"users.profile:write",\
    				"users:read",\
    				"search:read",\
    				"search:read.public",\
    				"search:read.private",\
    				"search:read.im",\
    				"search:read.mpim"\
    			]
    		}
    	},
    	"settings": {
    		"org_deploy_enabled": false,
    		"socket_mode_enabled": false,
    		"token_rotation_enabled": false
    	}
    }

### Create the app from scratch for OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/slack#create-the-app-from-scratch-for-oauth2)

1.  Open your [Slack API Apps](https://api.slack.com/apps)
     page.
    
2.  Select **Create New App > From scratch**.
    
3.  Enter an **App Name**.
    
4.  Select the **Workspace** where you'll be developing your app.
    
5.  Select **Create App**. The app details open.
    
6.  In the left menu under **Features**, select **OAuth & Permissions**.
    
7.  In the **Redirect URLs** section, select **Add New Redirect URL**.
    
8.  Copy the **OAuth Callback URL** from n8n and enter it as the new Redirect URL in Slack.
    
9.  Select **Add**.
    
10.  Select **Save URLs**.
    
11.  In the **Scopes** section, select appropriate scopes for your app. Refer to [Scopes](https://docs.n8n.io/integrations/builtin/credentials/slack#scopes)
     for a list of scopes.
    

Then finish connecting the app to n8n:

1.  In **Settings > Basic Information**, open the **App Credentials** section.
    
2.  Copy the **Client ID** and **Client Secret**. Paste these into the corresponding fields in n8n.
    
3.  In the left menu under **Features**, select **OAuth & Permissions**.
    
4.  In the **OAuth Tokens** section, select **Install to Workspace**. You must be a Slack workspace admin to complete this action.
    
5.  Select **Allow**.
    
6.  At this point, you should be able to select the OAuth button in your n8n credential to connect.
    

Refer to the Slack API [Quickstart](https://api.slack.com/quickstart)
 for more information. Refer to the Slack [Installing with OAuth](https://api.slack.com/authentication/oauth-v2)
 documentation for more details on the OAuth flow itself.

Scopes[](https://docs.n8n.io/integrations/builtin/credentials/slack#scopes)

----------------------------------------------------------------------------

Scopes determine what permissions an app has.

*   If you want your app to act on behalf of users who authorize the app, add the required scopes under the **User Token Scopes** section.
    
*   If you're building a bot, add the required scopes under the **Bot Token Scopes** section.
    

Here's the list of scopes the OAuth credential requires, which are a good starting point. The app manifests above already include these scopes:

**Scope name**

**Notes**

`channels:read`

`channels:write`

Not available as a bot token scope

`channels:history`

`chat:write`

`files:read`

`files:write`

`groups:read`

`groups:write`

For private-channel management operations

`groups:history`

`im:read`

`im:history`

`mpim:read`

`mpim:history`

`reactions:read`

`reactions:write`

`stars:read`

Not available as a bot token scope

`stars:write`

Not available as a bot token scope

`usergroups:read`

`usergroups:write`

`users.profile:read`

`users.profile:write`

Not available as a bot token scope

`users:read`

`search:read`

Deprecated by Slack; retained for node versions <= 2.6

`search:read.public`

For public-channel message search

`search:read.private`

Not available as a bot token scope

`search:read.im`

Not available as a bot token scope

`search:read.mpim`

Not available as a bot token scope

Common issues[](https://docs.n8n.io/integrations/builtin/credentials/slack#common-issues)

------------------------------------------------------------------------------------------

### Token expired[](https://docs.n8n.io/integrations/builtin/credentials/slack#token-expired)

Slack offers **token rotation** that you can turn on for bot and user tokens. This makes every tokens expire after 12 hours. While this may be useful for testing, n8n credentials using tokens with this enabled will fail after expiry. If you want to use your Slack credentials in production, this feature must be **off**.

To check if your Slack app has token rotation turned on, refer to the [Slack API Documentation | Token Rotation](https://api.slack.com/authentication/rotation)
.

**If your app uses token rotation**

Please note, if your Slack app uses token rotation, you can't turn it off again. You need to create a new Slack app with token rotation disabled instead.

[PreviousSIGNL4 credentials](https://docs.n8n.io/integrations/builtin/credentials/signl4)
[NextSnowflake credentials](https://docs.n8n.io/integrations/builtin/credentials/snowflake)

Last updated 10 days ago

Was this helpful?