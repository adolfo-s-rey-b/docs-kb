For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/ftp.md)
.

You can use these credentials to authenticate the following nodes:

*   [FTP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/ftp#prerequisites)

----------------------------------------------------------------------------------------

Create an account on a File Transfer Protocol (FTP) server like [JSCAPE](https://mft.jscape.com/lp/ftp-server)
, [OpenSSH](https://www.openssh.com/)
, or [FileZilla Server](https://filezilla-project.org/)
.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/ftp#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------

*   **FTP account**: Use this method if your FTP server doesn't support SSH tunneling or encrypted connections.
    
*   **SFTP account**: Use this method if your FTP server supports SSH tunneling and encrypted connections.
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/ftp#related-resources)

------------------------------------------------------------------------------------------------

File Transfer Protocol (FTP) and Secure Shell File Transfer Protocol (SFTP) are protocols for transferring files directly between an FTP/SFTP client and server.

Using FTP account[](https://docs.n8n.io/integrations/builtin/credentials/ftp#using-ftp-account)

------------------------------------------------------------------------------------------------

Use this method if your FTP server doesn't support SSH tunneling or encrypted connections.

To configure this credential, you'll need to:

1.  Enter the name or IP address of your FTP server's **Host**.
    
2.  Enter the **Port** number the connection should use.
    
3.  Enter the **Username** the credential should connect as.
    
4.  Enter the user's **Password**.
    

Review your FTP server provider's documentation for instructions on getting the information you need.

Using SFTP account[](https://docs.n8n.io/integrations/builtin/credentials/ftp#using-sftp-account)

--------------------------------------------------------------------------------------------------

Use this method if your FTP server supports SSH tunneling and encrypted connections.

To configure this credential, you'll need to:

1.  Enter the name or IP address of your FTP server's **Host**.
    
2.  Enter the **Port** number the connection should use.
    
3.  Enter the **Username** the credential should connect as.
    
4.  Enter the user's **Password**.
    
5.  For the **Private Key**, enter a string for either key-based or host-based user authentication
    
    *   Enter your Private Key in OpenSSH format. This is most often generated using the ssh-keygen `-o` parameter, for example: `ssh-keygen -o -a 100 -t ed25519`.
        
    
6.  If the **Private Key** is encrypted, enter the **Passphrase** used to decrypt it.
    
    *   If the **Private Key** doesn't use a passphrase, leave this field blank.
        
    

Review your FTP server provider's documentation for instructions on getting the information you need.

[PreviousFreshworks CRM credentials](https://docs.n8n.io/integrations/builtin/credentials/freshworkscrm)
[NextGetResponse credentials](https://docs.n8n.io/integrations/builtin/credentials/getresponse)

Last updated 10 days ago

Was this helpful?