For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md)
.

Two-factor authentication (2FA) adds a second authentication method on top of username and password. This increases account security. n8n supports 2FA using an authenticator app.

Enable 2FA[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth#enable-2fa)

-----------------------------------------------------------------------------------------------------------------------------

You need an authenticator app on your phone.

To enable 2FA in n8n:

1.  Go to you **Settings** > **Personal**.
    
2.  Select **Enable 2FA**. n8n opens a modal with a QR code.
    
3.  Scan the QR code in your authenticator app.
    
4.  Enter the code from your app in **Code from authenticator app**.
    
5.  Select **Continue**. n8n displays recovery codes.
    
6.  Save the recovery codes. You need these to regain access to your account if you lose your authenticator.
    

Disable 2FA for your instance[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth#disable-2fa-for-your-instance)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Self-hosted users can configure their n8n instance to disable 2FA for all users by setting `N8N_MFA_ENABLED` to false. Note that n8n ignores this if existing users have 2FA enabled. Refer to [Configuration methods](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
 for more information on configuring your n8n instance with environment variables.

Related resources[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------

*   [Verify user identity](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity)
    
*   [Connect LDAP](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap)
    
*   [Use SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml)
    
*   [Use OIDC](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc)
    

[PreviousVerify user identity](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity)
[NextConnect LDAP](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap)

Last updated 10 days ago

Was this helpful?