# Issue #4: Setup - Temporal Activity Function & Development Environment

## Overview
Setup and configuration for Temporal workflow activities with Python async functions.

---

## 1. Environment Setup

### Virtual Environment
Create a Python virtual environment:
```bash
python3 -m venv env
```

Activate the environment:
```bash
# On macOS/Linux
source env/bin/activate

# On Windows
env\Scripts\activate
```

Install dependencies:
```bash
pip install temporalio
```

---

## 2. Server Configuration

- **Temporal Server Address:** `project33junipermercury.tavdy.tmprl.cloud:7233`
- **Runtime Method:** `asyncio.run`

---

## 3. Code Example - Temporal Activity

Basic async activity function:
```python
from temporalio import activity

@activity.defn
async def greet(name: str) -> str:
    return f"Hello {name}"
```

---

## Tasks / Next Steps

- [ ] Set up Python virtual environment
- [ ] Install Temporal SDK and dependencies
- [ ] Configure Temporal server connection
- [ ] Implement and test activity functions
- [ ] Create workflow orchestration
- [ ] Add error handling and retry logic
- [ ] Write unit tests

---

## References

- [Temporal Python SDK Documentation](https://python.temporal.io/)
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html)
