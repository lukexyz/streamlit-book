import streamlit as st
import streamlit_book as stb

st.title("Admin view")

st.markdown("The library streamlit_book now provides an admin view by default.")

st.title("Access to Admin View")

st.markdown("""
To access the admin view, you have to add `?user=admin` to the URL (replacing the provided token).
A password will be required.
* The default password is `2lazy2change1password`
* You setup a stronger passoword in the cloud secrets, as shown on the link:
""")

def on_click():
    query_params = {"user":"admin"}
    st.experimental_set_query_params(**query_params)

st.title("Admin View Demo")

st.markdown("""
Use password `123` on this app to access the admin view.
""")

if st.button("Redirect to admin view", on_click=on_click):
    st.write("Redirected to admin view")
