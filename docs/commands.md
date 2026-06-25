# 命令大全

> 所有命令均支持 `/` 和 `.` 两种前缀（如 `/menu` 等价于 `.menu`）。
> 标注「菜单」的命令建议通过 `/menu` 图形界面操作。

## 基础命令

| 命令 | 说明 |
|------|------|
| `/menu`、`/start` | 显示主菜单 |
| `/zf [数量]` | 转发被回复的消息 |
| `/id` | 查询用户 / 群组 ID（支持中文显示） |
| `/dme [数量]` | 批量删除自己的消息 |
| `/help`、`/helpme` | 显示帮助信息 |

## 系统管理

| 命令 | 说明 |
|------|------|
| `/update` | 检查并更新到最新版本 |
| `/restart` | 重启机器人 |
| `/configstate` | 查看配置文件状态（生成可视化图片） |
| `/createconfig` | 创建默认配置文件 |
| `/sysstate` | 查看系统运行状态 |
| `/refreshcommands` | 刷新 Bot 命令菜单 |
| `/err` | 测试错误消息 |

## 排行榜与等待时间

| 命令 | 说明 |
|------|------|
| `/leaderboard` | 转账排行榜菜单（多站点） |
| `/transferwaittime` | 转账消息等待时间设置（0-300 秒） |
| `/lotterywaittime` | 抽奖消息等待时间设置（含启用 / 禁用开关） |

## 数据库管理

| 命令 | 说明 |
|------|------|
| `/backuplist` | 查看数据库备份列表 |
| `/dbrestore` | 恢复数据库备份 |
| `/export` | 导出数据到 Excel（菜单） |

## 定时任务

| 命令 | 说明 |
|------|------|
| `/scheduler_jobs` | 查看所有定时任务 |
| `/scheduler_control` | 定时任务开关控制（菜单） |
| `/customreply` | 自定义定时回复管理（菜单） |
| `/customreply_add` | 添加新的定时回复任务 |

## 抽奖功能

| 命令 | 说明 |
|------|------|
| `/lotteryprizeset` | 奖品匹配设置（菜单） |
| `/lotterywaittimeset` | 全局等待时间设置（菜单） |
| `/lottery_group_wait` | 群组等待时间设置（菜单） |
| `/autolotteryset` | 自动抽奖设置（菜单） |
| `/trapdetectionset` | 陷阱检测设置（菜单） |
| `/rpsnatch` | 抢红包监控设置 |
| `/sendprize [ID]` | 发送指定抽奖的奖品 |
| `/listprize` | 查看待发奖列表 |
| `/clearprize` | 清空待发奖列表 |
| `/prizehelp` | 发奖命令帮助 |

## 数字炸弹游戏

群内交互：**开启数字炸弹** / **持续数字炸弹** / **结束数字炸弹** / **我猜是 XX**（XX 为 1-100）。

| 命令 | 说明 |
|------|------|
| `/bomb_status` | 查看游戏状态 |
| `/bomb_quick` | 快速查看所有群组游戏状态 |
| `/bomb_cleanup` | 清理旧游戏数据 |
| `/bomb_test` | 测试游戏配置 |
| `/bomb_help` | 显示游戏帮助 |
| `/bomb_menu` | 显示游戏主菜单 |
| `/bomb_reward_set` | 设置游戏奖励 |
| `/bomb_autodelete` | 自动删除消息设置 |
| `/bombconfigset` | 高级游戏配置 |

## 朱雀功能

| 命令 | 说明 |
|------|------|
| `/dajie` | 大劫设置（菜单） |
| `/blacklist` | 黑名单管理 |
| `/ydx` | YDX 投注设置（菜单） |
| `/card` | 道具卡回收设置（菜单） |
| `/ydxtest` | YDX 测试 |
| `/ydxclean` | 清理 YDX 重复记录 |
| `/prizewheel` | 朱雀转盘 |
| `/getinfo` | 朱雀信息查询 |

## Cookie 与站点配置

| 命令 | 说明 |
|------|------|
| `/cookie` | Cookie 设置（菜单） |
| `/xcsrf` | X-CSRF 设置（菜单） |
| `/set115tocms` | 115 to CMS 配置（菜单） |
| `/share115tocms` | 115 to CMS 开关（菜单） |
| `/blockyword` | 屏蔽关键字设置（菜单） |
| `/ssd_click` | SSD 大额确认设置 |

## 用户脚本命令（需在对应群组使用）

| 命令 | 说明 |
|------|------|
| `/u2`、`/u2s` | U2/DMHY 转账 |
| `/xd21` | 21 点游戏 |
| `/betbonus` | 计算起始投注 |
