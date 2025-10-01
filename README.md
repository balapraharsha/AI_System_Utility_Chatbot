# 📊 AI System Utility – Smart Command-Line Assistant

This interactive AI-powered CLI tool simplifies file management, system monitoring, and task scheduling. It provides AI suggestions and humanized feedback to optimize productivity and system performance.

---

## 📁 Module Overview

The project includes modules for:

| Module              | Description                                |
|---------------------|--------------------------------------------|
| `file_manager.py`   | Create, move, delete, and organize files   |
| `system_monitor.py` | Track CPU, memory, and storage usage       |
| `scheduler.py`      | Schedule tasks and receive notifications   |
| `command_parser.py` | Parses natural language commands           |
| `main.py`           | Entry point to run the AI assistant        |

---

## 📌 Key Features

- ✅ File management: create, move, delete folders/files effortlessly  
- ✅ System monitoring: CPU, RAM, storage usage stats  
- ✅ Task scheduling: delayed execution with notifications  
- ✅ AI-powered assistance: understands natural language commands  
- ✅ Human-like feedback: informative and friendly messages  

---

## 📊 Functionalities Included

- 📁 **File operations**: create, rename, delete, move  
- ⚡ **System stats**: real-time CPU, memory, disk usage  
- ⏱️ **Task scheduler**: delayed execution with notifications  
- 🧠 **AI assistance**: command suggestions and guidance  

---

## 📈 Insights Summary

- Organizes your workflow efficiently  
- Reduces manual system management tasks  
- Provides actionable feedback and reminders  
- Suitable for developers, data scientists, and productivity enthusiasts  

---

## 🛠️ Tools & Technologies Used

- **Python 3.x**  
- `psutil` for system monitoring  
- `sched` for task scheduling  
- Command-line interface  

---

# 1. Clone the repository
git clone https://github.com/balapraharsha/AI_System_Utility_Chatbot.git

# 2. Navigate to the project folder
cd AI_System_Utility_Chatbot

# 3. Install required Python dependencies
pip install -r requirement.txt

# 4. Run the chatbot
python main.py

---

## 📂 Repository Structure

```bash
📁 AI_System_Utility_Chatbot/
├── 📁 Python Executable Files/
│   ├──  📄 config.py                  # Configuration settings for the chatbot
│   ├──  📄 intents.py                 # Predefined intents for AI suggestions or commands
│   ├──  📄 utils.py                   # Helper functions used across modules
│   ├──  📄 ai_suggestions.py          # AI-based suggestions and responses
│   ├──  📄 command_parser.py          # Parses user commands and routes them to modules
│   ├──  📄 file_manager.py            # Handles file system operations (create, move, delete)
│   ├──  📄 system_info.py             # Retrieves system information (CPU, RAM, storage)
│   ├──  📄 scheduler.py               # Task scheduling and timer functions
│   └── 📄 main.py                    # Entry point integrating all modules
├── 📄 AI System Utility Chatbot Documentation.pdf
├── 📄 README.md
└── 📄 requirement.txt
```

---
## 🤖 AI System Utility Chatbot – Commands



