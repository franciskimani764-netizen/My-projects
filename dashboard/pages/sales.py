import streamlit as st
import pandas as pd
import numpy as np

from database import get_connection

st.subheader("Sales page")
st.write("view your pages")

with st.form("Sales form"):
    product = st.text_input("Product: ")

    price = st.number_input("Price: ")

    sale_date = st.text_input("Sale date: ")

    submitted = st.form_submit_button("Add sale")

    if submitted:
        def get_connection():
            conn = get_connection
            cur = conn.cursor
            cur.execute("""
            INSERT INTO sales (product, price, sale_date) VALUES(?,?,?)
            """,(
            product,
            price,
            sale_date
            ))
            conn.commit()
            conn.close()
            st.success("Sale added sucesfully")



