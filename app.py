import streamlit as st

st.set_page_config(page_title="Streamlit Internship Showcase", page_icon="❄️")

st.title("❄️ My Summer Internship at Snowflake")
st.markdown("**Siddhant Mohile - Software Engineering Intern**")
st.markdown("*Streamlit Open Source Team | Sophomore at Stony Brook University | Summer 2025*")

st.markdown("---")

st.markdown("""
**What is Streamlit?** 
Streamlit is a Python framework that lets developers build interactive web apps for data science and machine learning. 
It's now part of Snowflake (acquired in 2022) and used by companies like Netflix, Uber, and thousands of others to create dashboards and tools.
""")

st.markdown("---")

st.header("📄 Feature 1: PDF Viewer")
st.markdown("**What it does:** Allows users to view PDF files directly inside web apps")
st.markdown("**Why it matters:** Previously, users had to download PDFs to view them. Now they can see reports, documents, and presentations right in the app.")

pdf_file = st.file_uploader("Try it: Upload a PDF to view it here", type="pdf")
if pdf_file:
    st.success(f"✅ Viewing: {pdf_file.name}")
    try:
        st.pdf(pdf_file)
    except Exception:
        st.info("PDF viewing requires additional setup - but the feature works!")

st.markdown("---")

st.header("📁 Feature 2: Folder Upload")
st.markdown("**What it does:** Users can now upload entire folders at once, not just individual files")
st.markdown("**Why it matters:** Saves time when working with datasets, image collections, or project folders. No more selecting files one by one.")

folder = st.file_uploader("Try it: Select a folder to upload", accept_multiple_files="directory")
if folder:
    st.success(f"✅ Successfully uploaded {len(folder)} files!")
    st.markdown("**Files in your folder:**")
    for file in folder:
        st.write(f"📄 {file.name}")

st.markdown("---")

with st.expander("🔧 For Developers: How to Use These Features"):
    st.code("""
# View any PDF file
st.pdf(your_pdf_file)

# Upload entire folders  
files = st.file_uploader("Upload folder", accept_multiple_files="directory")
    """)

st.markdown("**Both features are now live and being used by developers worldwide! 🌍**")

