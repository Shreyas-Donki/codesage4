import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image

im = Image.open("icon2.png")
st.set_page_config(page_title = "CodeSage", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English", "Hindi","Kannada"])

if lan == "English":
    home_title = "welcome to CodeSage - CodeSage has the potential to revolutionize how tech professionals are assessed and hired, while also providing a unique platform for continuous professional development."
    home_introduction = "Welcome to Code Sage, Connect, Collaborate, and Cultivate Your Tech Network  |  Artificial General Intelligence powered Next-Gen suite of automated hiring solutions"
   
    with st.sidebar:
        st.markdown('Code Sage - V1.0.1')
        st.markdown(""" 
        #### Let's contact:
        [Shreyas SD](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)
        
        Building the next Gen - Industry Disruptive Suite of Artificial Intelligence
        and Machine Learning powered solutions across 
        Software | Storage | Retail | E commerce | Ad tech | Energy & Gas |

                    
        #### Please fill the form, we'd love to have your feedback:
        [Feedback Form](https://docs.google.com/forms/d/13f4q03bk4lD7sKR7qZ8UM1lQDo6NhRaAKv7uIeXHEaQ/edit)
    
        #### Powered by
    
        [OpenAI](https://openai.com/)
    
        [FAISS](https://github.com/facebookresearch/faiss)
    
        [Langchain](https://github.com/hwchase17/langchain)
    
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown("CodeSage - Elevate Your Talent, One Question at a Time , while being Etheically and accurately Video and Audio Proctored by our Artificial Agents!")
    st.markdown("""\n""")
    st.markdown("CodeSage - Customized Feedback and SWOT analysis for each candidate , with the option of AI generated recommmendations for super fast upskilling.")
    st.markdown("""\n""")
    st.markdown("""Our AI powered next Gen  Sage, powered by SIA's(in house trained LLM's) feature transforms the recruitment process by leveraging our in house - next Gen LLM's for conducting dynamic aptitude ,technical interviews , coding continuos assessment. Designed to challenge candidates with a range of questions from basic to advanced levels, this system provides immediate, detailed feedback, ensuring a comprehensive assessment of skills and knowledge.
    Comprehensive Project Review""")
    st.markdown("""\n""")
    st.markdown("""Deep Dive into Your Projects, Uncover True Potential.""")
    st.markdown("""SkillSage takes a thorough look at candidates' previous projects, evaluating roles, responsibilities, and the implementation of solutions. This in-depth analysis not only highlights technical capabilities but also problem-solving skills and project impact, offering valuable insights into a candidate's real-world experience and contributions.
    Real-time Speech-to-Text and Text-to-Speech """)
    st.markdown("""\n""")
    st.markdown("""Deep Dive into Your Projects, Uncover True Potential.""")
    st.markdown("""SkillSage takes a thorough look at candidates' previous projects, evaluating roles, responsibilities, and the implementation of solutions. This in-depth analysis not only highlights technical capabilities but also problem-solving skills and project impact, offering valuable insights into a candidate's real-world experience and contributions.
    Real-time Speech-to-Text and Text-to-Speech """)
    st.markdown("""\n""")
    st.markdown("""Speak and Listen, Communication as Natural as It Gets.""")
    st.markdown("""Our platform features cutting-edge
    Automatic Speech Recognition technology, seamlessly converting spoken responses into text for analysis, followed by state-of-the-art text-to-speech feedback. This ensures an interactive, engaging interview experience that mirrors face-to-face conversations, enhancing communication and comprehension.
    Continuous Learning and Skill Enhancement """)
    st.markdown("""\n""")
    st.markdown("""Connect, Collaborate, and Cultivate Your Tech Network""")
    st.markdown("""Envisioned as the "Factbook" for tech professionals, SkillSage offers a unique space for users to connect, share knowledge, and collaborate. By fostering a community of like-minded individuals, our platform encourages networking and mutual learning, empowering tech professionals to build meaningful connections and advance their careers """)
    st.markdown("""\n""")
    st.markdown("""Why wait? get started for free!! No Credit card of payment option required for free trail period of 1 month!""")

    

    
    with st.expander("Updates"):
        st.write("""
        08/13/2024
        -Shreyas  Fix the error that occurs when the user input fails to be recorded. """)
    with st.expander("What's coming next?"):
        st.write("""
       AGI Powered Self sustaining hiring and tech socical media Eco-System """)
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Pick One platform  to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Coding","Customize!","Soft Skills"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the  will assess your technical skills as they relate to the job description.
           
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("hey Code Sage , Assess me!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the  will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the  will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own  and practice with it!
             - Configure  in different specialties.
             - Configure  in different personalities.
             - Different tones of voice.
             
             Coming at the end of July""")
    

