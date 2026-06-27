# Changelog

## v2.2.7 (2026-06-26)

**天空红包：回退智能发言资格判断 + /red 命令提前占位**

- 移除「消息差额 < 20 秒抢、≥ 20 等 10 秒」的逻辑及消息ID跟踪
- 恢复为 pre_send 占位发消息方案
- 新增监听 `/red` 发红包命令：在红包消息出现前先发一条占位消息（随即删除，不留痕），抢得发言资格
- `/red` 占位由 pre_send 开关控制，占位内容复用 pre_send_text
- 抢包函数内不再重复占位发言，避免账号发两次言

---

## v2.2.6 (2026-06-26)

**天空红包：智能发言资格判断**

- 记录本账号在各群最后发言的消息ID
- 差额 < 20：在最近发言人列表中，直接秒抢
- 差额 ≥ 20：等待10秒让限制解除后再抢
- 替代原 pre_send 占位发消息方案，更精准无副作用

---

## v2.2.5 (2026-06-26)

**天空红包：发言占位**

- 前10秒限最近发言人领取时，开启 `pre_send` 可在点击前先往群里发一条消息（随即删除），确保账号在发言人列表中
- 占位消息内容可通过菜单自定义（`pre_send_text`，默认 `.`）
- 菜单新增「发言占位」开关和「修改占位内容」按钮

---

## v2.2.4 (2026-06-26)

**多账号通知区分**

- 所有发送到 BOT_MESSAGE_CHAT 的通知均加入 `👤 账号: 昵称(@用户名)` 标识，多账号运行时一眼看出是哪个账号触发
- 覆盖文件：自动抽奖（xiaocai/common/hdhive）、自动发奖、朱雀/象岛/癫影红包、天空拼手气红包

**安全**

- `/login` 流程中手机号、验证码、两步验证密码消息发送后立即自动删除
- `.restart` 命令消息执行后自动删除

---

## v2.2.3 (2026-06-26)

**账号管理面板**

- `/start` 重写：列出所有账号当前状态，在线账号显示下线按钮，离线账号显示登录和移除按钮
- 按钮标签取 Telegram 真实昵称，不再显示 session 文件名
- 下线操作只断开连接，不删 session 文件；移除才删文件
- 手动下线的账号写入 `sessions/.paused`，重启不会自动连接

**登录流程**

- `/login` 检测到 session 文件已存在时要求确认，防止误覆盖
- 登录成功后自动将账号信息写入 `config.py`；昵称或 tgid 有变化时同步更新
- 检测同一 Telegram 账号是否已在另一个 session 中运行
- 验证码位数提示 5 → 6

**其他**

- `/start` 命令说明改为"账号管理"
- release.yml 从 CHANGELOG 提取对应版本内容作为发布说明

---

## v2.2.2 (2026-06-26)

**多账号支持**

- `config.py` 新增 `ACCOUNTS` 列表，每项含 `session`/`name`/`tgid`
- `MY_NAME`/`MY_TGID`/`NY_USERNAME` 从 `ACCOUNTS[0]` 自动推导
- `/login [session名]` 支持在 Bot 内登录任意账号
- 每个账号独立加载 `plugins/user/` 插件，功能互不干扰

**修复**

- `user_apps` 模块级列表未重置导致重启重复追加
- DI 容器初始化时可能绑定未连接的 client
- `login.py` 动态创建 client 使用相对路径 workdir
- `infra/config.py` 解析 ACCOUNTS 存 str 而非 dict 导致 ValidationError
- `manager.start_userbot` 默认 session 名硬编码

**重构**

- 移除所有用户插件中的 `if client != user_app: return` 守卫（27 个文件，50+ 处）
- 用户插件中 `MY_TGID` 替换为 `client.me.id`，`filters.user(MY_TGID)` 替换为 `filters.me`
- 排行榜标题改用 `client.me.first_name`
- `ydx_zhuque` state section 改为 `ZHUQUE_{client.me.id}`，多账号独立存储

---

## v2.2.1 (2026-06-22)

**癫影红包**

- 新增癫影积分红包抢包支持，逐格尝试，抢到即停
- 新增癫影红包配置菜单，接入红包管理
- 修复成功关键词：补充"抢到"（原仅有"抢到了"）
- 修复未抢按钮识别：只点末尾数字且不以 ✅ 开头的格子

**HDSky 转账**

