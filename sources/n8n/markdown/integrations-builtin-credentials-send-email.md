For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/send-email.md)
.

You can use these credentials to authenticate the following nodes:

*   [Send Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/send-email#prerequisites)

-----------------------------------------------------------------------------------------------

*   Create an email account on a service that supports SMTP.
    
*   Some email providers require that you enable or set up outgoing SMTP or generate an app password. Refer to your provider's documentation to see if there are other required steps.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/send-email#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------------

*   SMTP account
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/send-email#related-resources)

-------------------------------------------------------------------------------------------------------

Simple Message Transfer Protocol (SMTP) is a standard protocol for sending and receiving email. Most email providers offer instructions on setting up their service with SMTP. Refer to your provider's SMTP instructions.

Using SMTP account[](https://docs.n8n.io/integrations/builtin/credentials/send-email#using-smtp-account)

---------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **User** email address
    
*   A **Password**: This may be the user's password or an app password. Refer to the documentation for your email provider.
    
*   The **Host**: The SMTP host address for your email provider, often formatted as `smtp.<provider>.com`. Check with your provider.
    
*   A **Port** number: The port depends on the encryption method:
    
    *   Port `465` for SSL/TLS (implicit encryption)
        
    *   Port `587` for STARTTLS (explicit encryption)
        
    *   Port `25` for no encryption (not recommended) Check with your email provider for their specific requirements.
        
    
*   **SSL/TLS**: This toggle controls the encryption method:
    
    *   Turn **ON** for port `465` (uses implicit SSL/TLS encryption)
        
    *   Turn **OFF** for port `587` (uses STARTTLS explicit encryption)
        
    *   Turn **OFF** for port `25` (no encryption)
        
    
*   **Disable STARTTLS**: When SSL/TLS is disabled, the SMTP server can still try to [upgrade the TCP connection using STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS)
    . Turning this on prevents that behaviour.
    
*   **Client Host Name**: This name identifies the client to the server. May not be required for Gmail, Outlook.com, or Yahoo. Leave this field empty unless your email provider or administrator specifically requests it. If you do need to provide a value, use a fully qualified domain name (FQDN) such as `mail.yourdomain.com`. Avoid generic values like `localhost`.
    

### Provider instructions[](https://docs.n8n.io/integrations/builtin/credentials/send-email#provider-instructions)

Refer to the quickstart guides for these common email providers.

#### Gmail[](https://docs.n8n.io/integrations/builtin/credentials/send-email#gmail)

Refer to [Gmail](https://docs.n8n.io/integrations/builtin/credentials/send-email/gmail)
.

#### Outlook.com[](https://docs.n8n.io/integrations/builtin/credentials/send-email#outlookcom)

Refer to [Outlook.com](https://docs.n8n.io/integrations/builtin/credentials/send-email/outlook)
.

#### Yahoo[](https://docs.n8n.io/integrations/builtin/credentials/send-email#yahoo)

Refer to [Yahoo](https://docs.n8n.io/integrations/builtin/credentials/send-email/yahoo)
.

### My provider isn't listed[](https://docs.n8n.io/integrations/builtin/credentials/send-email#my-provider-isnt-listed)

If your email provider isn't listed here, search for `SMTP settings` to find their instructions. (These instructions may also be included with `IMAP settings` or `POP settings`.)

[PreviousSekoia credentials](https://docs.n8n.io/integrations/builtin/credentials/sekoia)
[NextGmail](https://docs.n8n.io/integrations/builtin/credentials/send-email/gmail)

Last updated 10 days ago

Was this helpful?