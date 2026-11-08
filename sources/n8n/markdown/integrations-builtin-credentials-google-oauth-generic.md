For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic.md)
.

This document contains instructions for creating a generic Google OAuth2 API credential for use with [custom operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

*   [Google Calendar](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar)
    
*   [Google Calendar Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger)
    
*   [Google Chat](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat)
    
*   [Google Contacts](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts)
    
*   [Google Docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledocs)
    
*   [Google Drive](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive)
    
*   [Google Drive Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger)
    
*   [Google Mail](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail)
    
*   [Google Mail Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger)
    
*   [Google Sheets](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)
    
*   [Google Sheets Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger)
    
*   [Google Slides](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides)
    
*   [Google Tasks](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googletasks)
    
*   [YouTube](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#prerequisites)

---------------------------------------------------------------------------------------------------------

*   Create a [Google Cloud](https://cloud.google.com/)
     account.
    

Set up OAuth[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#set-up-oauth)

-------------------------------------------------------------------------------------------------------

There are five steps to connecting your n8n credential to Google services:

1.  [Create a Google Cloud Console project](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#create-a-google-cloud-console-project)
    .
    
2.  [Enable APIs](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#enable-apis)
    .
    
3.  [Configure your OAuth consent screen](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#configure-your-oauth-consent-screen)
    .
    
4.  [Create your Google OAuth client credentials](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#create-your-google-oauth-client-credentials)
    .
    
5.  [Finish your n8n credential](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#finish-your-n8n-credential)
    .
    

### Create a Google Cloud Console project[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#create-a-google-cloud-console-project)

First, create a Google Cloud Console project. If you already have a project, jump to the [next section](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#enable-apis)
:

1.  Log in to your [Google Cloud Console](https://console.cloud.google.com/)
     using your Google credentials.
    
2.  In the top menu, select the project dropdown in the top navigation and select **New project** or go directly to the [New Project](https://console.cloud.google.com/projectcreate)
     page.
    
3.  Enter a **Project name** and select the location (**Organization** and/or **Parent resource**) for your project.
    
4.  Select **Create**.
    
5.  Check the top navigation and make sure the project dropdown has your project selected. If not, select the project you just created.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-83919da524e27c4e8236f4c68e98e970149a4c15%252Fgoogle-cloud-project-dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0ad4b84c2b450b698b4b5ad2cfc23071&sv=3)
    
    Check the project dropdown in the Google Cloud top navigation
    

### Enable APIs[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#enable-apis)

With your project created, enable the APIs you'll need access to:

1.  Access your [Google Cloud Console - Library](https://console.cloud.google.com/apis/library)
    . Make sure you're in the correct project.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-83919da524e27c4e8236f4c68e98e970149a4c15%252Fgoogle-cloud-project-dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0ad4b84c2b450b698b4b5ad2cfc23071&sv=3)
    
    Check the project dropdown in the Google Cloud top navigation
    
2.  Go to **APIs & Services > Library**.
    
3.  Search for and select the API(s) you want to enable. For example, for the Gmail node, search for and enable the Gmail API.
    
4.  Some integrations require other APIs or require you to request access:
    
    *   Google Perspective: [Request API Access](https://developers.perspectiveapi.com/s/docs-get-started)
        .
        
    *   Google Ads: Get a [Developer Token](https://developers.google.com/google-ads/api/docs/first-call/dev-token)
        .
        
    
    **Google Drive API required**
    
    The following integrations require the Google Drive API, as well as their own API:
    
    *   Google Docs
        
    *   Google Sheets
        
    *   Google Slides
        
    
    **Google Vertex AI API**
    
    In addition to the Vertex AI API you will also need to enable the [Cloud Resource Manager API](https://console.cloud.google.com/apis/api/cloudresourcemanager.googleapis.com/)
    .
    
5.  Select **ENABLE**.
    

### Configure your OAuth consent screen[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#configure-your-oauth-consent-screen)

If you haven't used OAuth in your Google Cloud project before, you'll need to [configure the OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent)
:

1.  Access your [Google Cloud Console - Library](https://console.cloud.google.com/apis/library)
    . Make sure you're in the correct project.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-83919da524e27c4e8236f4c68e98e970149a4c15%252Fgoogle-cloud-project-dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fbe88ac60181c8da69781cb10ba2efa5&sv=3)
    
    Check the project dropdown in the Google Cloud top navigation
    
2.  Open the left navigation menu and go to **APIs & Services > OAuth consent screen**. Google will redirect you to the Google Auth Platform overview page.
    
3.  Select **Get started** on the **Overview** tab to begin configuring OAuth consent.
    
4.  Enter an **App name** and **User support email** to include on the Oauth screen. Select **Next** to continue.
    
5.  For the **Audience**, select **Internal** for user access within your organization's Google workspace or **External** for any user with a Google account. Refer to Google's [User type documentation](https://support.google.com/cloud/answer/15549945?sjid=17061891731152303663-EU#user-type)
     for more information on user types. Select **Next** to continue.
    
    **Testing mode and test users**
    
    If you select **External**, your app will default to Testing mode. In this mode, only Google accounts you manually add as test users can complete the OAuth flow — everyone else will see an "access denied" screen. See [Google hasn't verified this app](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#google-hasnt-verified-this-app)
     to learn how to add them.
    
6.  Select the **Email addresses** Google should use to contact you about changes to your project. Select **Next** to continue.
    
7.  Read and accept the Google's User Data Policy. Select **Continue** and then select **Create**.
    
8.  In the left-hand menu, select **Branding**.
    
9.  In the **Authorized domains** section, select **Add domain**:
    
    *   If you're using n8n's Cloud service, add `n8n.cloud`
        
    *   If you're [self-hosting](https://docs.n8n.io/deploy/host-n8n)
        , add the domain of your n8n instance.
        
    
10.  Select **Save** at the bottom of the page.
    

### Create your Google OAuth client credentials[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#create-your-google-oauth-client-credentials)

Next, create the OAuth client credentials in Google:

1.  Access your [Google Cloud Console](https://console.cloud.google.com/)
    . Make sure you're in the correct project.
    
2.  In the **APIs & Services** section, select [**Credentials**](https://console.cloud.google.com/apis/credentials)
    .
    
3.  Select **\+ Create credentials** > **OAuth client ID**.
    
4.  In the **Application type** dropdown, select **Web application**.
    
5.  Google automatically generates a **Name**. Update the **Name** to something you'll recognize in your console.
    
6.  From your n8n credential, copy the **OAuth Redirect URL**. Paste it into the **Authorized redirect URIs** in Google Console.
    
    **OAuth redirect URL for self-hosting**
    
    If you're running n8n on your local machine, you don't need a public domain, SSL certificate, or port forwarding to use Google OAuth. Google allows localhost as a valid redirect URI for development purposes. Your n8n OAuth redirect URL will look something like this: `http://localhost:5678/rest/oauth2-credential/callback` For more details on acceptable redirect URIs, refer to [Google's redirect URI documentation](https://support.google.com/cloud/answer/15549257?hl=en#zippy=%2Cweb-applications)
    .
    
7.  Select **Create**.
    

### Finish your n8n credential[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#finish-your-n8n-credential)

With the Google project and credentials fully configured, finish the n8n credential:

1.  From Google's **OAuth client created** modal, copy the **Client ID**. Enter this in your n8n credential.
    
2.  From the same Google modal, copy the **Client Secret**. Enter this in your n8n credential.
    
3.  You must provide the scopes for this credential. Refer to [Scopes](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#scopes)
     for more information. Enter multiple scopes in a space-separated list, for example:
    
    Copy
    
        https://www.googleapis.com/auth/gmail.labels https://www.googleapis.com/auth/gmail.addons.current.action.compose
    
4.  In n8n, select **Sign in with Google** to complete your Google authentication.
    
5.  **Save** your new credentials.
    

Video[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#video)

-----------------------------------------------------------------------------------------

The following video demonstrates the steps described above:

Scopes[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#scopes)

-------------------------------------------------------------------------------------------

Google services have one or more possible access scopes. A scope limits what a user can do. Refer to [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes)
 for a list of scopes for all services.

n8n doesn't support all scopes. When creating a generic Google OAuth2 API credential, you can enter scopes from the **Supported scopes** list below. If you enter a scope that n8n doesn't already support, it won't work.

Supported scopes[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#supported-scopes)

Service

Available scopes

Gmail

*   `https://www.googleapis.com/auth/gmail.labels`
    
*   `https://www.googleapis.com/auth/gmail.addons.current.action.compose`
    
*   `https://www.googleapis.com/auth/gmail.addons.current.message.action`
    
*   `https://mail.google.com/`
    
*   `https://www.googleapis.com/auth/gmail.modify`
    
*   `https://www.googleapis.com/auth/gmail.compose`
    

Google Ads

*   `https://www.googleapis.com/auth/adwords`
    

Google Analytics

*   `https://www.googleapis.com/auth/analytics`
    
*   `https://www.googleapis.com/auth/analytics.readonly`
    

Google BigQuery

*   `https://www.googleapis.com/auth/bigquery`
    

Google Books

*   `https://www.googleapis.com/auth/books`
    

Google Calendar

*   `https://www.googleapis.com/auth/calendar`
    
*   `https://www.googleapis.com/auth/calendar.events`
    

Google Cloud Natural Language

*   `https://www.googleapis.com/auth/cloud-language`
    
*   `https://www.googleapis.com/auth/cloud-platform`
    

Google Cloud Storage

*   `https://www.googleapis.com/auth/cloud-platform`
    
*   `https://www.googleapis.com/auth/cloud-platform.read-only`
    
*   `https://www.googleapis.com/auth/devstorage.full_control`
    
*   `https://www.googleapis.com/auth/devstorage.read_only`
    
*   `https://www.googleapis.com/auth/devstorage.read_write`
    

Google Contacts

*   `https://www.googleapis.com/auth/contacts`
    

Google Docs

*   `https://www.googleapis.com/auth/documents`
    
*   `https://www.googleapis.com/auth/drive`
    
*   `https://www.googleapis.com/auth/drive.file`
    

Google Drive

*   `https://www.googleapis.com/auth/drive`
    
*   `https://www.googleapis.com/auth/drive.appdata`
    
*   `https://www.googleapis.com/auth/drive.photos.readonly`
    

Google Firebase Cloud Firestore

*   `https://www.googleapis.com/auth/datastore`
    
*   `https://www.googleapis.com/auth/firebase`
    

Google Firebase Realtime Database

*   `https://www.googleapis.com/auth/userinfo.email`
    
*   `https://www.googleapis.com/auth/firebase.database`
    
*   `https://www.googleapis.com/auth/firebase`
    

Google Perspective

*   `https://www.googleapis.com/auth/userinfo.email`
    

Google Sheets

*   `https://www.googleapis.com/auth/drive.file`
    
*   `https://www.googleapis.com/auth/spreadsheets`
    

Google Slide

*   `https://www.googleapis.com/auth/drive.file`
    
*   `https://www.googleapis.com/auth/presentations`
    

Google Tasks

*   `https://www.googleapis.com/auth/tasks`
    

Google Translate

*   `https://www.googleapis.com/auth/cloud-translation`
    

GSuite Admin

*   `https://www.googleapis.com/auth/admin.directory.group`
    
*   `https://www.googleapis.com/auth/admin.directory.user`
    
*   `https://www.googleapis.com/auth/admin.directory.domain.readonly`
    
*   `https://www.googleapis.com/auth/admin.directory.userschema.readonly`
    

Troubleshooting[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#troubleshooting)

-------------------------------------------------------------------------------------------------------------

### Google hasn't verified this app[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#google-hasnt-verified-this-app)

If using the OAuth authentication method, you might see the warning **Google hasn't verified this app**. To avoid this:

*   If your app **User Type** is **Internal**, create OAuth credentials from the same account you want to authenticate.
    
*   If your app **User Type** is **External**, you can add your email to the list of testers for the app: go to the [**Audience**](https://console.cloud.google.com/auth/audience) page and add the email you're signing in with to the list of **Test users**.
    

If you need to use credentials generated by another account (by a developer or another third party), follow the instructions in [Google Cloud documentation | Authorization errors: Google hasn't verified this app](https://developers.google.com/nest/device-access/reference/errors/authorization#google_hasnt_verified_this_app)
.

### Google Cloud app becoming unauthorized[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#google-cloud-app-becoming-unauthorized)

For Google Cloud apps with **Publishing status** set to **Testing** and **User type** set to **External**, consent and tokens expire after seven days. Refer to [Google Cloud Platform Console Help | Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615?hl=en#zippy=%2Ctesting)
 for more information. To resolve this, reconnect the app in the n8n credentials modal.

### redirect\_uri\_mismatch[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#redirecturimismatch)

This error means the redirect URI n8n is sending doesn't match any of the URIs registered in your Google Cloud Console OAuth client.

**Fix:** Copy the **OAuth Redirect URL** from your n8n credential panel and paste it exactly — including the protocol (`http` or `https`) and port number — into the **Authorized redirect URIs** field of your Google OAuth client.

### Access denied / "app not verified"[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#access-denied-app-not-verified)

This usually happens when your app is still in Testing mode and the Google account you're trying to authenticate with hasn't been added as a test user.

**Fix:** Go to **APIs & Services** > **OAuth consent screen** > **Test users** and add the account you're trying to use.

### invalid\_client[](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic#invalidclient)

This error typically means the Client ID or Client Secret in your n8n credential doesn't match what's in Google Cloud Console.

**Fix:** Go back to your OAuth client in Google Cloud Console, copy both values fresh, and re-enter them in n8n. Watch out for accidental spaces when copying.

[PreviousGoogle OAuth2 single service](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service)
[NextGoogle Service Account](https://docs.n8n.io/integrations/builtin/credentials/google/service-account)

Last updated 10 days ago

Was this helpful?