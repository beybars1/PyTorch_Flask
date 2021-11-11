# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app import transform_image, get_prediction
import requests

if __name__ == '__main__':
    resp = requests.post("http://localhost:5000/predict", files={"file": open('doomguy.jpg', 'rb')})
    print(resp.json())