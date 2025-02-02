# -*- coding: utf-8 -*-
"""Ejercicio2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hxG6RwOhBCRSChJcJDXaogIKOMKMszIF
"""

from IPython.display import display, Javascript
from google.colab.output import eval_js
import cv2
import numpy as np
import base64
from google.colab.patches import cv2_imshow

def capture_image():
    js = Javascript('''
        async function captureImage() {
            const video = document.createElement('video');
            video.style.display = 'none';
            document.body.appendChild(video);

            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            await video.play();

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);

            stream.getTracks()[0].stop();
            video.remove();

            return canvas.toDataURL('image/jpeg', 0.8);
        }
        captureImage();
    ''')
    display(js)
    data = eval_js('captureImage()')
    return data

def decode_image(data):
    encoded_data = data.split(',')[1]
    img_data = base64.b64decode(encoded_data)
    img_array = np.frombuffer(img_data, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

def main():
    data = capture_image()
    img = decode_image(data)

    print("Imagen original:")
    cv2_imshow(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Filtro en escala de grises:")
    cv2_imshow(gray)

    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    print("Filtro de desenfoque gaussiano:")
    cv2_imshow(blurred)

    edges = cv2.Canny(img, 100, 200)
    print("Filtro de detección de bordes:")
    cv2_imshow(edges)

main()