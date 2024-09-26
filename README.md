# Image Converter: JPG/JPEG/PNG to WebP

This Python script converts images from JPG, JPEG, or PNG formats to WebP format using PyTorch. It can utilize GPU acceleration if available, making it efficient for batch processing large numbers of images.

## Features

- Converts JPG, JPEG, and PNG images to WebP format
- Supports batch processing of images in a folder
- Option to use GPU acceleration for faster processing
- Preserves original filename (changes only the extension)

## Requirements

- Python 3.6+
- PyTorch
- torchvision
- Pillow (PIL)

## Installation

1. Clone this repository or download the script:

   ```
   git clone https://github.com/yourusername/image-converter.git
   cd image-converter
   ```

2. Set up a virtual environment (recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install torch torchvision Pillow
   ```

   Note: If you want to use GPU acceleration, make sure to install the CUDA-enabled version of PyTorch. Visit the [PyTorch website](https://pytorch.org/get-started/locally/) for specific installation instructions for your system.

## Environment Setup

To ensure your environment is correctly set up, follow these steps:

1. Check your Python version:

   ```
   python --version
   ```

   Ensure it's 3.6 or higher.

2. Verify PyTorch installation:

   ```
   python -c "import torch; print(torch.__version__)"
   ```

3. Check if CUDA is available (for GPU acceleration):

   ```
   python -c "import torch; print(torch.cuda.is_available())"
   ```

   If this returns `True`, your system is ready for GPU acceleration.

4. Verify torchvision installation:

   ```
   python -c "import torchvision; print(torchvision.__version__)"
   ```

5. Check Pillow installation:
   ```
   python -c "from PIL import Image; print(Image.__version__)"
   ```

## Usage

1. Place your JPG, JPEG, and/or PNG images in an input folder (e.g., 'input_images').

2. Run the script:

   ```
   python image_converter.py
   ```

3. The converted WebP images will be saved in the output folder (e.g., 'output_images').

## Customization

You can modify the following variables in the script to customize its behavior:

- `input_folder`: The folder containing the input images
- `output_folder`: The folder where converted images will be saved
- `use_gpu`: Set to `True` to use GPU acceleration (if available), or `False` to use CPU only

Example of customizing these variables in the script:

```python
input_folder = 'my_input_images'
output_folder = 'my_output_images'
convert_to_webp(input_folder, output_folder, use_gpu=True)
```

## How It Works

The script performs the following steps:

1. It checks if the output folder exists and creates it if necessary.
2. It sets up the device (CPU or GPU) based on availability and user preference.
3. It creates a transformation pipeline using PyTorch's `transforms` module.
4. It iterates through all files in the input folder, processing only JPG, JPEG, and PNG files.
5. For each image:
   - It opens the image using Pillow.
   - It converts the image to a PyTorch tensor and moves it to the selected device.
   - It performs any necessary processing (in this case, it just passes the image through).
   - It converts the processed tensor back to a PIL Image.
   - It saves the image in WebP format in the output folder.

The use of PyTorch allows for easy GPU acceleration and potential for adding more complex image processing operations in the future.

## Notes

- The script will create the output folder if it doesn't exist.
- The script preserves the original filename and only changes the extension to .webp.
- If you encounter any "out of memory" errors when using GPU, try processing fewer images at a time or switch to CPU mode.
- WebP format generally provides better compression than JPG or PNG while maintaining similar image quality.

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are correctly installed.
2. Check that your input images are not corrupted.
3. If using GPU, make sure your CUDA installation is correct.
4. For large images or large batches, try running on CPU if you encounter memory issues.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/pushpendra-kashyap/image-converter.git) if you want to contribute.

To contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

[Pushpendra Kumar kashyap]

For any additional questions or comments, please feel free to contact me at [pushpendrakumarkashyap0@gmail.com].
