import time

def log(message, log_file):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)
