# 3C Analysis

3C = Character / Camera / Control。

## 原则

出现“枪不跟手”“移动飘”“压枪怪”“镜头硬”时，不要先改武器参数。

先判断问题在哪一层。

## Control

检查：
- 输入延迟
- 鼠标 / 摇杆灵敏度
- ADS 灵敏度
- 响应曲线
- 死区
- Aim Assist
- 输入状态切换

## Character

检查：
- 最大速度
- 加速度
- 制动
- 转向
- 空中控制
- 重力
- 冲刺 / ADS / 蹲伏状态切换

数值速度正确，不代表启动、停止和转向过程正确。

## Camera

检查：
- FOV
- ADS 过渡
- Recoil Camera
- Camera Kick
- Camera Shake
- 回正
- Lag
- 状态切换时是否覆盖控制输入

## 控制权竞争

特别检查：

玩家输入 vs 系统后坐 vs 系统回正 vs 镜头插值

如果系统回正直接覆盖或抵消玩家输入，会产生“抢控制权”的感觉。

## 验证方式

一次只隔离一层：
- 固定角色移动，测镜头
- 固定镜头，测 Character Movement
- 关闭后坐恢复，测纯输入
- 固定枪械散布，测跟枪

避免同时改 3C 和枪械。
