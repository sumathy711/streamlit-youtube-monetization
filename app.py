import streamlit as st
import pandas as pd
import pickle

# 1. Load the saved tools
model = pickle.load(open('best_model.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

st.set_page_config(page_title="YouTube Revenue Predictor", page_icon="💰")
st.title("YouTube Content Monetization Modeler 🎥")

# 2. User Inputs (Left and Right Columns)
col1, col2 = st.columns(2)
with col1:
    views = st.number_input("Views", min_value=1, value=10000)
    likes = st.number_input("Likes", min_value=0, value=500)
    comments = st.number_input("Comments", min_value=0, value=50)
    subs = st.number_input("Subscribers", min_value=0, value=1000)
with col2:
    watch_time = st.number_input("Watch Time (Min)", min_value=0.0, value=30000.0)
    video_length = st.number_input("Video Length (Min)", min_value=0.1, value=10.0)
    category = st.selectbox("Category", ['Education', 'Music', 'Tech', 'Entertainment', 'Gaming', 'Lifestyle'])
    country = st.selectbox("Country", ['IN', 'CA', 'UK', 'US', 'DE', 'AU'])

# Hidden/Static Inputs
device = "Mobile" # Default
month = 3         # Default
is_weekend = 0    # Default

if st.button("Predict Revenue"):
    # 3. Create the input DataFrame
    input_data = pd.DataFrame({
        'views': [views], 'likes': [likes], 'comments': [comments],
        'watch_time_minutes': [watch_time], 'video_length_minutes': [video_length],
        'subscribers': [subs], 'category': [category], 'device': [device], 
        'country': [country], 'month': [month], 'is_weekend': [is_weekend]
    })

    # 4. The Feature Engineering that made the notebook work!
    input_data['engagement_rate'] = (likes + comments) / (views + 1)
    input_data['avg_view_duration'] = watch_time / (views + 1)
    input_data['retention_rate'] = watch_time / (views * video_length + 1)
    input_data['view_to_sub_ratio'] = views / (subs + 1)
    input_data['comment_to_like_ratio'] = comments / (likes + 1)
    input_data['performance_score'] = (views * 0.5 + likes * 0.3 + comments * 0.2)
    input_data['total_attention'] = views * watch_time
    input_data['quality_engagement'] = likes * watch_time

    # 5. Transform and Predict
    processed_input = preprocessor.transform(input_data)
    prediction = model.predict(processed_input)
    
    st.success(f"### 💰 Estimated Ad Revenue: ${prediction[0]:,.2f}")