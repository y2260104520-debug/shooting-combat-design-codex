---
name: game-design-methodology-router
description: '个人游戏设计方法论入口。根据任务自动路由到通用策划案工作流或射击战斗设计工作流。'
---

# 个人游戏设计方法论入口

本文件只负责路由，不承载完整知识。

## Skill 路由

### Game Design Workflow
读取 skills/game-design/SKILL.md。

适用于：系统策划案、玩法规则、功能设计、需求评审、规则补全、边界检查、文档整理、方案风险评审。

### Shooter Combat Design
读取 skills/shooter-design/SKILL.md。

适用于：枪械设计与平衡、TTK / eTTK / STK、后坐力、散布、伤害衰减、ADS、移动、镜头、3C、射击技能、武器生态、交战距离、UE / Lyra / GAS 射击战斗落地。

### 混合任务
若任务既包含射击战斗判断，又需要正式策划案：
1. 先使用 Shooter Combat Design 做判断。
2. 再使用 Game Design Workflow 整理规则、边界和验收文档。

## 知识优先级

1. 用户当前明确要求
2. 项目约定 conventions/
3. 已确认方法论 methodology/
4. 已验证案例 cases/
5. 参考知识 references/
6. 模型自身常识

## 方法论升级规则

Observation → Case → Candidate Rule → 人工确认 → Confirmed Rule → methodology/

Candidate Rule 在人工确认前不得直接写入正式 methodology/。
