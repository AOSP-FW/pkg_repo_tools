from typing import List
import bs4
from bs4 import BeautifulSoup
from pkg_repo_tools.models.repo import RepoLink
from pkg_repo_tools.utils.my_exceptions import ParseException

def marshalRepoLinks(html: str) -> List[RepoLink]:
    """ 给定一个 html，提取其中的 RepoLink。"""
    soup = BeautifulSoup(html, features="html.parser")
    repo_list_items = soup.find_all("a", class_="RepoList-item")
    repos = []
    for item in repo_list_items:
        item: bs4.element.Tag = item
        href = item.href # get href

        tag_name = item.findChild(class_="RepoList-itemName")
        if not tag_name or not tag_name.contents:
            raise ParseException(msg="name desc error")
        elif len(tag_name) > 1:
            raise ParseException(msg="name's num more than 1")
        name = tag_name.contents[0] # get name

        tag_desc = item.findChild(class_="RepoList-itemDescription")
        if not tag_desc:
            raise ParseException(msg="tag desc error")
        desc = tag_desc.contents[0] if len(tag_desc.contents) > 0 else "" # get desc

        repos.append(RepoLink(name, desc, href))
    return repos