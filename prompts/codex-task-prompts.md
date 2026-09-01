# Codex 任务提示词

> 新架构原则：先路由 Skill，再读 Methodology；只有缺行业知识、公式或参考时才读 References。

## 1. 初始化仓库理解

```text
读取 AGENTS.md、SKILL.md、README.md、USAGE.md。
不要修改文件。
只总结：
1. 两个主 Skill 分别解决什么问题；
2. methodology / cases / references 的职责区别；
3. 遇到新观点时为什么不能直接改 methodology。
```

## 2. 通用策划案评审

```text
读取：
AGENTS.md
SKILL.md
skills/game-design/SKILL.md
methodology/common/problem-definition.md
methodology/common/design-review.md
methodology/common/system-boundary.md
methodology/common/risk-reward.md

评审以下方案：
【粘贴方案】

要求：
- 先判断目标是否成立。
- 区分现象 / 原因 / 方案。
- 只找逻辑缺口、边界、风险和最小修改建议。
- 不主动扩展设计范围。
- 如果产生值得沉淀的新规则，只列 Candidate Rule，不自动修改 methodology。
```

## 3. 生成正式策划案

```text
先读取：
AGENTS.md
SKILL.md
skills/game-design/SKILL.md
与当前任务相关的 methodology/common/*

如果有项目约束，再读取对应 conventions/*.md。
只有确认需要正式出稿后，再选择 templates/ 中最合适的模板。

基于以下内容生成策划案：
【粘贴需求】

要求：
- 不确定内容标“待确认”。
- 先保证规则完整，再补表现和实现。
- 输出前自检触发、生效、结束、重复、上限、无合法结果、冲突和验收。
```

## 4. 分析枪械问题

```text
读取：
AGENTS.md
SKILL.md
skills/shooter-design/SKILL.md
methodology/shooter/combat-model.md
methodology/shooter/weapon-analysis.md
methodology/shooter/weapon-ecology.md
methodology/shooter/validation.md

分析：
【粘贴武器问题】

要求：
- 不直接接受用户提出的调参方案。
- 先区分理论 TTK、eTTK、命中率、距离覆盖、支付成本、结构性上位。
- 给最小干预方案。
- 给控制变量和验证方法。
- 需要具体公式或行业参考时，再读取 references/。
```

## 5. 分析射击技能

```text
读取：
AGENTS.md
SKILL.md
skills/shooter-design/SKILL.md
methodology/shooter/skill-analysis.md
methodology/shooter/validation.md

分析：
【粘贴技能】

要求：
- 明确解决什么战斗压力。
- 明确使用场景。
- 区分直接解决与创造解决条件。
- 检查击杀窗口、武器优势兑现、释放风险、反制、高低端差异、Meta 风险。
- 只在必要时读取 references/shooting-skill-design.md 等参考资料。
```

## 6. 分析 3C / 手感

```text
读取：
AGENTS.md
SKILL.md
skills/shooter-design/SKILL.md
methodology/shooter/3c-analysis.md
methodology/shooter/validation.md

分析：
【粘贴现象】

要求：
- 先区分 Control / Character / Camera。
- 检查玩家输入与系统后坐、回正、插值之间是否存在控制权竞争。
- 一次只建议隔离一层验证。
- 不默认归因于枪械参数。
```

## 7. UE / Lyra / GAS 落地

```text
读取：
AGENTS.md
SKILL.md
skills/shooter-design/SKILL.md
references/ue-lyra-gas-landing.md
如有项目约束则读取 conventions/*.md

基于以下功能：
【粘贴功能】

按：
输入 → 状态判断 → 激活 → 表现 → 结算 → 结束 → 冷却

输出策划可理解的落地链路，并说明每个关键参数对战斗体验的影响。
```

## 8. 修改已有文档

```text
读取 AGENTS.md、SKILL.md、与目标文件对应的 Skill，以及目标文件本身。

目标文件：
【路径】

反馈：
【修改要求】

要求：
- 保持原目标和结构。
- 只做最小必要修改。
- 如建议大改，先说明为什么原结构不能满足目标。
- 最后列修改点和仍待确认问题。
```

## 9. 提议沉淀方法论

```text
基于刚才已经完成的讨论，只判断是否产生值得复用的规则。
如果没有，直接回答“本轮无新增 Candidate Rule”。
如果有，最多列 3 条：
- Candidate Rule
- 适用条件
- 来源案例
不要修改任何文件。
```
