Created new repository
"Practice"

copied the url from middle right side:

https://github.com/austinmeier/practice.git

#typed in:
$git clone https://github.com/austinmeier/practice.git

#this downloads the repository
#the repository is stored in a directory on the computer where you were when you executed "git clone"
#to check the differences between the repo on your machine, and the one in the git cloud, type:

$git status

#you have to have cd "REPO_NAME" before typing that
#it will show you what is different

### step one of the commit ###
#type:

$git add FILE_NAME

#where "FILE_NAME" is the file that was different between local and git versions.
#you can use the command:

$git add .
#or
$git add -A

#these will preload every file in the folder
#this preloads the files to be committed
#to sync to the mothership type:

$git push

#this returns a warning message about the changes to git... unknown what to do with this information:
    warning: push.default is unset; its implicit value has changed in
    Git 2.0 from 'matching' to 'simple'. To squelch this message
    and maintain the traditional behavior, use:
    git config --global push.default matching

    To squelch this message and adopt the new behavior now, use:

    git config --global push.default simple

    When push.default is set to 'matching', git will push local branches
    to the remote branches that already exist with the same name.

    Since Git 2.0, Git defaults to the more conservative 'simple'
    behavior, which only pushes the current branch to the corresponding
    remote branch that 'git pull' uses to update the current branch.

    See 'git help config' and search for 'push.default' for further information.
    (the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
    'current' instead of 'simple' if you sometimes use older versions of Git)
    
#after all that, it will ask you for your git username, and password.  Enter them.
###CHANGES##


###changes part 2




