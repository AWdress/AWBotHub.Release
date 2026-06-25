# 故障排除

## 启动与登录

**`DI 容器尚未初始化`**  
不要直接运行 `python login.py`，通过 Bot 发送 `/login` 命令登录。

**容器启动后立即退出**  
检查 `config/config.py` 是否填写了 `API_ID`、`API_HASH`、`BOT_TOKEN`。环境变量缺失也会导致同样问题。

**`PeerIdInvalid: The peer id being used is invalid`**  
用 `/id` 命令验证群组 ID，并确认 Bot 已加入目标群组。

**`Cannot operate on a closed database`**  
运行 `python scripts/session_recovery.py` 恢复会话文件，然后重启。

---

## 配置

**`config/state.toml` 不存在**  
运行 `/createconfig` 命令创建默认配置，或手动复制 `config/config_example.py` 为 `config/config.py`。

---

## 图片生成

**`wkhtmltoimage` 未找到**  
- Docker 环境：已内置，检查镜像是否为最新版本。  
- 本地环境：从 [wkhtmltopdf 官网](https://wkhtmltopdf.org/downloads.html) 安装对应平台版本。

---

## 抽奖功能

**参与抽奖后无反应**  
检查奖品关键词是否在配置的 `PRIZE_LIST` 中，以及当前时间是否在允许的时间范围内。

**群组等待时间设置失败**  
先通过「抽奖设置 → 添加抽奖群组」将群组加入列表，再设置等待时间。

**拼手气红包不触发**  
确认监控目标 UID 已通过 `.rpsnatch` 菜单添加，且目标用户在监控的群组内。

---

## 数字炸弹游戏

**「开启数字炸弹」无反应**  
确认群组在有转账功能的群组列表中，且当前没有其他游戏正在进行。

**「我猜是 50」无反应**  
格式支持「我猜是 XX」「我猜 XX」「猜 XX」；数字须在当前范围内；每人 10 秒冷却。

---

## Supervisord

**无法访问 `http://localhost:51901`**  
检查端口映射，以及 `SUPERVISOR_USERNAME` / `SUPERVISOR_PASSWORD` 环境变量是否已设置。

---

## 日志

```bash
# 实时查看应用日志
docker-compose logs -f awbothub

# 查看 Supervisord 日志
docker exec -it awbothub tail -f /app/logs/supervisord.log
```

日志文件过大：进入「系统维护 → 日志清理」菜单，配置自动清理或立即清理。

---

## 转账功能

**Azusa 转账不触发**  
发送格式须为 `+数字`（如 `+100`），确认消息格式为「成功赠送 X 魔力值给对方…」。

---

更多帮助请提交 [Issue](https://github.com/AWdress/AWBotHub/issues)。
