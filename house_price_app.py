import streamlit as st
import numpy as np
import pickle
import os

# **获取当前脚本所在目录**
current_dir = os.path.dirname(os.path.abspath(__file__))

# **构建 house_price_model.pkl 的完整路径**
model_path = os.path.join(current_dir, "house_price_model.pkl")

# **尝试加载模型**
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    st.success("✅ Model Loaded Successfully!")
except FileNotFoundError:
    st.error("❌ Error: Model file 'house_price_model.pkl' not found!")
    st.stop()

# Streamlit 界面
st.title("🏠 House Price Prediction App")

# 用户输入
sqft = st.slider("House Area (sqft)", 500, 5000, 1500)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])

# 预测按钮
if st.button("Predict Price"):
    features = np.array([[sqft, bedrooms, bathrooms]])
    price = model.predict(features)[0]
    st.success(f"🏡 Estimated House Price: ${price:,.2f}")
