import os
import numpy as np

model_path = os.path.join(
    os.path.dirname(__file__), "../../tests/assets/COVID-Net-CXR-2.onnx"
)

npz_input_file = os.path.join(os.path.dirname(__file__), "./covidnet.npz")


def get_input():
    if os.path.exists(npz_input_file):
        return np.load(npz_input_file)["img"]

    def crop_top(img, percent=0.15):
        offset = int(img.shape[0] * percent)
        return img[offset:]

    def central_crop(img):
        size = min(img.shape[0], img.shape[1])
        offset_h = int((img.shape[0] - size) / 2)
        offset_w = int((img.shape[1] - size) / 2)
        return img[offset_h : offset_h + size, offset_w : offset_w + size]

    def process_image_file(filepath, size, top_percent=0.08, crop=True):
        import cv2

        img = cv2.imread(filepath)
        img = crop_top(img, percent=top_percent)
        if crop:
            img = central_crop(img)
        img = cv2.resize(img, (size, size))
        return img

    img = process_image_file(
        os.path.join(os.path.dirname(__file__), "../../tests/assets/ex-covid.jpeg"),
        size=480,
    )
    img = img.astype("float32") / 255.0
    img = img[np.newaxis, :, :, :]

    np.savez(npz_input_file, img=img)


def get_model():
    with open(model_path, "rb") as f:
        return f.read()
