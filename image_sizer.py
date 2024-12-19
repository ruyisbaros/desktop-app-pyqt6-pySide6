from PIL import Image


def reduce_jpg_size(image_path, output_path, max_size_mb=3, quality=90):
    """Reduces the size of a JPG image to below the specified max size."""
    image = Image.open(image_path)

    while True:
        image.save(output_path, "JPEG", quality=quality)
        file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
        if file_size_mb < max_size_mb:
            break
        quality -= 5
        if quality <= 0:
            print("Could not reduce image size below the specified limit.")
            break

    print(f"Image saved to {output_path} with size {file_size_mb:.2f} MB")


if __name__ == "__main__":
    import os
    image_path = "ft.jpg"  # Replace with your image path
    output_path = "ft_2.jpg"
    reduce_jpg_size(image_path, output_path)
