# 操作指南

- 将文件拷贝到本地仓库

```shell
$ git clone <url> #url在code下拉栏的位置可以找到
$ git clone git@github.com:Katzeee/FileManager.git #我的是这样的
```

- 第一次下载下来请创建本地个人分支

```shell
$ git checkout -b <分支名>
$ git checkout -b xjf
```

- 可以用以下命令检查所在分支

```shell
$ git branch #查看本地所有分支以及当前所在分支
$ git branch -r #查看远程分支
$ git checkout <分支名> #用于切换到其他分支
```

- 每次更改后可以再本地个人分支下进行保存备份

```shell
$ git add <文件名> #将文件保存至暂存区
$ git add . #点表示当前目录下所有文件
$ git status #查看文件状态
$ git commit -m "提交信息" #""中可写本次提交的信息
```

- 更改并commit完成之后，或小阶段完成之后可以上传到远程仓库的个人分支下

```shell
$ git push origin <分支名>
$ git push origin xjf
```

- 如何从远程仓库拉取某个分支的代码，可以是自己上传的，也可以是主分支上的代码

```shell
$ git pull origin <分支1>:<分支2> #将远程分支1上的文件拉到本地分支2上
$ git pull origin master:master #将远程仓库master分支拉到本地仓库master分支，通常在程序改动之后都得拉一次
$ git pull origin master:xjf #将远程仓库master分支拉到本地仓库xjf分支，当想在本地改动时请这么做
```

- 认为程序已经完成之后可以发起pull request，但不要直接merge

