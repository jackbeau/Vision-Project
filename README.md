# Team Project Report

## Achievement Overview:
Our team has successfully implemented an image to object character recognition (OCR) algrithm. Using various computer vision algorithms, we seperate the image of a document from it's background, align it and perform OCR. Specifically, we have achieved the following:

- Utilized morphology operations to create a blank canvas for document alignment.
- Implemented Canny edge detection and contour finding to identify document edges.
- Applied the Douglas-Peucker algorithm for corner detection to determine the quadrilateral representing the document boundaries.
- Conducted a perspective transform using homography to align the document.
- Performed objecct character recognition on the identified document.

Both team members actively contributed to coding, debugging, and documenting the project.

## Special Instructions:
To replicate our results and run the application locally, please follow these instructions:

1. Ensure that you have the necessary Python libraries installed: OpenCV, NumPy, and Matplotlib.
2. Clone the repository to your local machine.
3. Download the provided image files and place them in the appropriate directory as specified in the code.
4. Run the Python script to execute the document alignment process.
5. View the output displayed using Matplotlib to observe the aligned document.

You can change the code to use images you provide yourself, if you want to explore other results.

## Evidences of Functionality:

## Application Evaluation:
### What Our Application Can Do:
- Perform document alignment using morphology, edge detection, contour finding, corner detection, and perspective transform techniques.
- Handle various document orientations and sizes.
- Achieve accurate alignment results in most cases.
- Perform OCR on the document.

### What Our Application Cannot Do:
- Handle extremely skewed or distorted documents.
- Handle documents where all four corners are not visible, or with noisy backgrounds.
- Guarantee perfect alignment in all scenarios, especially when dealing with highly complex document layouts.
- Perform OCR on handwrighting.
