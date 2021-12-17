from typing import List
from pkg_repo_tools.models.repo import RepoLink
from pkg_repo_tools.utils.my_requests import MyRequest
from pkg_repo_tools.utils.my_htm_parser import marshalRepoLinks

class RepoLinkService:

    @classmethod
    def getRepoLinkListByPrefix(cls, prefix: str) -> List[RepoLink]:
        """
        :param prefix:  prefix of repo
        """
        resp = MyRequest.get(url="")
        repo_links = marshalRepoLinks(resp.text)
        return [
            link for link in repo_links
            if link.name.startswith(prefix)
        ]
