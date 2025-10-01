import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Pick a stable Gemini model
MODEL_NAME = "models/gemini-2.5-flash"

# List of all intents (40 commands)
INTENTS = [
    # File & Folder
    "create_file", "delete_file", "create_folder", "delete_folder",
    "rename_file", "rename_folder", "move_file", "move_folder",
    "copy_file", "copy_folder", "list_files", "search_files",
    "show_file_details", "count_files",

    # System Info
    "show_disk_usage", "show_free_space", "show_ram_usage", "show_cpu_usage",
    "list_processes", "kill_process", "show_system_info", "check_folder_size",
    "top_memory_processes", "top_cpu_processes",

    # Scheduler
    "schedule_backup", "run_script", "schedule_script", "delete_old_backups",
    "auto_organize", "reminder", "auto_delete_temp", "auto_compress",

    # AI Suggestions
    "suggest_archive", "suggest_large_unused", "cleanup_suggestions",
    "optimize_folders", "suggest_backup", "suggest_duplicates",
    "suggest_restructure", "suggest_rare_files"
]

def parse_command(user_input: str):
    """
    Uses Google Gemini to parse natural language input into:
    intent -> string (one of INTENTS)
    entities -> dictionary of parameters
    Always returns (intent, entities)
    """
    prompt = f"""
You are an AI assistant that parses system utility commands.
Map user input into one of these intents: {INTENTS}.
Extract all relevant entities (file_name, folder_name, script_path, time, etc.)
Return ONLY a Python dictionary in this format:

{{'action': 'intent_name', 'filename': 'example.txt', ...}}

Example:
Input: "Delete file report.txt"
Output: {{'action': 'delete_file', 'filename': 'report.txt'}}

Now parse this input:
"{user_input}"
"""

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Convert string to dictionary
        data = eval(text)

        intent = data.get("action", "unknown")
        return intent, data

    except Exception as e:
        print(f"Gemini parsing error: {e}")
        return "unknown", {}
