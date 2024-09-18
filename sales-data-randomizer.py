import csv
import random
import shutil
import time
import os
import logging
from datetime import datetime

# Configuration
CSV_FILE_PATH = 'sales_data.csv'
BACKUP_DIR = 'backup'
INTERVAL = 10  # seconds for demonstration purposes

# Setup logging
logging.basicConfig(filename='shuffle_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def backup_file(file_path, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_path = os.path.join(backup_dir, f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{os.path.basename(file_path)}")
    shutil.copy(file_path, backup_path)
    logging.info(f"Backup created: {backup_path}")

def shuffle_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        header, rows = reader[0], reader[1:]
        random.shuffle(rows)
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)
    logging.info(f"File shuffled: {file_path}")

def main():
    while True:
        try:
            backup_file(CSV_FILE_PATH, BACKUP_DIR)
            shuffle_csv(CSV_FILE_PATH)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
