import streamlit as st

st.write("# Siddhant Streamlit Internship Showcase")

st.write("## PDF Upload and Display")
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
if pdf_file:
    st.write(f"PDF uploaded: {pdf_file.name}")
    st.pdf(pdf_file)

st.write("## Directory Upload")
folder = st.file_uploader("Upload a folder here", accept_multiple_files="directory")
if folder:
    st.write(f"Uploaded {len(folder)} files from directory")
    for file in folder:
        st.write(f"File: {file.name} - Type: {file.type}")
        if file.type == "application/pdf":
            st.pdf(file)
        elif file.type.startswith("image/"):
            st.image(file)
        elif file.type.startswith("text/"):
            content = str(file.read(), "utf-8")
            st.code(content[:500])
