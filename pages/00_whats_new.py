import streamlit as st

st.title("What's new?")

st.markdown("""
On version 0.7.0, we added:
* Flexible multipage handling: you can have the classic page arrows or a lateral menu.
* User answers to provided questions can (optionally) be saved.
* Each user get's a unique token, so he can continue his session (and we can store his answers).
* Admin view: you get some stats on users and answers.
""")