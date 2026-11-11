# Agent Skills

## 源文件

Steiner Archive 自身收录的 Skill 位于 `skills/<name>/SKILL.md`，新建时参考 `templates/skill.md`。站点页面由 `pnpm sync:skills` 生成，不要手工维护生成页面。

- 名称使用小写英文、数字和连字符。
- 顶层 frontmatter 至少包含 `name` 和 `description`。
- 按仓库模板记录维护人、状态、适用范围和核验日期。
- 引用文件与 Skill 放在同一目录，使用相对链接。

模板默认设置 `metadata.internal: true`。模板、实验内容和未发布内容应保持隐藏；只有完成真实任务验证和审查后，才改为 `reviewed` 并移除 `internal`。

`internal` 只控制默认发现，不控制仓库访问权限。Skills CLI 不会根据 `metadata.status` 自动筛选，因此不能把状态字段当成权限边界。

## 内容要求

写清以下信息：

- 何时触发，以及何时不适用。
- 依赖、工具和必要输入。
- 具体操作步骤和需要按需读取的资源。
- 可执行的验证方法。
- 完成标准和已知边界。

说明应保留非显然的决策依据和项目约束，删除泛化常识、重复说明和不必要的脚手架。创建后至少用一个真实任务验证；仅通过格式校验或站点构建不等于 Skill 已验证。

Skill 源文件变化后运行仓库提供的 Skills 同步与检查命令，并检查生成结果是否与源文件一致。未获得用户明确授权时，不提交、不推送、不创建 MR。