# if lan ==  '中文':
#     home_title = "AI面试官"
#     home_introduction = "欢迎使用 AI 面试官，它能够通过生成式AI帮助您准备面试。"
#     with st.sidebar:
#         #### Let's contact:
#         [Shreyas SD](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)
        
#         Building the next Gen - Industry Disruptive Suite of Artificial Intelligence
#         and Machine Learning powered solutions across 
#         Software | Storage | Retail | E commerce | Ad tech | Energy & Gas |
#             #### 请填写表格，我们非常希望听到您的反馈：
#             [Feedback Form](https://docs.google.com/forms/d/13f4q03bk4lD7sKR7qZ8UM1lQDo6NhRaAKv7uIeXHEaQ/edit)

#             #### 使用的技术：

#             [OpenAI](https://openai.com/)

#             [FAISS](https://github.com/facebookresearch/faiss)

#             [Langchain](https://github.com/hwchase17/langchain)

#                         """)
#     st.markdown(
#         "<style>#MainMenu{visibility:hidden;}</style>",
#         unsafe_allow_html=True
#     )
#     st.image(im, width=100)
#     st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""", unsafe_allow_html=True)

#     st.markdown("""\n""")
#     # st.markdown("#### Greetings")
#     st.markdown(
#         "欢迎使用AI面试官！👏AI面试官是一款由生成式人工智能驱动的个人面试官，可以进行模拟面试。您可以上传您的简历或者复制粘贴工作描述，AI面试官会根据您的情况提出定制化的问题。"
#     )
#     st.markdown("""\n""")
#     with st.expander("更新日志"):
#         st.write("""
#             08/13/2023
#             - 修复了当用户输入失败时的报错问题 """)
#     with st.expander("未来计划"):
#         st.write("""
#             - 提供更加稳定和快速的语音交互
#             - 支持全中文的模拟面试 """)
#     st.markdown("""\n""")
#     st.markdown("#### 让我们开始吧!")
#     st.markdown("请选择以下其中一个开始您的面试！")
#     selected = option_menu(
#         menu_title=None,
#         options=["专业评估", "简历评估", "行为评估"],
#         icons=["cast", "cloud-upload", "cast"],
#         default_index=0,
#         orientation="horizontal",
#     )
#     if selected == '专业评估':
#         st.info("""
#                 📚在本次面试中，AI面试官将会根据职位描述评估您的技术能力。
#                 注意: 您回答的最大长度为4097个tokens!
#                 - 每次面试将会持续10到15分钟。
#                 - 您可以通过刷新页面来开始新的面试。
#                 - 您可以选择您喜欢的交互方式(文字/语音)
#                 - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Professional Screen")
#     if selected == '简历评估':
#         st.info("""
#                 📚在本次面试中，AI面试官将会根据您的简历评估您的过往经历。
#                 注意: 您回答的最大长度为4097个tokens!
#                 - 每次面试将会持续10到15分钟。
#                 - 您可以通过刷新页面来开始新的面试。
#                 - 您可以选择您喜欢的交互方式(文字/语音)
#                 - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Resume Screen")
#     if selected == '行为评估':
#         st.info("""
#             📚在本次面试中，AI面试官将会根据您的简历评估您的技术能力。
#             注意: 您回答的最大长度为4097个tokens!
#             - 每次面试将会持续10到15分钟。
#             - 您可以通过刷新页面来开始新的面试。
#             - 您可以选择您喜欢的交互方式(文字/语音)
#             - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Behavioral Screen")
#     st.markdown("""\n""")
#     st.markdown("#### 维基")
#     st.write(
#         '[点击查看常见问题，更新和计划！](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')
