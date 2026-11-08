For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc.md)
.

Known issues[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc#known-issues)

------------------------------------------------------------------------------------------------------------------------------------

### State parameter not supported[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc#state-parameter-not-supported)

When using OIDC providers that enforce the use of the `state` CSRF token parameter, authentication fails with the error:

Copy

    {"code":0,"message":"authorization response from the server is an error"}

n8n's current OIDC implementation doesn't handle the `state` parameter that some OIDC providers send as a security measure against CSRF attacks.

For now, the only work around is to configure your OIDC provider to disable the `state` parameter if possible.

n8n is working on adding full support for the OIDC `state` parameter in a future release.

### PKCE not supported[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc#pkce-not-supported)

OIDC providers that require PKCE (Proof Key for Code Exchange) may fail authentication or reject n8n's authorization requests. n8n's current OIDC implementation doesn't support PKCE.

The only work around is to configure your OIDC provider to not require PKCE for the n8n client if this option is available in your providers settings.

n8n plans on adding PKCE support in a future release

Related resources[](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------------

*   [Use OIDC](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc)
    
*   [Set up OIDC](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc)
    

[PreviousSet up OIDC](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc)
[NextFollow best practices](https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices)

Last updated 10 days ago

Was this helpful?