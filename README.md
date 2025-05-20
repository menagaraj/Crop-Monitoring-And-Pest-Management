
# Pest Detection from Crop Images

This project uses basic image processing with OpenCV to detect potential pest instances in crop images. The detection is based on filtering specific color ranges (brown shades) typically associated with pests.

## Features

- Loads and resizes the crop image.
- Converts the image to HSV color space.
- Detects pest-like regions based on color filtering.
- Highlights the detected regions.
- Displays the count of detected pest instances.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python numpy
````

## Usage

Place your crop image as `image.png` in the same directory as the script.

Run the script:

```bash
python pest_detection.py
```

## Example Console Output

```bash
Possible pest instances detected: 5
```

> The above output shows the number of brown-shaded contours detected in the image.

## Output Visualization

The script will open a window showing the original image masked with detected pest regions highlighted.

## Sample Output Image

![Console Output](console_output.png)

This shows the number of pests from the given image

---



