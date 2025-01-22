import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Resume", "Contact"])

# Home Section
if pages == "Home":
    st.title("Welcome to My Portfolio")
    st.image('https://media.licdn.com/dms/image/v2/D4E35AQHqYPV6tlw0iA/profile-framedphoto-shrink_400_400/profile-framedphoto-shrink_400_400/0/1735824421032?e=1738126800&v=beta&t=s1kHCKxVroOgydxJzRf70LFbEAL13YKsPNkir6TEH8E', width=200)  # Add your photo
    st.write("""
    Hi, I'm [Your Name], a passionate [Your Profession] specializing in [Your Specialization]. 
    Explore my portfolio to learn more about my work and skills.
    """)
    st.markdown("[LinkedIn Profile](https://linkedin.com/in/yourname) | [GitHub](https://github.com/yourname)")

# Projects Section
elif pages == "Projects":
    st.title("My Projects")
    st.write("Here are some of my featured projects:")
    
    project_data = [
        {"name": "Movie Recommendation System", "description": "Built using Streamlit and ML concepts.", "link": "https://github.com/yourname/movie-recommendation"},
        {"name": "Digit Recognition Model", "description": "An FCNN model with 98% validation accuracy.", "link": "https://github.com/yourname/digit-recognition"},
    ]
    
    for project in project_data:
        st.subheader(project["name"])
        st.write(project["description"])
        st.markdown(f"[View Project]({project['link']})")

# Skills Section
elif pages == "Skills":
    st.title("My Skills")
    skills = {
        "Programming Languages": ["Python", "JavaScript", "Java"],
        "Frameworks & Tools": ["Streamlit", "PyTorch", "Keras"],
        "Other Skills": ["Image Processing", "Machine Learning", "Web Development"]
    }
    
    for category, skill_list in skills.items():
        st.subheader(category)
        st.write(", ".join(skill_list))

# Resume Section
elif pages == "Resume":
    st.title("My Resume")
    st.write("Download my resume below:")
    # with open("resume.pdf", "rb") as file:
       
        # st.download_button(label="Download Resume", data=file, file_name="Your_Name_Resume.pdf", mime="application/pdf")

# Contact Section
elif pages == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out!")
    st.write("Email: yourname@example.com")
    st.write("LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourname)")
    st.write("GitHub: [Your GitHub](https://github.com/yourname)")
