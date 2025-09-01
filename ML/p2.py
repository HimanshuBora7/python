import cv2
import requests

def download_image(url):
   
        # sending HTTP request to get the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for successful download
        
        # the filename from the URL
        filename = "downloaded_image.jpg"
        
        # saving the image to disk
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully as {filename}")
        return filename
   


image_url = "https://media.gettyimages.com/id/2216597456/photo/from-the-world-of-john-wick-ballerina-berlin-premiere.jpg?s=1024x1024&w=gi&k=20&c=JZnoR1Mmq9UCKmIP1A4ENbwJ916w5KOItWPwI0MP_4A="  
downloaded_image = download_image(image_url)

# Step 2: Load the image into OpenCV
img = cv2.imread(downloaded_image)
if img is None:
        raise ValueError("image not loaded")
print("Image loaded into OpenCV successfully")


#Resizing the image to 300x300 pixels and save it as resized.jpg
resized_img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imwrite("resized.jpg", resized_img)
print("Resized image saved as resized.jpg")

#Converting the resized image to HSV color space and save it as hsv.jpg
hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv.jpg", hsv_img)
print("HSV image saved as hsv.jpg")

# converting HSV image back to BGR and save it as bgr.jpg
bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imwrite("bgr.jpg", bgr_img)
print("BGR image saved as bgr.jpg")
