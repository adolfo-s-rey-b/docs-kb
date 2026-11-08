For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/totp.md)
.

You can use these credentials to authenticate the following nodes:

*   [TOTP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/totp#prerequisites)

-----------------------------------------------------------------------------------------

Generate a TOTP **Secret** and **Label**.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/totp#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------

*   Secret and label
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/totp#related-resources)

-------------------------------------------------------------------------------------------------

Time-based One-time Password (TOTP) is an algorithm that generates a one-time password (OTP) using the current time. Refer to [Google Authenticator | Key URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format)
 for more information.

Using secret and label[](https://docs.n8n.io/integrations/builtin/credentials/totp#using-secret-and-label)

-----------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Secret**: The secret key encoded in the QR code during authenticator setup. It's an arbitrary key value encoded in Base32, for example: `BVDRSBXQB2ZEL5HE`. Refer to [Google Authenticator Secret](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#secret)
     for more information.
    
*   A **Label**: The identifier for the account. It contains an account name as a URI-encoded string. You can include prefixes to identify the provider or service managing the account. If you use prefixes, use a literal or url-encoded colon to separate the issuer prefix and the account name, for example: `GitHub:john-doe`. Refer to [Google Authenticator Label](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#label)
     for more information.
    

[PreviousToggl credentials](https://docs.n8n.io/integrations/builtin/credentials/toggl)
[NextTravis CI credentials](https://docs.n8n.io/integrations/builtin/credentials/travisci)

Last updated 10 days ago

Was this helpful?