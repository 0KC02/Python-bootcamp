import os
import threading
from PIL import Image

# Constants for resizing
MAX_WIDTH = 800
MAX_HEIGHT = 800
SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg')

def resize_image(image_path):
    """
    Resizes a single image to a maximum size while maintaining aspect ratio.
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Get the original size
            original_size = img.size
            # Calculate the resizing factor
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
            # Save the resized image (overwriting the original)
            img.save(image_path)
            print(f"Resized {image_path}: {original_size} -> {img.size}")
    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

def process_directory(directory_path):
    """
    Processes all supported image files in the specified directory using multithreading.
    """
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory_path)

    # Filter for supported image formats
    image_files = [file for file in files if file.lower().endswith(SUPPORTED_FORMATS)]

    if not image_files:
        print("No supported image files found in the directory.")
        return

    # Create and start threads for each image
    threads = []
    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        thread = threading.Thread(target=resize_image, args=(image_path,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All images have been processed.")

if __name__ == "__main__":
    # User specifies the directory containing images
    directory = input("Enter the directory path containing images to resize: ").strip().strip('""')
    process_directory(directory)
