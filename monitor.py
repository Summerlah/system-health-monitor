import psutil
import time
import json
from datetime import datetime

with open("config.json") as f:
    config = json.load(f)

CPU_THRESHOLD = config["cpu_threshold"]
MEM_THRESHOLD = config["memory_threshold"]
DISK_THRESHOLD = config["disk_threshold"]
INTERVAL = config["interval_seconds"]

def log(message):
    with open("system_health.log", "a") as file:
        file.write(message + "\n")

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = f"[{timestamp}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    log(status)

    if cpu > CPU_THRESHOLD:
        log("⚠️ High CPU usage detected")
    if memory > MEM_THRESHOLD:
        log("⚠️ High Memory usage detected")
    if disk > DISK_THRESHOLD:
        log("⚠️ High Disk usage detected")

while True:
    check_system()
    time.sleep(INTERVAL)
