# repo_crawler

## 1. Usage

创建虚拟环境，安装对应依赖。此后直接：

```shell
> python crawler.py
```

此后会在 `crawler.py` 同级目录产生一个 `framework.repo.list`，记录 `framework` 中所有 `repo` 级条目。

## 2. Misc

* 是爬虫，`utils/my_requests.py` 里面内置了代理，`HTTP/HTTPS` 端口 7890；
* 也可以使用缓存下来的 `cache-2021-12-17.htm`。
