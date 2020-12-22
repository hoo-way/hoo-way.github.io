# Markdown4Zhihu

将Markdown文件的本地图片替换为github.io上的网络图片。

## 环境
1. 安装python3
2. 安装 `ipi3 install pillow `
3. 安装 `ipi3 install pathlib2 `

## 使用方法

1. 按照这个（https://pages.github.com/）常见一个github.io的仓库。复制一份这个仓库中的内容到你的仓库（https://github.com/hoo-way/hoo-way.github.io）

2. 然后，打开`doc4zhihu/zhihu-publisher.py`文件，在文件开头有这么一句：`GITHUB_REPO_PREFIX = "https://hoo-way.github.io/doc4zhihu/data/"`请修改`hoo-way`为您自己的GitHub用户名

3. 这里我们假设您的文件名为`README.md`，并将其和图片文件夹放到`Data`目录下，接着打开terminal(Linux/MacOS)或Git Bash(Windows)(或其他任何支持Git命令的终端)，输入以下命令：

`python3 zhihu-publisher.py --input="./data/README.md"`

4. OK，all set. 在`data`目录下，你可以看到一个`README_for_zhihu.md`的文件，将它上传至知乎编辑器即可。

Note:在上传前，先用浏览器验证一下README_for_zhihu.md中生成的图片可以访问
