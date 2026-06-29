# UE / Lyra / GAS 落地链路

## 1. 结论

射击技能落地时，策划应优先描述“战斗体验链路”，再补实现结构。不要一开始陷入纯程序节点。

标准链路：

```text
输入 Input
→ 状态判断 State Check
→ 技能激活 Ability Activation
→ 成本/冷却 Cost & Cooldown
→ 表现 Gameplay Cue / Montage / Camera
→ 目标/命中 Targeting
→ 效果结算 Gameplay Effect
→ 结束 End Ability
→ 冷却/复位 Cooldown & Reset
```

---

## 2. GAS 基础对应

| 策划概念 | GAS / Lyra 常见对应 | 中文说明 |
|---|---|---|
| 技能 | Gameplay Ability | 游戏能力，技能逻辑主体 |
| 技能效果 | Gameplay Effect | 游戏效果，如伤害、治疗、加速、减速 |
| 表现触发 | Gameplay Cue | 游戏提示，用于特效、音效、镜头反馈 |
| 标签 | Gameplay Tag | 游戏标签，用于状态判断和规则筛选 |
| 冷却 | Cooldown Gameplay Effect | 冷却效果 |
| 消耗 | Cost Gameplay Effect | 成本效果，如能量、弹药、资源 |
| 输入 | Enhanced Input Action | 增强输入动作 |
| 目标选择 | Targeting / Trace | 目标筛选 / 射线检测 |
| 任务 | Ability Task | 技能任务，如等待输入、等待蒙太奇结束 |

---

## 3. 策划写技能需求时要写清楚

| 模块 | 要写什么 |
|---|---|
| 输入 | 按下、松开、长按、双击、是否可取消 |
| 状态判断 | 是否死亡、倒地、换弹、开镜、空中、滑铲、冷却中 |
| 激活条件 | 资源、距离、目标、地面/空中、武器状态 |
| 表现 | 动画、特效、音效、UI、镜头、准星变化 |
| 结算 | 范围、目标数量、命中规则、阵营筛选、遮挡判断 |
| 结束 | 到期、取消、被打断、目标丢失、被摧毁 |
| 冷却 | 何时进入冷却，失败是否进冷却 |
| 反制 | 敌人如何观察、打断、摧毁、躲避 |

---

## 4. 技能落地示例：治疗无人机

```text
输入：按下技能键
→ 状态判断：玩家存活、技能未冷却、资源足够、当前不处于禁用技能状态
→ 技能激活：生成无人机 Actor（角色对象）
→ 表现：播放部署动画、音效、UI 图标
→ 搜索：无人机以自身为中心搜索友方低血量目标
→ 结算：对范围内目标周期性施加 Gameplay Effect（治疗效果）
→ 中断：目标离开范围 / 无人机被摧毁 / 持续时间结束
→ 结束：销毁无人机，清理 UI
→ 冷却：部署成功后进入冷却；释放失败不进冷却
```

---

## 5. 参数对体验的影响

| 参数 | 体验影响 |
|---|---|
| Cast Time（施法时间） | 决定释放风险 |
| Duration（持续时间） | 决定窗口长度 |
| Radius（半径） | 决定场景适配和站位要求 |
| Tick Interval（结算间隔） | 决定反馈频率和治疗平滑度 |
| Cooldown（冷却） | 决定技能循环频率 |
| Max Targets（最大目标数） | 决定团队收益上限 |
| Break Conditions（中断条件） | 决定反制空间 |
| Post Fire Delay（释放后开火延迟） | 决定技能能否直接转化击杀 |

---

## 6. Lyra 文档写法建议

策划文档不需要写完整蓝图图，但要写：

```text
输入动作：IA_XXX（增强输入动作）
技能蓝图：GA_XXX（Gameplay Ability，游戏能力）
效果：GE_XXX（Gameplay Effect，游戏效果）
表现：GC_XXX（Gameplay Cue，游戏提示）
标签：Ability.XXX / State.XXX（Gameplay Tag，游戏标签）
```

并说明每个资源影响什么战斗体验。
