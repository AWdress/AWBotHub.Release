# 版本管理指南 (v2.x)

## 概述
本项目使用基于 Git 标签的语义化版本管理，格式为 `v主版本.次版本.修订版本`（如 `v2.1.1`）。

## 版本类型

### 主版本 (Major)
- 架构级重构（如从脚本版迁移至 v2.0 六边形架构）。
- 示例：`v1.0.0` → `v2.0.0`

### 次版本 (Minor)
- 向后兼容的功能性新增（如 v2.1.1 的交互式登录）。
- 示例：`v2.1.0` → `v2.1.1`

### 修订版本 (Patch)
- 向后兼容的问题修正或小幅优化。
- 示例：`v2.1.1` → `v2.1.2`

## 使用方法

### 1. 查看当前版本信息
```bash
python scripts/version.py info
```

### 2. 创建新版本

#### 补丁版本（Bug修复）
```bash
python scripts/version.py patch "修复红包抢取超时问题"
```

#### 小版本（新功能）
```bash
python scripts/version.py minor "添加supervisord Web管理界面"
```

#### 大版本（重大更新）
```bash
python scripts/version.py major "重构核心架构"
```

#### 指定版本号
```bash
python scripts/version.py create v1.2.3 "自定义版本发布"
```

## 自动化流程

### 开发构建
- 每次推送到 `main` 分支时自动构建
- 版本号格式：`main-<commit-hash>`
- 镜像标签：`latest`, `dev`, `main-<hash>`

### 正式发布
- 推送版本标签时自动触发发布流程
- 构建多平台镜像（AMD64 + ARM64）
- 镜像标签：`v1.0.0`, `latest`

## 版本标签示例

```bash
# 查看所有版本标签
git tag -l --sort=-version:refname

# 创建并推送版本标签
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## Docker镜像标签

### 开发版本
- `ghcr.io/awdress/awbothub:latest` - 最新开发版本
- `ghcr.io/awdress/awbothub:dev` - 开发版本
- `ghcr.io/awdress/awbothub:main-abc1234` - 特定提交版本

### 正式版本
- `ghcr.io/awdress/awbothub:v1.0.0` - 特定版本
- `ghcr.io/awdress/awbothub:latest` - 最新正式版本

## 发布检查清单

发布新版本前，请确保：

- [ ] 所有测试通过
- [ ] 文档已更新
- [ ] 版本号符合语义化版本规范
- [ ] 提交信息清晰明确
- [ ] 代码已合并到主分支

## 回滚版本

如果需要回滚到之前的版本：

```bash
# 查看历史版本
git tag -l --sort=-version:refname

# 回滚到特定版本
git checkout v1.0.0
git tag -a v1.0.1 -m "回滚到稳定版本"
git push origin v1.0.1
```

## 注意事项

1. **版本号唯一性**：每个版本号只能使用一次
2. **标签推送**：创建标签后需要推送到远程仓库
3. **构建时间**：正式版本构建时间较长（多平台）
4. **安全扫描**：正式版本会自动进行安全漏洞扫描
