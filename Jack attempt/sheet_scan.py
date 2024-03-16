import cv2
import numpy as np
import matplotlib.pyplot as plt

high_quality = False 			# HQ is slower but better
image_name = "5-notice.png"		# Image name plus extension
BW = False						# Black and white vs colour output document 

img = cv2.imread('./Jack attempt/' + image_name, cv2.IMREAD_COLOR)

if not high_quality:			# Rescale the image to 1920p
	size_lim = 1920
	size_max = max(img.shape)

	if size_max > size_lim:
		resize_scale = size_lim / size_max
		img = cv2.resize(img, None, fx=resize_scale, fy=resize_scale)

orig = img.copy() 				# Store original

# Close image 3 times with 6x6 kernel to remove text
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((6,6),np.uint8), iterations=3)

# Use the GrabCut algorithm to identify foreground and background regions.
mask = np.zeros(img.shape[:2], np.uint8) # Blank mask populated with fgd / bgd information later
Models = {"bgd": np.zeros((1, 65), np.float64), "fgd": np.zeros((1, 65), np.float64)}
rect = (15, 15, img.shape[1]-15, img.shape[0]-15)	# Initial guess for foreground region
cv2.grabCut(img, mask, rect, Models['bgd'], Models['fgd'], 5, cv2.GC_INIT_WITH_RECT)	# Perform GrabCut to iteratively improve foreground estimate

# Create a mask where px are either foreground or background - remove the uncertainty in the output from GrabCut
bgdMask = np.where((mask==3) | (mask==1), 1, 0).astype('uint8')
img = img * bgdMask[:, :, np.newaxis]	# Apply mask to image to remove background

gray = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (11, 11), 0) # Blurred grayscale image

# Find edges using Canny algorithm
canny = cv2.Canny(gray, 100, 200)
canny = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))) # Dilate edges using 5x5 disk strel

outline = np.zeros_like(img)		# Blank canvas the size of image
contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # Find contours for the edges
sheet = sorted(contours, key=cv2.contourArea, reverse=True)[:5] # Keep only the largest contour as the edge
con = cv2.drawContours(outline, sheet, -1, (0, 255, 255), 3)

def order_points(pts):
	'''Rearrange coordinates to order: top-left, top-right, bottom-right, bottom-left'''
	rect = np.zeros((4, 2), dtype='float32')
	pts = np.array(pts)

	sum = pts.sum(axis=1)
	rect[0] = pts[np.argmin(sum)]	# Top left point will have lowest sum (~0 + ~0)
	rect[2] = pts[np.argmax(sum)]	# Bottom right point will have highest sum (large number + large number)
	
	diff = np.diff(pts, axis=1)
	rect[1] = pts[np.argmin(diff)]	# Top right point will have lowest difference (~0 - large number)
	rect[3] = pts[np.argmax(diff)]	# Bottom left point has highest difference (large number - ~0)

	return rect.astype('int').tolist()

outline = np.zeros_like(img)		# Blank canvas the sizer of image

for cont in sheet:
	# Approximate the contour.
	epsilon = 0.02 * cv2.arcLength(cont, True)	# Specify approximation accuracy for curve
	corners = cv2.approxPolyDP(cont, epsilon, True) # Use Ramer-Douglas-Peucker algorithm to approximate contour
	
	if len(corners) == 4:			# If approximated contour has 4 corners, we've found the sheet - break the loop
		break

cv2.drawContours(outline, cont, -1, (0, 255, 255), 3)
cv2.drawContours(outline, corners, -1, (0, 255, 0), 10)
corners = sorted(np.concatenate(corners).tolist())

# Rearranging the order of the corner points.
corners = order_points(corners)

(tl, tr, br, bl) = corners
# Finding the maximum width.
widths = {
	"A": np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2)),
	"B": np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
}
maxWidth = max(int(widths["A"]), int(widths["B"]))

# Finding the maximum height.
heights = {
	"A": np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2)),
	"B": np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
}
maxHeight = max(int(heights["A"]), int(heights["B"]))

# Final destination co-ordinates.
dest_corners = [
	[0, 0],
	[maxWidth, 0],
	[maxWidth, maxHeight],
	[0, maxHeight]]

H_T = cv2.getPerspectiveTransform(np.float32(corners), np.float32(dest_corners))					# Calculate Homography Transform
final = cv2.warpPerspective(orig, np.float32(H_T), (maxWidth, maxHeight), flags=cv2.INTER_LINEAR)	# Apply Homography Transform

# Display results 
plt.figure(); 
plt.subplot(131); plt.imshow(orig); plt.axis('off'); plt.title("Original image")
plt.subplot(132); plt.imshow(con); plt.axis('off'); plt.title("Edges")
plt.subplot(133); plt.imshow(final); plt.axis('off'); plt.title("Scanned Form")
plt.show()