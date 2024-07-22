# Team Project Report

## Achievement Overview:
Our team has successfully implemented an algorithm to flatten images of documents and extract textual information using optical character recognition (OCR). Using various computer vision algorithms, we separate the image of a document from it's background, align it and perform OCR. Specifically, we have achieved the following:

- Used morphology operations to remove detail/text from a document to aid edge detection.
- Implemented Canny edge detection and contour finding to identify document edges.
- Applied the Ramer-Douglas-Peucker algorithm for corner detection to determine the quadrilateral representing the document boundaries.
- Conducted a perspective transform using Homography to align the document.
- Performed Optical Character Recognition on the identified document.

Both team members actively contributed to coding, debugging, and documenting the project.

## Special Instructions:
To replicate our results and run the application locally, please follow these instructions:

1. Clone the repository to your local machine.
2. Ensure that you have the necessary Python libraries installed: OpenCV, NumPy, Matplotlib and OCRmyPDF. You can install these by runnning `pip install -r requirements.txt`. Note that OCRmyPDF has several dependencies which may not be installed by default (pytesseract and ghostscript in particular), and these may require separate installation.
3. Add your input images to the img directory within the project.
4. Run the Python script to execute the document alignment process. Change the `image_name` to match the desired input image.
5. View the output displayed using Matplotlib to observe the aligned document. The OCR output in saved in the ourput directory.

## Evidences of Functionality:

A number of results have been provided in the outputs directory. For further insights into the algorithm, below the original image, identified edges and resulting image transformation can be seen for `4-notice.png`.

![Result](src/Result.png)

Once transformed, OCR is performed to identify text in the image, and append it on a transparent layer in a PDF. Below this text has been highlighted to show the successful output.

![OCR Output](src/OCR_result.png)

## Application Evaluation:
### What Our Application Can Do:
- Perform document alignment using morphological operations, edge detection, contour finding, corner detection, and perspective transform techniques.
- Handle various document orientations and sizes.
- Achieve accurate alignment results in most cases.
- Perform OCR on the document.

### What Our Application Cannot Do:
- Handle extremely skewed or distorted documents, or documents with non-straight (i.e. curved/distorted edges).
- Handle documents where all four corners are not visible, or with noisy backgrounds.
- Guarantee perfect alignment in all scenarios, especially when dealing with highly complex document layouts.
- Perform OCR on handwriting.
