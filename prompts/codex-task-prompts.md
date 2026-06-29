# Codex 任务提示词

## 1. 初始化仓库理解

```text
请读取 AGENTS.md、SKILL.md、README.md、USAGE.md，理解本仓库的射击战斗设计工作流。
不要修改文件，只总结：
1. 这个仓库用于什么；
2. 之后生成枪械/技能/TTK文档时需要优先读取哪些文件；
3. 输出文件应该放在哪里。
```

## 2. 填项目约定

```text
读取 conventions/TEMPLATE.md。
基于以下项目描述，生成一份项目约定文件：conventions/my-project.md。
项目描述：
【粘贴你的项目描述】
要求：不确定的字段保留“待确认”，不要编造确定数值。
```

## 3. 生成武器设计

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/gunplay-framework.md、references/weapon-balance.md、references/ttk-etk-model.md、templates/blank-weapon-design.md。
生成一版【武器名】武器设计文档，输出到 output/weapons/weapon-【英文名】-design.md。
重点：强势距离、TTK/eTTK、BTK档位、生态侵蚀、风险点、验收标准。
```

## 4. 分析 TTK 改动

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/ttk-etk-model.md、references/weapon-balance.md、templates/blank-ttk-change-report.md。
分析以下 TTK 改动：
【粘贴改动】
输出到 output/tuning/ttk-change-【主题】.md。
要求：区分理论 TTK 和实战 eTTK，检查护甲、爆头、治疗、技能、武器生态的二阶影响。
```

## 5. 生成技能设计

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/shooting-skill-design.md、references/meta-rules.md、references/anti-patterns.md、templates/blank-skill-design.md。
生成一版【技能名】技能设计文档，输出到 output/skills/skill-【英文名】-design.md。
要求：说明技能解决什么压力、在什么场景成立、是否创造击杀窗口、释放风险、反制窗口、高低端收益差异、资源需求和验收标准。
```

## 6. 生成 UE / Lyra / GAS 功能需求

```text
读取 AGENTS.md、SKILL.md、conventions/my-project.md、references/ue-lyra-gas-landing.md、templates/blank-feature-requirement.md。
生成【功能名】功能需求文档，输出到 output/features/feature-【英文名】-requirement.md。
要求按：输入 → 状态判断 → 技能激活 → 表现 → 结算 → 结束 → 冷却。
所有 UE / Lyra / GAS 术语后加中文说明。
```

## 7. 修改已有文档

```text
读取 AGENTS.md 和目标文件：【文件路径】。
根据以下反馈修改文档：
【反馈】
要求：保留原结构，只修改必要内容；最后列出修改点。
```
