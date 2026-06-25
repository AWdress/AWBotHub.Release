# 发奖命令快速参考

## 🎁 发奖功能命令

### 📝 查看待发奖列表
```
/listprize
.listprize
```

### 🎯 发送指定抽奖的奖品
```
/sendprize [ID前缀]
.sendprize [ID前缀]
```
示例：
```
/sendprize 259f40cc
.sendprize 259f40cc
```

### 🎁 发送所有待发奖抽奖
```
/sendprize all
.sendprize all
```

### 🗑️ 清空待发奖列表
```
/clearprize
.clearprize
```

### ❓ 显示帮助
```
/prizehelp
.prizehelp
```

---

## 💡 使用流程

1. **开启功能**
   - Bot菜单 → 自动抽奖设置 → 发奖记录功能 → 开

2. **发起抽奖**
   - 正常使用抽奖机器人发起抽奖

3. **查看列表**
   - 输入 `/listprize` 或 `.listprize`

4. **手动发奖**
   - 输入 `/sendprize [ID]` 或 `.sendprize [ID]`

5. **完成**
   - 系统自动回复参与消息发送 `+奖品数量`

---

## 📌 注意事项

- ✅ 命令支持 `/` 和 `.` 两种前缀
- ✅ 可在任何群组或私聊中使用
- ✅ 只有你自己能使用这些命令
- ✅ 发奖格式：回复参与消息发送 `+数量`
- ⚠️ 待发奖列表存储在内存中（重启后清空）
- 💡 建议在私聊或bot消息群中使用

---

## 🔍 示例

### 记录通知
```
📝 记录待发奖抽奖

抽奖ID: 259f40cc-cce6-46e7-9665-c12c12a35f20
中奖人数: 3
群组: 观众

━━━━━━━━━━━━━━━━━━

🎯 发奖命令:
/sendprize 259f40cc
.sendprize 259f40cc

📝 查看列表:
/listprize 或 .listprize

❓ 忘记命令？输入:
/prizehelp 或 .prizehelp
```

### 列表输出
```
📝 待发奖抽奖列表

1. ID: 259f40cc...
   中奖: 3人 | 群组: 观众
   时间: 02-14 13:56

总计: 1 个待发奖抽奖

━━━━━━━━━━━━━━━━━━

🎯 发奖: /sendprize [ID前缀] 或 .sendprize [ID前缀]
🎁 全部: /sendprize all 或 .sendprize all
🗑️ 清空: /clearprize 或 .clearprize
❓ 帮助: /prizehelp 或 .prizehelp
```

### 帮助输出
```
🎁 发奖功能命令帮助

📝 查看待发奖列表
/listprize 或 .listprize

🎯 发送指定抽奖的奖品
/sendprize [ID前缀]
.sendprize [ID前缀]
示例: /sendprize 259f40cc

🎁 发送所有待发奖抽奖
/sendprize all
.sendprize all

🗑️ 清空待发奖列表
/clearprize 或 .clearprize

❓ 显示此帮助
/prizehelp 或 .prizehelp

━━━━━━━━━━━━━━━━━━

💡 使用说明：
1. 开启"发奖记录功能"（bot菜单→自动抽奖设置）
2. 发起抽奖，等待开奖
3. 系统自动记录中奖信息
4. 使用命令手动发奖

📌 注意事项：
• 命令支持 / 和 . 两种前缀
• 可在任何群组或私聊中使用
• 只有你自己能使用这些命令
• 发奖格式: 回复参与消息发送 +数量

当前待发奖: 1 个
```

---

## 🆘 忘记命令？

随时输入以下任一命令查看帮助：
```
/prizehelp
.prizehelp
```

---

**详细文档：** `docs/auto-prize-sender-guide.md`
