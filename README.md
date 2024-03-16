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
- Perform OCR on handwriting.

---

# Personal Statements

## Jack's Personal Statement:

### Personal Contribution:
In this project, I primarily focused on implementing the corner detection using the Douglas-Peucker algorithm and the perspective transform using homography. I contributed to coding these functionalities, debugging, and ensuring their integration with the overall project. I furthermore implemented the OCR functionality.

### Reflection:
Throughout this project, I've learned a great deal about the practical application of computer vision techniques in real-world scenarios. Specifically, diving deep into corner detection algorithms expanded my understanding of geometric transformations and image processing. Moreover, working collaboratively with my team member allowed me to enhance my GitHub skills. Having used a number of OCR tools for my Masters project, integrating this was quite an easy task.

### Design Decisions:
One of the key design decisions I made was to utilize the Douglas-Peucker algorithm for corner detection due to its efficiency and accuracy in identifying key points in the document contours. Additionally, opting for homography-based perspective transform provided a robust method for aligning documents.

### Mistakes and Lessons Learned:
One mistake I made during the project was underestimating the complexity of fine-tuning parameters for the corner detection algorithm. This led to some initial inaccuracies in corner localization, which required iterative adjustments and testing. This experience taught me the importance of thorough parameter tuning and testing before finalizing implementation.

### Future Improvements:
In the future, I would explore alternative solutions to make the OCR work with handwriting.

## James's Personal Statement:

### Personal Contribution:
In this project, my primary contributions revolved around implementing the morphology operations, Canny edge detection, and contour finding algorithms. I also compiled the code togeather and appropriately documented it.

### Reflection:
Engaging in this project provided me with valuable insights into the practical applications of computer vision algorithms, especially in document processing tasks. Implementing morphology operations and edge detection techniques deepened my understanding of image preprocessing steps crucial for subsequent analysis. 

### Design Decisions:
A key design decision I made was to apply morphological operations to create a blank canvas for document alignment. Additionally, opting for Canny edge detection followed by contour finding allowed us to accurately identify document boundaries, paving the way for further processing steps.

### Mistakes and Lessons Learned:
Similarly to Jack, fine-tuning the paramaters turned out to be the biggest challenge, as it proved to be a challenge to make the edge detection work on a wide range of images.

### Future Improvements:
If I were to do this project again, I would invest more time upfront in understanding and experimenting with parameter settings for corner detection, and explore altertnative solutions to make the code work with noisy backgrounds. The homography transform was also the slowest part of the code, and required severly downscaling the resolution of the image, which is an aspect of the project which could be further optimised.

