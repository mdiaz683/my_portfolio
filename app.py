import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
import os
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

from PIL import Image, ExifTags

def fix_image_orientation(image_path):
    img = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = img._getexif()

        if exif is not None:
            orientation_value = exif.get(orientation)

            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except:
        pass

    return img

#test

# Set page title
st.set_page_config(page_title="Maria Diaz", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Harry Chang';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_maria1 = Image.open("images/maria1.jpg")
img_maria2 = Image.open("images/maria2.jpg")
img_ifg = Image.open("images/ifg.jpg")
#Assets for competitions
img_lit = Image.open("images/legalease.jpg")
img_lifehack2 = Image.open("images/lifehack2.jpg")
img_lifehack = Image.open("images/lifehack.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_ecc = Image.open("images/ecc.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/sji.jpg")
img_unil = Image.open("images/unil2.png")
img_FIU = Image.open("images/FIU.jpg")
img_uah = Image.open("images/uah.jpeg")
img_gmss = Image.open("images/gmss.jpg")
img_sjij = Image.open("images/sjij.jpg")
img_dsa = Image.open("images/dsa.jpg")
# Assets for experiences
img_quest = Image.open("images/questlogo.jpg")
img_scor = Image.open("images/scor.jpg")
img_iasg = Image.open("images/iasg.jpg")
img_sshsph = Image.open("images/sshsph.jpg")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
# Assets for experience
img_trc = Image.open("images/trc.png")
img_nttdata = Image.open("images/nttdata.jpg")
img_cordis = Image.open("images/cordis.jpg")

# Assets for projects
img_fin_web = Image.open("images/fin_web.png")
img_sql = Image.open("images/sql.png")
img_pdf = Image.open("images/pdf.jpg")
img_bot = Image.open("images/bot.jpg")
img_finger = Image.open("images/finger.png")
img_sql = Image.open("images/sql.png")
img_forecast = Image.open("images/forecast.png")

# Assets for blog
img_qb = Image.open("images/qb.jpg")
img_mayans = Image.open("images/mayans.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
img_bmsaew = Image.open("images/bmsaew.png")
img_dac1 = Image.open("images/dac1.png")
img_dac2 = Image.open("images/dac2.png")
img_diploma2 = Image.open("images/diploma.jpg")


# Assets for gallery
img_program = Image.open("gallery/IMG_8509.jpg")
img_confer = Image.open("gallery/IMG_2396.jpg")
img_grad1 = Image.open("gallery/IMG_2675.jpg")
img_grad2 = Image.open("gallery/IMG_2691.jpg")
img_friends= Image.open("gallery/IMG_2719.jpg")
img_diploma = Image.open("gallery/IMG_8506.jpg")
img_finds = Image.open("gallery/IMG_8480.jpg")



#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/ff8c00/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_maria2, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Maria Diaz",
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Conferences", "Gallery", "Resume", "Contact"],
                         icons=['person fill', 'clock history', 'tools', 'book half',  'clipboard', 'trophy fill', 'image', 'paperclip', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    linkedin_url = "https://www.linkedin.com/in/maria-diaz-alba/"
    github_url = "https://github.com/mdiaz683"
    email_url = "mailto:m.mariadiazalba@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Maria Diaz")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("AI Engineer | Data Analyst | Forensic Sciences & Technologies")
            st.write("👋🏻 Hi, I'm Maria!  Originally from Madrid, Spain, now based in Miami, I’ve taken an exciting journey from forensic sciences and cybersecurity into the world of artificial intelligence. Along the way, I discovered my passion for building impactful tech solutions that connect innovation with real-world needs.")
            st.write("💼 I love tackling challenges, exploring how AI can solve emerging societal demands, and ensuring technology is applied ethically and meaningfully. My main interests lie in AI research, the creative side of machine learning, and building deep learning models that bring groundbreaking ideas to life.")
            st.write("🌍 Beyond tech, I’m always looking for my next adventure—whether it's traveling, discovering new places, or meeting inspiring people who expand my personal and professional horizons.")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, AI Engineer, AI Consultant")

            mention(label="Resume", icon="📄", url="https://drive.google.com/file/d/1eSHuJj-5ptm19K7bpig3n9aj9qyX2NeF/view?usp=drive_link",)

        with middle_column:
            st.empty()
        with right_column:
            st.image(img_maria1)


elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_cordis)
        with text_column:
            st.subheader("Data Science & AI Engineering Intern, [Cordis Corporation](https://cordis.com/na/home?regionPref=71030)")
            st.write("*July 2025 to Present*")
            st.markdown("""
            - Supported AI integration and data-driven process optimization for different business challenges.
            
            `Python` `Skforecast` `Pandas` `Streamlit` `ChatGPT` `Power Automate` `Power BI` `Excel` 
            """)

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_nttdata)
        with text_column:
            st.subheader("Digital Technology Consultant - AI/ML & Security Intern, [NTT DATA](https://www.nttdata.com/global/en/)")
            st.write("*May to July 2025*")
            st.markdown("""
            - Participated in the development of an enterprise AI governance and operationalization framework, aligning with industry standards such as the NIST AI Risk Management Framework.            - Utilised Librosa, Matplotlib and Scikit-Learn to detect anomalies for predictive maintenance of machines using spectrograms and principal component analysis (PCA)
            - Performed a technical and strategic evaluation of Azure’s AI Foundry stack to assess its alignment with the framework and uncover key capabilities and gaps in supporting enterprise AI readiness and compliance.
            
            `Microsoft Azure` `Azure AI Foundry`
            """)

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_trc)
        with text_column:
            st.subheader("Cyber Intelligence / AI Solutions Researcher Intern, [TRC](https://trc.es/)")
            st.write("*March to July 2024*")
            st.markdown("""
            - Worked with cyber intelligence team to implement innovative security measures based on threat hunting and leak detection.
            - Developed an AI-driven tool using ML techniques to assess risk levels for credentials detected in Telegram data leaks, leveraging a custom bot built with the Telegram API to automate data collection, prioritize analysis, and boost evaluation efficiency.
            """)

            if st.button("→ *Credential Risk Assessment Tool*"):
                st.session_state["option_menu"] = "Projects"

            st.markdown("""
            `Python` `Pandas` `Telegram API` `Dash` `Plotly` `Streamlit` `Excel` 
            """)


    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`R`, `Python`, `SQL`, `Java`, `Stata`, `MATLAB`")
    txt3("Academic Interests","`Data Visualization`, `Market Basket Analysis`, `Recommendation Systems`, `Natural Language Processing`")
    txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Plotly`, `Librosa`, `Folium`, `Gephi`, `GIS`, `Tableau`, `Power BI`, `Google Data Studio`, `Domo`, `Google Analytics`")
    txt3("Database Systems", "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`, `Google BigQuery`, `Cloud Firestore`, `InfluxDB`, `ScyllaDB`")
    txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Heroku`, `Streamlit Cloud`, `Render`, `Hugging Face`, `Minio`")
    txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
    txt3("Version Control", "`Git`, `Docker`, `MLFlow`")
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`, `Wordpress`, `Webflow`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `JAX`")
    txt3("Task Management Tools", "`Asana`, `Notion`, `ClickUp`, `Slack`, `Jira`, `Confluence`, `Miro`, `Mural`")
    txt3("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_FIU)
            with text_column:
                st.subheader("Master of Science - Applied Artificial Intelligence & IoT, [Florida International University](https://www.fiu.edu/) (2024-2025)")
                st.write("Relevant Coursework: Computers and the Humanities, Convex Optimization, Data Science in Practice, Data Structures and Algorithms, Data Visualization, Database Technology and Management, Linear Algebra, Multivariable Calculus, Optimization for Large-Scale Data-Driven Inference, Probability, Programming Tools for Economics, Regression Analysis, Statistical Learning")
                st.markdown("""
                - [NUS Product Club](https://linkedin.com/company/nusproductclub) - Co-founder & President (2023-24)
                - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
                - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_uah)
            with text_column:
                st.subheader("Bachelor of Science - Forensic Sciences and Technologies, [Universidad de Alcalá de Henares](https://uah.es/es/) (2020-2024)")
                st.write("Coursework: Foundations of Medicinal Chemistry, Pharmaceutical Biochemistry, Statistics for Life Sciences, Human Anatomy and Physiology, Quantitative Reasoning")
                st.markdown("""
                Withdrew from course in 2020, before performing a clean slate transfer to pursue a Bachelor's Degree in Data Science and Analytics
                - [NUS Students' Science Club](https://www.nussciencelife.com/) - Marketing Executive, Welfare Subcommittee
                - Pharmaceutical Science (Class of 2023) - Assistant Class Representative
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_unil)
            with text_column:
                st.subheader("Bachelor of Science - Forensic Sciences and Technologies, [Université de Lausanne](https://www.unil.ch/unil/fr/home.html) (2023 - 2024)")
                st.write("Coursework: H2 Chemistry, H2 Economics, H2 Mathematics, H1 Project Work, H1 Chinese, H1 History")
                st.markdown(""" 
                - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
                - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
                """)
    elif selected == "Modules":
        st.subheader("Modules")
        st.write("*List of modules taken at National University of Singapore*")
        with st.container():
            sem1, mid, sem2 = st.columns((1,0.1,1))
            with sem1:
                st.write("**Academic Year 2019/20 Semester 1**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |AY1130| Human Anatomy and Physiology I       |4 MCs|
                |GER1000| Quantitative Reasoning              |4 MCs|
                |PR1110A| Foundations for Medicinal Chemistry |4 MCs|
                |PR1111A|Pharmaceutical Biochemistry          |4 MCs|
                |ST1232| Statistics for Life Sciences         |4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **20 Modular Credits (MCs)**
                """)
            with mid:
                st.empty()
            with sem2:
                st.write("**Academic Year 2020/21 Semester 1**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |CS1010S|Programming Methodology|4 MCs|
                |DSA1101|Introduction to Data Science|4 MCs|
                |GER1000|Quantitative Reasoning|4 MCs|
                |MA1102R|Calculus|4 MCs|
                |SP1541|Exploring Science Communication Through Popular Science|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **20 Modular Credits (MCs)**
                """)
        with st.container():
            sem1, mid, sem2 = st.columns((1,0.1,1))
            with sem1:
                st.write("**Academic Year 2020/21 Semester 2**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |CFG1002|Career Catalyst|2 MCs|
                |EC1301|Principles of Economics|4 MCs|
                |GEQ1000|Asking Questions|4 MCs|
                |GES1010|Nation-Building in Singapore|4 MCs|
                |GET1030|Computers and the Humanities|4 MCs|
                |MA1101R|Linear Algebra I|4 MCs|
                |ST2131|Probability|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **26 Modular Credits (MCs)**
                """)
            with mid:
                st.empty()
            with sem2:
                st.write("**Academic Year 2020/21 Special Term (Part II)**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |CS2040|Data Structures and Algorithms|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **4 Modular Credits (MCs)**
                """)
        with st.container():
            sem1, mid, sem2 = st.columns((1,0.1,1))
            with sem1:
                st.write("**Academic Year 2021/22 Semester 1**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |DSA2102|Essential Data Analytics Tools: Numerical Computation|4 MCs|
                |EC2101|Microeconomic Analysis I|4 MCs|
                |EC2102|Macroeconomic Analysis I|4 MCs|
                |EC2204|Financial Accounting for Economists|4 MCs|
                |EC3305|Programming Tools for Economics|4 MCs|
                |GEH1049|Public Health in Action|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **24 Modular Credits (MCs)**
                """)
            with mid:
                st.empty()
            with sem2:
                st.write("**Academic Year 2021/22 Semester 2**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |ALS1010|Learning to Learn Better|2 MCs|
                |DSA2101|Essential Data Analytics Tools: Data Visualization|4 MCs|
                |GES1037|A History of Singapore in Ten Objects|4 MCs|
                |IS1103|Ethics in Computing|4 MCs|
                |IT2002|Database Technology and Management|4 MCs|
                |MA2104|Multivariable Calculus|4 MCs|
                |ST2132|Mathematical Statistics|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **26 Modular Credits (MCs)**
                """)
        with st.container():
            sem1, mid, sem2 = st.columns((1,0.1,1))
            with sem1:
                st.write("**Academic Year 2022/23 Semester 1**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |CFG1003|Financial Wellbeing - Introduction|0 MCs|
                |CS3244|Machine Learning|4 MCs|
                |DSA3101|Data Science in Practice|4 MCs|
                |DSA3102|Essential Data Analytics Tools: Convex Optimization|4 MCs|
                |ST3131|Regression Analysis|4 MCs|
                |ST3248|Statistical Learning I|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **20 Modular Credits (MCs)**
                """)
            with mid:
                st.empty()
            with sem2:
                st.write("**Academic Year 2022/23 Semester 2**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |DSA4212|Optimization for Large-Scale Data-Driven Inference|4 MCs|
                |LSM1301|General Biology|4 MCs|
                |ST4248|Statistical Learning II|4 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **12 Modular Credits (MCs)**
                """)
        with st.container():
            sem1, mid, sem2 = st.columns((1,0.1,1))
            with sem1:
                st.write("**Academic Year 2023/24 Semester 1**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |CS4225|Big Data Systems for Data Science|4 MCs|
                |DSA4199|Applied Project in Data Science and Analytics|8 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: **12 Modular Credits (MCs)**
                """)
            with mid:
                st.empty()
            with sem2:
                st.write("**Academic Year 2022/23 Semester 2 (Expected)**")
                st.markdown("""
                |Code|Module Title                       |Workload|
                |--------|--------------------------------------|---------|
                |DSA426X|Sense-Making Case Analysis|4 MCs|
                |ST4234|Bayesian Statistics|4 MCs|
                |DSA4199|Applied Project in Data Science and Analytics|8 MCs|
                """)
                st.write("")
                st.markdown("""
                Total Workload for Semester: *16 Modular Credits (MCs)**
                """)
        with st.container():
            left, mid, right = st.columns((0.1,1,0.1))
            with left:
                st.empty()
            with mid:
                st.write("**Graduation Requirements**")
                st.image(img_dsa)
            with right:
                st.empty()
    #elif selected == "Module Reviews":
        #st.subheader("Module Reviews")
        #st.write("*Reviews for selected modules taken in university*")


elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Inventory Forecasting Model for Supply Chain Optimization")
            st.write("*Project for US-based company, Cordis Corporation*")
            st.markdown("""
            - Developed a machine learning model to forecast product demand and optimize inventory capacity planning to improve stocking accuracy and reduce overages.
            """)
            # st.write("[Github Repo](https://github.com/mdiaz683/Forecasting-Model-for-Stock-Capacity-Optimization)")
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/Forecasting-Model-for-Stock-Capacity-Optimization",)
        with image_column:
            st.image(img_forecast)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Web Application for Financial Reconciliation Automation")
            st.write("*Project for US-based company, Cordis Corporation*")
            st.markdown("""
            - Built a lightweight web-based tool that streamlined the reconciliation of planned vs. actual expenses, eliminating the need for manual spreadsheet manipulation.
            """)
            mention(label="Streamlit App", icon="streamlit", url="https://github.com/mdiaz683/Finance-Web-App-for-BVA",)
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/Finance-Web-App-for-BVA",)
        with image_column:
            st.image(img_fin_web)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("AI-Driven Biometric Intelligence: Gender Prediction via CNN-Based Fingerprint Analysis")
            st.write("*Research project to be published on Springer Nature*")
            st.markdown("""
            - Book chapter to be included in the forthcoming volume AI-Enabled Forensic Investigations Network in Digital Sciences, edited by [Prof. S. S. Iyengar](https://people.cis.fiu.edu/iyengar/) (Springer Nature).
            - This project explores the application of Convolutional Neural Networks (CNNs) for gender classification from fingerprint images.
            - By leveraging deep learning architectures, it aims to uncover patterns that distinguish male and female fingerprints, offering potential applications in forensic science and biometric security.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/CNNFingerprints",)
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1as1y-U6B4kN6ID8iJ2Sr6dt9tGMUps2Q/view?usp=drive_link",)

        with image_column:
            st.image(img_finger)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Credential Risk Assessment Tool - Cyber Threat Intelligence Telegram Bot")
            st.write("*Internship project for TRC company*")
            st.markdown("""
            - Developed an AI-driven tool to assess risk levels of credentials exposed in Telegram data leaks, utilizing a custom bot built with the Telegram API to scrape suspicious channels
            - Conducted in-depth data engineering research, including feature selection, data collection, and preprocessing to build a high-quality dataset.
            - Designed, trained, and evaluated a Machine Learning model to enhance risk assessment accuracy.
            - Deployed the AI tool in a web-based triage system, enabling automated risk classification and visualization of credential threats.
            - Presented the project at the CNN-CERT (National Cryptologic Center) Cyberdefense Conference.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/Credential-Risk-Assessment-Tool",)
        with image_column:
            st.image(img_bot)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Malicious PDF Detection Using Autoencoders Trained on Metadata")
            st.write("*Master’s Project for Deep Learning course*")
            #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            - This project explores the use of deep autoencoders for detecting malicious PDF files through anomaly detection based on metadata.
            - The goal is to build a lightweight and interpretable model capable of flagging suspicious documents without requiring labeled malicious data during training.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/anomaly-detection-pdfs",)
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1waPLggKnYFvwgIvQovRZSWlLelZjgMkO/view?usp=drive_link",)
        with image_column:
            st.image(img_pdf)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Relational Database for a Professional Social Network")
            st.write("*Master’s Project for Data Engineering course*")
            st.markdown("""
            - This project focuses on the design and implementation of a relational database system inspired by professional social networks like LinkedIn.
            - The project aimed to convert a denormalized dataset of users, posts, and reactions into a normalized relational database, ensuring data integrity, consistency, and proper relational structure.
            """)
            #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/Social-Network-Database",)
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/10_N4Vb4uNyHBjfixW3mWYOhZ3NYCejOH/view?usp=drive_link",)

        with image_column:
            st.image(img_sql)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Comparison of KNN and Decision Tree Algorithms for Classification in Fire Detection Systems")
            st.write("*Master’s Project for Machine Learning course*")
            st.markdown("""
            - This project compares the performance of K-Nearest Neighbors (KNN) and Decision Tree algorithms in predicting fire incidents using IoT sensor data.
            - The objective is to determine which of these Machine Learning algorithms provides better results for classification tasks
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/mdiaz683/KNN-vs-DT",)
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1UR7aodakPSTZpnGAWIfZoCxNdaow_ifm/view?usp=drive_link",)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Smart Home Security System using Raspberry Pi")
            st.write("*Master’s Project for IoT Programming course*")
            st.markdown("""
            - System designed to enhance home security and comfort by integrating real-time monitoring and automated alerts.
            - Built on a Raspberry Pi it implements a multi-sensor system with real-time monitoring, automated alerts, and a web-based interface for remote access and data visualization.
            """)
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1LCnw3J6gcvV3rurytjSE38GDXNYGx6Jo/view?usp=drive_link",)

elif choose == "Conferences":
    # overview.createPage()
    st.header("Conferences")

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("FINDS 2025 - US Army Funded National Conference: AI-Enabled Forensic Investigations Network in Digital Sciences")
            st.write("*Florida International University, Miami, US*")
            st.markdown("""
            “AI-Driven Biometric Intelligence: Gender Prediction via CNN-Based Fingerprint Analysis”
            """)
            mention(label="US Army Funded National Conference", icon="🔗", url="https://finds.fiu.edu/conference.html",)
        with image_column:
            st.image(img_diploma2)


    with st.container():
        col1, col2, col3, col4 = st.columns((1,2,2,1))
        with col1:
            st.empty()
        with col2:
            st.image(img_confer, width=350)
        with col3:
            corrected_img_finds = fix_image_orientation("gallery/IMG_8480.jpg")
            st.image(corrected_img_finds, width=350)
        with col4:
            st.empty()

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("CNN-CERT (National Cryptologic Center) Cyberdefense Conference")
            st.write("*Madrid, Spain*")
            st.markdown("""
            *“Development of a Telegram tool for detecting exfiltrated passwords”*
            - Telegram bot developed to detect leaked credentials in public Telegram groups and channels through data scraping, analyzing txt files, and assigning criticality levels to alerts using machine learning and AI techniques.
            """)
        with image_column:
            st.image(img_bot)

    with st.container():
        col1, col2, col3 = st.columns((1, 3, 1))
        with col1:
            st.empty()
        with col2:
            st.video("https://www.youtube.com/watch?v=rWYVFkxzB7A")
        with col3:
            st.empty()

elif choose == "Gallery":
    st.header("Gallery")
    st.subheader("Some of my highlights throughout my educational and professional years!")

    gallery_path = "gallery"
    valid_extensions = (".jpg", ".jpeg", ".png", ".webp")

    image_files = [
        os.path.join(gallery_path, f)
        for f in os.listdir(gallery_path)
        if f.lower().endswith(valid_extensions)
    ]

    num_columns = 3
    cols = st.columns(num_columns)

    for i, img_path in enumerate(image_files):
        corrected_img = fix_image_orientation(img_path)
        with cols[i % num_columns]:
            st.image(corrected_img, use_container_width=True)


elif choose == "Resume":
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF document, you can open it in a new tab or download it below.*")

    # Ruta local del PDF (ajústala según tu estructura de proyecto)
    pdf_path = "docs/MariaDiaz_Resume.pdf"

    # Mostrar PDF dentro de Streamlit
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Botón de descarga
    with open(pdf_path, "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="docs/MariaDiaz_Resume.pdf",
            mime="application/pdf"
        )

elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at m.mariadiazalba@gmail.com or use the form below!")
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/maria-diaz-alba/"
            github_url = "https://github.com/mdiaz683"
            email_url = "mailto:m.mariadiazalba@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            st.image(img_ifg)

