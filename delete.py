import os
import hashlib

IMAGE_EXTS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

def file_hash(filepath):
    """Return SHA256 hash of the file."""
    hash_obj = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def is_image_file(filename):
    return filename.lower().endswith(IMAGE_EXTS)

def remove_duplicate_images(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: โฟลเดอร์ {folder_path} ไม่มีอยู่จริง")
        return

    hashes = {}
    removed_count = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if not is_image_file(filename):
                continue
            file_path = os.path.join(root, filename)
            try:
                file_digest = file_hash(file_path)
                if file_digest in hashes:
                    print(f"Removing duplicate image: {file_path}")
                    os.remove(file_path)
                    removed_count += 1
                else:
                    hashes[file_digest] = file_path
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    print(f"Total removed images: {removed_count}")

if __name__ == "__main__":
    folder = r"c:\Users\PAYA\OneDrive\Desktop\learn python"  # เปลี่ยน path ตามต้องการ
    remove_duplicate_images(folder)