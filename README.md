# 经济地理每日重点简报

目标：https://charon411.github.io/economic-geography-brief/

当前为待发布文件，未确认上线。真实收录：2026-11-01 第34期、2026-11-17 第50期。未找到第51期，未建立占位条目。配色取自第34期。原始简报按字节保留，图片均无本地路径依赖。

## 首次发布
1. 在 Charon411 下创建公开仓库 economic-geography-brief，默认分支 main。
2. 将本目录内容提交至仓库根目录，包括隐藏目录 .github（不需要上传 _site）。
3. 仓库 Settings → Pages → Build and deployment → Source 选择 GitHub Actions。
4. Actions → Publish briefs → Run workflow。等部署成功后打开目标网址核验。

## 后续更新
将实际 HTML 放入 briefs，命名为 YYYY-MM-DD-期号.html，例如真实第51期取得后按其实际日期命名。页面 title 与 subtitle 沿用现有格式。提交到 main 会自动扫描真实文件、校验日期、按日期和期号倒序构建目录并发布。不要上传占位文件。引用本地附件时需一并放入 briefs 并保持相对路径。

这套流程自动发布已经制作并提交的简报，不会自动生成每日研究内容，也不能自动读取 ChatGPT 附件。未来可由有仓库写入权限的简报制作流程提交 HTML，复用同一发布流程。

本地构建：python3 scripts/build.py；index.html 可直接打开，_site 为发布内容。

核验：已验证两份原始文件一致、倒序、链接文件存在与月份数据。尚未完成浏览器交互或 Mac/iPad 实机验证（浏览器连接超时）。
