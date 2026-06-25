# GitHub Actions 自动化构建

本文档说明如何使用GitHub Actions自动构建和发布Docker镜像。

## 🚀 功能特性

- **自动构建**: 当Dockerfile或相关文件变更时自动构建镜像
- **多平台支持**: 支持linux/amd64和linux/arm64架构
- **安全扫描**: 使用Trivy进行漏洞扫描
- **自动发布**: 支持标签发布和手动发布
- **缓存优化**: 使用GitHub Actions缓存加速构建

## 📋 触发条件

### 自动构建触发
当以下文件发生变更时，会自动触发构建：
- `Dockerfile`
- `docker-entrypoint.sh`
- `requirements.txt`
- `pyproject.toml`
- `.github/workflows/docker-build.yml`

### 分支触发
- `main` 分支推送
- `master` 分支推送
- Pull Request到`main`或`master`分支

### 手动触发
- 在GitHub Actions页面点击"Run workflow"按钮
- 使用`workflow_dispatch`事件

## 🏷️ 镜像标签策略

### 自动构建标签
- `latest`: 主分支的最新版本
- `dev`: 开发版本
- `{branch-name}`: 分支名称标签
- `{branch-name}-{commit-sha}`: 分支名+提交SHA

### 发布标签
- `{version}`: 版本号标签（如v1.0.0）
- `latest`: 最新发布版本

## 🔧 使用方法

### 1. 设置GitHub Secrets

确保以下secrets已配置：
- `GITHUB_TOKEN`: 自动提供，用于推送镜像到GitHub Container Registry

### 2. 自动构建

推送代码到主分支：
```bash
git add .
git commit -m "Update Dockerfile"
git push origin main
```

### 3. 手动发布

#### 方法1: 使用标签
```bash
git tag v1.0.0
git push origin v1.0.0
```

#### 方法2: 使用GitHub Actions界面
1. 进入GitHub仓库的Actions页面
2. 选择"Release"工作流
3. 点击"Run workflow"
4. 输入版本标签（如v1.0.0）
5. 点击"Run workflow"

### 4. 使用构建的镜像

```bash
# 拉取最新镜像
docker pull ghcr.io/your-username/your-repo:latest

# 运行容器
docker run -d --name awbothub \
  -v /path/to/config:/app/config \
  -v /path/to/logs:/app/logs \
  -v /path/to/sessions:/app/sessions \
  ghcr.io/your-username/your-repo:latest
```

## 📊 构建状态

### 查看构建状态
1. 进入GitHub仓库
2. 点击"Actions"标签
3. 查看构建历史和状态

### 构建日志
- 点击具体的构建任务
- 查看详细的构建日志
- 下载构建产物

## 🔍 安全扫描

每次构建都会自动进行安全扫描：
- 使用Trivy扫描镜像漏洞
- 结果上传到GitHub Security tab
- 发现高危漏洞时会阻止构建

## 🏥 健康检查

镜像包含健康检查功能：
- `/health`: 完整健康检查
- `/health/ready`: 就绪检查
- `/health/live`: 存活检查

```bash
# 检查容器健康状态
docker inspect --format='{{.State.Health.Status}}' awbothub

# 手动健康检查
curl http://localhost:8080/health
```

## 🐛 故障排除

### 构建失败
1. 检查Dockerfile语法
2. 查看构建日志中的错误信息
3. 确保所有依赖文件存在

### 推送失败
1. 检查GitHub token权限
2. 确认仓库有packages写入权限
3. 检查镜像名称格式

### 安全扫描失败
1. 查看Trivy扫描报告
2. 更新基础镜像版本
3. 修复已知漏洞

## 📝 最佳实践

### 1. 版本管理
- 使用语义化版本号（如v1.0.0）
- 为重要更新创建标签
- 保持latest标签指向稳定版本

### 2. 安全
- 定期更新基础镜像
- 使用非root用户运行容器
- 扫描并修复安全漏洞

### 3. 性能
- 使用多阶段构建减小镜像大小
- 利用Docker层缓存
- 使用.dockerignore排除不必要文件

### 4. 监控
- 设置构建通知
- 监控镜像拉取统计
- 定期检查构建历史

## 🔗 相关链接

- [GitHub Actions文档](https://docs.github.com/en/actions)
- [Docker Buildx文档](https://docs.docker.com/buildx/)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [Trivy安全扫描](https://trivy.dev/)
