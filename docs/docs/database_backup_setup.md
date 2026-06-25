# 数据库备份配置说明 (v2.1.1)

## 概述
AWBotHub 支持自动数据库备份功能。新版架构通过 `infra/config.py` 统一管理数据库连接，支持定时将备份发送到 Telegram 监控群组。

## 配置要求

### 1. 核心配置
确保您的环境变量或 `config.py` 中已正确配置数据库：

- **MySQL**: 需配置 `DB_ADDRESS`, `DB_USER`, `DB_PASSWORD` 等。
- **SQLite**: 默认路径为 `db_file/SQLite/tgbot.db`，会自动进行文件级备份。

### 2. 定时任务
备份任务已集成在 APScheduler 中。您可以通过以下 Bot 指令进行管理：
- `/scheduler_jobs`: 查看备份任务状态。
- `/scheduler_control`: 开启或关闭自动备份任务。
    "dbset": "mySQL",
    "address": "mysql",  # 使用容器名作为主机地址
    "db_name": "your_database_name",
    "port": 3306,  # MySQL 容器内部端口
    "user": "your_mysql_user",
    "password": "your_mysql_password",
}
```

**重要说明**：
- `address` 应该设置为 `"mysql"`（容器名），而不是 `"localhost"` 或 IP 地址
- 这样应用容器可以通过 Docker 网络直接访问 MySQL 容器

### 3. 备份功能特性

#### 自动备份
- 每天 06:06:06 自动执行备份
- 备份文件格式：`{数据库名}_backup_{时间戳}.sql.gz`
- 自动压缩备份文件
- 保留最近 8 天的备份

#### 手动操作
- `/backuplist` - 查看备份文件列表
- `/dbrestore 序号` - 还原指定备份

### 4. 故障排除

#### 常见问题

1. **找不到 mysqldump 命令**
   - 解决方案：Dockerfile 已包含 `mysql-client` 包
   - 如果仍有问题，脚本会自动尝试安装

2. **无法连接到数据库**
   - 检查容器网络配置
   - 确认数据库地址设置为容器名 `"mysql"`
   - 检查数据库容器是否正常运行

3. **权限错误**
   - 脚本使用 `--no-tablespaces` 参数避免权限问题
   - 确保数据库用户有备份权限

#### 调试步骤

1. 检查容器网络连接：
```bash
docker exec -it AWBotHub ping mysql
```

2. 测试数据库连接：
```bash
docker exec -it AWBotHub mysql -h mysql -u your_user -p your_database
```

3. 查看备份日志：
```bash
docker logs AWBotHub | grep -i backup
```

## 备份文件存储

- 本地路径：`/app/db_file/mysqlBackup/`
- 挂载路径：`/your/local/path/db_file:/app/db_file`
- 文件格式：`.sql.gz`（压缩的 SQL 文件）

## 安全建议

1. 定期检查备份文件完整性
2. 将备份文件同步到外部存储
3. 测试备份还原流程
4. 监控备份任务执行状态
