import os
import shutil

# โฟลเดอร์ที่ต้องการจัดไฟล์
SOURCE_FOLDER = "./test_downloads"
# ตรวจสอบว่าโฟลเดอร์มีอยู่จริงก่อนดำเนินการ
if not os.path.isdir(SOURCE_FOLDER ):
    # ถ้าโฟลเดอร์ไม่มีอยู่จริง ให้แสดงข้อความแจ้งเตือน
    print(f'Error: ไฟล์เดอร์ {SOURCE_FOLDER} ไม่มีอยู่จริง')
# กำหนดนามสกุลไฟล์และโฟลเดอร์เป้าหมาย
EXTENSION_MAP = {
    "Word": [".doc", ".docx"],
    "PowerPoint": [".ppt", ".pptx"],
    "Excel": [".xls", ".xlsx"],
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Others": []  # สำหรับไฟล์อื่น ๆ
}

def get_target_folder(filename):
    """Return the target folder based on the file extension."""
    # แยกนามสกุลไฟล์ออกจากชื่อไฟล์
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions: # ถ้านามสกุลไฟล์ตรงกับนามสกุลที่กำหนด
            return folder # ถ้าไฟล์ตรงกับนามสกุลที่กำหนด จะย้ายไปโฟลเดอร์ที่ตรงกับนามสกุลนั้น
    return "Others" # ถ้าไม่ตรงกับนามสกุลใด ๆ จะย้ายไปโฟลเดอร์ "Others"

def organize_files(): # ฟังก์ชันหลักสำหรับจัดระเบียบไฟล์
    for filename in os.walk(SOURCE_FOLDER): 
        filepath = os.path.join(SOURCE_FOLDER, filename) 

        if os.path.isfile(filepath):
            folder_name = get_target_folder(filename) # เรียกใช้ฟังก์ชันเพื่อหาชื่อโฟลเดอร์เป้าหมายตามนามสกุลไฟล์
            target_folder = os.path.join(SOURCE_FOLDER, folder_name) # สร้างเส้นทางสำหรับโฟลเดอร์เป้าหมาย
            os.makedirs(target_folder, exist_ok=True) # สร้างโฟลเดอร์เป้าหมายถ้ายังไม่มี
            # ย้ายไฟล์ไปยังโฟลเดอร์เป้าหมาย
            try:
                shutil.move(filepath, os.path.join(target_folder, filename)) 
                print(f"Moved: {filename} → {folder_name}/") # แสดงข้อความเมื่อย้ายไฟล์สำเร็จ
            except Exception as e:
                print(f"Error moving {filename}: {e}") # แสดงข้อความเมื่อเกิดข้อผิดพลาดในการย้ายไฟล์


if __name__ == "__main__":
    organize_files()