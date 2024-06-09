import json
import sys
from datetime import datetime as dt

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_data = self.parse_log_file()

    def parse_log_file(self):
        logs = []
        with open(self.log_file, 'r') as f:
            log_line = f.readline()
            while log_line:
                log = json.loads(log_line)
                for info in log.keys():
                    if info not in ('time', 'level', 'msg'):
                        log['msg'] += f' | {info}: {log[info]}'
                logs.append({
                    'timestamp': self.parse_timestamp(log['time']),
                    'level': log['level'],
                    'message': log['msg']
                })
                log_line = f.readline()
        return logs
    
    def filter_logs_by_timestamp(self, start, end):
        start = self.parse_timestamp(start)
        end = self.parse_timestamp(end)
        filtered_logs = [log for log in self.log_data if start <= log['timestamp'] <= end]
        return filtered_logs

    @staticmethod
    def parse_timestamp(timestamp_str):
        try:
            timestamp = dt.fromisoformat(timestamp_str)
            formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            return formatted_timestamp
        except ValueError:
            print(f"Invalid timestamp format: {timestamp_str}. Please use ISO format (YYYY-MM-DDTHH:MM:SS)")
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
        if filter_by.upper() in ['ERROR', 'WARNING', 'INFO']:
            filtered_logs = log_analyzer.filter_logs_by_level(filter_by.upper())
        else:
            filtered_logs = log_analyzer.filter_logs_by_message(filter_by.lower())
        print('Filtered Logs:')
        for log in filtered_logs:
            print(f'{log["timestamp"]} - {log["level"]}: {log["message"]}')

if __name__ == '__main__':
    main()