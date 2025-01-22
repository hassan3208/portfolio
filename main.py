import streamlit as st
from PIL import Image

# Set Page Configurations
st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Navigate to:", ["Home", "Projects", "Skills", "Resume", "Contact"])

# Header
st.markdown(
    """
    <style>
    .main-header {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        color: #2E86C1;
    }
    </style>
    <div class="main-header">Welcome to My Portfolio</div>
    """,
    unsafe_allow_html=True,
)

# Sections
if pages == "Home":
    # Home Section
    st.title("Welcome to My Portfolio")
    col1, col2 = st.columns([1, 2])

    with col1:
        # Add a professional photo (replace with your actual path)
        image = 'https://media.licdn.com/dms/image/v2/D4E03AQFuY-_QX5_mew/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1712939971884?e=1743033600&v=beta&t=22-KQ5SrS7rs27ZSAsY8Zk78YYRcyVHtW72C0gd-P4Y'
        st.image(image, caption="Hassan", width=250)

    with col2:
        st.write(
            """
            Hi, I'm **Hassan**, As a computer scientist, programmer, and AI enthusiast, I am constantly driven by a passion for using technology to solve complex problems and improve lives. My goal is to expand my expertise in artificial intelligence and explore its transformative potential to address real-world challenges.

            I thrive on continuous learning and growth, and I am eager to collaborate with like-minded individuals to develop innovative solutions that shape a better future. With a strong foundation in programming and an unwavering curiosity for AI, I am excited to contribute meaningfully to the evolving technological landscape.
            """
        )
        st.markdown(
            """
            **Connect with me:**  
            [LinkedIn](https://www.linkedin.com/in/hassan-imran-bb41902ba/) | [GitHub](https://github.com/hassan3208) | [Portfolio Website](#)
            """
        )

elif pages == "Projects":
    # Projects Section
    st.title("My Projects")
    st.write("Below are some of my key projects showcasing my expertise and skills:")

    projects = [
        {
            "name": "Document reader bot",
            "description": "An LLM based chatbot that process the uploaded document and answer the queries, with an intuitive UI built using Streamlit.",
            "link": "https://github.com/hassan3208/rocky-bot",
        },
        {
            "name": "LinkedIn job search",
            "description": "It is a webscrapping project. You can search for a job title it will return you a csv file of top related jobs.",
            "link": "https://github.com/hassan3208/linkdin",
        },
        {
            "name": "Movie Recommender",
            "description": "A simple NLP based project in which you can type for one movie title and it will display you 5 reccommended movvies related to it.",
            "link": "https://github.com/hassan3208/Movie-recomended-system/",
        },
        
        {
            "name": "Diabetes Predictor",
            "description": "This project is a diabetes prediction application built using an Artificial Neural Network (ANN). The model predicts the probability of diabetes based on user input data such as age, hypertension, heart disease, BMI, HbA1c level, and blood glucose level. With a 97% validation accuracy, this application provides a reliable tool for early diabetes risk assessment.",
            "link": "https://github.com/hassan3208/Diabetes-prediction",
        },
    ]

    for project in projects:
        with st.expander(project["name"]):
            st.write(project["description"])
            st.markdown(f"[View Project Here]({project['link']})")

elif pages == "Skills":
    # Skills Section
    st.title("My Skills")
    st.write("Here are the tools and technologies I specialize in:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming & Development")
        st.write("""
        - Python
        - SQL
        - HTML & CSS
        - C++
        """)

        st.subheader("AI & Machine Learning")
        st.write("""
        - Generative AI
        - PyTorch
        - Scikit-learn
        - Transformers
        - TensorFlow
        - OpenCV
        - Data Preprocessing and Transformation
        """)

    with col2:
        st.subheader("Data Science & Analytics")
        st.write("""
        - Data Visualization (Matplotlib, Seaborn, Plotly)
        - Exploratory Data Analysis (EDA)
        - ETL
        - Data Analysis
        """)

    with col3:
        st.subheader("Database Design & Management")
        st.write("""
        - RDBMS
        - Firebase
        - SQLite
        - Database Schema Design
        - ERD Diagramming and Normalization
        - Advanced SQL Queries (Joins, CTEs, Window Functions)
        """)

        st.subheader("Tools & Frameworks")
        st.write("""
        - Google Colab
        - Jupyter
        - NumPy
        - Pandas
        - Matplotlib
        - Scikit-learn
        - TensorFlow
        - PyTorch
        - Streamlit
        - OpenCV
        - YOLO
        - Hugging Face
        - APIs
        """)

elif pages == "Resume":
    # Resume Section
    st.title("Resume")
    st.write("Below you can download my resume and view my professional experience:")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(
            """
            **Experience Highlights:**
            - Developed a movie recommendation engine on given dataset.
            - Design end-to-end machine learning project for Diabetes predictor.
            - Designed intuitive job search engine.
            """
        )

    # with col2:
    #     # Add Resume Download Option (replace with your file path)
    #     with open("resume.pdf", "rb") as file:
    #         st.download_button(
    #             label="Download My Resume",
    #             data=file,
    #             file_name="Your_Name_Resume.pdf",
    #             mime="application/pdf",
    #         )

elif pages == "Contact":
    # Contact Section
    st.title("Get in Touch")
    st.write("Feel free to reach out for collaborations, projects, or any professional inquiries.")

    # Display contact information
    st.subheader("Contact Information")
    st.markdown(
        """
        - **Email:** [itsmywork1019@gmail.com](mailto:your-email@example.com)
        - **Phone:** +923328425042
        """
    )

