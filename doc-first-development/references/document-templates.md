# 文档模板

只复制当前任务需要的模板，并把占位内容替换为项目事实。不要保留无意义的示例文字。

## `AGENTS.md`

```md
# AGENTS.md

## 项目

- 目标：<一句话说明产品和用户价值>
- 用户：<主要用户>
- 技术栈：<语言、框架、包管理器>
- 入口：<主要运行入口>

## 文档地图

- 架构：[ARCHITECTURE.md](ARCHITECTURE.md)
- 计划：[docs/PLANS.md](docs/PLANS.md)
- 产品规格：[docs/product-specs/index.md](docs/product-specs/index.md)
- 设计：[docs/DESIGN.md](docs/DESIGN.md)
- 前端：[docs/FRONTEND.md](docs/FRONTEND.md)
- 质量：[docs/QUALITY_SCORE.md](docs/QUALITY_SCORE.md)
- 可靠性：[docs/RELIABILITY.md](docs/RELIABILITY.md)
- 安全：[docs/SECURITY.md](docs/SECURITY.md)

## 验证

- 安装：`<command>`
- 测试：`<command>`
- Lint：`<command>`
- 构建：`<command>`

## 必须遵守

- 按任务规模更新受影响文档，沿用已有布局；用户要求先审阅或存在关键待决事项时提供具体审阅对象。
- 同一范围的已有批准持续有效，只确认新增且需要用户决定的部分。
- <项目特有的关键约束>
```

## `ARCHITECTURE.md`

````md
# 架构

状态：草稿
最后验证：<date>

## 系统概览

<2-4 句话说明系统目标和运行形态。>

## 模块与边界

| 模块 | 职责 | 拥有的数据 | 不允许依赖 |
| --- | --- | --- | --- |
| <module> | <responsibility> | <data> | <constraint> |

## 依赖方向

```text
<调用方> -> <被调用方>
```

## 运行时与数据归属

- <进程、服务或客户端边界>
- <主要数据存储及归属>

## 外部集成

- <service/link/constraint>

## 架构不变量

- <invariant>
  - 强制方式：<test/lint/script/manual check>

## 风险与待治理项

- <risk and owner>
````

## 执行计划

```md
# <任务名>

状态：待审阅
负责人：<name>

## 目标

<1-3 句话说明结果。>

## 范围

- 包含：<in scope>
- 不包含：<out of scope>

## 现状与假设

- <known fact>
- 待确认：<unknown>

## 子任务

- [ ] <子任务 1>
  - 涉及：<files/modules>
  - 验收：<observable result>
- [ ] <子任务 2>
  - 涉及：<files/modules>
  - 验收：<observable result>

## 依赖与工具

- <MCP or dependency, or "无">
- 不使用时的替代方案：<fallback>

## 风险与回滚

- 风险：<risk>
- 回滚：<revert strategy>

## 验证

- <test/build/lint>
- <manual or browser check>
- <data or observability check>

## 进度记录

- <date>：<progress>

## 决策记录

- <date>：<decision and reason>

## 完成后的文档更新

- [ ] 更新 `ARCHITECTURE.md` / 产品规格 / 其他专题文档
- [ ] 将本计划移动到 `docs/exec-plans/completed/`
```

## 产品规格

```md
# <功能名>

状态：草稿

## 用户问题

<who has what problem, with what evidence>

## 目标用户

- <primary user>

## 核心流程

1. <step>
2. <step>

## 边界与失败状态

- <empty/loading/error/permission/limit>

## 验收标准

- [ ] <observable user outcome>
- [ ] <edge case>

## 指标与观测

- <metric or signal>
```

## 技术设计

```md
# <设计名>

状态：草稿

## 问题

<problem and constraints>

## 方案

<chosen design>

## 备选方案

| 方案 | 优点 | 缺点 | 不采用原因 |
| --- | --- | --- | --- |
| <option> | <pros> | <cons> | <reason> |

## 边界与依赖

- <boundary>
- <dependency>

## 失败与回滚

- <failure mode>
- <rollback>

## 验证

- <test or proof>
```

## 计划索引

```md
# 计划

## 当前任务

### <task>

- 状态：待审阅
- 目标：<goal>
- 范围：<scope>
- 验收：<acceptance>
- 验证：<verification>
- 执行计划：<link or "不适用">

## 活跃执行计划

| 计划 | 状态 | 负责人 | 开始时间 |
| --- | --- | --- | --- |
| <link> | <status> | <owner> | <date> |
```

## 设计文档索引

```md
# 设计文档

| 文档 | 状态 | 归属 | 最后验证 |
| --- | --- | --- | --- |
| <link> | <status> | <owner> | <date> |
```

## 产品规格索引

```md
# 产品规格

| 规格 | 状态 | 归属 | 最后验证 |
| --- | --- | --- | --- |
| <link> | <status> | <owner> | <date> |
```

## 生成型文档

```md
# <generated artifact>

状态：待更新
数据来源：<source>
生成命令：`<command>`
生成时间：<date or version>
允许手工修改：否

## 内容

<generated content>
```

## 核心工程原则

```md
# 核心工程信念

## <principle>

- 规则：<what must remain true>
- 原因：<why>
- 强制方式：<test/lint/review/script>
- 例外：<allowed exceptions>
```

## 专题文档

`DESIGN.md`、`FRONTEND.md`、`PRODUCT_SENSE.md`、`QUALITY_SCORE.md`、`RELIABILITY.md` 和 `SECURITY.md` 使用同一基本结构：

```md
# <主题>

状态：草稿
最后验证：<date>

## 目标

<what this document protects>

## 不变量

- <rule and enforcement>

## 当前约定

- <convention>

## 已知风险

- <risk and owner>

## 何时更新

- <trigger>

## 验证方式

- <check>
```

## 技术债追踪

```md
# 技术债

| 事项 | 影响 | 优先级 | 归属 | 计划 | 状态 |
| --- | --- | --- | --- | --- | --- |
| <item> | <impact> | <P0-P3> | <owner> | <plan> | <status> |
```