| Description                                  | Example Command                                 | Status      | Output / Action                                                                 |
|----------------------------------------------|-------------------------------------------------|------------|-------------------------------------------------------------------------------|
| **Create a new file**                        | `create_file report.txt`                        | Functional | 📝 Created file: report.txt                                                   |
| **Delete a file**                            | `delete_file report.txt`                        | Functional | 🗑️ Deleted file: report.txt or ⚠️ Couldn't find report.txt                    |
| **Create a folder**                          | `create_folder MyFolder`                        | Functional | 📁 Folder created: MyFolder                                                   |
| **Delete a folder**                          | `delete_folder MyFolder`                        | Functional | 🗑️ Deleted folder: MyFolder or ⚠️ Folder MyFolder not found                   |
| Rename a file                                | `rename_file old.txt new.txt`                   | Skeleton   | Placeholder – function exists but not implemented                             |
| Rename a folder                              | `rename_folder OldFolder NewFolder`             | Skeleton   | Placeholder                                                                   |
| Move a file                                  | `move_file file.txt DestFolder`                 | Skeleton   | Placeholder                                                                   |
| Move a folder                                | `move_folder SrcFolder DestFolder`              | Skeleton   | Placeholder                                                                   |
| Copy a file                                  | `copy_file file.txt DestFolder`                 | Skeleton   | Placeholder                                                                   |
| Copy a folder                                | `copy_folder SrcFolder DestFolder`              | Skeleton   | Placeholder                                                                   |
| List files in a folder                        | `list_files MyFolder`                           | Skeleton   | Placeholder                                                                   |
| Search files by extension                     | `search_files txt MyFolder`                     | Skeleton   | Placeholder                                                                   |
| Show file details                             | `show_file_details report.txt`                  | Skeleton   | Placeholder                                                                   |
| Count files in a folder                        | `count_files MyFolder`                          | Skeleton   | Placeholder                                                                   |
| Show disk usage                               | `show_disk_usage`                               | Functional | 🖴 Disk usage: 45% (example)                                                  |
| Show free space                               | `show_free_space`                               | Skeleton   | Placeholder                                                                   |
| Show RAM usage                                | `show_ram_usage`                                | Functional | 💾 RAM usage: 65% (example)                                                   |
| Show CPU usage                                | `show_cpu_usage`                                | Functional | 💻 CPU usage: 23% (example)                                                   |
| List running processes                         | `list_processes`                                | Functional | 🔍 Active processes: PID: Name                                                |
| Kill a process                                | `kill_process 1234`                              | Functional | ✅ Killed process 1234 or ⚠️ Couldn't kill 1234                                |
| Show system info                              | `show_system_info`                               | Skeleton   | Placeholder                                                                   |
| Check folder size                              | `check_folder_size MyFolder`                     | Skeleton   | Placeholder                                                                   |
| Top memory-consuming processes                | `top_memory_processes`                           | Skeleton   | Placeholder                                                                   |
| Top CPU-consuming processes                   | `top_cpu_processes`                              | Skeleton   | Placeholder                                                                   |
| Schedule a folder backup                       | `schedule_backup MyFolder 30`                   | Functional | ⏱ Task scheduled. Backup completed -> MyFolder_backup_...                     |
| Run a Python script immediately               | `run_script my_script.py`                        | Functional | ✅ Script my_script.py executed                                                |
| Schedule a Python script                       | `schedule_script my_script.py 60`               | Functional | ⏱ Task scheduled. Script executed at scheduled time                           |
| Delete old backups                             | `delete_old_backups MyFolder`                   | Functional | 🗑️ Deleted old backup MyFolder_backup_...                                     |
| Auto-organize files by extension              | `auto_organize MyFolder`                        | Functional | 📂 Auto-organized files by extension                                          |
| Set a reminder                                 | `reminder "Check emails" 15`                    | Functional | ⏱ Task scheduled. Reminder: Check emails                                      |
| Auto-delete temp files                         | `auto_delete_temp Downloads`                     | Functional | 🧹 Temp files cleared                                                          |
| Auto-compress folder                            | `auto_compress MyFolder`                         | Functional | 📦 Compressed to MyFolder_compressed.zip                                      |
| Suggest files for archiving                     | `suggest_archive MyFolder`                       | Functional | 🤖 Archive candidates: [...]                                                  |
| Suggest large & old unused files               | `suggest_large_unused MyFolder`                  | Functional | 📌 Large unused files: [...]                                                  |
| Cleanup suggestions                             | `cleanup_suggestions MyFolder`                   | Functional | 🧹 Cleanup suggestions: [...]                                                |
| Optimize folders                                 | `optimize_folders MyFolder`                       | Functional | 📂 Possible optimizations: [...]                                              |
| Suggest backups                                  | `suggest_backup MyFolder`                         | Functional | 💾 Suggestion: back up 'MyFolder' periodically                                |
| Suggest duplicate files                          | `suggest_duplicates MyFolder`                      | Functional | 🔁 Duplicate files: [...]                                                    |
| Suggest folder restructure                       | `suggest_restructure MyFolder`                     | Functional | 📂 Restructure suggestion: [...]                                              |
| Suggest rarely touched files                     | `suggest_rare_files MyFolder`                      | Functional | ⏳ Rarely touched files: [...]                                                |


---

## 🚀 Future Enhancements

- 🔹 Complete all **skeleton commands** to make them fully functional.
  - Rename, move, copy files & folders
  - List files, search, show details, count files
  - System info commands (free space, top memory/CPU processes)
- 🔹 Add **GUI interface** for easier access to all commands.

---

## 👨‍💻 Developed By

**Bala Praharsha .M**  
📧 [balapraharsha.m@gmail.com]  
🔗 [LinkedIn](https://linkedin.com/in/mannepalli-bala-praharsha) | [GitHub](https://github.com/balapraharsha)  

---

## ⭐ If you like this project, give it a ⭐ and feel free to fork or contribute!
