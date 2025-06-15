import os
from decouple import Config, RepositoryEnv

# Lấy đường dẫn đến file `.env` nằm tại thư mục gốc
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
ENV_PATH = os.path.join(BASE_DIR, '.env')

# Load file .env thủ công
config = Config(repository=RepositoryEnv(ENV_PATH))
print(ENV_PATH)
class Settings:
    def __init__(self):
        self.MYSQL_HOST = config('MYSQL_HOST')
        self.MYSQL_PORT = config('MYSQL_PORT', cast=int)
        self.MYSQL_USER = config('MYSQL_USER')
        self.MYSQL_PASSWORD = config('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = config('MYSQL_DATABASE')

        self.KAFKA_BOOTSTRAP_SERVERS = config('KAFKA_BOOTSTRAP_SERVERS')
        self.KAFKA_TOPIC = config('KAFKA_TOPIC_PREFIX') + '_cdc'

        self.MONGODB_URI = f"mongodb://{config('MONGODB_HOST')}:{config('MONGODB_PORT')}"
        self.MONGODB_DATABASE = config('MONGODB_DATABASE')

        self.REDIS_HOST = config('REDIS_HOST')
        self.REDIS_PORT = config('REDIS_PORT', cast=int)
        self.REDIS_DB = config('REDIS_DB', cast=int)

        self.SPARK_MASTER = config('SPARK_MASTER')
        self.SPARK_APP_NAME = config('SPARK_APP_NAME')
