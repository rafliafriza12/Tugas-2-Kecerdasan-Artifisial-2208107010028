import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Muat model
model = load_model('cifar10_model.h5')

# Nama kelas untuk CIFAR-10
class_names = [
    'Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck'
]

# Judul aplikasi
st.title("Aplikasi Klasifikasi Gambar CIFAR-10")

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar yang di-upload
    img = image.load_img(uploaded_file, target_size=(32, 32))  # Ganti sesuai ukuran input model
    img_array = image.img_to_array(img) / 255.0  # Normalisasi
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch

    # Prediksi
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)

    # Tampilkan gambar
    st.image(img, caption='Gambar yang Diupload', use_column_width=True)
    
    # Tampilkan hasil prediksi
    st.write(f'Prediksi: {class_names[predicted_class]}')
