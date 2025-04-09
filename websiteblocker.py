import time
from datetime import datetime

# Path to the hosts file (Windows & Linux/Mac)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows
# hosts_path = "/etc/hosts"  # Linux/Mac

redirect_ip = "127.0.0.1"  # Redirects the blocked websites
blocked_websites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

# Define blocking hours (e.g., 9 AM to 5 PM)
start_hour = 9
end_hour = 17

while True:
    current_hour = datetime.now().hour

    with open(hosts_path, "r+") as file:
        content = file.read()

        if start_hour <= current_hour < end_hour:
            print("Blocking websites...")
            for website in blocked_websites:
                if website not in content:
                    file.write(f"{redirect_ip} {website}\n")
        else:
            print("Unblocking websites...")
            lines = content.splitlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in blocked_websites):
                    file.write(line + "\n")
            file.truncate()

    time.sleep(60)  # Check every 60 seconds
