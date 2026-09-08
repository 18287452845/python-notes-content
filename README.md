# Python 编程基础教学讲义

本仓库是 Python 编程基础课程的 **Markdown 内容仓库**，负责保存讲义正文、课程图片和课程目录。网页模板、样式、构建脚本和 Cloudflare 部署配置位于独立的 [`python-notes-site`](https://github.com/18287452845/python-notes-site) 仓库。

## 目录

- `01-基础语法/`
- `02-数据结构/`
- `03-函数与模块/`
- `04-文件与异常/`
- `05-面向对象/`
- `06-基础项目/`
- `拓展-办公自动化/`
- `拓展-Web与爬虫/`
- `拓展-数据分析/`
- `拓展-机器学习/`
- `archive/`

基础课建议按 `01-基础语法` → `02-数据结构` → `03-函数与模块` → `04-文件与异常` → `05-面向对象` → `06-基础项目` 的顺序使用。

## 内容规范

- 原始讲义以 Markdown 为准，网页中的讲义页面由构建脚本自动生成。
- 图片放在对应章节的 `assets/` 目录，讲义中优先使用相对路径引用。
- 每篇讲义结尾使用 `### 知识点总结`，总结应覆盖概念、操作方法、代码要点、命名规则、注意事项和学习重点。
- 代码示例保持初学者可读，使用明确的语言标记，例如 ` ```python `。
- 数学公式使用 MathJax 支持的 `$...$`、`$$...$$`、`\(...\)` 或 `\[...\]` 格式。
- 不要在代码示例中保留无实际教学作用的 `Version: 1.0`、`Author: XX` 模板信息。

## 网页同步

Markdown 提交到 `main` 后，由网页仓库的 GitHub Actions 拉取本仓库并重新生成网站：

```text
修改 Markdown 或 assets
        ↓
提交到 python-notes-content/main
        ↓
python-notes-site 定时拉取并构建
        ↓
校验 HTML、目录、资源和代码高亮
        ↓
提交生成后的 public/
        ↓
使用 Wrangler 部署到 Cloudflare Pages
```

默认每 15 分钟同步一次。如果配置了内容仓库的 `SITE_REPO_DISPATCH_TOKEN`，也可以在内容提交后立即通知网页仓库开始同步。

## GitHub 仓库

- 内容仓库：[`18287452845/python-notes-content`](https://github.com/18287452845/python-notes-content)
- 网页仓库：[`18287452845/python-notes-site`](https://github.com/18287452845/python-notes-site)

修改讲义时只提交内容仓库；修改网页布局、目录交互、代码高亮或构建逻辑时提交网页仓库。不要手动编辑网页仓库中的生成 HTML。

## 仓库与网页同步

- 本仓库是 Markdown 内容仓库：`python-notes-content`。
- 网页模板、构建脚本和生成页面位于独立的 `python-notes-site` 仓库。
- 修改 Markdown 后，网页仓库会定时拉取本仓库并重新生成网页；配置 `SITE_REPO_DISPATCH_TOKEN` 后可以在提交后立即触发同步。
- 网页仓库构建成功后通过 GitHub Actions 使用 Wrangler 部署到现有 Cloudflare Pages 项目 `python-notes`。
