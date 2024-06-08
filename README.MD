# Log Analyzer

The Log Analyzer is a Python script designed to parse and analyze log files. It provides functionalities to filter logs by timestamp, log level, or message, as well as generate summaries of the logs.

*Astana IT University: Final Project #6 task -> SRE tool!*

## How to Run

To run the Log Analyzer script, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git:

   ```
   git clone https://github.com/silvermete0r/logs_analyzer_script_py.git
   ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory:

   ```
   cd log-analyzer
   ```

3. **Install Dependencies**: If you haven't already installed the required dependencies, do so using pip:

   ```
   pip install -r requirements.txt
   ```

4. **Prepare Log File**: Place your log file (e.g., `test.log`) in the project directory. Ensure that the log file follows the expected format (`YYYY-MM-DD HH:MM:SS - LEVEL: MESSAGE`) for the script to parse it correctly.

5. **Run the Script**: Execute the script, passing the path to the log file as a command-line argument:

   ```
   python script.py test.log
   ```

   This command will display a summary of the logs contained in the `test.log` file.

6. **Additional Options**: You can also filter logs by timestamp, log level, or message content. Here are some examples:

   - Filter logs by timestamp range:

     ```
     python script.py test.log "2024-06-08 10:00:00" "2024-06-08 10:30:00"
     ```

   - Filter logs by log level:

     ```
     python script.py test.log ERROR
     ```

   - Filter logs by message content:

     ```
     python script.py test.log "Database connection failed"
     ```

   Replace `"test.log"` with the path to your log file and adjust filtering criteria as needed.

# Feel free to use!

Feel free to copy, use, and modify this project to suit your needs. You can also use it as a template to create your own log analysis tool or similar projects.
