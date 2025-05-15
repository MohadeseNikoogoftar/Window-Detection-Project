import os
import random
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

# CONFIG
images_folder = "images_all"
labels_folder = "labels_all"
output_base = "dataset"
classes = ["window"]
train_ratio = 0.8

# Create folders
for split in ["train", "val"]:
    os.makedirs(f"{output_base}/images/{split}", exist_ok=True)
    os.makedirs(f"{output_base}/labels/{split}", exist_ok=True)

# Match images with labels
image_files = [f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))]
image_files = [f for f in image_files if os.path.exists(os.path.join(labels_folder, Path(f).stem + ".txt"))]

