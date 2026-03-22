def analyze_logs(file):
    error_count = 0
    warning_count = 0

    with open(file, 'r') as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")


if __name__ == "__main__":
    analyze_logs("logs.txt")
