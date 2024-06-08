import re
import sys
from datetime import datetime as dt

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_data = self.parse_log_file()

    def parse_log_file(self):
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f:
                match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+): (.+)', line)
                if match:
                    logs.append({
                        'timestamp': dt.strptime(match.group(1), '%Y-%m-%d %H:%M:%S'),
                        'level': match.group(2),
                        'message': match.group(3)
                    })
        return logs
    
    def filter_logs_by_timestamp(self, start, end):
        start = self.parse_timestamp(start)
        end = self.parse_timestamp(end)
        filtered_logs = [log for log in self.log_data if start <= log['timestamp'] <= end]
        return filtered_logs

    @staticmethod
    def parse_timestamp(timestamp_str):
        try:
            return dt.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print(f"Invalid timestamp format: {timestamp_str}. Please use the format 'YYYY-MM-DD HH:MM:SS'")
            sys.exit(1)

    def filter_logs_by_level(self, level):
        filtered_logs = [log for log in self.log_data if log['level'] == level]
        return filtered_logs
    
    def filter_logs_by_message(self, message):
        filtered_logs = [log for log in self.log_data if message in log['message']]
        return filtered_logs

    def get_logs_summary(self):
        error_logs = self.filter_logs_by_level('ERROR')
        warning_logs = self.filter_logs_by_level('WARNING')
        info_logs = self.filter_logs_by_level('INFO')
        summary = {
            'total_logs': len(self.log_data),
            'error_logs': len(error_logs),
            'warning_logs': len(warning_logs),
            'info_logs': len(info_logs)
        }
        return summary

def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py <log_file> [start_time end_time | log_level | message]')
        sys.exit(1)
    
    log_file = sys.argv[1]
    log_analyzer = LogAnalyzer(log_file)

    if len(sys.argv) == 2:
        summary = log_analyzer.get_logs_summary()
        print('Logs Summary:')
        print(f'Total Logs: {summary["total_logs"]}')
        print(f'Error Logs: {summary["error_logs"]}')
        print(f'Warning Logs: {summary["warning_logs"]}')
        print(f'Info Logs: {summary["info_logs"]}')
    elif len(sys.argv) == 4:
        start = sys.argv[2]
        end = sys.argv[3]
        filtered_logs = log_analyzer.filter_logs_by_timestamp(start, end)
        print('Filtered Logs:')
        for log in filtered_logs:
            print(f'{log["timestamp"]} - {log["level"]}: {log["message"]}')
    elif len(sys.argv) == 3:
        filter_by = sys.argv[2]
        if filter_by in ['ERROR', 'WARNING', 'INFO']:
            filtered_logs = log_analyzer.filter_logs_by_level(filter_by)
        else:
            filtered_logs = log_analyzer.filter_logs_by_message(filter_by)
        print('Filtered Logs:')
        for log in filtered_logs:
            print(f'{log["timestamp"]} - {log["level"]}: {log["message"]}')

if __name__ == '__main__':
    main()