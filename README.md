# AWBotHub - Telegram 自动化工具

![AWBotHub Logo](assets/logo.png)

[![Python](https://img.shields.io/badge/Python-3.13+-green.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://hub.docker.com/r/awdress/awbothub)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Version](https://img.shields.io/badge/Version-v2.2.3-orange.svg)](CHANGELOG.md)

基于**六边形架构**的 Telegram 多账号自动化工具，专为 PT 站点设计。支持自动抽奖、红包监控、排行榜生成、数字炸弹游戏及多站点转账管理。

> 基于 [DonneChang/tgbot-py](https://github.com/DonneChang/tgbot-py) 开发，感谢原作者。

---

## 📚 文档导航

| 文档 | 说明 |
|------|------|
| [命令大全](docs/commands.md) | 所有 Bot 命令速查（支持 `/` 和 `.` 两种前缀） |
| [配置指南](docs/config_template_guide.md) | config.py 各字段详细说明 |
| [自动发奖指南](docs/auto-prize-sender-guide.md) | 自动发奖功能完整说明 |
| [发奖命令速查](docs/prize-commands-quick-ref.md) | 发奖相关命令参考 |
| [抢红包陷阱通知](docs/trap-notification-templates.md) | 陷阱检测通知模板 |
| [自定义定时回复](docs/custom_auto_reply_usage.md) | 定时回复配置说明 |
| [数据库备份](docs/database_backup_setup.md) | 备份与恢复配置 |
| [Supervisord Web 界面](docs/supervisord-web-ui.md) | Web 管理界面使用说明 |
| [版本管理](docs/version-management.md) | 版本选择与更新说明 |
| [GitHub Actions](docs/github-actions.md) | CI/CD 配置说明 |
| [故障排除](docs/troubleshooting.md) | 常见问题解决方案 |
| [更新日志](CHANGELOG.md) | 完整版本历史 |

---

## ✨ 主要功能

- **多账号管理**：`config.py` 配置多个 TG 账号，每个账号独立运行所有插件；Bot 内 `/start` 可查看状态、一键登录/下线/移除
- **智能抽奖**：自动识别抽奖消息，多群组监控，奖品关键词匹配，陷阱检测拦截
- **拼手气红包**：监控指定用户发包，OCR 图片口令识别（失败自动降级复制模式），三层陷阱防护
- **自动发奖**：中奖自动记录，支持手动/自动发奖模式，Bot 消息推送
- **多站点转账排行榜**：ZM、Azusa、PTVicomo、HDDolby、SpringSunday、Audiences、Zhuque
- **数字炸弹游戏**：单次/持续模式，智能难度，范围缩小机制，魔力值奖励
- **AI 人形回复**：私聊/群组 AI 对话（OpenAI 兼容格式）
- **朱雀功能**：大劫、YDX 投注、道具卡回收、转盘
- **系统管理**：Supervisord 集成、健康检查、会话监控、自动备份、日志清理

---

## 👥 多账号配置

`config/config.py` 中配置 `ACCOUNTS` 列表，每项含 session 文件名、昵称和 TG ID：

```python
ACCOUNTS = [
    {"session": "account1", "name": "Alice", "tgid": 123456789},
    {"session": "account2", "name": "Bob",   "tgid": 987654321},
]
```

- 每个账号独立加载所有 `plugins/user/` 插件，状态互不干扰
- 发送 `/start` 查看所有账号状态，支持一键下线（断开连接）或移除（删 session 文件）
- 发送 `/login <账号名>` 可在 Bot 内完成交互式登录，成功后自动写入 `config.py`
- 手动下线的账号重启后不会自动连接（状态持久化到 `sessions/.paused`）



## 🚀 快速开始

### 方式一：Docker（推荐）

```bash
git clone https://github.com/AWdress/AWBotHub.git
cd AWBotHub
```

准备配置目录：
```bash
mkdir -p config sessions logs db_file temp_file
cp config/config_example.py config/config.py
# 编辑 config/config.py，填入 API_ID、API_HASH、BOT_TOKEN 等
```

使用项目根目录已有的 `docker-compose.yml` 启动：
```bash
docker-compose up -d
```

**主要环境变量：**

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `TZ` | 时区 | `Asia/Shanghai` |
| `SUPERVISOR_USERNAME` | Web 界面用户名 | 必填 |
| `SUPERVISOR_PASSWORD` | Web 界面密码 | 必填 |
| `GITHUB_TOKEN` | 私有库同步 Token | 可选 |
| `GIT_BRANCH` | 同步分支 | `dev` |
| `USE_MIRROR` | 国内镜像加速（海外 VPS 设 `false`） | `true` |

启动后访问 Supervisord 管理界面：`http://your-host:51901`

查看日志：
```bash
docker-compose logs -f awbothub
```

### 方式二：源码运行

```bash
git clone https://github.com/AWdress/AWBotHub.git
cd AWBotHub
pip install -r requirements.txt

cp config/config_example.py config/config.py
cp config/reply_message_example.py config/reply_message.py
# 编辑 config/config.py

python main.py
```

> `wkhtmltoimage` 需单独安装（系统二进制，非 pip 包）：[wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

---

## 🔐 首次登录

启动后向 Bot 发送 `/login`，按提示完成手机号和验证码验证。

> 不要直接运行 `python login.py`，那只用于手动建会话文件，不会启动监听。

---

## 📋 系统要求

- Python 3.13+
- 内存 512MB+（推荐 1GB+）
- 网络可访问 Telegram（海外 VPS 无需镜像）
- SQLite（默认）或 MySQL 8.0+

---

## 🤝 贡献 · 支持

- 提交 [Issue](https://github.com/AWdress/AWBotHub/issues) 反馈问题
- 提交 Pull Request 参与开发

---

**免责声明**：本项目仅供学习和研究使用，使用者需自行承担使用风险。请遵守 Telegram 使用条款。
