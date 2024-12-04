import re
from datetime import datetime


def parse_log_file(log_file_path="../logs/app.log", start_time="2024-12-03 21:40:00", end_time="2024-12-03 21:59:00"):
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    success_count = 0
    error_count = 0

    log_format_regex = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} - .* - (.*)$'

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.match(log_format_regex, line)

            if not match:
                continue

            log_time_str, log_message = match.groups()
            log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M:%S')

            if start_time <= log_time <= end_time:
                if "success on execute" in log_message.lower():
                    success_count += 1
                elif "error on execute" in log_message.lower():
                    error_count += 1

    return {
        "success_on_execute": success_count,
        "error_on_execute": error_count
    }


if __name__ == "__main__":
    try:
        results = parse_log_file()
        print(f"Success on execute: {results['success_on_execute']}")
        print(f"Error on execute: {results['error_on_execute']}")
    except Exception as e:
        print(f"An error occurred: {e}")
