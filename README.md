# shooting-combat-design-codex

**射击战斗设计 Codex 仓库模板** —— 用于让 Codex / Cursor / GPT 等 agent 在一个 GitHub 仓库里，稳定产出射击游戏的战斗策划文档。

它不是游戏工程项目，也不是 UE 插件；它是一套 **仓库级规则 + 射击战斗知识库 + 文档模板 + Codex 任务提示词**。

## 这版和原 act-combat-design 的区别

原仓库偏 **ACT / 二次元动作 / 角色与 Boss 招式设计**。本仓改成射击方向：

- 武器生态（Weapon Ecosystem）
- TTK / eTTK（理论击杀时间 / 实战击杀时间）
- STK / BTK（击杀子弹数）
- 命中率（Hit Rate）
- 后坐力（Recoil）
- 散布（Spread / Bloom）
- 伤害衰减（Damage Falloff）
- 3C / 镜头 / 移动（Character / Camera / Control）
- 射击技能设计（信息、位移、控场、治疗、护盾、爆发窗口）
- 地图交战空间（Engagement Space）
- Meta 塌缩风险（Meta Collapse）
- UE / Lyra / GAS 落地链路

## 为什么适合 Codex

Codex 更适合“基于仓库文件做持续改动”。所以本仓在原有 `SKILL.md` 基础上新增了：

- `AGENTS.md`：Codex 读取的仓库级行为规则。
- `prompts/codex-task-prompts.md`：可直接复制给 Codex 的任务提示词。
- `templates/`：输出文档的固定格式。
- `references/`：射击战斗方法论知识库。
- `conventions/`：项目战斗约定。Codex 每次分析都必须优先读取。

## 目录结构

```text
shooting-combat-design-codex/
├─ AGENTS.md                         # ★ Codex 仓库级规则
├─ SKILL.md                          # 射击战斗设计方法论入口
├─ USAGE.md                          # 使用说明
├─ README.md
├─ conventions/
│  ├─ TEMPLATE.md                     # ★ 项目战斗约定模板
│  └─ example-conventions-tps-br.md   # 示例：TPS PVPVE 大逃杀
├─ references/
│  ├─ gunplay-framework.md            # 枪械射击体验总框架
│  ├─ weapon-balance.md               # 武器生态与平衡
│  ├─ ttk-etk-model.md                # TTK / eTTK / STK 模型
│  ├─ shooting-skill-design.md        # 射击技能设计
│  ├─ 3c-camera-movement.md           # 3C / 镜头 / 移动
│  ├─ map-engagement-space.md         # 地图交战空间
│  ├─ ue-lyra-gas-landing.md          # UE / Lyra / GAS 落地链路
│  ├─ meta-rules.md                   # 射击战斗元规则
│  └─ anti-patterns.md                # 反模式自检
├─ templates/
│  ├─ blank-weapon-design.md
│  ├─ blank-skill-design.md
│  ├─ blank-ttk-change-report.md
│  ├─ blank-gunplay-tuning-report.md
│  ├─ blank-feature-requirement.md
│  └─ blank-resource-requirements.md
├─ prompts/
│  └─ codex-task-prompts.md
├─ output/                            # Codex 产出区
└─ knowledge-local/                   # 本地项目知识，不建议进公开仓库
```

## 最小使用流程

1. 把本仓上传到 GitHub。
2. 用 Codex 打开 / 连接这个仓库。
3. 先填写 `conventions/TEMPLATE.md`，或者复制 `example-conventions-tps-br.md` 改成你的项目。
4. 在 Codex 里发任务，例如：

```text
读取 AGENTS.md、SKILL.md、conventions/example-conventions-tps-br.md。
按 templates/blank-weapon-design.md，生成一版“中距离卡宾枪”的武器设计文档。
输出到 output/weapons/carbine-midrange.md。
```

## 使用原则

- **先项目约定，再做设计**：不确定 TTK、移动强度、主要交战距离时，不要直接给结论。
- **默认输出 Markdown**：便于版本管理和 PR 审阅。
- **不要让 Codex 一次做太大**：一次只做一个武器、一个技能、一个平衡报告。
- **数值必须区分假设值和项目值**：没有真实数据时，只能写“建议区间 / 示例值”。
- **所有输出要有风险点**：特别是 Meta 塌缩、生态侵蚀、强弱端差异、反制窗口。

## License

MIT。保留原仓库 MIT License 声明。本仓为射击方向改写版。
