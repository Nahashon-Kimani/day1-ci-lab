#!/bin/bash
# git init creates a new git repository in the current directory
git init

# git add adds files to the staging area, preparing them for commit
git add .

# git commit creates a new commit with the changes that have been staged, along with a message describing the commit
git commit -m "first commit"

# git branch renames the current master branch to main. 
git branch -M main 

# git remote adds a remote repository to the local repository, allowing you to push and pull changes to and from the remote repository. 
# In this case, we are adding a remote repository named "origin" with the URL of the GitHub repository where we want to push our code.
git remote add origin https://github.com/Nahashon-Kimani/intro-to-cicd.git

# git push pushes the changes in the local repository to the remote repository
git push -u origin main