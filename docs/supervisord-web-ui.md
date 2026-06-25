# Supervisord Web 管理界面

本文档说明如何访问和使用 Supervisord 的 Web 管理界面。

## 🌐 访问地址

### 本地访问
- **URL**: http://localhost:51901
- **用户名**: 在配置中设定的 `SUPERVISOR_USERNAME`
- **密码**: 在配置中设定的 `SUPERVISOR_PASSWORD`

### Docker Compose 访问
- **URL**: http://localhost:51901
- **端口映射**: `51901:51901`

## 🔧 配置说明

### 环境变量配置
在 `docker-compose.yml` 中设置：
```yaml
environment:
  - SUPERVISOR_USERNAME=your_username  # 替换为您的用户名
  - SUPERVISOR_PASSWORD=your_password  # 替换为您的密码
```

### 默认配置
如果未设置环境变量，将使用默认值：
- **用户名**: `admin`
- **密码**: `admin123`

## 📋 功能特性

### 1. 进程管理
- 查看所有进程状态
- 启动/停止/重启进程
- 查看进程日志
- 监控进程资源使用

### 2. 日志查看
- 实时查看进程日志
- 下载日志文件
- 清空日志

### 3. 配置管理
- 查看supervisord配置
- 重新加载配置
- 重启supervisord服务

### 4. 系统信息
- 查看系统资源使用情况
- 监控进程状态
- 查看事件日志

## 🚀 使用方法

### 1. 启动容器
```bash
# 使用docker-compose启动
docker-compose up -d

# 或使用docker run
docker run -d \
  --name awbothub \
  -p 52901:51901 \
  -e SUPERVISOR_USERNAME=admin \
  -e SUPERVISOR_PASSWORD=admin123 \
  your-image:latest
```

### 2. 访问Web界面
1. 打开浏览器
2. 访问 http://localhost:52901
3. 输入用户名和密码
4. 点击登录

### 3. 管理进程
- **查看状态**: 在主页查看所有进程状态
- **启动进程**: 点击进程名称，然后点击"Start"
- **停止进程**: 点击进程名称，然后点击"Stop"
- **重启进程**: 点击进程名称，然后点击"Restart"

### 4. 查看日志
- 点击进程名称
- 选择"Stdout"或"Stderr"标签
- 查看实时日志输出

## 🔒 安全配置

### 1. 修改默认密码
```yaml
environment:
  - SUPERVISOR_USERNAME=your_secure_username
  - SUPERVISOR_PASSWORD=your_secure_password
```

### 2. 使用强密码
- 至少8个字符
- 包含大小写字母、数字和特殊字符
- 避免使用常见密码

### 3. 网络安全
- 仅在受信任的网络中暴露端口
- 考虑使用反向代理
- 定期更新密码

## 🐛 故障排除

### 1. 无法访问Web界面
**检查项目**:
- 容器是否正在运行
- 端口映射是否正确
- 防火墙是否阻止访问

**解决方案**:
```bash
# 检查容器状态
docker ps

# 检查端口映射
docker port awbothub

# 查看容器日志
docker logs awbothub
```

### 2. 登录失败
**检查项目**:
- 用户名和密码是否正确
- 环境变量是否设置正确

**解决方案**:
```bash
# 检查环境变量
docker exec awbothub env | grep SUPERVISOR

# 重新设置环境变量
docker-compose down
docker-compose up -d
```

### 3. 进程状态异常
**检查项目**:
- 进程配置是否正确
- 日志中是否有错误信息

**解决方案**:
- 在Web界面查看进程日志
- 检查supervisord配置文件
- 重启相关进程

## 📊 监控功能

### 1. 实时监控
- 进程状态实时更新
- 资源使用情况监控
- 事件日志实时显示

### 2. 历史记录
- 进程启动/停止历史
- 错误日志记录
- 性能统计信息

### 3. 告警功能
- 进程异常退出告警
- 资源使用过高告警
- 配置错误告警

## 🔗 相关链接

- [Supervisord官方文档](http://supervisord.org/)
- [Supervisord Web界面文档](http://supervisord.org/configuration.html#inet-http-server-section-settings)
- [Docker Compose文档](https://docs.docker.com/compose/)

## 📝 注意事项

1. **安全性**: Web界面默认没有加密，建议在内网使用
2. **性能**: 频繁刷新可能影响性能，建议适度使用
3. **备份**: 定期备份supervisord配置文件
4. **更新**: 定期更新supervisord版本以获得最新功能和安全修复
