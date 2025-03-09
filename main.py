import time
import random
from concurrent.futures import ThreadPoolExecutor

def download_file(file_id):
    download_time = random.randint(2, 5)  # สุ่มเวลาที่ใช้ดาวน์โหลด
    print(f"Starting download: File-{file_id} (ETA: {download_time}s)")
    time.sleep(download_time)
    print(f"Finished downloading: File-{file_id}")
    return f"File-{file_id} downloaded in {download_time}s"

def main():
    file_ids = range(1, 6)  # จำลองไฟล์ 5 ไฟล์

    with ThreadPoolExecutor(max_workers=3) as executor:  # ใช้ 3 เธรด
        results = executor.map(download_file, file_ids)

    print("\nAll downloads complete:")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
