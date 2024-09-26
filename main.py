import os
import torch
from torchvision import transforms
from PIL import Image

def convert_to_webp(input_folder, output_folder, use_gpu=False):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Set up device (CPU or GPU)
    device = torch.device("cuda" if use_gpu and torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Set up transformation pipeline
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Open the image
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Get the filename without extension
                name = os.path.splitext(filename)[0]

                # Convert image to tensor and move to device
                img_tensor = transform(img).unsqueeze(0).to(device)

                # Perform any GPU-based processing here (e.g., resizing, filtering)
                # For this example, we'll just pass the image through
                processed_tensor = img_tensor

                # Convert back to PIL Image
                processed_img = transforms.ToPILImage()(processed_tensor.squeeze(0).cpu())

                # Save as WebP
                processed_img.save(os.path.join(output_folder, f"{name}.webp"), 'WEBP')
                print(f"Converted {filename} to {name}.webp")

# Example usage
input_folder = 'input_images'
output_folder = 'output_images'
convert_to_webp(input_folder, output_folder, use_gpu=True)