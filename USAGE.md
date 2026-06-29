# 使用说明 · Codex 用法

## 1. 最推荐用法

把整个 `shooting-combat-design-codex` 文件夹放进一个 GitHub 仓库，然后在 Codex 中连接该仓库。

Codex 适合做：

- 根据模板生成 Markdown 策划文档。
- 修改已有文档。
- 批量整理枪械 / 技能 / TTK 报告。
- 把散乱内容整理成固定结构。
- 生成需求文本、验收标准、资源需求表草稿。

Codex 不适合直接替你决定项目最终数值。没有项目数据时，它只能给建议区间和风险判断。

---

## 2. 第一次使用

### Step 1：复制项目约定

从这里复制一份：

```text
conventions/TEMPLATE.md
```

改名，例如：

```text
conventions/my-project.md
```

然后填写项目核心约定：

```text
项目类型：TPS PVPVE 大逃杀
TTK：中等偏长
移动强度：中等，有少量位移技能
主要交战距离：10-50m
枪械复杂度：轻量化，但保留后坐和散布差异
技能设计边界：技能创造窗口，不直接替代枪械击杀
```

### Step 2：让 Codex 读取规则

在 Codex 里输入：

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md。
之后所有射击战斗设计输出，都按这些规则执行。
```

---

## 3. 常用 Codex 任务

### 生成枪械设计

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/weapon-balance.md、references/ttk-etk-model.md。
按 templates/blank-weapon-design.md，生成一版“中距离卡宾枪”的武器设计文档。
重点判断：是否侵蚀 AR / SMG、10-40m 强势距离是否成立、理论 TTK 和实战 eTTK 如何区分。
输出到 output/weapons/weapon-carbine-midrange-design.md。
```

### 生成技能设计

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/shooting-skill-design.md。
按 templates/blank-skill-design.md，生成一版“治疗无人机”技能设计文档。
要求包含：释放风险、治疗窗口、反制方式、多人治疗规则、高低端收益差异、资源需求、验收标准。
输出到 output/skills/skill-heal-drone-design.md。
```

### 生成 TTK 调整报告

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/ttk-etk-model.md、references/weapon-balance.md。
按 templates/blank-ttk-change-report.md，分析“基础 BTK +2，只动基础血量，不动护甲”的调整方案。
重点判断：是否成立、哪些武器受影响最大、爆头收益是否变化、护甲价值是否被稀释。
输出到 output/tuning/ttk-change-btk-plus-2.md。
```

### 生成 UE / Lyra / GAS 功能需求

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/ue-lyra-gas-landing.md。
按 templates/blank-feature-requirement.md，生成一版“战术飞扑”的功能需求文档。
要求按：输入 → 状态判断 → 技能激活 → 表现 → 结算 → 结束 → 冷却。
输出到 output/features/feature-tactical-dive-requirement.md。
```

---

## 4. 使用建议

- 一次只让 Codex 生成一个文档。
- 先让 Codex 输出 Markdown，不要一开始就要求 HTML / xlsx。
- 重要文档先生成草稿，再让 Codex 按反馈改第二版。
- 数值不确定时，让 Codex 标注“待验证”，不要强行补确定值。
- 项目资料、已有枪械表、技能表，可以放进 `knowledge-local/project-knowledge/`。

---

## 5. 不建议的用法

不要这样问：

```text
帮我把整个射击游戏战斗系统设计完。
```

更好的问法：

```text
先基于 conventions/my-project.md，生成武器生态框架。
只输出武器分类、强势距离、生态边界和风险点。
输出到 output/tuning/weapon-ecosystem-framework.md。
```

---

## 6. 文件改动后怎么检查

让 Codex 最后输出：

```text
列出本次新增 / 修改文件，并说明每个文件的用途。
```

你重点看三件事：

1. 有没有读项目约定。
2. 有没有区分 TTK（理论击杀时间）和 eTTK（实战击杀时间）。
3. 有没有写风险点和反制窗口。
