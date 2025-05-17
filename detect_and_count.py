import torch
from pathlib import Path
import cv2
from matplotlib import pyplot as plt

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/window_detector/weights/best.pt')

model.conf = 0.3  # Confidence threshold

# Folder with your test images
test_images_folder = 'test_images'
output_folder = 'output_images'
Path(output_folder).mkdir(exist_ok=True)

