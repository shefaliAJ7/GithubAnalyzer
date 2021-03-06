#Dummy file to simulate and test under development python classes



#import statements
from github import Github
from .GitConnectionManager import GitConnectionManager

from .GitCommitData import GitCommitData

from .GitPullRequestData import GitPullRequestData
from .GitCollaboratorData import GitCollaboratorData
from .DatabaseManager import DatabaseManager


#----------------------------------------------------------------------------------------
#Sample code to iterate through all the repositories belonging to a user_
#_and print all the collaborators in each repository

#g = Github("username", "password")

#for repo in g.get_user().get_repos():
#    print(repo.name)
#    #print(dir(repo))

#    for user in repo.get_collaborators():
#        print(" - " + user.login)



#----------------------------------------------------------------------------------------
#Sample code showing an example of how to validate a repository on gitHub_
#_using the GitConnectionManager class

#manager = GitConnectionManager()

#if(manager.isValidRepository("sarthak-tiwari/ScrumDevils-SER_515")):
#    print("valid repo")
#else:
#    print("invalid repo")



#----------------------------------------------------------------------------------------
#Sample code showing two ways of how to get a list of collaborators in a_
#_repository using the GitData class

#manager = GitConnectionManager()

#gitData = GitData(manager.getConnection())

##--(1)
#for user in gitData.getUserList("ScrumDevils-SER_515"):
#    print(user)

##--(2)
#gitData.setGitHubRepository("ScrumDevils-SER_515")
#for user in gitData.getUserList():
#    print(user)



#----------------------------------------------------------------------------------------
#Sample code showing how to get a list of commits in a_
#_repository using the GitCommitData class
#manager = GitConnectionManager()

#gitData = GitCommitData(manager.getConnection())
#gitData.setGitHubRepository("ScrumDevils-SER_515")

#result = gitData.getCommitData()

#print("Count of Commits: " + str(len(result)))

#for commit in result:
#    print(commit.commiterName)
#    print(commit.commitDate)
#    print("Number of Additions: " + str(commit.numberOfAdditions))
#    print("Number of Deletions: " + str(commit.numberOfDeletions))
#    print("Files Modified: " + commit.filesModified)
#    print("Link: " + commit.linkToGithub)
#    print(commit.commitMessage)
#    print("----------\n")



#----------------------------------------------------------------------------------------
#Sample code showing how to get a list of pull requests in a_
#_repository using the GitPullRequestData class
#manager = GitConnectionManager()

#gitData = GitPullRequestData(manager.getConnection())
#gitData.setGitHubRepository("ScrumDevils-SER_515")

#(pullRequestData, pullReviewData) = gitData.getPullRequestData()

#DatabaseManager.insertPullRequestDataValues(pullRequestData)
#DatabaseManager.insertPullReviewDataValues(pullReviewData)



#----------------------------------------------------------------------------------------
#Sample code testing DatabaseManager Class

#manager = GitConnectionManager()

#gitData = GitCommitData(manager.getConnection())
#gitData.setGitHubRepository("ScrumDevils-SER_515")

#result = gitData.getCommitData()

#DatabaseManager.insertCommitDataValues("ScrumDevils-SER_515", result)

#manager = GitConnectionManager()
#gitData = GitCommitData(manager.getConnection())
#gitData.setGitHubRepository("ScrumDevils-SER_515")

#gitData.test()



#----------------------------------------------------------------------------------------
#Sample code testing GitCollaboratorData Class

#manager = GitConnectionManager()

#gitData = GitCollaboratorData(manager.getConnection())
#gitData.setGitHubRepository("ScrumDevils-SER_515")

#result = gitData.getCollaboratorData()
#DatabaseManager.insertCollaboratorDataValues("sarthak-tiwari/ScrumDevils-SER_515", result)



#----------------------------------------------------------------------------------------
#Sample code testing DatabaseManager Class

def getDataFromGitHubIntoDB(repositoryName):

	manager = GitConnectionManager()

	collaboratorData = GitCollaboratorData(manager.getConnection()).getCollaboratorData(repositoryName)
	print("Got Collaborator Data !")
	commitData = GitCommitData(manager.getConnection()).getCommitData(repositoryName)
	print("Got Commit Data !")
	(pullRequestData, pullReviewData) = GitPullRequestData(manager.getConnection()).getPullRequestData(repositoryName)
	print("Got Pull Request Data !")

	DatabaseManager.populateRepository(repositoryName, collaboratorData, commitData, pullRequestData, pullReviewData)
	print("Data Inserted !")