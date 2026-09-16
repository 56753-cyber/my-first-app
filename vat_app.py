import streamlit as st

st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

vat = price * 0.07
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")

net_price = price + vat  # แก้ไขจาก - เป็น +
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")  # แก้ไขจาก t.header เป็น st.header

st.divider()
st.write("นางสาว สาริศา สาธรรม เลขที่ 28  ม.4/17")
