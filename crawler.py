from pkg_repo_tools.services.repo_link import RepoLinkService

with open("framework.repo.list", "w") as f:
    repo_link_list = RepoLinkService.getRepoLinkListByPrefix("platform/frameworks")
    for link in repo_link_list:
        f.write(link.name[len("platform/"):] + "\n")
