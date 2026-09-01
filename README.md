# shooting-combat-design-codex

个人游戏设计方法论与 AI Skill 仓库。

目标不是做“大而全百科”，而是沉淀稳定可复用的判断方式，让不同 AI 按同一套方法处理策划任务。

## 两个主 Skill

### Game Design Workflow
用于日常策划案、系统设计、规则评审和文档整理。

需求输入 → 目标判断 → 问题定义 → 系统拆解 → 规则补全 → 边界检查 → 风险评审 → 方案输出 → 验收标准

入口：skills/game-design/SKILL.md

### Shooter Combat Design
用于射击战斗、枪械、技能、3C、TTK / eTTK 和武器生态分析。

现象 → 战斗问题 → 发生场景 → 影响指标 → 根因假设 → 生态影响 → 方案 → 副作用 → 验证方法

入口：skills/shooter-design/SKILL.md

## 目录职责

| 目录 | 作用 |
|---|---|
| skills/ | AI 执行方式和任务流程 |
| methodology/ | 已确认的个人方法论 |
| cases/ | 有上下文的设计案例与决策 |
| conventions/ | 具体项目的规则与约束 |
| references/ | 行业知识、公式、参考框架 |
| templates/ | 正式策划文档模板 |
| output/ | 任务产出 |
| knowledge-local/ | 本地项目知识和临时积累 |

## 知识优先级

用户当前要求 → 项目 conventions → 已确认 methodology → 已验证 cases → references → 模型常识

## 方法论更新

Observation → Case → Candidate Rule → 人工确认 → Confirmed Rule → methodology/

GitHub 只保存提炼后的知识，不保存完整聊天记录。

## 现有射击资料

原 references/、conventions/、templates/、prompts/、output/ 和 knowledge-local/ 保留。现有 references/ 作为射击参考知识层，不自动等同于个人确认的方法论。

## 原则

- 先判断问题，再生成方案。
- 只读相关文件，不全库硬塞上下文。
- 不明确的数据标记为假设或待验证。
- 方法论与案例分开。
- 通用策划和射击战斗分开。
- 当前保持 Markdown 轻量结构，不建数据库。

## License

MIT。
