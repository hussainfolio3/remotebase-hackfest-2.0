from utils import get_threshold, remove_background
import cv2
import os
from rembg import remove


# Parse Arguments
# json_data = json.loads(sys.argv[1])
IMAGE_ID = "222"  # json_data['image_id'] if 'image_id' in json_data else None
IMAGE_PATH = (
    "./v3.jpg"  # json_data['image_path'] if 'image_path' in json_data else None
)
THRESH_VAL = None  # json_data['thresh_val'] if 'thresh_val' in json_data else None
OUT_DIR = ""  # json_data['out_dir'] if 'out_dir' in json_data else 'result'

BG_RM = True

# *** Segmentation Steps ***#

# 1. Open Image
image = cv2.imread(IMAGE_PATH)
input_image = image
# print(image.shape)
if BG_RM:
    image = remove(image)
    print(image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    print(image.shape)
    cv2.imwrite("removed_bg_out_path.jpg", image)

# 2. Image:Adjust:Size
# image  = resize_img(image)

# 3. Image: Color: Split Channel
# 4. Use Blue channel
#blue_channel, _, _ = cv2.split(image)
blue_channel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# 5. Image: Adjust: Threshold
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
thresh_bg_img = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh_bg_img = cv2.erode(thresh_bg_img, None, iterations=2)
thresh_bg_img = cv2.dilate(thresh_bg_img, None, iterations=2)

# Remove Background
bg_removed = remove_background(blue_channel, thresh_bg_img)

# get threshold ImageJ default algorithm

if not THRESH_VAL:
    THRESH_VAL, _, _ = get_threshold(bg_removed)

#getting thresh from frontend slider 
# THRESH_VAL = get_thresh(THRESH_VAL)
# print(THRESH_VAL)

# 6. Apply Threshold
ret, thresh_img = cv2.threshold(bg_removed, THRESH_VAL, 255, cv2.THRESH_BINARY)

# 7. Analyze: Analyze particle: Overlay (check Display results and summary)
contours, hierarchy = cv2.findContours(
    thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)
depigmentation_cnts = [cnt for cnt in contours]


# 3. Depigmented area demarcated.
depigmentation_area = sum(cv2.contourArea(cnt) for cnt in depigmentation_cnts)
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 30]
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)


# 5. Percent depigmentation value.
contours, _ = cv2.findContours(thresh_bg_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 30]
total_area = sum(cv2.contourArea(x) for x in contours)
depigmentation_percentage = (depigmentation_area * 100) / total_area
# print(f"{depigmentation_percentage:.2f}%")


# Show Image
thresh_img = cv2.cvtColor(thresh_img, cv2.COLOR_GRAY2BGR)
out_path = os.path.join(
    OUT_DIR, f"{IMAGE_ID}_{THRESH_VAL}_{depigmentation_percentage:.2f}.jpg"
)
cv2.imwrite(out_path, image)


# Create response
res = {
    "preprocessed_image": out_path,
    "depigmentation_percentage": f"{depigmentation_percentage:.2f}%",
    # "partical_analysis": depigmentation_cnts
}
print("result",res)
# show_result(res)
# show_image(cv2.cvtColor(input_image,cv2.COLOR_BGRA2RGB),cv2.cvtColor(image, cv2.COLOR_BGRA2RGB))
# predict_cancer(input_image)