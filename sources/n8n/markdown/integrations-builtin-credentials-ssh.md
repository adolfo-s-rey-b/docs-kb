For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/ssh.md)
.

You can use these credentials to authenticate the following nodes:

*   [SSH](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/ssh#prerequisites)

----------------------------------------------------------------------------------------

*   Create a remote server with SSH enabled.
    
*   Create a user account that can `ssh` into the server using one of the following:
    
    *   Their own [password](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-password)
        
    *   An SSH [private key](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-private-key)
        
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/ssh#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------

*   [Password](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-password)
    : Use this method if you have a user account that can `ssh` into the server using their own password.
    
*   [Private key](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-private-key)
    : Use this method if you have a user account that uses an SSH key for the server or service.
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/ssh#related-resources)

------------------------------------------------------------------------------------------------

Secure Shell (SSH) protocol is a method for securely sending commands over a network. Refer to [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
 for an example of SSH setup.

Using password[](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-password)

------------------------------------------------------------------------------------------

Use this method if you have a user account that can `ssh` into the server using their own password.

To configure this credential, you'll need to:

1.  Enter the IP address of the server you're connecting to as the **Host**.
    
2.  Enter the **Port** to use for the connection. SSH uses port `22` by default.
    
3.  Enter the **Username** for a user account with `ssh` access on the server.
    
4.  Enter the **Password** for that user account.
    

Using private key[](https://docs.n8n.io/integrations/builtin/credentials/ssh#using-private-key)

------------------------------------------------------------------------------------------------

Use this method if you have a user account that uses an SSH key for the server or service.

To configure this credential, you'll need to:

1.  Enter the IP address of the server you're connecting to as the **Host**.
    
2.  Enter the **Port** to use for the connection. SSH uses port `22` by default.
    
3.  Enter the **Username** of the account that generated the private key.
    
4.  Enter the entire contents of your SSH **Private Key**.
    
5.  If you created a **Passphrase** for the **Private Key**, enter the passphrase.
    
    *   If you didn't create a passphrase for the key, leave blank.
        
    

[PreviousSpotify credentials](https://docs.n8n.io/integrations/builtin/credentials/spotify)
[NextStackby credentials](https://docs.n8n.io/integrations/builtin/credentials/stackby)

Last updated 10 days ago

Was this helpful?