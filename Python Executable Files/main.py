import os
import shutil
import psutil
import time
import sched
from datetime import datetime
from command_parser import parse_command

task_scheduler = sched.scheduler(time.time, time.sleep)

def schedule_job(delay_secs, fn, *args):
    task_scheduler.enter(delay_secs, 1, fn, args)
    print(f"⏱ Task scheduled to run in {delay_secs} sec(s).")

def check_scheduler():
    while task_scheduler.queue:
        task_scheduler.run(blocking=False)
        time.sleep(0.5)

def safe_path(pathname):
    if not pathname or not os.path.exists(pathname):
        print(f"⚠️ Couldn't find '{pathname}'... using current dir instead.")
        return "."
    return pathname

def suggest_big_old_files(folder="."):
    folder = safe_path(folder)
    flagged = []
    size_limit = 10*1024*1024
    cutoff_time = datetime.now().timestamp()-(30*24*3600)
    for fname in os.listdir(folder):
        fpath = os.path.join(folder,fname)
        if os.path.isfile(fpath):
            if os.path.getsize(fpath)>size_limit and os.path.getmtime(fpath)<cutoff_time:
                flagged.append(fname)
    return flagged

def find_duplicates(folder="."):
    folder = safe_path(folder)
    seen_sizes = {}
    dupes = []
    for fname in os.listdir(folder):
        fpath = os.path.join(folder,fname)
        if os.path.isfile(fpath):
            fsize = os.path.getsize(fpath)
            if fsize in seen_sizes: dupes.append(fname)
            else: seen_sizes[fsize]=fname
    return dupes
kill_process <PID>
def find_old_files(folder="."):
    folder = safe_path(folder)
    rare_files=[]
    cutoff=datetime.now().timestamp()-(60*24*3600)
    for fname in os.listdir(folder):
        path=os.path.join(folder,fname)
        if os.path.isfile(path) and os.path.getmtime(path)<cutoff:
            rare_files.append(fname)
    return rare_files

def suggest_for_archive(folder="."):
    folder = safe_path(folder)
    return list(set(suggest_big_old_files(folder)+find_old_files(folder)))

def run_command(intent,entities):
    folder=safe_path(entities.get("folder_name","."))
    filename=entities.get("filename")
    script_path=entities.get("script_path")
    delay=int(entities.get("delay",10))
    if intent=="create_file":
        with open(filename,"w") as f: f.write("")
        print(f"📝 Created file: {filename}")
    elif intent=="delete_file":
        if filename and os.path.exists(filename): os.remove(filename); print(f"🗑️ Deleted file: {filename}")
        else: print(f"⚠️ Couldn't find {filename}")
    elif intent=="create_folder": os.makedirs(folder,exist_ok=True); print(f"📁 Folder created: {folder}")
    elif intent=="delete_folder":
        if os.path.exists(folder): shutil.rmtree(folder); print(f"🗑️ Deleted folder: {folder}")
        else: print(f"⚠️ Folder {folder} not found")
    elif intent=="show_cpu_usage": print("💻 CPU usage:", psutil.cpu_percent(interval=1),"%")
    elif intent=="show_ram_usage": print("💾 RAM usage:", psutil.virtual_memory().percent,"%")
    elif intent=="show_disk_usage": print("🖴 Disk usage:", psutil.disk_usage('/').percent,"%")
    elif intent=="list_processes":
        print("🔍 Active processes:")
        for proc in psutil.process_iter(['pid','name']): print(f" - {proc.info['pid']}: {proc.info['name']}")
    elif intent=="kill_process":
        pid=entities.get("pid")
        if pid:
            try: psutil.Process(int(pid)).terminate(); print(f"✅ Killed process {pid}")
            except Exception as e: print(f"⚠️ Couldn't kill {pid}: {e}")
        else: print("⚠️ No PID provided.")
    elif intent=="schedule_backup":
        def backup(): dst=f"{folder}_backup_{int(time.time())}"; shutil.copytree(folder,dst,dirs_exist_ok=True); print(f"💾 Backup completed -> {dst}")
        schedule_job(delay,backup)
    elif intent=="run_script":
        if script_path and os.path.exists(script_path): os.system(f"python \"{script_path}\""); print(f"✅ Script {script_path} executed.")
        else: print(f"⚠️ Script {script_path} not found.")
    elif intent=="schedule_script":
        def run_scheduled(): 
            if script_path and os.path.exists(script_path): os.system(f"python \"{script_path}\""); print(f"✅ Scheduled script {script_path} ran.")
        schedule_job(delay,run_scheduled)
    elif intent=="delete_old_backups":
        for fname in os.listdir("."):
            if fname.startswith(folder) and "_backup_" in fname: shutil.rmtree(fname); print(f"🗑️ Deleted old backup {fname}")
    elif intent=="auto_organize":
        for fname in os.listdir(folder):
            src=os.path.join(folder,fname)
            if os.path.isfile(src):
                ext=fname.split('.')[-1] if '.' in fname else "misc"
                dst_dir=os.path.join(folder,ext)
                os.makedirs(dst_dir,exist_ok=True)
                shutil.move(src,os.path.join(dst_dir,fname))
        print("📂 Auto-organized files by extension.")
    elif intent=="reminder":
        message=entities.get("message","Reminder!")
        def notify(): print(f"⏰ Reminder: {message}")
        schedule_job(delay,notify)
    elif intent=="auto_delete_temp":
        temp_dir=folder
        for fname in os.listdir(temp_dir):
            try: os.remove(os.path.join(temp_dir,fname))
            except IsADirectoryError: pass
        print("🧹 Temp files cleared.")
    elif intent=="auto_compress": shutil.make_archive(f"{folder}_compressed",'zip',folder); print(f"📦 Compressed to {folder}_compressed.zip")
    elif intent=="suggest_archive":
        suggestion=suggest_for_archive(folder)
        print("🤖 Archive candidates:",suggestion if suggestion else "None")
    elif intent=="suggest_large_unused":
        biggies=suggest_big_old_files(folder)
        print("📌 Large unused files:",biggies if biggies else "None")
    elif intent=="cleanup_suggestions":
        clean_me=suggest_big_old_files(folder)+find_old_files(folder)
        print("🧹 Cleanup suggestions:",clean_me if clean_me else "Looks clean")
    elif intent=="optimize_folders": print("📂 Possible optimizations:", suggest_for_archive(folder))
    elif intent=="suggest_backup": print(f"💾 Suggestion: back up '{folder}' periodically.")
    elif intent=="suggest_duplicates": dupes=find_duplicates(folder); print("🔁 Duplicate files:",dupes if dupes else "None")
    elif intent=="suggest_restructure": print("📂 Restructure suggestion:", suggest_for_archive(folder))
    elif intent=="suggest_rare_files": oldies=find_old_files(folder); print("⏳ Rarely touched files:",oldies if oldies else "None")
    else: print(f"❌ Unknown intent: {intent}")

def main():
    print("=== 🤖 AI System Utility ==="); print("Type a command (or 'exit' to quit).")
    while True:
        try: cmd=input(">> ").strip()
        except KeyboardInterrupt: print("\n🛑 Bye bye!"); break
        if cmd.lower() in ("exit","quit"): print("👋 See you later!"); break
        intent,stuff=parse_command(cmd)
        if intent=="unknown": print("❌ Didn't get that, sorry."); continue
        run_command(intent,stuff)
        check_scheduler()

if __name__=="__main__": main()
