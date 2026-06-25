#######################登录基础配置########################

API_ID = "your_api_id"  # 从 https://my.telegram.org 获取
API_HASH = "your_api_hash"  # 从 https://my.telegram.org 获取
BOT_TOKEN = "your_bot_token"  # 从 @BotFather 获取

# 多账号配置：每项含 session（文件名）、name（昵称）、tgid（Telegram ID）
ACCOUNTS = [
    {"session": "YourUsername", "name": "YourName", "tgid": 1234567890},
    # {"session": "Account2", "name": "Name2", "tgid": 0},
]

# 以下从主账号自动推导，无需手动设置
MY_NAME     = ACCOUNTS[0]["name"]    if ACCOUNTS else ""
MY_TGID     = ACCOUNTS[0]["tgid"]    if ACCOUNTS else 0
NY_USERNAME = ACCOUNTS[0]["session"] if ACCOUNTS else ""

# Web 控制面板配置 (可选)
# 如果设置了 WEB_UI_URL，Bot 菜单会显示控制面板按钮
WEB_UI_URL = "" 
WEB_UI_PORT = 18000 # 监听端口，如果被占用请修改此处
# 如果设置为 True，程序启动时会自动使用 ngrok 开启公网映射，无需手动设置 WEB_UI_URL
NGROK_ENABLE = False
NGROK_TOKEN = "" # 建议在 ngrok.com 注册获取 token 以解除限制


###################################AI 对话配置##################################

# AI 模拟真人对话配置
AI_INFO = {
    "enabled": False,              # 是否启用 AI 功能
    "provider": "openai",          # AI 提供商，目前仅支持 openai (兼容格式)
    "api_key": "your_api_key",     # API 密钥
    "base_url": "https://api.openai.com/v1",  # API 代理/基础地址
    "model": "gpt-3.5-turbo",      # 使用的模型名称
    "system_prompt": "你是一个混迹 PT 圈多年的大佬，说话幽默但带点毒舌，喜欢用‘骚年’称呼别人。", # AI 人设/系统提示词
    "max_history": 10,             # 上下文记忆轮数
    "white_list_chats": [],        # 白名单群组/用户 ID 列表，为空则不限制（建议私聊使用）
    "enable_private_chat": True,   # 私聊是否分发 AI 回复
    "enable_group_chat": True,     # 群聊/超级群是否分发 AI 回复
    "enable_explain_command": True, # 是否允许 .ai /ai 消息解释命令
}


########################运行代理配置########################

proxy_set = {
    "proxy_enable": False,  # 如果需要使用代理登录则设为true 反之False
    # tg登录的代理
    "proxy": {
        "scheme": "http",  # "socks4", "socks5" and "http" are supported
        "hostname": "your_proxy_host",
        "port": 7890,
        "username": "your_proxy_username",
        "password": "your_proxy_password",
    },
    # 网页访问用代理
    "PROXY_URL": "http://your_proxy_host:7890",
}


PT_GROUP_ID = {
    "GROUP_1_ID": -1001234567890,  # 群组1 ID
    "GROUP_2_ID": -1001234567891,  # 群组2 ID
    "GROUP_3_ID": -1001234567892,  # 群组3 ID
    "BOT_MESSAGE_CHAT": MY_TGID,  # 本脚本发各种提示的群
}

###################################auto_lotttery配置#############################

#参与抽奖的群组
LOTTERY_TARGET_GROUP = [
    PT_GROUP_ID['GROUP_1_ID'],
    PT_GROUP_ID['GROUP_2_ID'],
    PT_GROUP_ID['GROUP_3_ID'],
]
#参与抽奖的奖品
PRIZE_LIST = {
    "GROUP_1_ID": ["奖品1", "奖品2", "奖品3"],
    "GROUP_2_ID": ['魔力', '积分'],            
    "GROUP_3_ID": ['金币','💎币','GB','邀请'],
    # 用户可以直接在这里添加新的群组ID和奖品
    # 格式: "群组ID": ['奖品1', '奖品2', '奖品3']
    # 示例: "GROUP_4_ID": ['自定义奖品1', '自定义奖品2'],
}   #设置需要参数的奖品名 支持动态修改新增key和群组ID

