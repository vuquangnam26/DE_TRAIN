from ETL.config.settings import Settings

settings = Settings()

# In ra các cấu hình để test
print("✅ Testing .env Configuration:")
print("MYSQL_HOST:", settings.MYSQL_HOST)
print("MYSQL_PORT:", settings.MYSQL_PORT)
print("MYSQL_USER:", settings.MYSQL_USER)
print("MYSQL_PASSWORD:", settings.MYSQL_PASSWORD)
print("MYSQL_DATABASE:", settings.MYSQL_DATABASE)

print("MONGODB_URI:", settings.MONGODB_URI)
print("MONGODB_DATABASE:", settings.MONGODB_DATABASE)

print("REDIS_HOST:", settings.REDIS_HOST)
print("REDIS_PORT:", settings.REDIS_PORT)
print("REDIS_DB:", settings.REDIS_DB)

print("KAFKA_BOOTSTRAP_SERVERS:", settings.KAFKA_BOOTSTRAP_SERVERS)
print("KAFKA_TOPIC:", settings.KAFKA_TOPIC)

print("SPARK_MASTER:", settings.SPARK_MASTER)
print("SPARK_APP_NAME:", settings.SPARK_APP_NAME)
