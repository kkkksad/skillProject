# 我的 AI 开发 Skills

覆盖项目规划、功能开发、需求变更、Bug 修复及知识沉淀。点击中文名称查看用途、适用时机和使用示例。

共 15 个技能：从项目提取 13 个，保留原有 2 个。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [开发与协作规范](project-dev-standards/README.md) | 定义代码风格、命名、Git 提交和协作规则。 |
| [项目初始化](project-initialization/README.md) | 依据规格创建目录、配置并初始化工程。 |
| [产品概述](project-product-overview/README.md) | 整理产品愿景、用户、场景、模块和验收标准。 |
| [项目需求澄清](project-requirements-clarification/README.md) | 通过提问明确目标用户、核心价值和关键特性。 |
| [开发路线图](project-roadmap-planning/README.md) | 根据模块依赖划分阶段和里程碑。 |
| [项目结构设计](project-structure/README.md) | 设计项目目录、模块职责和依赖关系。 |
| [技术栈选型](project-tech-stack/README.md) | 结合业务需求比较并确定技术方案。 |
| [已有功能变更](feature-evolution/README.md) | 分析变更影响，同步规格并形成增量任务。 |
| [功能编码实现](feature-implementation/README.md) | 按 RED → GREEN → REFACTOR 实现指定阶段，并执行适用验收。 |
| [功能需求澄清](feature-requirements-clarification/README.md) | 梳理场景、业务规则、边界和验收标准 AC。 |
| [功能任务拆解](feature-task-planning/README.md) | 按依赖和阶段拆分适合 TDD 的开发任务。 |
| [功能技术设计](feature-tech-design/README.md) | 设计 API、数据模型、核心逻辑和 AC 覆盖关系。 |
| [Bug 修复工作流](bugfix-workflow/README.md) | 定位原因、修复错误并记录验证结果。 |
| [文档优先开发](doc-first-development/README.md) | 维护中文文档体系、设计计划和开发审阅流程。 |
| [Steiner Archive 知识贡献](steiner-archive-contribution/README.md) | 按仓库规范整理文章、提示词和 Agent Skills。 |

## 推荐使用顺序

- 新项目：需求澄清 → 产品概述 → 技术选型 → 项目结构 → 开发规范 → 路线图 → 初始化。
- 新功能：功能需求澄清 → 技术设计 → 任务拆解 → 按阶段编码与验收。
- 已有功能调整：feature-evolution 管理变更，再执行对应开发任务。
- 行为不符合既定需求：bugfix-workflow。

## 使用与安装

1. 选择技能并阅读对应 README.md。
2. 将完整技能文件夹复制到 AI 工具支持的技能目录。Codex 通常使用 ~/.codex/skills/，保留 SKILL.md 和全部资源。
3. 按工具要求刷新或重启会话，通过技能名称或使用示例调用。
4. 技能中的 specs/ 路径通常指正在开发的目标项目。需准备项目自身的上下文及前置规格；具体条件以各 SKILL.md 为准。

随附的 [上下文规则](docs/specs/PROJECT-CONTEXT.md) 和 [阶段边界规则](docs/specs/GUARDRAILS.md) 是源资料中的通用规则，供按项目需要选用，不会自动安装到目标项目。部分技能提及 Playwright MCP、Supabase MCP 或任务工具，使用时需要相应环境或明确适配方案。

## 来源与随附资料

- [Skills 工作流 V3 版本介绍](docs/Skills工作流V3版本介绍.md)。原介绍使用 SpecForge V3 名称，原文保留。
- 本次提取来源：项目内 docs/开发SKILLS/skills/。13 个技能及模板资源原样复制，新增 README.md 用于展示。
- doc-first-development、steiner-archive-contribution 是目标文件夹原有技能，原定义和资源保留。
- 将本文件夹内容上传到 GitHub 仓库根目录即可展示首页，打开任一技能目录会展示其中文说明。
- 本次未新增许可证或改变原内容授权。
