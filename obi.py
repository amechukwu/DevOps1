from github import Github
import yaml
import os
# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('amec0001_credentials.yml'))
# Extract the user and token from the data object
# 0. Complete these 2 lines below
user = 'amechukwu'
token = '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'
# using an access token
g = Github(token)
repo = g.get_repo(user)
## Complete your tasks from here
# 1. Get all branches you have created for your public repo

repo = g.get_repo("PyGithub/PyGithub")
list(repo.get_branches())


# 2. Get all pull requests you have created

repo = g.get_repo("PyGithub/PyGithub")
pr = repo.get_pull(664)
pr


# 3. Get a list of commits you have created in your `main` branch.

commit = repo.get_commit(sha=sha)
print(commit.commit.author.date)
print(commit.commit.committer.date)


