import easyocr
import cv2
import matplotlib.pyplot as plt

def perform_ocr(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path)
    text_output = []
    image = cv2.imread(image_path)

    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        text_output.append(text)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    return " ".join(text_output)

if __name__ == "__main__":
    image_path = "data/image.png"
    extracted_text = perform_ocr(image_path)
    print(f"extracted Text: {extracted_text}")