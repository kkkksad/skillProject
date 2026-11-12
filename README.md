# 我的 AI 开发 Skills

覆盖项目规划、全栈开发、真实联调、发布验收、需求变更及 Bug 修复。完整项目从 [全栈项目流程](fullstack-workflow/README.md) 进入，单项任务直接使用对应技能。

共 17 个技能：原有 15 个，补充统一流程入口与发布交付 2 个。其中 Steiner Archive 是特定仓库扩展，其余用于通用项目；不要求每次运行全部技能。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [全栈项目流程](fullstack-workflow/README.md) | 识别项目现状，调度必要阶段并核对交付范围。 |
| [开发与协作规范](project-dev-standards/README.md) | 定义代码风格、命名、Git 提交和协作规则。 |
| [项目初始化](project-initialization/README.md) | 依据规格创建目录、配置并初始化工程。 |
| [产品概述](project-product-overview/README.md) | 整理产品愿景、用户、场景、模块和验收标准。 |
| [项目需求澄清](project-requirements-clarification/README.md) | 通过提问明确目标用户、核心价值和关键特性。 |
| [开发路线图](project-roadmap-planning/README.md) | 根据模块依赖划分阶段和里程碑。 |
| [项目结构设计](project-structure/README.md) | 设计项目目录、模块职责和依赖关系。 |
| [技术栈选型](project-tech-stack/README.md) | 结合业务需求比较并确定技术方案。 |
| [已有功能变更](feature-evolution/README.md) | 分析变更影响，同步规格并形成增量任务。 |
| [功能编码实现](feature-implementation/README.md) | 按任务规模实现阶段或完整功能，并执行适用验收。 |
| [功能需求澄清](feature-requirements-clarification/README.md) | 梳理场景、业务规则、边界和验收标准 AC。 |
| [功能任务拆解](feature-task-planning/README.md) | 按依赖和阶段拆分适合 TDD 的开发任务。 |
| [功能技术设计](feature-tech-design/README.md) | 设计前端交互、API 契约、数据模型与 AC 覆盖关系。 |
| [Bug 修复工作流](bugfix-workflow/README.md) | 定位原因、修复错误并记录验证结果。 |
| [发布与交付验收](project-release/README.md) | 核对配置、迁移与恢复，执行授权内发布及目标环境冒烟。 |
| [文档优先开发](doc-first-development/README.md) | 按任务规模维护文档和计划，需要审阅时提供具体对象。 |
| [Steiner Archive 知识贡献](steiner-archive-contribution/README.md) | 按仓库规范整理文章、提示词和 Agent Skills。 |

## 推荐使用顺序

- 完整项目：使用 fullstack-workflow 作为入口，按现状跳过已满足的阶段；单次需求或设计任务不必使用总入口。
- 新项目：需求澄清 → 产品概述 → 技术选型 → 项目结构/开发规范 → 路线图 → 初始化 → 按功能切片开发与真实联调 → 按约定发布交付。
- 新功能：功能需求澄清（仅信息不足时）→ 技术设计 → 任务拆解 → 按阶段编码与验收；已确认信息复用。
- 已有功能调整：feature-evolution 管理变更，再执行对应开发任务。
- 行为不符合既定需求：bugfix-workflow。
- 发布准备/测试环境部署/上线：project-release；只要求准备时完成审查结果后停止，明确授权部署时继续验证目标环境。

例如：

> 用 $fullstack-workflow 从零完成一个预约管理系统，先明确最小业务范围，开发到本地可运行并验收。

> 用 $fullstack-workflow 接手这个项目，完成评论列表和真实接口联调，部署到已配置的测试环境。

技术栈、框架和平台遵循项目约束；不强制前后端分离、Docker、微服务或某个数据库。纯前端、纯 API、离线工具按实际边界裁剪步骤。

## 使用与安装

1. 选择技能并阅读对应 README.md。
2. 将完整技能文件夹复制到 AI 工具支持的技能目录。Codex 通常使用 ~/.codex/skills/，保留 SKILL.md 和全部资源。
3. 按工具要求刷新或重启会话，通过技能名称或使用示例调用。
4. `specs/`、`docs/` 指目标项目，`assets/`、`references/`、`scripts/` 指当前技能目录。新项目默认使用 `specs/`；已有项目沿用原文档布局并记录路径映射。前置条件看实际信息是否明确，不仅看固定文件名是否存在。

使用统一流程时建议一起安装通用阶段技能；只需要某一项时可单独安装。doc-first-development 在用户要求文档体系或仓库采用文档优先时配合使用；Steiner Archive 仅按其仓库场景安装。与其他流程类技能同时使用时复用同一份需求、设计、计划和验收证据，避免重复澄清、审批和建档。

随附的 [上下文规则](docs/specs/PROJECT-CONTEXT.md) 和 [阶段边界规则](docs/specs/GUARDRAILS.md) 可按项目需要选用，不会自动安装到目标项目。单个技能包含必要的上下文和边界说明，缺少这两个公共文件也可执行。

## 执行模式

- 轻量修改：目标明确、局部且低风险，直接实现并做相称验证，不强制生成完整规格和报告。
- 普通功能：保留需求/AC、设计、任务与验证的追溯，复用已有文档。
- 重大变更：明确影响、风险、兼容性、回滚与验收；关键决策未确认时先给具体审阅对象。
- 用户只要求规划或文档时完成相应产出后停止；明确要求端到端完成时衔接后续步骤，同一范围的已有确认持续有效。
- 本地实现与验收、发布准备、目标环境发布分别记录；没有远端部署请求时不自行发布。

验证优先使用实际可用工具：浏览器 MCP 或 Playwright CLI、匹配数据库的客户端或集成测试、环境中的任务工具或 Markdown 清单均可。不依赖特定 MCP 品牌；关键验收无法执行时标为未验证。

## 验证维护

文档骨架脚本的回归测试只写入临时目录，在本仓库根目录执行：

```sh
python -m unittest discover -s doc-first-development/tests -v
```

还应检查各技能的 frontmatter、相对资源路径、阶段交接和实际场景行为。格式检查通过不等于已在真实项目端到端验证。当前职责划分、冲突调整和推荐裁剪见 [全栈流程检查](docs/全栈Skill流程检查.md)。

## 来源与随附资料

- [Skills 工作流 V3 版本介绍](docs/Skills工作流V3版本介绍.md)。原介绍使用 SpecForge V3 名称，原文保留。
- 原始提取来源：项目内 docs/开发SKILLS/skills/。初次提取时保留了 13 个技能及模板资源；后续维护补齐了路径交接、执行模式、全栈联调与发布流程。
- doc-first-development、steiner-archive-contribution 是目标文件夹原有技能；当前维护保持各技能职责与来源说明。
- 将本文件夹内容上传到 GitHub 仓库根目录即可展示首页，打开任一技能目录会展示其中文说明。
- 本次未新增许可证或改变原内容授权。
