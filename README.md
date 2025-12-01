# Password Stuff
CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'C@rlsberg9075';

---

# ✅ **README.md — Windows & Mac Development Environment Guide**

````markdown
# Crumble Development Environment Guide

This guide explains how to run Ubuntu on Windows (via WSL2), manage WSL, and run Docker for both Windows and macOS.  
These instructions ensure you can develop Crumble consistently across both platforms.

---

## 🚀 Requirements

### Windows (WSL2 workflow)

- Windows 10 or 11
- WSL2 installed
- Ubuntu (20.04 or 22.04) installed from Microsoft Store
- Docker Desktop **or** Docker installed directly inside Ubuntu

### macOS

- macOS Ventura or newer
- Homebrew
- Docker Desktop for Mac

---

## 🧭 How to Launch Ubuntu on Windows (WSL2)

You can start Ubuntu in three different ways:

### **1. Start Menu**

1. Press **Windows key**
2. Type **Ubuntu**
3. Click the Ubuntu app (e.g., "Ubuntu", "Ubuntu 22.04")

---

### **2. Windows Terminal / PowerShell**

Run:

```powershell
wsl
```
````

Or launch a specific distribution:

```powershell
wsl -d Ubuntu
```

---

### **3. Windows Terminal Tab Menu**

If Windows Terminal is installed:

- Open **Windows Terminal**
- Click the ▼ next to the tab
- Select **Ubuntu**

---

## 🛑 How to Close Ubuntu / Restart WSL

### **Close Ubuntu session**

Inside Ubuntu:

```bash
exit
```

### **Restart all WSL instances (recommended before running Docker)**

Run from PowerShell _outside Ubuntu_:

```powershell
wsl --shutdown
```

This stops all running Linux distros and resets the WSL2 VM.

---

## 🐳 Running Docker on Windows

You have two supported setups:

---

### 💡 **Option 1 — Use Docker Desktop (Recommended)**

1. Install Docker Desktop
   [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

2. Under _Settings → General_, ensure:

   - ☑ Use the WSL 2 based engine

3. Under _Settings → Resources → WSL Integration_, ensure:

   - ☑ Enable integration with Ubuntu

4. Start Docker Desktop

5. Test Docker in Ubuntu:

```bash
docker run hello-world
```

---

### 💡 **Option 2 — Install Docker Inside Ubuntu (WSL-native)**

_(Only works if Ubuntu is running under WSL2)_

Inside Ubuntu:

```bash
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER
```

Restart WSL:

```powershell
wsl --shutdown
```

Test:

```bash
docker run hello-world
```

---

## 🐘 Running PostgreSQL in Docker

From Ubuntu or PowerShell:

```bash
docker run --name crumble-postgres \
  -e POSTGRES_USER=crumble_user \
  -e POSTGRES_PASSWORD=supersecurepassword \
  -e POSTGRES_DB=crumble_db \
  -p 5432:5432 \
  -d postgres:16
```

Start the DB:

```bash
docker start crumble-postgres
```

Stop it:

```bash
docker stop crumble-postgres
```

---

# 🍎 macOS Instructions

### Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Docker Desktop (Required)

Download:
[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

After installation:

- Open Docker Desktop
- Allow required permissions

### Run Postgres (same command as Windows)

```bash
docker run --name crumble-postgres \
  -e POSTGRES_USER=crumble_user \
  -e POSTGRES_PASSWORD=supersecurepassword \
  -e POSTGRES_DB=crumble_db \
  -p 5432:5432 \
  -d postgres:16
```

### Check Docker status on macOS

```bash
docker info
docker ps
```

### No WSL required on Mac

You run everything directly inside macOS Terminal.

---

# 🔁 Cross-Platform Tips for Crumble Development

### Database

- Use **Docker Postgres** for both Mac + Windows to keep the environment identical.
- Same username/password across systems.
- If switching machines, export/import DB:

```bash
docker exec -t crumble-postgres pg_dump -U crumble_user crumble_db > dump.sql
```

To restore:

```bash
docker exec -i crumble-postgres psql -U crumble_user crumble_db < dump.sql
```

---

### Python / Django

Use **venv** on both systems:

```bash
python3 -m venv crumble_env
source crumble_env/bin/activate   # macOS or Ubuntu
crumble_env\Scripts\activate      # Windows PowerShell
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run Django:

```bash
python manage.py runserver
```

---

## 🧹 Helpful WSL Commands

### List distros

```powershell
wsl -l -v
```

### Set Ubuntu as default

```powershell
wsl --set-default Ubuntu
```

### Terminate a single distro

```powershell
wsl --terminate Ubuntu
```

---

# 🎉 Done

You now have a full cross-platform setup for:

- Ubuntu on Windows
- Docker on Windows (WSL2)
- Docker on macOS
- PostgreSQL container
- Restarting and managing WSL
