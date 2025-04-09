import time
from datetime import datetime

# Path to the hosts file (Windows)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"
blocked_websites = ["www.facebook.com", "facebook.com"]

# Define blocking hours (e.g., 9 PM to 5 AM)
start_hour = 21
end_hour = 5

while True:
    current_hour = datetime.now().hour

    # Determine if current time is within the blocking period
    if start_hour <= end_hour:
        is_block_time = start_hour <= current_hour < end_hour
    else:
        is_block_time = current_hour >= start_hour or current_hour < end_hour

    with open(hosts_path, "r+") as file:
        content = file.read()
        file.seek(0)

        if is_block_time:
            print("Blocking websites...")
            for website in blocked_websites:
                if website not in content:
                    file.write(f"{redirect_ip} {website}\n")
        else:
            print("Unblocking websites...")
            lines = content.splitlines()
            for line in lines:
                if not any(website in line for website in blocked_websites):
                    file.write(line + "\n")
            file.truncate()

    time.sleep(60)  # Check every 60 seconds

