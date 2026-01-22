import os
import sys

log_file = "logs/app.log"
keywords = ["ERROR", "FAIL", "CRITICAL"]

alert_key = os.getenv("ALERT_KEY")

if not alert_key:
    print("Missing ALERT_KEY")
    sys.exit(2)

found = False

with open(log_file, "r") as f:
    for line in f:
        for k in keywords:
            if k in line:
                print("Found issue:", line.strip())
                found = True

if found:
    print("Using secret to alert (simulated):", alert_key[:4] + "***")
    sys.exit(1)

print("No critical issues found")
sys.exit(0)
