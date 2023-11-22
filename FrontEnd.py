import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the model
model = tf.keras.models.load_model('air_quality_model.keras')

# Define the image size
img_size = (224, 224)

st.title('Air Quality Index Predictor')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=img_size)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    x = image.img_to_array(img)
    x /= 255.
    x = np.expand_dims(x, axis=0)

    # Make a prediction using the model
    prediction = model.predict(x)

#---- Second commit ends here ----------------------
    
    # Print the predicted class (0 for clean air, 1 for polluted air)
    aqi=prediction[0]*500
    st.write("Estimated AQI: ",aqi)
    if aqi<=50:
      st.write("The air in the image is clean")
    elif aqi>50 and aqi<=100:
        st.write("The air in the image is satisfactory")
    elif aqi>100 and aqi<=200:
      st.write("The air in the image is moderately polluted")
    elif aqi>200 and aqi<=300:
      st.write("The air in the image is poor")
    elif aqi>300 and aqi<=400:
      st.write("The air in the image is heavily polluted")
    elif aqi>400:
      st.write("The air in the image is severely polluted")

