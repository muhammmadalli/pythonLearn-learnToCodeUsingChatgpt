import os
from PIL import Image

def create_thumbnails(input_dir: str, output_dir: str = "thumbnails", size: tuple = (50, 50)):
    """
    Creates 50x50 pixel thumbnails for all image files in the specified directory.
    
    :param input_dir: Directory containing image files.
    :param output_dir: Directory to save thumbnails. Defaults to "thumbnails".
    :param size: Tuple indicating the size of thumbnails. Defaults to (50, 50).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        try:
            with Image.open(file_path) as img:
                img.thumbnail(size)
                thumbnail_path = os.path.join(output_dir, file_name)
                img.save(thumbnail_path, format=img.format)
                print(f"Thumbnail created: {thumbnail_path}")
        except Exception as e:
            print(f"Skipping {file_name}: {e}")

if __name__ == "__main__":
    input_directory = "images"  # Change this to your image directory
    create_thumbnails(input_directory)
