# 06. 调度与编排

> 如何让数千张 GPU 高效协同工作？调度系统是 AI Infra 的「大脑」。

---

## 为什么需要调度系统

- GPU 集群资源有限，多个训练/推理任务需要排队竞争
- 训练任务需要一次性拿到所有 GPU（gang scheduling），否则死锁
- 推理服务需要根据负载动态扩缩容
- 故障恢复：节点宕机后如何自动重调度

---

## Ray

> 分布式 Python 计算框架，vLLM / SGLang 的多节点推理调度基础。

- **GitHub**：https://github.com/ray-project/ray
- **文档**：https://docs.ray.io/
- **论文**：[Ray: A Distributed Framework for Emerging AI Applications](https://arxiv.org/abs/1712.05889)

### 核心概念

```python
import ray

@ray.remote
def my_task(x):
    return x * 2

# 异步执行，返回 ObjectRef
future = my_task.remote(42)
result = ray.get(future)  # 阻塞等待结果

# GPU 任务
@ray.remote(num_gpus=1)
class GPUWorker:
    def inference(self, input):
        ...
```

### Ray 在推理系统中的应用

- **vLLM 多节点推理**：多台机器的 Worker 通过 Ray Actor 管理
- **Ray Serve**：在线推理服务，支持 autoscaling
- **Ray Data**：数据预处理 pipeline

### 推荐资料

- [Ray 官方教程](https://docs.ray.io/en/latest/ray-overview/getting-started.html)
- [vLLM 多节点部署文档](https://docs.vllm.ai/en/latest/serving/distributed_serving.html)

---

## Kubernetes + GPU 调度

> 云原生容器编排，大规模 GPU 集群的标准基础设施。

- **文档**：https://kubernetes.io/docs/
- **GPU 支持**：需要 NVIDIA device plugin

### GPU 资源管理

```yaml
# Pod 申请 GPU 资源
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: trainer
    resources:
      limits:
        nvidia.com/gpu: 8  # 申请 8 张 GPU
```

### Volcano（批调度）

- **GitHub**：https://github.com/volcano-sh/volcano
- K8s 原生调度器不支持 gang scheduling（所有 Pod 同时启动）
- Volcano 专为 AI/HPC 工作负载设计：Gang Scheduling、队列管理、抢占

```yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: llm-train
spec:
  minAvailable: 16  # 必须同时拿到 16 个 Pod 才启动（gang scheduling）
  tasks:
  - replicas: 16
    template:
      spec:
        containers:
        - resources:
            limits:
              nvidia.com/gpu: 8
```

### 常用工具

| 工具 | 说明 |
|------|------|
| **NVIDIA device plugin** | K8s 识别和分配 GPU 资源 |
| **DCGM Exporter** | GPU 监控指标导出到 Prometheus |
| **MIG（Multi-Instance GPU）** | A100/H100 支持，将单张 GPU 切分成多个隔离实例 |
| **Time-slicing** | GPU 时分复用，多个 Pod 共享同一张 GPU |

---

## Slurm

> HPC（高性能计算）传统调度器，学术集群和超算中心的标配。

- **文档**：https://slurm.schedmd.com/
- 原生支持 MPI，gang scheduling，节点独占

### 基本使用

```bash
# 提交训练任务
sbatch --nodes=4 --ntasks-per-node=8 --gres=gpu:8 train.sh

# 查看队列
squeue -u $USER

# 取消任务
scancel <job_id>

# 交互式申请节点
srun --nodes=1 --gres=gpu:8 --pty bash
```

### Slurm + PyTorch 分布式

```bash
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:8

srun torchrun \
  --nnodes=$SLURM_NNODES \
  --nproc_per_node=8 \
  --rdzv_id=$SLURM_JOB_ID \
  --rdzv_backend=c10d \
  --rdzv_endpoint=$MASTER_ADDR:$MASTER_PORT \
  train.py
```

---

## 推理服务编排

### 在线推理服务栈

```
用户请求
  ↓
API Gateway / Load Balancer
  ↓
Ray Serve / Triton Inference Server / vLLM Server
  ↓
GPU Worker Pool
  ↓
模型实例（vLLM / SGLang）
```

### 自动扩缩容（Autoscaling）

- **Ray Serve**：基于请求队列深度自动增减 replica
- **K8s HPA + KEDA**：基于 GPU 利用率或自定义指标扩缩
- **关键指标**：GPU 显存利用率、请求排队时间、TTFT 分位数

---

## 可观测性

| 工具 | 用途 |
|------|------|
| **DCGM（Data Center GPU Manager）** | GPU 健康监控，温度/功耗/显存/ECC 错误 |
| **Prometheus + Grafana** | 指标采集与可视化 |
| **OpenTelemetry** | 分布式追踪，定位推理延迟来源 |
| **vLLM Metrics** | 暴露 Prometheus 格式指标（TTFT/TPOT/队列深度）|
| **Nsight Systems** | 单节点 GPU timeline 分析 |

---

## 故障恢复

大规模训练中节点故障是常态，需要：
- **Checkpoint**：定期保存模型状态，故障后从最近 ckpt 恢复
- **Elastic Training**：节点数变化时自动重新分配（Torch Elastic / Horovod Elastic）
- **快速 Checkpoint**：异步写到分布式存储，减少 checkpoint 时间占比

**推荐资料**：
- [MegaScale 论文](https://arxiv.org/abs/2402.15627) — 字节万卡训练，故障恢复章节
- [Gemini 训练基础设施](https://arxiv.org/abs/2312.11805) — Google 大规模训练实践

