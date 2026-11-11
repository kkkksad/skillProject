#!/usr/bin/env python3
"""Create missing repository documentation files without overwriting existing ones."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


AGENTS = """# AGENTS.md

## 项目

- 目标：待确认
- 用户：待确认
- 技术栈：待确认
- 入口：待确认

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

- 安装：待确认
- 测试：待确认
- Lint：待确认
- 构建：待确认

## 必须遵守

- 按任务规模更新受影响的文档，沿用已有文档布局。
- 用户要求先审阅或存在影响范围的关键待确认项时，先提交具体文档供审阅。
- 同一范围的已有批准持续有效；范围变化时只确认新增决策。
"""

ARCHITECTURE = """# 架构

状态：草稿
最后验证：待确认

## 系统概览

待确认。

## 模块与边界

| 模块 | 职责 | 拥有的数据 | 不允许依赖 |
| --- | --- | --- | --- |
| 待确认 | 待确认 | 待确认 | 待确认 |

## 依赖方向

待确认。

## 运行时与数据归属

- 待确认。

## 外部集成

- 待确认。

## 架构不变量

- 待确认。

## 风险与待治理项

- 待确认。
"""

DESIGN_INDEX = """# 设计文档

| 文档 | 状态 | 归属 | 最后验证 |
| --- | --- | --- | --- |
| [核心工程信念](core-beliefs.md) | 草稿 | 待确认 | 待确认 |
"""

CORE_BELIEFS = """# 核心工程信念

状态：草稿

| 原则 | 原因 | 强制方式 | 例外 |
| --- | --- | --- | --- |
| 待确认 | 待确认 | 待确认 | 待确认 |
"""

TECH_DEBT = """# 技术债

状态：待审阅

| 事项 | 影响 | 优先级 | 归属 | 计划 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 暂无已登记事项 | - | - | - | - | - |
"""

PRODUCT_INDEX = """# 产品规格

| 规格 | 状态 | 归属 | 最后验证 |
| --- | --- | --- | --- |
| 待确认 | 草稿 | 待确认 | 待确认 |
"""

PLANS = """# 计划

## 当前任务

### 待确认

- 状态：待审阅
- 目标：待确认
- 范围：待确认
- 验收：待确认
- 验证：待确认
- 执行计划：待确认

## 活跃执行计划

| 计划 | 状态 | 负责人 | 开始时间 |
| --- | --- | --- | --- |
| 暂无 | - | - | - |
"""

DESIGN = """# 设计

状态：草稿
最后验证：待确认

## 目标

待确认。

## 不变量

- 待确认。

## 当前约定

- 待确认。

## 已知风险

- 待确认。

## 何时更新

- 待确认。

## 验证方式

- 待确认。
"""

TOPIC_TITLES = {
    "docs/FRONTEND.md": "前端",
    "docs/PRODUCT_SENSE.md": "产品判断",
    "docs/QUALITY_SCORE.md": "质量评分",
    "docs/RELIABILITY.md": "可靠性",
    "docs/SECURITY.md": "安全",
}

KEEP_FILES = {
    "docs/exec-plans/active/.gitkeep": "",
    "docs/exec-plans/completed/.gitkeep": "",
    "docs/generated/.gitkeep": "",
    "docs/references/.gitkeep": "",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a missing documentation harness in a repository."
    )
    parser.add_argument("repo", nargs="?", default=".", help="Repository root")
    parser.add_argument(
        "--task-title",
        help="Create an active execution plan with this title",
    )
    parser.add_argument(
        "--task-slug",
        help="Filename slug for the active execution plan; defaults to the title",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report files that would be created without writing them",
    )
    args = parser.parse_args()
    if args.task_slug is not None and not args.task_title:
        parser.error("--task-slug requires --task-title")
    if args.task_title is not None and not args.task_title.strip():
        parser.error("--task-title must not be blank")
    return args


def execution_plan(title: str) -> str:
    return f"""# {title}

状态：待审阅

## 目标

待确认。

## 范围

- 包含：待确认
- 不包含：待确认

## 子任务

- [ ] 待拆分
  - 涉及：待确认
  - 验收：待确认

## 依赖与工具

- 无，或待确认。

## 风险与回滚

- 风险：待确认。
- 回滚：待确认。

## 验证

- 待确认。

## 进度记录

- 待确认。

## 决策记录

- 待确认。

## 完成后的文档更新

- [ ] 更新受影响的专题文档
- [ ] 将本计划移动到 `docs/exec-plans/completed/`
"""


def slugify(value: str) -> str:
    slug = re.sub(r"[\W_]+", "-", value.lower()).strip("-")
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:10]
    if not slug:
        return f"task-{digest}"
    if re.fullmatch(r"con|prn|aux|nul|com[1-9]|lpt[1-9]", slug):
        slug = f"task-{slug}"
    if len(slug) > 80:
        slug = f"{slug[:64].rstrip('-')}-{digest}"
    return slug


def topic_document(title: str) -> str:
    return f"""# {title}

状态：草稿
最后验证：待确认

## 目标

待确认。

## 不变量

- 待确认。

## 当前约定

- 待确认。

## 已知风险

- 待确认。

## 何时更新

- 待确认。

## 验证方式

- 待确认。
"""


def build_files(task_title: str | None, task_slug: str | None) -> dict[str, str]:
    files = {
        "AGENTS.md": AGENTS,
        "ARCHITECTURE.md": ARCHITECTURE,
        "docs/design-docs/index.md": DESIGN_INDEX,
        "docs/design-docs/core-beliefs.md": CORE_BELIEFS,
        "docs/exec-plans/tech-debt-tracker.md": TECH_DEBT,
        "docs/product-specs/index.md": PRODUCT_INDEX,
        "docs/PLANS.md": PLANS,
        "docs/DESIGN.md": DESIGN,
    }
    files.update(KEEP_FILES)
    for relative_path, title in TOPIC_TITLES.items():
        files[relative_path] = topic_document(title)

    if task_title:
        slug = slugify(task_slug or task_title)
        files[f"docs/exec-plans/active/{slug}.md"] = execution_plan(task_title)

    return files


def main() -> int:
    args = parse_args()
    root = Path(args.repo).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Repository root not found: {root}")

    files = build_files(args.task_title, args.task_slug)
    if args.task_title:
        relative_plan = f"docs/exec-plans/active/{slugify(args.task_slug or args.task_title)}.md"
        plan = root / relative_plan
        if plan.exists():
            if not plan.is_file():
                raise SystemExit(f"Plan path is not a file: {relative_plan}; choose another --task-slug")
            first_line = plan.read_text(encoding="utf-8").splitlines()[:1]
            if first_line != [f"# {args.task_title}"]:
                raise SystemExit(
                    f"Plan already belongs to another task: {relative_plan}; "
                    "choose a unique --task-slug. No files were changed."
                )
    directories = {
        "docs/exec-plans/active",
        "docs/exec-plans/completed",
        "docs/generated",
        "docs/references",
    }

    created: list[Path] = []
    skipped: list[Path] = []

    for relative_dir in sorted(directories):
        path = root / relative_dir
        if args.dry_run:
            continue
        path.mkdir(parents=True, exist_ok=True)

    for relative_path, content in files.items():
        path = root / relative_path
        if path.exists():
            skipped.append(path)
            continue
        created.append(path)
        if not args.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    action = "Would create" if args.dry_run else "Created"
    for path in created:
        print(f"{action}: {path.relative_to(root)}")
    for path in skipped:
        print(f"Skipped existing: {path.relative_to(root)}")

    if not created:
        print("Documentation baseline already exists; review and update it instead.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
