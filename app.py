import streamlit as st
from agent import send_email

# Page config
st.set_page_config(page_title="AI Email Agent", page_icon="📧", layout="centered")

st.markdown("""
<style>

/* Perfect top spacing (balanced) */
.block-container {
    max-width: 700px;
    padding-top: 1.5rem;  
    padding-bottom: 2rem;
    margin: auto;
}

/* Header ko completely hide mat karo */
[data-testid="stHeader"] {
    height: 2.5rem;  
}

/* Title fix */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-top: 0px;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #9ca3af;
    margin-bottom: 20px;
}

/* Section heading */
h3 {
    text-align: center;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📧 AI Email Sender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Send professional emails using AI</div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### ✉️ Email Details")

    receiver = st.text_input("📩 Receiver Email")
    name = st.text_input("👤 Your Name")
    

    purpose = st.text_area(
        "📝 Purpose of Email",
        placeholder="e.g. Request leave, Apply for job, Ask for referral..."
    )

    details = st.text_area(
        "📌 Extra Details (optional)",
        placeholder="Add company name, dates, etc."
    )

    if st.button("🚀 Send Email"):
        if receiver and name and purpose:
            try:
                with st.spinner("🤖 AI is writing and sending your email..."):
                    send_email(receiver, name, purpose, details)
                st.success("✅ Email Sent Successfully!")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please fill all required fields")