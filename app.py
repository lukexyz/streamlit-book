import streamlit as st
import streamlit_book as stb

# Streamlit page properties
st.set_page_config()

st.header('Hello')

# Streamit book properties
stb.set_book_config(menu_title="streamlit_book",
                    menu_icon="lightbulb",
                    options=[
                            "What's new on v0.7.0?",
                            "Core Features",
                            ],
                    paths=[
                          "pages/00_whats_new.py", # single file
                          "pages/01 Multitest", # a folder
                          ],
                    icons=[
                          "code",
                          "robot",
                          ],
                    save_answers=True,
                    )