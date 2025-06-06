# 🚀 Modern Data Pipeline Project

A comprehensive real-time data pipeline implementation following modern data engineering practices. This project demonstrates Change Data Capture (CDC) from MySQL, streaming through Kafka, processing with PySpark, and storing in MongoDB/Redis.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start with Docker](#quick-start-with-docker)
- [Configuration](#configuration)
- [Key Components](#key-components)
- [Development Workflow](#development-workflow)
- [Production Deployment](#production-deployment)
- [Monitoring & Observability](#monitoring--observability)
- [Testing Strategy](#testing-strategy)
- [Contributing](#contributing)

## 📁 Project Structure

```
data-pipeline-project/
├── README.md
├── requirements.txt
├── setup.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── database.yaml
│   ├── kafka.yaml
│   └── spark.yaml
│
├── src/
│   ├── __init__.py
│   │
│   ├── connectors/
│   │   ├── __init__.py
│   │   ├── mysql_connector.py
│   │   ├── mongodb_connector.py
│   │   ├── redis_connector.py
│   │   └── kafka_connector.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── mysql_schemas.py
│   │   ├── kafka_schemas.py
│   │   └── validation.py
│   │
│   ├── triggers/
│   │   ├── __init__.py
│   │   ├── database_trigger.py
│   │   ├── cdc_handler.py
│   │   └── scheduler.py
│   │
│   ├── producers/
│   │   ├── __init__.py
│   │   ├── kafka_producer.py
│   │   └── data_publisher.py
│   │
│   ├── consumers/
│   │   ├── __init__.py
│   │   ├── kafka_consumer.py
│   │   └── spark_streaming.py
│   │
│   ├── transformations/
│   │   ├── __init__.py
│   │   ├── data_cleaner.py
│   │   ├── data_validator.py
│   │   ├── business_logic.py
│   │   └── spark_transformations.py
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── mongodb_writer.py
│   │   ├── redis_cache.py
│   │   └── batch_writer.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── metrics.py
│       ├── helpers.py
│       └── exceptions.py
│
├── jobs/
│   ├── __init__.py
│   ├── realtime_pipeline.py
│   ├── batch_pipeline.py
│   └── data_quality_check.py
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_connectors.py
│   │   ├── test_transformations.py
│   │   └── test_validators.py
│   ├── integration/
│   │   ├── test_pipeline.py
│   │   └── test_kafka_flow.py
│   └── fixtures/
│       ├── sample_data.json
│       └── test_config.yaml
│
├── scripts/
│   ├── setup_databases.py
│   ├── create_kafka_topics.py
│   ├── run_pipeline.py
│   └── monitoring.py
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── pipeline_testing.ipynb
│   └── performance_analysis.ipynb
│
├── deployment/
│   ├── kubernetes/
│   │   ├── namespace.yaml
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   ├── helm/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
│
├── monitoring/
│   ├── prometheus/
│   │   └── rules.yaml
│   ├── grafana/
│   │   └── dashboards/
│   └── alerts/
│       └── pipeline_alerts.yaml
│
└── docs/
    ├── architecture.md
    ├── setup_guide.md
    ├── api_documentation.md
    └── troubleshooting.md
```

## 🏗️ Architecture Overview

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  MySQL  │───▶│ Trigger │───▶│  Kafka  │───▶│  Spark  │───▶│MongoDB/ │
│ (Source)│    │  (CDC)  │    │(Stream) │    │(Process)│    │ Redis   │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Data Flow:**
1. **MySQL CDC**: Monitor binlog để capture changes (INSERT/UPDATE/DELETE)
2. **Kafka Streaming**: Publish events với data validation
3. **Spark Processing**: Real-time transformation và business logic
4. **Storage**: Write vào MongoDB và cache Redis

## ✨ Features

- 🔄 **Real-time Change Data Capture** từ MySQL binlog
- 📨 **Event-driven Architecture** với Apache Kafka
- ⚡ **Stream Processing** với PySpark Structured Streaming
- 🗄️ **Multi-storage Support** (MongoDB, Redis caching)
- 🔍 **Data Validation** với Pydantic schemas
- 📊 **Observability** với Prometheus/Grafana
- 🐳 **Containerized Deployment** với Docker/Kubernetes
- 🧪 **Comprehensive Testing** (unit, integration, performance)
- 📈 **Auto-scaling** và fault tolerance

## 🛠️ Prerequisites

- **Docker** và **Docker Compose**
- **Python 3.9+**
- **Java 8/11** (cho Apache Spark)
- **Git**

## 🚀 Quick Start with Docker

### 1. Clone Repository
```bash
git clone <repository-url>
cd data-pipeline-project
```

### 2. Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Chỉnh sửa cấu hình theo môi trường
nano .env
```

### 3. Start Infrastructure với Docker Compose
```bash
# Start tất cả services
docker-compose up -d

# Kiểm tra services đang chạy
docker-compose ps

# Xem logs
docker-compose logs -f
```

### 4. Initialize Database & Kafka Topics
```bash
# Setup MySQL schemas
docker-compose exec pipeline python scripts/setup_databases.py

# Tạo Kafka topics
docker-compose exec pipeline python scripts/create_kafka_topics.py
```

### 5. Run Data Pipeline
```bash
# Chạy pipeline
docker-compose exec pipeline python scripts/run_pipeline.py

# Hoặc chạy realtime job
docker-compose exec pipeline python jobs/realtime_pipeline.py
```

### 6. Access Services
- **Pipeline API**: http://localhost:8080
- **Kafka UI**: http://localhost:8081
- **Spark UI**: http://localhost:4040
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090

## ⚙️ Configuration

### Docker Environment Variables (.env)
```bash
# Database Configuration
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_USER=pipeline_user
MYSQL_PASSWORD=secure_password
MYSQL_DATABASE=source_db

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
KAFKA_TOPIC_PREFIX=data_pipeline

# MongoDB Configuration
MONGODB_URI=mongodb://mongodb:27017
MONGODB_DATABASE=processed_data

# Redis Configuration
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

# Spark Configuration
SPARK_MASTER=local[*]
SPARK_APP_NAME=DataPipeline

# Monitoring
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000
```

### Configuration Files
- `config/database.yaml` - Database connection settings
- `config/kafka.yaml` - Kafka topics và consumer groups
- `config/spark.yaml` - Spark job configurations

## 🔧 Key Components

### 1. Config Management
- **Centralized configuration** với YAML files
- **Environment-specific settings**
- **Database connection parameters** với retry logic

### 2. Connectors
- **Modular database connectors** (MySQL, MongoDB, Redis)
- **Kafka integration** cho messaging
- **Connection pooling** và retry mechanisms

### 3. Data Flow Components

#### Triggers & CDC (Change Data Capture)
```python
# src/triggers/cdc_handler.py
class MySQLCDCHandler:
    def setup_binlog_listener(self):
        # Monitor MySQL binlog for changes
        pass
    
    def handle_change_event(self, event):
        # Process INSERT/UPDATE/DELETE events
        pass
```

#### Kafka Integration
```python
# src/producers/kafka_producer.py
class DataProducer:
    def publish_change_event(self, topic, data):
        # Send data to Kafka topic
        pass
```

#### Spark Processing
```python
# src/consumers/spark_streaming.py
class SparkStreamProcessor:
    def process_kafka_stream(self):
        # Real-time data processing
        pass
    
    def write_to_storage(self, df):
        # Write to MongoDB/Redis
        pass
```

### 4. Modern Features

#### Data Validation
- **Pydantic models** cho data validation
- **Schema evolution handling**
- **Data quality checks** tự động

#### Observability
- **Prometheus metrics** collection
- **Structured logging** với correlation IDs
- **Distributed tracing** cho debugging

#### Containerization
- **Docker containers** cho tất cả components
- **Kubernetes deployment** manifests
- **Helm charts** cho easy deployment

## 🛠️ Development Workflow

### Local Development
```bash
# Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start services với Docker Compose
docker-compose up -d

# Run pipeline locally
python scripts/run_pipeline.py
```

### Docker Development
```bash
# Build custom image
docker build -t data-pipeline:dev .

# Run với development compose
docker-compose -f docker-compose.dev.yml up -d

# Attach to container để debug
docker-compose exec pipeline bash
```

### Testing Strategy
- **Unit tests** cho individual components
- **Integration tests** cho end-to-end flow
- **Performance testing** với sample data

```bash
# Run tests trong container
docker-compose exec pipeline pytest tests/

# Run với coverage
docker-compose exec pipeline pytest --cov=src tests/
```

## 🚢 Production Deployment

### Docker Production
```bash
# Build production image
docker build -f Dockerfile.prod -t data-pipeline:prod .

# Deploy với production compose
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes Deployment
```bash
# Apply Kubernetes manifests
kubectl apply -f deployment/kubernetes/

# Sử dụng Helm
helm install data-pipeline deployment/helm/

# Check pods
kubectl get pods -n data-pipeline
```

### Scalability Considerations
- **Horizontal scaling** với Kubernetes HPA
- **Kafka partitioning** cho parallel processing
- **Redis clustering** cho high availability
- **Load balancing** cho API endpoints

### Reliability Features
- **Error handling** và retry mechanisms
- **Dead letter queues** cho failed messages
- **Health checks** và monitoring
- **Circuit breakers** cho external dependencies

### Security
- **Secret management** với Kubernetes secrets
- **Network policies** và encryption
- **Access control** và authentication
- **Container security** scanning

## 📊 Monitoring & Observability

### Metrics Dashboard
- **Pipeline throughput** (messages/second)
- **Processing latency** (p95, p99)
- **Error rates** và failed messages
- **Resource utilization** (CPU, memory)
- **Data quality scores**

### Alerting
```bash
# Configure alerts
kubectl apply -f monitoring/alerts/pipeline_alerts.yaml

# View Prometheus rules
kubectl apply -f monitoring/prometheus/rules.yaml
```

### Log Aggregation
- **Structured logging** với JSON format
- **Correlation IDs** cho request tracing
- **Log levels** configuration
- **Centralized logging** với ELK stack

## 🧪 Testing Strategy

### Test Categories
1. **Unit Tests**: Individual component testing
2. **Integration Tests**: End-to-end pipeline testing
3. **Performance Tests**: Load và stress testing
4. **Data Quality Tests**: Schema validation và data integrity

### Running Tests
```bash
# All tests
docker-compose exec pipeline pytest

# Specific categories
docker-compose exec pipeline pytest tests/unit/
docker-compose exec pipeline pytest tests/integration/

# Performance tests
docker-compose exec pipeline pytest tests/performance/ -v
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes và add tests
4. Run tests: `docker-compose exec pipeline pytest`
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Create Pull Request

### Development Guidelines
- Follow **PEP 8** style guide
- Write **comprehensive tests**
- Update **documentation**
- Add **type hints**
- Include **docstrings**

## 📄 Architecture Benefits

This structure follows modern data engineering best practices:

- ✅ **Microservices Architecture**: Modular, scalable components
- ✅ **Event-Driven Design**: Loosely coupled, reactive systems
- ✅ **Infrastructure as Code**: Reproducible deployments
- ✅ **Observability-First**: Comprehensive monitoring
- ✅ **Cloud-Native**: Container-ready, Kubernetes-native
- ✅ **DevOps Integration**: CI/CD pipeline ready
- ✅ **Data Quality**: Built-in validation và monitoring
- ✅ **Fault Tolerance**: Resilient error handling

## 🆘 Troubleshooting

### Common Issues

#### Services Not Starting
```bash
# Check Docker status
docker-compose ps

# View logs
docker-compose logs <service-name>

# Restart services
docker-compose restart
```

#### Data Not Flowing
```bash
# Check Kafka topics
docker-compose exec kafka kafka-topics --list --bootstrap-server localhost:9092

# Monitor pipeline
docker-compose exec pipeline python scripts/monitoring.py
```

### Support
- 📖 **Documentation**: [docs/](docs/)
- 🐛 **Issues**: GitHub Issues
- 💬 **Discussions**: GitHub Discussions

---

**Built with ❤️ using modern data engineering practices**