- 转出识别改用 `self_mentioned` 实体过滤，不再依赖回复链
- `get`/`pay` 改用文本匹配，不依赖 reply 链；排行榜回复目标改为原始消息
- `pay` 记录收款方，用缓存消息 id 作为回复目标
- 清理调试日志

**其他修复**

- 修复抽奖等待参与者超时后 `lottery_list` KeyError
- 修复配置菜单输入提示消息用完后未自动删除
- 红包管理菜单改名：发红包→人形红包，抢红包→影巢红包

---

## v2.2.0 (2026-06-19)

**新增 HDSky 转赠排行榜**

- 新增 `plugins/user/transfer/hdsky/`，监听天空官方群转赠消息，自动记录转入/转出
- 加入排行榜菜单站点列表，支持收/付排行榜与到账通知开关

**重命名 tianqi → hdsky**

- 过滤器、回调前缀、配置 section、配置文件全部重命名
- `TIANQI_REDPACKET` 自动迁移到 `HDSKY_REDPACKET`，原有配置不丢失

**其他**

- 天空红包播报排版统一为与抽奖消息一致的风格
- `.ai` 命令改用独立系统提示词，不套用人形回复人设

---

## v2.1.9 (2026-06-12)

修复 v2.1.8 大规模文件拆分后多个 `_helpers` 模块的运行时错误：

- `_prize_sender_helpers.py`：补 `MY_TGID` 导入；`pending_prizes` 单例移入本模块
- `_number_bomb_helpers.py`：懒加载代理解决 `bomb_game` 单例循环导入
- `_trap_detection_helpers.py`：补 `json` 导入
- `_bomb_monitor_helpers.py`：补 `MY_TGID` 导入
- `_rp_integration_helpers.py`：补 `json`/`re` 导入及 `_SNATCH_SECTION` 常量
- `lottery_group_wait_time.py`：从 helpers 导入共享的 `_edit_context`
- `bomb_game_monitor.py`：删除拆分遗留的孤儿代码行

新增三道验证防线：pyflakes 静态检查 + 114 个插件模块真实导入 + pytest 42 用例。

---

## v2.1.8 (2026-06-11)

**文件拆分**

13 个 300~1400 行的大文件拆分为主文件 + `_helpers` 模块，涉及 auto_lottery、bomb_game、main_menu、auto_prize_sender、number_bomb 等。

**测试**

- 新增 `tests/unit/core/`，pytest 框架，42 个 domain 层单元测试
- `.gitignore` 修正：`test*` 改为 `test*.session*`，不再排除 tests 目录

**依赖**

- `requirements.txt` 全部 pin 到实际运行版本
- 标注 wkhtmltopdf 为系统二进制

**代码质量**

- 消除全项目 32 处裸 `except:`，改为 `except Exception:`
- 52 个文件配置引用迁移到 `from core import`

**文档**

- README 从 1132 行精简至约 150 行，改为导航式入口
- 新增 `docs/commands.md` 和 `docs/troubleshooting.md`

---

## v2.1.7 (2026-06-10)

- 修复通过独立 `login.py` 登录时 DI 容器未初始化导致 `ai_human_reply` 对每条消息报错
- 新增 `get_container_or_none()`，容器未就绪时返回 None 而非抛异常
- `manager.start_userbot` 重建 client 后调用 `rebind_user_client()` 同步容器绑定
- 根目录 `login.py` 不再加载插件，只用于创建/校验 session 文件
- `pyproject.toml` 版本号同步至 2.1.7

---

## v2.1.6 (2026-05-13)

- 修复群内 `.ban` / `.unban` 快捷黑名单命令

## v2.1.5 (2026-05-09)

- 修复 `.ai` 提示词开关与天行日志汇总问题

## v2.1.4 (2026-05-07)

- 修复 `/start` 在已登录状态下无响应

## v2.1.3 (2026-05-01)

- AI 图片下载改为临时文件，使用后自动清理

## v2.1.2 (2026-05-01)

- 修复 AI 助手返回主菜单时跳转错误

---

## v2.1.1 (2026-04-28)

- 新增 `/login` 交互式登录，支持验证码和两步验证
- `core/manager.py` 统一管理 client 生命周期
- `Client` 新增 `ask` 交互接口

---

## v2.0.0 (2026-04-25)

迁移到六边形架构。新增 `core/`/`adapters/`/`infra/`/`plugins/` 目录结构，修复红包、转账、炸弹游戏、会话管理等一批问题。详见 git log。

---

更早版本见 git 提交记录。
