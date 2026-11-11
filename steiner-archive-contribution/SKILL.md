---
name: steiner-archive-contribution
description: 在 Steiner Archive 仓库中新增、修订或发布知识文章、提示词片段和 Agent Skills；按仓库现有的 content、templates、状态字段、校验脚本与 Git MR 流程沉淀经过验证的团队记忆。
metadata:
  short-description: 按 Steiner Archive 规范贡献可验证的团队知识
---

# Steiner Archive 知识贡献

只在目标仓库是 Steiner Archive 知识站时使用本 skill。典型识别标志是仓库根目录同时存在 `content/`、`templates/` 和 `package.json`。它不替代通用文档优先开发流程；该仓库已经有自己的内容结构和发布规范。

官方入口：[贡献一份记忆](http://frontend.gitlab.roboticplus.com:2022/reading-steiner/steiner-archive/getting-started/contributing/)。

## 开始前

1. 读取仓库根目录的 `AGENTS.md`（如存在）、`package.json`、相关 `templates/` 模板和同类 `content/` 记录。
2. 检查工作区状态，确认不会覆盖用户已有改动。
3. 以仓库当前模板、类型定义和脚本为准。官方站点与本 skill 不一致时，采用仓库事实，并指出需要同步的规范。
4. 判断贡献类型，只读取需要的说明：
   - 知识文章、领域记录、ADR、排障记录：读 [content-records.md](references/content-records.md)。
   - 可复制、可填空的提示词片段：读 [prompt-snippets.md](references/prompt-snippets.md)。
   - Steiner Archive 自身的 Agent Skill：读 [agent-skills.md](references/agent-skills.md)。
   - 提交前检查、预览和 Git MR：读 [validation-and-publishing.md](references/validation-and-publishing.md)。

## 不可跳过的规则

- 从真实问题和现场证据出发。不要编造维护人、适用范围、模型效果、测试结果或核验日期。
- 未完成实际验证或审查时使用 `draft`；只有证据充分且审查完成后才能使用 `reviewed`。
- 环境、版本或适用边界变化后，重新验证再更新 `lastVerified`。不要仅因编辑文字而刷新核验日期。
- 优先修订现有记录并保留历史决策。弃用记录要保留原因和替代入口。
- 使用仓库模板和目标目录，不要套用通用 `docs/` 骨架，也不要手工修改生成的站点页面。
- 没有明确授权时，不执行 `git commit`、`git push`、创建 MR 或合并操作。

## 完成工作

运行仓库定义的验证命令；如果内容贡献没有特殊说明，至少检查 `pnpm check`、`pnpm build` 和 `pnpm check:links`。涉及提示词交互、搜索或 Skills 同步时，再读取发布说明并补充相应检查。

最终汇报：

- 新增或修改了哪些记录。
- 使用了哪些真实证据，哪些内容仍是 `draft`。
- 执行了哪些命令及结果。
- 是否仍需领域维护人、资产维护人或其他人工审查。
- 如有失败或未验证项，明确说明，不要用构建成功代替内容验证。
