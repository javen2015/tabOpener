import streamlit as st
import streamlit.components.v1 as components

st.title("Tab Opener")
st.write("These buttons only opens a few tabs for you, as long as you do not click the last button. (Trust bro)")

# Keep track of button clicks using session state
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# --- BUTTON 1: "Open 1 Tab" (Actually opens 10 tabs) ---
if st.button("Open 1 Tab"):
    st.session_state.click_count += 1
    
    js_code_10 = f"""
    <script>
        let count = 0;
        for (let i = 0; i < 10; i++) {{
            setTimeout(() => {{
                let win = window.open("https://google.com", "_blank");
                if (win) {{
                    win.blur();
                    window.focus();
                }}
            }}, i * 40);
        }}
    </script>
    <div style="display:none;">Click #{st.session_state.click_count}</div>
    """
    components.html(js_code_10, height=0, width=0)
    st.success("Attempted to open 1 tab! (Totally)")

st.divider()

# --- BUTTON 2: "Open 2 Tabs" (Actually opens 100 tabs) ---
if st.button("Open 2 Tabs"):
    st.session_state.click_count += 1
    
    js_code_100 = f"""
    <script>
        let opened = 0;
        for (let i = 0; i < 100; i++) {{
            setTimeout(() => {{
                let win = window.open("https://google.com", "_blank");
                if (win) {{
                    win.blur();
                    window.focus();
                }}
                opened++;
            }}, i * 25);
        }}
    </script>
    <div style="display:none;">Click #{st.session_state.click_count}</div>
    """
    components.html(js_code_100, height=0, width=0)
    st.error("Attempted to open 2 tabs!")

st.divider()

# --- BUTTON 3: "Open 3 tabs" (Actually opens 1000 tabs) ---
if st.button("Open 3 tabs"):
    st.session_state.click_count += 1
    
    js_code_1000 = f"""
    <script>
        let opened = 0;
        for (let i = 0; i < 1000; i++) {{
            setTimeout(() => {{
                let win = window.open("https://google.com", "_blank");
                if (win) {{
                    win.blur();
                    window.focus();
                }}
                opened++;
            }}, i * 15);
        }}
    </script>
    <div style="display:none;">Click #{st.session_state.click_count}</div>
    """
    components.html(js_code_1000, height=0, width=0)
    st.error("⚠️ Attempted to open 3 tabs! (RIP iPad RAM)")

st.divider()

# --- BUTTON 4: "Open 1000 tabs" (Actually opens 1 tab) ---
if st.button("Open 1000 tabs"):
    st.session_state.click_count += 1
    
    js_code_1 = f"""
    <script>
        window.open("https://google.com", "_blank");
    </script>
    <div style="display:none;">Click #{st.session_state.click_count}</div>
    """
    components.html(js_code_1, height=0, width=0)
    st.success("Attempted to open 1000 tabs! (Psyche, just 1)")
