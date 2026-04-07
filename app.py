import streamlit as st
import streamlit.components.v1 as components
import time

# 1. Page Configuration
st.set_page_config(page_title="My Eternal Promise", page_icon="💍", layout="centered")

# 2. Advanced Cinematic CSS
st.markdown("""
<style>
    /* Dark Romantic Background */
    .stApp {
        background: linear-gradient(135deg, #1a001a 0%, #4a0000 100%);
        color: white;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu, header, footer {visibility: hidden;}

    /* Glassmorphism Message Cards */
    .love-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 15px 25px;
        margin: 10px 0;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        animation: fadeIn 0.8s ease-out;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .heart-icon {
        color: #ff4b4b;
        margin-right: 15px;
        font-size: 1.5rem;
    }

    .message-text {
        font-family: 'Georgia', serif;
        font-size: 1.4rem;
        color: #ffd700; /* Gold text */
        text-shadow: 0 0 8px rgba(255, 215, 0, 0.5);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Elegant Button */
    .stButton>button {
        background: linear-gradient(45deg, #ffd700, #ff8c00);
        color: black !important;
        border: none;
        padding: 15px 50px;
        font-weight: bold;
        border-radius: 50px;
        font-size: 1.2rem;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. Auto-Scroll JavaScript (Smooth following)
scroll_js = """
<script>
    function scrollToEnd() {
        const scroller = window.parent.document.querySelector('.main');
        scroller.scrollTo({ top: scroller.scrollHeight, behavior: 'smooth' });
    }
    scrollToEnd();
</script>
"""

# 4. App Header
st.markdown("<h1 style='text-align: center; color: #ffd700; font-family: serif;'>To My Dearest...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>I have 1,000 things to tell you.</p>", unsafe_allow_html=True)

# Placeholder for the wall of messages
wall_container = st.container()

# 5. The Proposing Loop
if st.button('Begin My Promise'):
    for i in range(1, 1001):
        with wall_container:
            # Each message is a NEW card added to the screen
            st.markdown(f"""
                <div class="love-card">
                    <span class="heart-icon">❤</span>
                    <span class="message-text"><b>{i}.</b> I Love You Forever</span>
                </div>
            """, unsafe_allow_html=True)
        
        # Inject JS to follow the newest message
        components.html(scroll_js, height=0, width=0)
        
        time.sleep(1) # 1 second delay as requested

    # Final Celebration
    st.balloons()
    st.snow()
    st.markdown("<h1 style='text-align: center; color: #ffd700; font-size: 4rem;'>WILL YOU BE MINE?</h1>", unsafe_allow_html=True)