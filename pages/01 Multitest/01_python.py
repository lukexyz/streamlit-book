import streamlit as st
import streamlit_book as stb

st.markdown("# Python")

st.markdown("""
This is a **python file** that gets rendered using streamlit_book,
providing examples for the python functions to create certain types of activities.
""")

st.markdown("---")
st.markdown("A true-or-false question using python syntax:")
stb.true_or_false(
                    "Do you like the latest streamlit_book release", # required argument
                    True # required argument
                    )

st.markdown("---")
st.markdown("A single choice question using python syntax:")
stb.single_choice(
                    "What is the current streamlit_book version?", # required argument
                    ["0.4.0", "0.5.0", "0.7.0"], # required argument
                    2 # required argument
                    )

st.markdown("---")
st.markdown("A multiple choice question using python syntax:")
stb.multiple_choice(
                    "What are ...", # required argument
                    {"a":True, "b":False, "c":False} # required argument
                    )

st.markdown("---")
st.markdown("A simple to-do list using python syntax:")
stb.to_do_list( 
                tasks={"a":True, "b":False, "c":False}, # mandatory
                header="Description 02", # optional argument
                success="Bravo!" # optional argument
                )

st.markdown("---")
st.markdown("Social media buttons using python syntax:")
stb.share("Demo of streamlit_book v0.7.0", "https://share.streamlit.io/sebastiandres/stb_demo_v070/main")