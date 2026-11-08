For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control.md)
.

Link a Git repository to an n8n instance and configure your source control.

n8n uses source control to provide environments. Refer to [Environments in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
 for more information.

Prerequisites[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#prerequisites)

------------------------------------------------------------------------------------------------------------------------

To use source control with n8n, you need a Git repository with either:

*   SSH access (using deploy keys), or
    
*   HTTPS access (using Personal Access Tokens)
    

This document assumes you are familiar with Git and your Git provider.

Step 1: Set up your repository and branches[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#step-1-set-up-your-repository-and-branches)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For a new setup:

1.  Create a new repository for use with n8n.
    
2.  Create the branches you need. For example, if you plan to have different environments for test and production, set up a branch for each.
    

To help decide what branches you need for your use case, refer to [Branch patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
.

Step 2: Configure Git in n8n[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#step-2-configure-git-in-n8n)

-----------------------------------------------------------------------------------------------------------------------------------------------------

1.  Go to **Settings** > **Environments**.
    
2.  Choose your connection method:
    
    *   **SSH**: In **Git repository URL**, enter the SSH URL for your repository (for example, `git@github.com:username/repo.git`).
        
    *   **HTTPS**: In **Git repository URL** enter the HTTPS URL for your repository (for example, `https://github.com/username/repo.git`).
        
    
3.  Configure authentication based on your connection method:
    
    *   **For SSH**: n8n supports ED25519 and RSA public key algorithms. ED25519 is the default. Select **RSA** under **SSH Key** if your git host requires RSA. Copy the SSH key.
        
    *   **For HTTPS**: Enter your credentials:
        
        *   **Username**: Your Git provider username.
            
        *   **Token**: Your Personal Access Token (PAT) from your Git provider.
            
        
    

Step 3: Set up authentication[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#step-3-set-up-authentication)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Configure authentication based on your chosen connection method.

### SSH authentication (using deploy keys)[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#ssh-authentication-using-deploy-keys)

Set up SSH access by creating a deploy key for the repository using the SSH key from n8n. The key must have write access.

The steps depend on your Git provider. Help links for common providers:

*   [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
    
*   [GitLab | Deploy keys](https://docs.gitlab.com/ee/user/project/deploy_keys/)
    

### HTTPS authentication (using Personal Access Tokens)[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#https-authentication-using-personal-access-tokens)

Create a Personal Access Token (PAT) with repository access permissions.

Help links for creating PATs with common providers:

*   [GitHub | Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
    
*   [GitLab | Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
    
*   [Bitbucket | App passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)
    

Required permissions for your token:

*   Repository read/write access
    
*   Contents read/write (for GitHub)
    
*   Source code pull/push (for GitLab)
    

#### Git hosts with a private certificate authority[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#git-hosts-with-a-private-certificate-authority)

**Feature availability**

Private certificate authorities for Git connections are available from n8n 2.40.0.

If your Git host uses a certificate from a private certificate authority (CA), set the `GIT_SSL_CAINFO` environment variable on the n8n instance to the path of a PEM file that contains the CA certificate. Git uses its own trust store, so the [custom certificate authority](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities)
 configuration for n8n doesn't apply to Git connections. If you keep the certificates in a directory indexed with `c_rehash`, set `GIT_SSL_CAPATH` to the directory instead.

The file or directory replaces the default trust store for Git. If the instance also connects to public Git hosts, include their root certificates.

Step 4: Connect n8n and configure your instance[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#step-4-connect-n8n-and-configure-your-instance)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  In **Settings** > **Environments** in n8n, select **Connect**. n8n connects to your Git repository.
    
2.  Under **Instance settings**, choose which branch you want to use for the current n8n instance.
    
3.  **Optional**: select **Protected instance** to prevent users editing source-controlled resources in this instance. This is useful for protecting production instances.
    
4.  **Optional**: choose a custom color for the instance. This will appear in the menu next to the source control push and pull buttons. It helps users know which instance they're in.
    
5.  Select **Save settings**.
    

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Use Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
    
*   [Choose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
    
*   [Push and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
    
*   [Compare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
    
*   [Move work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousChoose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
[NextPush and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)

Last updated 10 days ago

Was this helpful?