from pathlib import Path 
from tkinter import PROJECTING 
import streamlit as st # type: ignore 
from PIL import Image # type: ignore 
 
# --------------- Path Setting  ---------------# 
current_dir = Path(_file_).parent 
css_file = current_dir / "style" / "main.css" 
resume_file = current_dir / "assect" / "cvc.pdf"  
profile_pic = current_dir / "assect" / "tej.png"   
 
# --- General Setting -------------------------# 
PAGE_TITLE = "Student Profile" 
PAGE_ICON = ":wave:"   
NAME = "Sumit Dhote" 
DESCRIPITION = """Student in SB Jain Institue of Technology and Management 
Research""" 
EMAIL = "sumitdhote392@gmail.com" 
SOCIAL_MEDIA = { 
    "GitHub": "https://github.com/sumitdhote",  
    "LinkedIn": "https://www.linkedin.com/in/sumit dhote768a8325a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", 
} 
 
# ----------- Streamlit App Configuration -----------------# 
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON) 
 
#-----------LOAD CSS,PDF,AND PROFILE PIC---# 
with open(css_file) as f: 
  
 
 
 st.markdown("<style>{}<style>".format(f.read()),unsafe_allow_html=True) 
with open(resume_file,"rb") as pdf_file: 
 PDFbyte = pdf_file.read() 
profile_pic=Image.open(profile_pic) 
 
#---HERO SECTION---# 
col1, col2 = st.columns(2, gap="small") 
with col1: 
 st.image(profile_pic, width=230) 
with col2: 
 st.title(NAME) 
 st.write(DESCRIPITION) 
 st.download_button( 
   label="Download Resume", 
   data=PDFbyte, 
   file_name=resume_file.name, 
   mime="application/octet-stream" )  
 st.write("     ",EMAIL,"     ") 
 
#-----SOCIAL LINKS-----# 
st.write("#") 
cols = st.columns(len(SOCIAL_MEDIA)) 
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()): 
 cols[index].write(f"[{platform}]({link})") 
 
#---OBJECTIVE ---# 
st.write("#") 
st.subheader("Objective") 
st.write( 
"""-  To work in the Organization which can provide me the platform to enhance my 
skills and learning.""") 
 
  
 
#---SKILLS AND CERTIFICATE---# 
st.write("#") 
st.subheader("Skills and Certificate") 
st.write("Skills") 
st.write( 
""" -  ✓My strengths lie in web development.,  - ✓Basic Photoshop Skills., - ✓Video Editing 
""" 
) 
 
st.write("Certification") 
st.write( 
""" - C,  - C ++ , - Java,  - Python,  - Web development,  - IBM (Data Science). 
""" 
) 
st.write("----") 
 
#------ACADAMIC PROJECT---------# 
st.subheader("Project") 
st.write("""Project 1:-Title:- Smart Parking System (2023-2024). - Description:- For thesmart parking systems make finding an available spot more manageable, there will be less search traffic in the street.""") 
 
  
 
st.write("""Project 2 
Title:- Expenditure noter. - Description:- For tracking your personal expenses on show on interactive window 
and make a plan according to the expenditure.""") 
 
#------INTERNSHIP-------# 
st.write("---") 
st.subheader("Internship") 
st.write("Two weeks of training of in  Appplication Development using java at IT Networks Pvt .Ltd, IT park, Nagpur.")