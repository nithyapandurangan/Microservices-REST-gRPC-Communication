
# Microservices REST API & gRPC Comparison

## Objective
The goal of this project is to build three microservices using **FastAPI**, implement communication between them using **REST API** and **gRPC (bidirectional streaming)**, and compare the **CPU utilization** and **throughput** of both communication methods.

## Prerequisites
1. Python 3.x
2. Virtual environment setup
3. Install required libraries

```bash
pip install fastapi uvicorn grpcio grpcio-tools apachebench ghz
```

## Microservice Roles
1. **Service 1 (Producer):** Generates data or processes incoming requests.
2. **Service 2 (Processor):** Processes data received from Service 1.
3. **Service 3 (Aggregator):** Aggregates processed data and sends responses.

## Microservices Implementation using FastAPI

### Service 1: Producer
- **File:** `service1.py`
- **Run:**
  ```bash
  uvicorn service1:app --host 127.0.0.1 --port 8000 --reload
  ```

### Service 2: Processor
- **File:** `service2.py`
- **Run:**
  ```bash
  uvicorn service2:app --host 127.0.0.1 --port 8001 --reload
  ```

### Service 3: Aggregator
- **File:** `service3.py`
- **Run:**
  ```bash
  uvicorn service3:app --host 127.0.0.1 --port 8002 --reload
  ```

## Testing REST API Communication
Test REST API communication using `curl` 
```bash
 curl http://127.0.0.1:8002/aggregate 
  ```

## Microservices Implementation using gRPC
### Define gRPC Protocol:
- **File:** `services.proto`

### Service 1: gRPC Producer
- **File:** `grpc_service1.py`
- **Run:**
  ```bash
  python grpc_service1.py
  ```

### Service 2: gRPC Processor
- **File:** `grpc_service2.py`
- **Run:**
  ```bash
  python grpc_service2.py
  ```

### Service 3: gRPC Aggregator
- **File:** `grpc_service3.py`
- **Run:**
  ```bash
  python grpc_service3.py
  ```
  
## Testing gRPC Communication
Test REST API communication using `grpcurl` 
```bash
 grpcurl -plaintext -d '{}' localhost:50051 ProducerService.Generate
  ```

## Performance Measurement

### 1. REST API Performance (Using ApacheBench)
Run the following command to test REST API performance:
```bash
ab -n 1000 -c 50 http://127.0.0.1:8002/aggregate
```

### 2. gRPC Performance (Using ghz)
Run the following command to test gRPC performance:
```bash
ghz --insecure --proto services.proto --call AggregatorService.Aggregate -n 1000 -c 50 localhost:50053
```

### Key Observations:
- **gRPC Performance:** Outperforms REST API with higher requests per second (7327 vs 930) and lower average response times (6.46 ms vs 53.748 ms).
- **REST API Performance:** Shows higher latency and lower throughput but handles a reasonable number of requests at around 930 requests per second.
- **gRPC Latency:** Low latency with 90% of requests completed within 6.55 ms.

## CPU Utilization Measurement (Using htop)

### 1. REST API
- **Command:** `ab -n 1000 -c 50 http://127.0.0.1:8002/aggregate`
- **CPU%:** 57.9%
- **Memory:** 0.3%
- **Time Taken:** 19 seconds

### 2. gRPC
- **Command:** `ghz --insecure --proto services.proto --call AggregatorService.Aggregate -n 1000 -c 50 localhost:50053`
- **CPU%:** 14.4%
- **Memory:** 0.2%
- **Time Taken:** 8 seconds

### Summary of Observations:
- **Higher CPU% for REST API:** The higher CPU usage for REST API is due to the overhead of processing HTTP requests, especially under high concurrency.
- **Lower CPU% for gRPC:** gRPC uses a more efficient binary format (Protobuf) and HTTP/2, which leads to reduced CPU usage while handling requests concurrently.
- **Faster Processing with gRPC:** gRPC processes requests faster due to its more efficient handling of requests (8 seconds for gRPC vs 19 seconds for REST API).

