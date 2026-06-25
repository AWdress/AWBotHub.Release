# 配置指南 (v2.1.1)

## 概述
AWBotHub 现已全面升级为基于 `pydantic-settings` 的统一配置系统。系统支持多源配置加载，优先级如下：
1. **环境变量** (以 `TG_` 或 `DB_` 等为前缀)
2. **.env 文件** (存放在项目根目录)
3. **运行时状态文件** (`config/state.toml`) - 由 Web 控制面板修改后自动更新
4. **旧版配置文件** (`config/config.py`) - 仅作过渡期兼容支持

## 核心配置项

### 1. Telegram 基础配置 (TG_)
这些配置决定了机器人如何连接到 Telegram：
- `TG_API_ID`: 您的 API ID (从 my.telegram.org 获取)
- `TG_API_HASH`: 您的 API Hash
- `TG_BOT_TOKEN`: 您的 Bot Token (从 @BotFather 获取)
- `TG_MY_TGID`: 您的个人 Telegram ID

### 2. Web 控制面板与公网映射
- `TG_WEB_UI_PORT`: Web 控制面板监听端口 (默认: 18000)
- `TG_NGROK_ENABLE`: 是否自动开启 ngrok 映射 (true/false)
- `TG_NGROK_TOKEN`: 您的 ngrok Authtoken

### 3. 数据库配置 (DB_)
- `DB_DBSET`: 数据库类型 (`SQLite` 或 `mySQL`)
- `DB_SQLITE_PATH`: SQLite 数据库路径 (默认: `db_file/SQLite/tgbot.db`)

## 快速配置方法

### 方法 A: 使用 Web 控制面板 (推荐)
1. 启动机器人。
2. 在 Bot 中进入 `基础设置` -> `🌐 Web 控制面板`。
3. 在网页中直观修改奖品关键词、目标群组等配置。

### 方法 B: 编辑 .env 文件
在项目根目录创建 `.env` 文件：
```env
TG_API_ID=1234567
TG_API_HASH=your_api_hash
TG_BOT_TOKEN=your_bot_token
TG_MY_TGID=7016579329
TG_NGROK_ENABLE=true
```

### 方法 C: 兼容旧版 config.py
您依然可以编辑 `config/config.py`。新版程序在启动时会**自动检测并补全**该文件中缺失的新字段。
    "password": "your_database_password",  # 数据库密码
}
```

### 5. 数字炸弹游戏配置（可选）
```python
NUMBER_BOMB_CONFIG = {
    "enable_range_shrink": True,  # 是否启用范围缩小机制
    "shrink_mechanism": {
        "distance_1_5": 0,    # 距离1-5的缩小幅度
        "distance_6_15": 1,   # 距离6-15的缩小幅度
        "distance_16_30": 2,  # 距离16-30的缩小幅度
        "distance_31_plus": 4, # 距离31+的缩小幅度
    }
}
```

## 获取配置信息

### Telegram API 信息
1. 访问 https://my.telegram.org/apps
2. 登录您的Telegram账号
3. 创建新应用获取 `API_ID` 和 `API_HASH`

### Bot Token
1. 在Telegram中搜索 @BotFather
2. 发送 `/newbot` 创建新机器人
3. 按提示设置机器人名称和用户名
4. 获取 `BOT_TOKEN`

### 群组ID
1. 将机器人添加到目标群组
2. 在群组中发送消息
3. 查看机器人日志获取群组ID（通常以-100开头）

### 数据库信息
- **MySQL**: 需要MySQL服务器地址、端口、数据库名、用户名和密码
- **SQLite**: 只需要设置 `"dbset": "SQLite"`，其他字段可忽略

## 安全注意事项

1. **不要提交真实配置**: 确保 `config.py` 在 `.gitignore` 中
2. **保护敏感信息**: API密钥、数据库密码等敏感信息不要泄露
3. **定期更换密钥**: 建议定期更换API密钥和数据库密码
4. **使用环境变量**: 生产环境建议使用环境变量存储敏感信息

## 配置验证

配置完成后，可以运行以下命令验证配置是否正确：

```bash
python -c "from config.config import *; print('配置加载成功')"
```

如果出现错误，请检查：
1. 所有占位符是否已替换
2. 语法是否正确
3. 引号是否匹配
4. 缩进是否正确

## 常见问题

### Q: 如何获取群组ID？
A: 将机器人添加到群组后，在群组中发送消息，查看机器人日志中的chat_id。

### Q: 代理配置不生效？
A: 确保 `proxy_enable` 设为 `True`，并检查代理服务器地址和端口是否正确。

### Q: 数据库连接失败？
A: 检查数据库服务器是否运行，用户名密码是否正确，网络是否可达。

### Q: 数字炸弹游戏不工作？
A: 检查 `NUMBER_BOMB_CONFIG` 配置是否正确，确保所有字段都有值。
