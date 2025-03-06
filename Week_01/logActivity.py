import subprocess

# Path to auth.log file
log_file = '/var/log/auth.log'

# List of suspicious keywords
suspicious_keywords = [
    'Failed password',
    'Invalid user',
    'session opened for user root',
    'Accepted password',
    'sudo:',
    'su:',
    'rhost='
]

def monitor_log():
    print("📄 Monitoring auth.log for suspicious activity...")
    try:
        # Use subprocess to run tail -f command
        process = subprocess.Popen(['tail', '-f', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            line = process.stdout.readline().decode('utf-8')
            if line:
                for keyword in suspicious_keywords:
                    if keyword in line:
                        print(f"⚠️ [ALERT] Suspicious Activity Detected: {line.strip()}")
                        print("🚫 Stopping script...")
                        process.terminate()
                        return  # Stop the script
            else:
                pass
    except FileNotFoundError:
        print(f"❌ File not found: {log_file}\nMake sure logging is enabled and the file exists.")
    except PermissionError:
        print("🔑 Permission denied: Try running the script with sudo.")
    except KeyboardInterrupt:
        print("🛑 Script stopped by user.")

if __name__ == '__main__':
    print("🔍 Starting log monitoring script...")
    monitor_log()
