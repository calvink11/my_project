import glob
import os
import gradio as gr
import torch
import torchvision
import numpy as np
from PIL import Image

model = torch.hub.load('./yolov5', 'custom', 'trained_weights/best.pt', source='local',force_reload=True)  # local repo
model.conf = 0.35  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold

def inference(im):
    results = model(im)
    img_result = results.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(img_result[0])


title = "Yolov5 Traffic Signal object detection"
description = "Yolov5 交通訊號模型"
article = """
            - Select an image from the examples provided as demo image
            - Click submit button to make image detection
            - Click clear button to try new image for detection
          """

# initializzing examples
test_imgs = [img_path for img_path in glob.glob('./examples/*.jpg')]
#test_imgs = [os.path.join('./examples',img_path) for img_path in os.listdir('./examples')]

included_extensions = ['jpg', 'jpeg', 'png']
test_imgs = [os.path.join('./examples', img_path) for img_path in os.listdir('./examples')
             if any(img_path.endswith(ext) for ext in included_extensions)]

examples = test_imgs

# Gradio app design
inputs = gr.components.Image(type='pil', label="Original Image")
outputs = gr.components.Image(type="pil", label="Output Image")

gr.Interface(
    fn=inference,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
    article=article,
    allow_flagging="never",
    examples=examples).launch(enable_queue=True)

interface.launch()
# interface.launch(server_name='0.0.0.0')
# interface.launch(server_name='163.18.23.20')
