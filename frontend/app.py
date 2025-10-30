# # import streamlit as st
# # import requests
# # import pandas as pd

# # API_URL = "http://localhost:8000/predict"

# # # ===================== Page Config =====================
# # st.set_page_config(
# #     page_title="Sentiment Analysis App",
# #     page_icon="📝",
# #     layout="wide"
# # )

# # # ===================== App Title =====================
# # st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Sentiment Analysis App</h1>", unsafe_allow_html=True)
# # st.markdown("<p style='text-align: center; color: grey;'>Enter your review below to predict sentiment</p>", unsafe_allow_html=True)
# # st.markdown("---")

# # # ===================== Sidebar Input =====================
# # st.sidebar.header("Enter Review")
# # test_text = st.sidebar.text_area("Your review:")



# # if st.button("Predict review class"):
# #     input_text_review = {
# #         "review":str(test_text)
# #     }


# #     try:
# #         response = requests.post(API_URL, json=input_text_review)
# #         if response.status_code == 200:
# #             result = response.json()
# #             prediction_response = result['Response']
            

# #             # ===================== Display Sentiment =====================
# #             color = "#FF4B4B" if prediction_response['sentiment_prediction'] == "Negative" else "#FFA500" if prediction_response['sentiment_prediction'] == "Neutral" else "#4CAF50"
# #             st.markdown(f"<div style='padding: 15px; background-color: #1E1E1E; border-radius: 10px; color: {color}; text-align: center; font-size: 24px; font-weight: bold;'>{prediction_response['sentiment_prediction']}</div>", unsafe_allow_html=True)

# #             prob_dict = prediction_response['class_probabilities']
# #             st.subheader("Sentiment Probabilities")
# #             st.bar_chart(pd.DataFrame(list(prob_dict.values()), index=list(prob_dict.keys()), columns=["Probability"]))


# #         else:
# #             st.error(f"API error: {response.status_code} - {response.text}")

# #     except requests.exceptions.ConnectionError:
# #         st.error("Could not connect to the FastAPI server. Make sure it's run on port 8000")






# import streamlit as st
# import requests
# import pandas as pd

# # ===================== Config =====================
# API_URL = "http://127.0.0.1:8000/predict"
# st.set_page_config(page_title="Sentiment Analysis", page_icon="📝", layout="wide")

# # ===================== Title =====================
# st.title("📝- Sentiment Analysis App -📝")
# st.markdown(
#     "<p style='text-align: center; color: grey;'>Analyze customer reviews and get instant sentiment predictions</p>",
#     unsafe_allow_html=True,
# )
# st.divider()

# # ===================== Sidebar =====================
# st.sidebar.header("💬 Enter Review")
# review_text = st.sidebar.text_area("Type your review here:")

# # ===================== Predict Button =====================
# if st.sidebar.button("🔍 Predict Sentiment"):
#     if not review_text.strip():
#         st.warning("⚠️ Please enter a review before predicting.")
#     else:
#         try:
#             response = requests.post(API_URL, json={"review": review_text})
            
#             if response.status_code == 200:
#                 result = response.json()["Response"]
#                 sentiment = result["sentiment_prediction"]
#                 probabilities = result["class_probabilities"]

#                 # ===================== Sentiment Box =====================
#                 colors = {"Positive": "#4CAF50", "Neutral": "#FFA500", "Negative": "#FF4B4B"}
#                 st.markdown(
#                     f"""
#                     <div style='padding: 15px; 
#                                 background-color: #1E1E1E; 
#                                 border-radius: 12px; 
#                                 color: {colors.get(sentiment, "white")}; 
#                                 text-align: center; 
#                                 font-size: 26px; 
#                                 font-weight: bold;'>
#                         {sentiment}
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#                 # ===================== Probability Chart =====================
#                 st.subheader("📊 Sentiment Probabilities")
#                 prob_df = pd.DataFrame.from_dict(probabilities, orient="index", columns=["Probability"])
#                 st.bar_chart(prob_df)

#             else:
#                 st.error(f"❌ API error: {response.status_code} - {response.text}")

#         except requests.exceptions.ConnectionError:
#             st.error("🚫 Could not connect to the FastAPI server. Make sure it's running on port 8000.")







import streamlit as st
import pandas as pd
import requests

# ===================== Config =====================
st.set_page_config(page_title="Sentiment Analysis", page_icon="📝", layout="wide")

API_URL = "http://127.0.0.1:8000/predict"  # FastAPI endpoint

# ===================== Title =====================
st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        📝 - Sentiment Analysis App - 📝
    </h1>
    <p style='text-align: center; color: grey;'>
        Analyze customer reviews and get instant sentiment predictions
    </p>
    """,
    unsafe_allow_html=True,
)
st.divider()

# ===================== Sidebar =====================
st.sidebar.header("💬 Enter Review")
review_text = st.sidebar.text_area("Type your review here:")

# ===================== Predict Button =====================
if st.sidebar.button("🔍 Predict Sentiment"):
    if not review_text.strip():
        st.warning("⚠️ Please enter a review before predicting.")
    else:
        try:
            # ====== Send request to FastAPI backend ======
            response = requests.post(API_URL, json={"review": review_text})

            if response.status_code == 200:
                result = response.json().get("Response", {})

                sentiment = result.get("sentiment_prediction", "Unknown")
                probabilities = result.get("class_probabilities", {})

                # ===================== Sentiment Box =====================
                colors = {"Positive": "#4CAF50", "Neutral": "#FFA500", "Negative": "#FF4B4B"}
                st.markdown(
                    f"""
                    <div style='padding: 20px; 
                                background-color: #1E1E1E; 
                                border-radius: 12px; 
                                color: {colors.get(sentiment, "white")}; 
                                text-align: center; 
                                font-size: 30px; 
                                font-weight: bold;
                                margin-bottom: 20px;'>
                        {sentiment}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # ===================== Probability Section =====================
                st.subheader("📊 Sentiment Probabilities")
                st.markdown("")
                st.markdown("")

                # Use flexbox to display probabilities
                prob_html = "<div style='display:flex; justify-content: space-around; color:white; font-size:16px; margin:10px 0;'>"
                for sent, prob in probabilities.items():
                    prob_html += f"<span style='font-weight:bold;'>{sent}: {prob*100:.2f}%</span>"
                prob_html += "</div>"

                st.markdown(prob_html, unsafe_allow_html=True)
                prob_df = pd.DataFrame.from_dict(probabilities, orient="index", columns=["Probability"])
                st.bar_chart(prob_df)

            else:
                st.error(f"❌ API Error: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("🚫 Could not connect to the FastAPI server. Make sure it's running on port 8000.")
        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")












