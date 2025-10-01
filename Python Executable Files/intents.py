from file_manager import *
from system_info import *
from scheduler import *
from ai_suggestions import *

# Map all 40 intents to functions
INTENT_FUNCTIONS = {
    # File & Folder
    "create_file": create_file,
    "delete_file": delete_file,
    "create_folder": create_folder,
    "delete_folder": delete_folder,
    "rename_file": rename_file,
    "rename_folder": rename_folder,
    "move_file": move_file,
    "move_folder": move_folder,
    "copy_file": copy_file,
    "copy_folder": copy_folder,
    "list_files": list_files,
    "search_files": search_files,
    "show_file_details": show_file_details,
    "count_files": count_files,

    # System Info
    "show_disk_usage": show_disk_usage,
    "show_free_space": show_free_space,
    "show_ram_usage": show_ram_usage,
    "show_cpu_usage": show_cpu_usage,
    "list_processes": list_processes,
    "kill_process": kill_process,
    "show_system_info": show_system_info,
    "check_folder_size": check_folder_size,
    "top_memory_processes": top_memory_processes,
    "top_cpu_processes": top_cpu_processes,

    # Scheduler
    "schedule_backup": schedule_backup,
    "run_script": run_script,
    "schedule_script": schedule_script,
    "delete_old_backups": delete_old_backups,
    "auto_organize": auto_organize,
    "reminder": reminder,
    "auto_delete_temp": auto_delete_temp,
    "auto_compress": auto_compress,

    # AI Suggestions
    "suggest_archive": suggest_archive,
    "suggest_large_unused": suggest_large_unused,
    "cleanup_suggestions": cleanup_suggestions,
    "optimize_folders": optimize_folders,
    "suggest_backup": suggest_backup,
    "suggest_duplicates": suggest_duplicates,
    "suggest_restructure": suggest_restructure,
    "suggest_rare_files": suggest_rare_files
}
