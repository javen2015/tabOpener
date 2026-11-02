# import streamlit as st
# st.title("Tab Opener!")
# from webbrowser import open
# if st.button("Open tabs"):
#     while True:
#         open("https://google.com")
import streamlit as st
import streamlit.components.v1 as components

st.title("10-Tab Opener!")
st.write("Click the button below to open 10 Google tabs at once.")

# Keep track of button clicks using session state
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if st.button("Open 10 Tabs"):
    # Increment count so Streamlit forces the HTML component to re-render and execute
    st.session_state.click_count += 1
    
    # JavaScript loop to safely open exactly 10 tabs without crashing
    js_code = f"""
    <script>
        for (let i = 0; i < 100; i++) {{
            window.open("https://google.com", "_blank");
        }}
    </script>
    <div style="display:none;">Click #{st.session_state.click_count}</div>
    """
    # Execute the JavaScript
    components.html(js_code, height=0, width=0)
    st.success("Attempted to open 100 tabs!")
