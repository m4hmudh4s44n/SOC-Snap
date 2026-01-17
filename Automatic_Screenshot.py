import time
import os
import zipfile
import smtplib
import shutil  # Added for folder deletion 🧹
from mss import mss
from datetime import datetime
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "receiver_email@gmail.com"
APP_PASSWORD = "xxxx xxxx xxxx xxxx" 
SAVE_DIR = r"D:\Programming Languages\PYTHON\Cyber\SS"

def create_report_zip(zip_name, source_folder):
    """Compresses all images into a single ZIP file."""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder, subfolders, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.png'):
                    zf.write(os.path.join(folder, file), file)

def send_email(zip_path):
    """Sends the ZIP file via Gmail SMTP."""
    msg = EmailMessage()
    msg['Subject'] = f"SOC Alert: Screenshot Report {datetime.now().strftime('%H:%M:%S')}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content("Automated SOC Mission Complete. Attached: ZIP containing batch screenshots.")

    with open(zip_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='zip',
            filename=os.path.basename(zip_path)
        )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

def run_mission():
    # 1. User Input
    try:
        total_time = int(input("Enter total monitoring time (seconds): "))
        interval = int(input("Enter interval between shots (seconds): "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    if interval > total_time:
        print("Error: Interval cannot be longer than total time.")
        return

    num_shots = total_time // interval
    os.makedirs(SAVE_DIR, exist_ok=True)

    print(f"\n🚀 Mission Started: {num_shots} shots every {interval}s.")
    
    # 2. Capture Loop
    with mss() as sct:
        for i in range(1, num_shots + 1):
            timestamp = datetime.now().strftime("%H-%M-%S")
            filename = os.path.join(SAVE_DIR, f"capture_{i}_{timestamp}.png")
            sct.shot(output=filename)
            print(f" [📷] Shot {i}/{num_shots} saved.")
            
            if i < num_shots:
                time.sleep(interval)

    # 3. Finalize: Zip, Mail, and Cleanup
    zip_name = f"SOC_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    print(f"\n📦 Creating ZIP: {zip_name}")
    create_report_zip(zip_name, SAVE_DIR)
    
    print("📧 Dispatching to SOC HQ...")
    try:
        send_email(zip_name)
        print("✅ Success: Email sent.")
        
        # Cleanup: Delete the local images and the ZIP file 🧹
        print("🧹 Cleaning up local evidence...")
        shutil.rmtree(SAVE_DIR)  # Deletes the screenshot folder
        os.remove(zip_name)      # Deletes the temporary ZIP file
        print("✨ Local drive is clean.")
        
    except Exception as e:
        print(f"❌ Email Failed: {e}")
        print("⚠️ Cleanup aborted to preserve data.")

if __name__ == "__main__":
    run_mission()