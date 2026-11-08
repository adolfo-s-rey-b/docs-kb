For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml.md)
.

Set up SAML SSO in n8n with Okta.

**Workforce Identity and Customer Identity**

This guide covers setting up Workforce Identity. This is the original Okta product. Customer Identity is Okta's name for Auth0, which they've acquired.

Prerequisites[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml#prerequisites)

--------------------------------------------------------------------------------------------------------------------------------------------------------

You need an Okta Workforce Identity account, and the redirect URL and entity ID from n8n's SAML settings.

Okta Workforce may enforce two factor authentication for users, depending on your Okta configuration.

Read the [Set up SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml)
 guide first.

Setup[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml#setup)

----------------------------------------------------------------------------------------------------------------------------------------

In addition to the following instructions, this visual step-by-step guide shows how to set up SAML in n8n with Okta:

[n8n-saml-with-okta.pdf](https://1614847662-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwMJrGrimpx3PxCJpUswm%2Fuploads%2Fgit-blob-e7917f5ec4a79c07cd271ee2038aca608c0d244e%2Fn8n-saml-with-okta.pdf?alt=media&token=527bd750-f50b-4722-a7cc-225038bd18e1)

PDF · 6MB

Download[Open](https://1614847662-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwMJrGrimpx3PxCJpUswm%2Fuploads%2Fgit-blob-e7917f5ec4a79c07cd271ee2038aca608c0d244e%2Fn8n-saml-with-okta.pdf?alt=media&token=527bd750-f50b-4722-a7cc-225038bd18e1)

Visual step-by-step guide for setting up SAML with Okta

1.  In your Okta admin panel, select **Applications** > **Applications**.
    
2.  Select **Create App Integration**. Okta opens the app creation modal.
    
3.  Select **SAML 2.0**, then select **Next**.
    
4.  On the **General Settings** tab, enter `n8n` as the **App name**.
    
5.  Select **Next** .
    
6.  On the **Configure SAML** tab, complete the following **General** fields:
    
    *   **Single sign-on URL**: the **Redirect URL** from n8n.
        
    *   **Audience URI (SP Entity ID)**: the **Entity ID** from n8n.
        
    *   **Default RelayState**: leave this empty.
        
    *   **Name ID format**: `EmailAddress`.
        
    *   **Application username**: `Okta username`.
        
    *   **Update application username on**: `Create and update`.
        
    
7.  Create **Attribute Statements**:
    
    **Name**
    
    **Name format**
    
    **Value**
    
    `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname`
    
    URI Reference
    
    user.firstName
    
    `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname`
    
    URI Reference
    
    user.lastName
    
    `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn`
    
    URI Reference
    
    user.login
    
    `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
    
    URI Reference
    
    user.email
    
8.  Select **Next**. Okta may prompt you to complete a marketing form, or may take you directly to your new n8n Okta app.
    
9.  Assign the n8n app to people:
    
    1.  On the n8n app dashboard in Okta, select **Assignments**.
        
    2.  Select **Assign** > **Assign to People**. Okta displays a modal with a list of available people.
        
    3.  Select **Assign** next to the person you want to add. Okta displays a prompt to confirm the username.
        
    4.  Leave the username as email address. Select **Save and Go Back**.
        
    5.  Select **Done**.
        
    
10.  Get the metadata XML: on the **Sign On** tab, copy the Metadata URL. Navigate to it, and copy the XML. Paste this into **Identity Provider Settings** in n8n.
    
11.  Select **Save settings**.
    
12.  Select **Test settings**. n8n opens a new tab. If you're not currently logged in, Okta prompts you to sign in. n8n then displays a success message confirming the attributes returned by Okta.
    

### Instance and project access provisioning[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml#instance-and-project-access-provisioning)

n8n supports two ways to provision instance and project roles via SSO. Choose one based on where you want the mapping logic to live:

*   **Map rules on your IdP**: configure n8n-specific attributes (`n8n_instance_role` and `n8n_projects`) in Okta, and n8n reads them directly from the SAML response. Steps below.
    
*   **Map rules inside n8n**: send group membership from Okta as a SAML attribute, and define mapping expressions inside n8n. No n8n-specific configuration is needed in Okta beyond the group attribute. See [Map rules inside n8n](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml#map-rules-inside-n8n)
     on the main SAML setup page.
    

In n8n, set **Role assignment** to **Instance roles via SSO** or **Instance and project roles via SSO**, then choose your preferred **Role mapping method**.

#### Map rules on your IdP[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml#map-rules-on-your-idp)

**Adding the required attributes**

1.  In your Okta admin panel, select **Applications** > **Applications**.
    
2.  Go to the configuration of your n8n application
    
3.  On the **General** tab, click **Edit** next to **SAML Settings**
    
4.  In the page that opens, continue to step 2: **Configure SAML**
    
5.  Add the following two **Attribute Statements**:
    
    **Name**
    
    **Name format**
    
    **Value**
    
    n8n\_instance\_role
    
    Basic
    
    appuser.n8n\_instance\_role
    
    n8n\_projects
    
    Basic
    
    appuser.n8n\_projects
    
6.  Click **Next**
    
7.  Click **Finish**
    

**Updating the app profile**

1.  In your Okta admin panel, select **Directory** > **Profile Editor**.
    
2.  Go to the profile of your n8n application
    
3.  Click **Add Attribute**
    
4.  Add the **n8n\_instance\_role** attribute
    
    *   **Data type**: string
        
    *   **Display name**: n8n\_instance\_role
        
    *   **Variable name**: n8n\_instance\_role
        
    *   **Attribute type**: Group
        
    
5.  Add the **n8n\_projects** attribute
    
    *   **Data type**: string array
        
    *   **Display name**: n8n\_projects
        
    *   **Variable name**: n8n\_projects
        
    *   **Attribute type**: Group
        
    *   **Group priority**: Combine values across groups
        
    

Now when you go to **Directory** > **Groups** and edit the assigned n8n application, you can configure the **n8n\_instance\_role** and **n8n\_projects** to be sent to n8n upon logging in via SAML.

Related resources[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Use SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml)
    
*   [Set up SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml)
    
*   [Azure AD SAML setup](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml)
    
*   [Troubleshoot SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml)
    
*   [Manage users with SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml)
    

[PreviousManage users with SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml)
[NextSet up Azure AD SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml)

Last updated 10 days ago

Was this helpful?