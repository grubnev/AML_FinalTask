import streamlit as st
from PIL import Image
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from io import BytesIO

# Загрузка модели
model = torchvision.models.resnet50(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 10)
model.load_state_dict(torch.load('models/resnet50_cifar10.pth'))
model.eval()

# Список классов
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# Функция для предсказания
def predict(image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image)
    _, predicted = output.max(1)
    return predicted.item(), classes[predicted.item()]

# Streamlit UI
st.title('Image Classification')
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label_index, label_name = predict(image)
    st.write(f'Prediction: {label_name} (class {label_index})')

# API endpoint for predictions
def prediction_endpoint():
    if st.sidebar.button("Run API"):
        with open("test_image.jpg", "rb") as file:
            img_bytes = file.read()
        img = Image.open(BytesIO(img_bytes))
        index, label = predict(img)
        st.write(f'API Prediction: {label} (class {index})')

st.sidebar.header("API Testing")
prediction_endpoint()
