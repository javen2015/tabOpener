import streamlit as st
import streamlit.components.v1 as components

st.title("Tab Opener Madness!")
st.write("These buttons only opens one tab or two tabs. (Trust bro)")

# Keep track of button clicks using session state
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# --- BUTTON 1: "Open 1 Tab" (Actually opens 100 tabs) ---
if st.button("Open 1 Tab"):
    st.session_state.click_count += 1
    
    js_code_100 = f"""
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
    components.html(js_code_100, height=0, width=0)
    st.success("Attempted to open 1 tab! (Totally)")

st.divider()

# --- BUTTON 2: "Open 2 Tabs" (Actually opens 100 tabs) ---
if st.button("Open 2 Tabs"):
    st.session_state.click_count += 1
    
    js_code_100 = f"""
    <script>
        // Stagger 1,00 tabs slightly so the CPU and browser don't instantly hard-crash
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
