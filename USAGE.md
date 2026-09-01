# 使用说明

## 日常策划案

读取：
- AGENTS.md
- SKILL.md
- skills/game-design/SKILL.md
- 与问题相关的 methodology/common/*
- 如有项目约束，再读 conventions/*

示例：
“评审这个随机事件系统。先判断目标和规则是否成立，只找逻辑缺口、边界和风险，不主动扩展设计范围。”

## 射击战斗

读取：
- AGENTS.md
- SKILL.md
- skills/shooter-design/SKILL.md
- 与问题相关的 methodology/shooter/*
- 必要时再读 references/*

示例：
“分析这把 AR 为什么中距离过强。先区分理论 TTK、eTTK、命中率、距离覆盖和结构性上位，再给最小调整方案和验证方法。”

## 混合任务

先用 Shooter Combat Design 得出战斗结论，再用 Game Design Workflow 整理成正式规则、参数、边界和验收文档。

## 方法论沉淀

一次讨论的新观点不要直接写入 methodology/。

Observation → Case → Candidate Rule → 人工确认 → Confirmed Rule

只有 Confirmed Rule 才进入 methodology/。

## 不要放进仓库

原始聊天记录、大量重复版本、完整项目资产、无筛选网页资料、为“以后也许有用”而保存的杂项。
