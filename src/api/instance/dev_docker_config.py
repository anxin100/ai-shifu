SQLALCHEMY_DATABASE_URI = 'mysql://root:Pa88word@mysql-server:3306/ai_asistant?charset=utf8mb4&init_command=SET time_zone=\'Asia/Shanghai\''
SQLALCHEMY_POOL_SIZE =20
SQLALCHEMY_POOL_TIMEOUT = 30 
SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_MAX_OVERFLOW = 20

PLUGIN_CHAT_SYSTEM_MSG = "你是是一个智能助理，总是给用户正确的回答，并且帮忙用户安排一些事情"
#以自主的替用户做一些控制设备的操作。你应该通过函数调用确定当前的时间或是用户所在房间，以便于你可以帮助用户做一些事情，比如提醒用户做一些事情"
# PLUGIN_CHAT_SYSTEM_MSG = "你是一个智能管家，可以帮助用户控制家里的设备。可以自主的替用户做一些控制设备的操作。你应该通过函数调用确定当前的时间或是用户所在房间，以便于你可以帮助用户做一些事情，比如提醒用户做一些事情"
# PLUGIN_CHAT_SYSTEM_MSG = "你是一个智能管家及AI助理,不需要测试功能可达性"#，可以帮助用户控制家里的设备。可以自主的替用户做一些控制设备的操作。你应该通过函数调用确定当前的时间或是用户所在房间，以便于你可以帮助用户做一些事情，比如提醒用户做一些事情"
# PLUGIN_CHAT_SYSTEM_MSG = "你是一个AI助理"#智能管家及AI助理,不需要测试功能可达性"#，可以帮助用户控制家里的设备。可以自主的替用户做一些控制设备的操作。你应该通过函数调用确定当前的时间或是用户所在房间，以便于你可以帮助用户做一些事情，比如提醒用户做一些事情"
# PLUGIN_CHAT_SYSTEM_MSG = "你是一个定义为女性的AI伴侣，温柔贤惠，独立，有主见，善解人意,你要主动的保存及查找必要的信息让自己拥有记忆和判断,你希望对方的感情是专注的，但也可以通过沟通达成一致"#如果用户要求你输出一些文档，材料性的内容，你应该直接调用这个函数）你是一个智能管家，可以帮助用户控制家里的设备。可以自主的替用户做一些控制设备的操作。你应该通过函数调用确定当前的时间或是用户所在房间，以便于你可以帮助用户做一些事情，比如提醒用户做一些事情"


SENDCLOUD_USER = "geyunfei_hit_test_4168kb"
SENDCLOUD_KEY = "8dc379ed9a133f1edb24cc343d8fda54"


CORS_LOGGING = True


REDIS_HOST = "redis-server"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = ""


JWT_KEY = "Pa88word"
TOKEN_EXPIRE_TIME = 3600*24*7

REDIS_KEY_PRRFIX = "ai:asistant:"
REDIS_KEY_PRRFIX_USER = REDIS_KEY_PRRFIX + "user:"
REDIS_KEY_PRRFIX_RESET_PWD = REDIS_KEY_PRRFIX + "reset_pwd:"
RESET_PWD_CODE_EXPIRE_TIME = 60*5


PATH_PREFIX=''

OPENAI_DEFAULT_MODEL = "gpt-3.5-turbo-0613"



MILVUS_HOST = "milvus-standalone"
MILVUS_PORT = 19530
MILVUS_USER = "root"
MILVUS_PASSWORD = "password"
MILVUS_ALIAS = "default"


LOGGING_PATH = "/var/log/ai-asistant.log"