# 奖品匹配规则配置 - 简化版：只要奖品名包含关键词就行
PRIZE_MATCH_RULES = {
    "case_sensitive": False,  # 是否区分大小写
}

# 陷阱抽奖检测配置
TRAP_LOTTERY_DETECTION = {
    "case_sensitive": False,  # 关键词匹配是否区分大小写
    "enable_prize_pattern_check": True,  # 是否启用奖品名称检测
    "enable_creator_blacklist": True,  # 是否启用创建者黑名单
    "enable_participant_check": True,  # 是否启用参与人数检测
    "max_participants": 1,  # 最大参与人数（超过视为陷阱）
    "blacklist_creator_ids": [],  # 创建者黑名单ID列表
    "suspicious_keywords": [
        # 中文关键词 - 脚本/机器人/封禁相关
        "脚本", "挂机", "机器人", "外挂", "bot", "自动", "作弊", "刷", "假人",
        "测试脚本", "测试机器人", "测试bot", "检测脚本", "检测机器人",
        "封禁", "封", "禁", "ban", "banned", "封号", "封禁测试", "测试封禁",
        
        # 拼音变体
        "jiao ben", "jiaoben", "gua ji", "guaji", "ji qi ren", "jiqiren",
        "wai gua", "waigua", "zi dong", "zidong", "zuo bi", "zuobi",
        "feng jin", "fengjin", "feng hao", "fenghao",
        
        # 英文关键词
        "script", "bot", "auto", "cheat", "hack", "fake", "test", "ban", "banned", "block", "blocked",
        
        # 空格分隔变体
        "脚 本", "挂 机", "机 器 人", "外 挂", "自 动", "作 弊", "封 禁", "封 号",
        
        # 符号分隔变体
        "脚-本", "脚_本", "脚.本", "挂-机", "挂_机", "机-器-人", "封-禁", "封_禁",
        
        # 数字混淆变体
        "脚本1", "脚本2", "机器人1", "bot1", "bot2", "ban1", "封禁1",
        
        # 同音字变体
        "角本", "叫本", "挂鸡", "鸡器人", "外挂", "歪挂", "丰禁", "风禁",
        
        # 繁体字
        "腳本", "掛機", "機器人", "外掛", "自動", "作弊", "封禁", "封號",
        
        # 其他变体
        "jb", "gb", "jqr", "wg", "zd", "zb", "fj", "fn",
        "脚木", "挂几", "鸡器", "外瓜", "自冻", "做弊", "封尽",
        
        # 更多拼音组合
        "jiao-ben", "jiao_ben", "gua-ji", "gua_ji", "feng-jin", "feng_jin",
        
        # 英文变体
        "scr1pt", "b0t", "aut0", "che4t", "h4ck", "b4n", "b@n",
        
        # 混合变体
        "脚本bot", "机器人script", "auto脚本", "bot机器人", "ban脚本", "封禁bot",
        
        # 零宽字符后的变体（实际使用时会被过滤）
        "脚​本", "机​器​人", "外​挂", "封​禁",
    ]
}

################################数据库配置##############################

DB_INFO = {
    "dbset": "mySQL",  # mySQL/SQLite/PostgreSQL
    "address": "your_database_host",  # 数据库服务器地址
    "db_name": "your_database_name",  # 数据库名称
    "port": 3306,  # 数据库端口
    "user": "your_database_user",  # 数据库用户名
    "password": "your_database_password",  # 数据库密码
}

###################################数字炸弹游戏配置#############################

# 数字炸弹游戏配置
NUMBER_BOMB_CONFIG = {
    "enable_range_shrink": True,  # 是否启用范围调整机制
    "shrink_mechanism": {
        "distance_1_5": 0,    # 距离1-5：不调整范围
        "distance_6_15": 0,   # 距离6-15：不调整范围
        "distance_16_30": -1,  # 距离16-30：惩罚扩大1个数字
        "distance_31_plus": -2, # 距离31+：惩罚扩大2个数字
    }
}