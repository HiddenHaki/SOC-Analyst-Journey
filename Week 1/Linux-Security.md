# Day 1 - SOC Analyst Journey 🚀

Welcome to my SOC Analyst Journey documentation!

## 🔥 Tasks Completed on 4th March

### 1. Linux Security Basics
#### ✅ File Permissions in Linux
I learned the basics of Linux file permissions:
- **Read (r)**: View file contents
- **Write (w)**: Modify file contents
- **Execute (x)**: Run executable files

### Commands Learned:
| Command    | Description                  |
|-----------|-----------------------------|
| `ls -l`   | List files with permissions |
| `chmod`   | Change file permissions    |
| `chown`   | Change file ownership      |
| `useradd` | Add new users             |
| `passwd`  | Set user passwords        |
| `groups`  | View user groups         |

---
### 📌 Task 1: Create a New User
Command:
```bash
sudo useradd socuser
sudo passwd socuser
```
✅ User **socuser** created successfully!

---
### 📌 Task 2: Set File Permissions
Created a text file and assigned **read and write** permissions:
```bash
echo "Sensitive Data" > secret.txt
sudo chmod 660 secret.txt
ls -l secret.txt
```
Output:
```
-rw-rw---- 1 root socuser 14 Mar 4 10:00 secret.txt
```
✅ Permissions applied successfully!

---
### 2. Log Monitoring Script
I wrote a Python script to monitor **/var/log/auth.log** for suspicious activities.

Script Path: `logActivity.py`

Command to run the script:
```bash
sudo python3 logActivity.py
```
Example Output:
```
📄 Monitoring auth.log for suspicious activity...
⚠️ [ALERT] Suspicious Activity Detected: Failed password for invalid user
🚫 Stopping script...
```
✅ Log monitoring working perfectly!

---
### 📌 Screenshots
📸 Added screenshots in the `screenshots` folder.

---
### Conclusion
Today's tasks helped me understand:
- Linux user management
- File permissions
- Log monitoring with Python

👉 Follow my SOC Analyst Journey!

---
### GitHub Repository 📄
[My SOC Analyst Journey](https://github.com/HiddenHaki/SOC-Analyst-Journey)
