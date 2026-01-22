log_file = "logs/app.log"
keywords = ["ERROR", "FAIL", "CRITICAL"]

found_issue = False  # cờ đánh dấu có lỗi hay không

try:
    with open(log_file, "r") as f:
        for line in f:
            for k in keywords:
                if k in line:
                    print("Found issue:", line.strip())
                    found_issue = True

    if found_issue:
        print("Log check FAILED")
        exit(1)
    else:
        print("Log check PASSED")
        exit(0)

except FileNotFoundError:
    print("Log file not found:", log_file)
    exit(2)
