# import streamlit as st
# import warnings

# warnings.filterwarnings("ignore")

# from chatbot import ask_bot

# # =====================================
# # Page Config
# # =====================================

# st.set_page_config(
#     page_title="BCET AI Assistant",
#     page_icon="🎓",
#     layout="wide"
# )

# # =====================================
# # Sidebar
# # =====================================

# with st.sidebar:

#     st.title("🎓 BCET AI Assistant")

#     st.markdown(
#         """
# ### Balasore College of Engineering & Technology

# Ask questions about:

# • Admissions

# • Departments

# • Faculty Members

# • Placements

# • Hostel Facilities

# • Committees

# • Fees

# • Contact Information

# • College Facilities
# """
#     )

#     if st.button("🗑 Clear Chat"):

#         st.session_state.messages = []

#         st.session_state.chat_history = []

#         st.rerun()

# # =====================================
# # Main Header
# # =====================================

# st.title(
#     "🎓 BCET AI Assistant"
# )

# st.caption(
#     "Ask anything about BCET"
# )

# # =====================================
# # Session State
# # =====================================

# if "messages" not in st.session_state:

#     st.session_state.messages = []

# if "chat_history" not in st.session_state:

#     st.session_state.chat_history = []

# # =====================================
# # Display Previous Messages
# # =====================================

# for message in st.session_state.messages:

#     with st.chat_message(
#         message["role"]
#     ):

#         st.markdown(
#             message["content"]
#         )

# # =====================================
# # Chat Input
# # =====================================

# query = st.chat_input(
#     "Ask a question about BCET..."
# )

# # =====================================
# # Process User Query
# # =====================================

# if query:

#     # -----------------------------
#     # Store User Message
#     # -----------------------------

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": query
#         }
#     )

#     with st.chat_message(
#         "user"
#     ):

#         st.markdown(
#             query
#         )

#     # -----------------------------
#     # Generate Response
#     # -----------------------------

#     with st.chat_message(
#         "assistant"
#     ):

#         with st.spinner(
#             "🔍 Searching BCET Knowledge Base..."
#         ):

#             answer = ask_bot(
#                 query,
#                 st.session_state.chat_history
#             )

#             st.markdown(
#                 answer
#             )

#     # -----------------------------
#     # Save Assistant Message
#     # -----------------------------

#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": answer
#         }
#     )

#     # -----------------------------
#     # Update Memory
#     # -----------------------------

#     st.session_state.chat_history.append(
#         (
#             "User",
#             query
#         )
#     )

#     st.session_state.chat_history.append(
#         (
#             "Assistant",
#             answer
#         )
#     )
##--------------------------------------------------------------------------

# import streamlit as st
# import warnings

# warnings.filterwarnings("ignore")

# from chatbot import ask_bot

# # ======================================
# # PAGE CONFIG
# # ======================================

# st.set_page_config(
#     page_title="BCET AI Assistant",
#     page_icon="🎓",
#     layout="wide"
# )

# # ======================================
# # CUSTOM CSS
# # ======================================

# st.markdown(
#     """
# <style>

# /* Main Background */

# .stApp{
#     background: linear-gradient(
#         135deg,
#         #f5f7fa,
#         #c3cfe2
#     );
# }

# /* Header */

# .main-header{
#     background: linear-gradient(
#         90deg,
#         #003366,
#         #00509e
#     );

#     padding:20px;
#     border-radius:15px;

#     color:white;
#     text-align:center;

#     box-shadow:0px 4px 15px rgba(0,0,0,0.2);
# }

# /* Cards */

# .info-card{
#     background:white;
#     padding:15px;
#     border-radius:15px;
#     box-shadow:0px 3px 10px rgba(0,0,0,0.1);
#     margin-bottom:15px;
# }

# /* Chat Messages */

# [data-testid="stChatMessage"]{

#     border-radius:15px;

#     padding:10px;

#     margin-bottom:10px;

#     box-shadow:0px 2px 8px rgba(0,0,0,0.1);
# }

# /* Sidebar */

# section[data-testid="stSidebar"]{
#     background-color:#003366;
#     color:white;
# }

# /* Footer */

# .footer{
#     text-align:center;
#     padding:15px;
#     color:#555;
#     font-size:14px;
# }

# </style>
# """,
#     unsafe_allow_html=True
# )

# # ======================================
# # SIDEBAR
# # ======================================

# with st.sidebar:

#     st.image(
#         "assets/bcet_logo.png",
#         width=120
#     )

#     st.markdown(
#         """
# # 🎓 BCET Assistant
# """
#     )

#     st.markdown(
#         """
# ### Ask About

# ✅ Admissions

# ✅ Departments

# ✅ Faculty

# ✅ Placements

# ✅ Hostel

# ✅ Facilities

# ✅ Committees

# ✅ Contact Information
# """
#     )

#     st.divider()

#     if st.button(
#         "🗑 Clear Chat",
#         use_container_width=True
#     ):

#         st.session_state.messages = []

#         st.session_state.chat_history = []

#         st.rerun()

# # ======================================
# # HEADER
# # ======================================

# st.markdown(
#     """
# <div class="main-header">

# <h1>🎓 BCET AI Assistant</h1>

# <p>
# Balasore College of Engineering and Technology
# </p>

# </div>
# """,
#     unsafe_allow_html=True
# )

# st.write("")

# # ======================================
# # INFO CARDS
# # ======================================

# col1, col2, col3 = st.columns(3)

# with col1:

#     st.markdown(
#         """
# <div class="info-card">

# <h4>🏫 College Info</h4>

# Ask about departments,
# faculty and facilities.

# </div>
# """,
#         unsafe_allow_html=True
#     )

# with col2:

#     st.markdown(
#         """
# <div class="info-card">

# <h4>📄 Documents</h4>

# Search PDF notices,
# prospectus and reports.

# </div>
# """,
#         unsafe_allow_html=True
#     )

# with col3:

#     st.markdown(
#         """
# <div class="info-card">

# <h4>🤖 AI Powered</h4>

# Powered by Gemini,
# LangChain and FAISS.

# </div>
# """,
#         unsafe_allow_html=True
#     )

# # ======================================
# # SESSION STATE
# # ======================================

# if "messages" not in st.session_state:

#     st.session_state.messages = []

# if "chat_history" not in st.session_state:

#     st.session_state.chat_history = []

# # ======================================
# # DISPLAY CHAT
# # ======================================

# for message in st.session_state.messages:

#     with st.chat_message(
#         message["role"]
#     ):

#         st.markdown(
#             message["content"]
#         )

# # ======================================
# # INPUT
# # ======================================

# query = st.chat_input(
#     "Ask anything about BCET..."
# )

# # ======================================
# # PROCESS QUERY
# # ======================================

# if query:

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": query
#         }
#     )

#     with st.chat_message("user"):

#         st.markdown(query)

#     with st.chat_message("assistant"):

#         with st.spinner(
#             "🔍 Searching BCET Knowledge Base..."
#         ):

#             answer = ask_bot(
#                 query,
#                 st.session_state.chat_history
#             )

#             st.markdown(answer)

#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": answer
#         }
#     )

#     st.session_state.chat_history.append(
#         (
#             "User",
#             query
#         )
#     )

#     st.session_state.chat_history.append(
#         (
#             "Assistant",
#             answer
#         )
#     )

# # ======================================
# # FOOTER
# # ======================================

# st.markdown(
#     """
# <hr>

# <div class="footer">

# BCET AI Assistant |
# Built using LangChain + Gemini + FAISS + Streamlit

# </div>
# """,
#     unsafe_allow_html=True
# )

##############################################################################################################
# # from dotenv import load_dotenv
# # import os

# # from langchain_google_genai import ChatGoogleGenerativeAI
# # from langchain_community.vectorstores import FAISS
# # from langchain_huggingface import HuggingFaceEmbeddings

# # # =====================================
# # # Load Environment Variables
# # # =====================================

# # load_dotenv(override=True)

# # api_key = os.getenv("GOOGLE_API_KEY")

# # print("\n" + "=" * 50)
# # print("API KEY FOUND:", api_key is not None)

# # if api_key:
# #     print("API KEY STARTS WITH:", api_key[:10] + "...")
# # else:
# #     print("GOOGLE_API_KEY NOT FOUND")

# # print("=" * 50 + "\n")

# # # =====================================
# # # Validate API Key
# # # =====================================

# # if not api_key:
# #     raise ValueError(
# #         "GOOGLE_API_KEY not found in .env file"
# #     )

# # # =====================================
# # # Load Embedding Model
# # # =====================================

# # print("Loading Embedding Model...")

# # embeddings = HuggingFaceEmbeddings(
# #     model_name="all-MiniLM-L6-v2"
# # )

# # # =====================================
# # # Load FAISS Vector Store
# # # =====================================

# # print("Loading Vector Store...")

# # vectorstore = FAISS.load_local(
# #     "vectorstore",
# #     embeddings,
# #     allow_dangerous_deserialization=True
# # )

# # print("Vector Store Loaded Successfully")

# # # =====================================
# # # Gemini LLM
# # # =====================================

# # print("Loading Gemini Model...")

# # llm = ChatGoogleGenerativeAI(
# #     model="gemini-3.1-flash-lite",
# #     google_api_key=api_key,
# #     temperature=0.2
# # )

# # print("Gemini Ready")

# # # =====================================
# # # Chat Function
# # # =====================================

# # def ask_bot(query):

# #     try:

# #         # =====================================
# #         # Retrieve Similar Documents
# #         # =====================================

# #         docs = vectorstore.similarity_search(
# #             query,
# #             k=10
# #         )

# #         if not docs:
# #             return (
# #                 "I could not find relevant information "
# #                 "in the BCET knowledge base."
# #             )

# #         # =====================================
# #         # Build Context
# #         # =====================================

# #         context = "\n\n".join(
# #             doc.page_content
# #             for doc in docs
# #         )

# #         # =====================================
# #         # Collect Sources
# #         # =====================================

# #         sources = sorted(
# #             list(
# #                 set(
# #                     doc.metadata.get(
# #                         "source",
# #                         "Unknown"
# #                     )
# #                     for doc in docs
# #                 )
# #             )
# #         )

# #         # =====================================
# #         # Prompt
# #         # =====================================

# #         prompt = f"""
# # You are BCET Assistant.

# # You help students, parents,
# # faculty members and visitors.

# # Use ONLY the provided context.

# # RULES:

# # 1. Answer only from the context.
# # 2. Never invent information.
# # 3. If the answer is not available, reply:

# # "I could not find that information in the BCET documents."

# # 4. Use bullet points whenever possible.
# # 5. Keep answers concise and professional.
# # 6. If asked about:
# #    - Admissions
# #    - Departments
# #    - Placements
# #    - Hostel
# #    - Committees
# #    - Faculty
# #    - Fees
# #    - Facilities

# #    answer only from the retrieved context.

# # CONTEXT:
# # {context}

# # QUESTION:
# # {query}
# # """

# #         # =====================================
# #         # Gemini Response
# #         # =====================================

# #         response = llm.invoke(prompt)

# #         # =====================================
# #         # Extract Text
# #         # =====================================

# #         if isinstance(response.content, str):

# #             answer = response.content

# #         elif isinstance(response.content, list):

# #             answer = ""

# #             for item in response.content:

# #                 if isinstance(item, dict):

# #                     answer += item.get(
# #                         "text",
# #                         ""
# #                     )

# #                 else:

# #                     answer += str(item)

# #         else:

# #             answer = str(
# #                 response.content
# #             )

# #         # =====================================
# #         # Add Sources
# #         # =====================================

# #         answer += "\n\n### Sources\n"

# #         for source in sources:

# #             answer += f"- {source}\n"

# #         return answer

# #     except Exception as e:

# #         return f"""
# # ❌ Error

# # {str(e)}

# # Possible Reasons:

# # • Invalid Gemini API Key

# # • Internet Connection Issue

# # • Missing Vector Store

# # • Gemini Service Unavailable

# # • Incorrect .env Configuration
# # """


# #----------------------------from dotenv import load_dotenv
# from dotenv import load_dotenv
# import os

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings

# # =====================================
# # Load Environment Variables
# # =====================================

# load_dotenv(override=True)

# api_key = os.getenv("GOOGLE_API_KEY")

# print("\n" + "=" * 50)
# print("API KEY FOUND:", api_key is not None)

# if api_key:
#     print("API KEY STARTS WITH:", api_key[:10] + "...")
# else:
#     print("GOOGLE_API_KEY NOT FOUND")

# print("=" * 50 + "\n")

# # =====================================
# # Validate API Key
# # =====================================

# if not api_key:
#     raise ValueError(
#         "GOOGLE_API_KEY not found in .env file"
#     )

# # =====================================
# # Load Embedding Model
# # =====================================

# print("Loading Embedding Model...")

# embeddings = HuggingFaceEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )

# # =====================================
# # Load Vector Store
# # =====================================

# print("Loading Vector Store...")

# vectorstore = FAISS.load_local(
#     "vectorstore",
#     embeddings,
#     allow_dangerous_deserialization=True
# )

# print("Vector Store Loaded Successfully")

# # =====================================
# # Gemini Model
# # =====================================

# print("Loading Gemini Model...")

# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite",
#     google_api_key=api_key,
#     temperature=0.2
# )

# print("Gemini Ready")

# # =====================================
# # Chat Function
# # =====================================

# def ask_bot(
#     query,
#     chat_history=None
# ):

#     try:

#         # =====================================
#         # Greeting Handler
#         # =====================================

#         query_lower = query.lower().strip()

#         greetings = [
#             "hi",
#             "hello",
#             "hey",
#             "good morning",
#             "good afternoon",
#             "good evening"
#         ]

#         if query_lower in greetings:

#             return """
# 👋 Hello!

# I am the BCET AI Assistant.

# You can ask me about:

# • Admissions

# • Departments

# • Faculty Members

# • Placements

# • Hostel Facilities

# • Fees

# • Committees

# • College Information

# • Contact Details
# """

#         # =====================================
#         # Retrieve Relevant Documents
#         # =====================================

#         docs = vectorstore.max_marginal_relevance_search(
#             query,
#             k=10,
#             fetch_k=50
#         )

#         if not docs:

#             return (
#                 "I could not find relevant information "
#                 "in the BCET knowledge base."
#             )

#         # =====================================
#         # Build Context
#         # =====================================

#         context = "\n\n".join(

#             doc.page_content[:1000]

#             for doc in docs
#         )

#         # =====================================
#         # Collect Sources
#         # =====================================

#         sources = sorted(

#             list(

#                 set(

#                     doc.metadata.get(
#                         "source",
#                         "Unknown"
#                     )

#                     for doc in docs
#                 )
#             )
#         )

#         # =====================================
#         # Prompt
#         # =====================================

#         prompt = f"""
# You are BCET Assistant.

# You help students, parents,
# faculty members and visitors.

# Use ONLY the provided context.

# RULES:

# 1. Answer only from the context.

# 2. Never invent information.

# 3. If the answer is not available,
# reply exactly:

# "I could not find that information in the BCET documents."

# 4. Use bullet points whenever possible.

# 5. Keep answers concise and professional.

# 6. If asked about:

# - Admissions
# - Departments
# - Placements
# - Hostel
# - Committees
# - Faculty
# - Fees
# - Facilities
# - Principal
# - Director
# - Chairman
# - Contact Information

# answer only from the retrieved context.

# CONTEXT:
# {context}

# QUESTION:
# {query}
# """

#         # =====================================
#         # Gemini Response
#         # =====================================

#         response = llm.invoke(
#             prompt
#         )

#         # =====================================
#         # Extract Response Text
#         # =====================================

#         if isinstance(
#             response.content,
#             str
#         ):

#             answer = response.content

#         elif isinstance(
#             response.content,
#             list
#         ):

#             answer = ""

#             for item in response.content:

#                 if isinstance(
#                     item,
#                     dict
#                 ):

#                     answer += item.get(
#                         "text",
#                         ""
#                     )

#                 else:

#                     answer += str(item)

#         else:

#             answer = str(
#                 response.content
#             )

#         # =====================================
#         # Add Sources
#         # =====================================

#         if sources:

#             answer += "\n\n### Sources\n"

#             for source in sources[:5]:

#                 answer += f"• {source}\n"

#         return answer

#     except Exception as e:

#         return f"""
# ❌ Error

# {str(e)}

# Possible Reasons:

# • Invalid Gemini API Key

# • Internet Connection Issue

# • Missing Vector Store

# • Gemini Service Unavailable

# • Incorrect .env Configuration
# """

#--------------------------------------
# from dotenv import load_dotenv
# import os

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# import os

# os.environ["TOKENIZERS_PARALLELISM"] = "false"

# # =====================================
# # Load Environment Variables
# # =====================================

# load_dotenv(override=True)

# api_key = os.getenv("GOOGLE_API_KEY")

# print("\n" + "=" * 50)
# print("API KEY FOUND:", api_key is not None)

# if api_key:
#     print("API KEY STARTS WITH:", api_key[:10] + "...")
# else:
#     print("GOOGLE_API_KEY NOT FOUND")

# print("=" * 50 + "\n")

# # =====================================
# # Validate API Key
# # =====================================

# if not api_key:
#     raise ValueError(
#         "GOOGLE_API_KEY not found in .env file"
#     )

# # =====================================
# # Load Embedding Model
# # =====================================

# print("Loading Embedding Model...")

# embeddings = HuggingFaceEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )

# # =====================================
# # Load Vector Store
# # =====================================

# print("Loading Vector Store...")

# vectorstore = FAISS.load_local(
#     "vectorstore",
#     embeddings,
#     allow_dangerous_deserialization=True
# )

# print("Vector Store Loaded Successfully")

# # =====================================
# # Gemini Model
# # =====================================

# print("Loading Gemini Model...")

# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite",
#     google_api_key=api_key,
#     temperature=0.2
# )

# print("Gemini Ready")

# # =====================================
# # Chat Function
# # =====================================

# def ask_bot(
#     query,
#     chat_history=None
# ):

#     try:

#         # =====================================
#         # Greeting Handler
#         # =====================================

#         query_lower = query.lower().strip()

#         greetings = [
#             "hi",
#             "hello",
#             "hey",
#             "good morning",
#             "good afternoon",
#             "good evening"
#         ]

#         if query_lower in greetings:

#             return """
# 👋 Hello!

# I am the BCET AI Assistant.

# You can ask me about:

# • Admissions
# • Departments
# • Faculty Members
# • Placements
# • Hostel Facilities
# • Fees
# • Committees
# • College Information
# • Contact Details
# """

#         # =====================================
#         # Retrieve Documents
#         # =====================================

#         docs = vectorstore.max_marginal_relevance_search(
#             query,
#             k=10,
#             fetch_k=50
#         )

#         if not docs:

#             return (
#                 "I could not find relevant information "
#                 "in the BCET knowledge base."
#             )

#         # =====================================
#         # Build Context
#         # =====================================

#         context = "\n\n".join(

#             doc.page_content[:1000]

#             for doc in docs
#         )

#         # =====================================
#         # Conversation Memory
#         # =====================================

#         history_text = ""

#         if chat_history:

#             history_text = "\n".join(

#                 [
#                     f"{role}: {message}"
#                     for role, message
#                     in chat_history[-6:]
#                 ]

#             )

#         # =====================================
#         # Collect Sources
#         # =====================================

#         sources = sorted(

#             list(

#                 set(

#                     doc.metadata.get(
#                         "source",
#                         "Unknown"
#                     )

#                     for doc in docs

#                 )

#             )

#         )

#         # =====================================
#         # Prompt
#         # =====================================

#         prompt = f"""
# You are BCET Assistant.

# You help students, parents,
# faculty members and visitors.

# Use ONLY the provided context.

# RULES:

# 1. Answer only from the context.

# 2. Never invent information.

# 3. If the answer is not available,
# reply exactly:

# "I could not find that information in the BCET documents."

# 4. Use bullet points whenever possible.

# 5. Keep answers concise and professional.

# 6. If asked about:

# - Admissions
# - Departments
# - Placements
# - Hostel
# - Committees
# - Faculty
# - Fees
# - Facilities
# - Principal
# - Director
# - Chairman
# - Contact Information

# answer only from the retrieved context.

# CONVERSATION HISTORY:
# {history_text}

# CONTEXT:
# {context}

# CURRENT QUESTION:
# {query}
# """

#         # =====================================
#         # Gemini Response
#         # =====================================

#         response = llm.invoke(
#             prompt
#         )

#         # =====================================
#         # Extract Text
#         # =====================================

#         if isinstance(
#             response.content,
#             str
#         ):

#             answer = response.content

#         elif isinstance(
#             response.content,
#             list
#         ):

#             answer = ""

#             for item in response.content:

#                 if isinstance(
#                     item,
#                     dict
#                 ):

#                     answer += item.get(
#                         "text",
#                         ""
#                     )

#                 else:

#                     answer += str(item)

#         else:

#             answer = str(
#                 response.content
#             )

#         # =====================================
#         # Add Sources
#         # =====================================

#         if sources:

#             answer += "\n\n### Sources\n"

#             for source in sources[:5]:

#                 answer += f"• {source}\n"

#         return answer

#     except Exception as e:

#         return f"""
# ❌ Error

# {str(e)}

# Possible Reasons:

# • Invalid Gemini API Key

# • Internet Connection Issue

# • Missing Vector Store

# • Gemini Service Unavailable

# • Incorrect .env Configuration
# """



##################################
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

from chatbot import ask_bot

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="BCET AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# FORCE LIGHT THEME LOOK
# ======================================

st.markdown(
    """
<style>

/* ======================================
GLOBAL APP
====================================== */

.stApp{
    background: linear-gradient(
        135deg,
        #f4f7fb 0%,
        #dfe9f3 100%
    );
}

/* ======================================
SIDEBAR
====================================== */

/* ======================================
SIDEBAR
====================================== */

section[data-testid="stSidebar"]{

    background: linear-gradient(
        180deg,
        #003366 0%,
        #004080 100%
    ) !important;

    min-width: 320px !important;
}

/* Sidebar Content */

section[data-testid="stSidebar"] .block-container{

    padding-top: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Sidebar Text */

section[data-testid="stSidebar"] *{

    color: white !important;
}

/* Sidebar Button */

section[data-testid="stSidebar"] button{

    background: linear-gradient(
        90deg,
        #ff4b4b,
        #d90429
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;
}

/* ======================================
HEADER
====================================== */

.main-header{

    background: linear-gradient(
        135deg,
        #003b7a 0%,
        #0059b3 50%,
        #0073e6 100%
    );

    padding: 45px 30px;

    border-radius: 28px;

    text-align: center;

    color: white;

    position: relative;

    overflow: hidden;

    box-shadow:
        0px 10px 30px rgba(0,0,0,0.18),
        inset 0px 1px 1px rgba(255,255,255,0.15);

    margin-bottom: 28px;

    border: 1px solid rgba(255,255,255,0.12);
}

/* Glass overlay */

.main-header::before{

    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    background: linear-gradient(
        120deg,
        rgba(255,255,255,0.12),
        rgba(255,255,255,0.02)
    );

    z-index: 1;
}

/* Header Content */

.header-content{

    position: relative;

    z-index: 2;
}

/* Main Title */

.header-title{

    font-size: 62px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 10px;

    color: white !important;

    text-shadow:
        0px 4px 12px rgba(0,0,0,0.25);
}

/* Subtitle */

.header-subtitle{

    font-size: 24px;

    font-weight: 500;

    color: rgba(255,255,255,0.92) !important;

    margin-top: 10px;
}

/* Floating Glow Effect */

.main-header::after{

    content: "";

    position: absolute;

    width: 250px;
    height: 250px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;

    top: -80px;
    right: -60px;

    filter: blur(10px);
}

/* ======================================
INFO CARDS
====================================== */

.info-card{
    background: rgba(255,255,255,0.95);

    padding: 20px;

    border-radius: 18px;

    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);

    transition: 0.3s;

    min-height: 150px;
}

.info-card:hover{
    transform: translateY(-5px);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
}

/* ======================================
CHAT MESSAGES
====================================== */

[data-testid="stChatMessage"]{
    background: rgba(255,255,255,0.9);

    border-radius: 18px;

    padding: 12px;

    margin-bottom: 12px;

    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

/* ======================================
CHAT INPUT
====================================== */

[data-testid="stChatInput"]{
    background: white;

    border-radius: 15px;

    padding: 8px;

    border: 1px solid #d1d5db;

    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

/* ======================================
CLEAR CHAT BUTTON
====================================== */

div.stButton > button{
    background: linear-gradient(
        90deg,
        #ff4b4b,
        #d90429
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 12px !important;

    font-weight: bold !important;

    width: 100% !important;

    transition: 0.3s !important;

    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}

div.stButton > button:hover{
    transform: scale(1.03);
    background: linear-gradient(
        90deg,
        #ff1e1e,
        #b3001b
    ) !important;
}

/* ======================================
TEXT COLORS
====================================== */
/* ======================================
TEXT COLORS
====================================== */

/* Normal Text */

body{
    color: #1f2937;
}

/* KEEP HEADER TEXT WHITE */

.main-header h1{
    color: white !important;
}

.main-header p{
    color: rgba(255,255,255,0.95) !important;
}

/* ======================================
HIDE STREAMLIT BRANDING
====================================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

}
/* FORCE SIDEBAR OPEN */

section[data-testid="stSidebar"]{
    display: block !important;
    visibility: visible !important;
    width: 320px !important;
    min-width: 320px !important;
}

/* Main content spacing */

.main .block-container{
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Remove collapsed sidebar */

button[kind="header"]{
    display: none !important;
}

</style>
""",
    unsafe_allow_html=True
)

# ======================================
# SIDEBAR
# ======================================

with st.sidebar:

    st.image(
        "assets/bcet_logo.png",
        width=120
    )

    st.markdown(
        """
# 🎓 BCET Assistant
"""
    )

    st.markdown(
        """
### Ask About

✅ Admissions

✅ Departments

✅ Faculty

✅ Placements

✅ Hostel

✅ Facilities

✅ Committees

✅ Contact Information
"""
    )

    st.markdown("---")

    if st.button(
        "🗑️ Clear Chat History",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.chat_history = []

        st.rerun()

# ======================================
# HEADER
# ======================================

st.markdown(
    """
<div class="main-header">

<h1>🎓 BCET AI Assistant</h1>

<p>
Balasore College of Engineering and Technology
</p>

</div>
""",
    unsafe_allow_html=True
)

# ======================================
# INFO CARDS
# ======================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
<div class="info-card">

<h3>🏫 College Info</h3>

<p>
Ask about departments,
faculty and facilities.
</p>

</div>
""",
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
<div class="info-card">

<h3>📄 Documents</h3>

<p>
Search PDF notices,
prospectus and reports.
</p>

</div>
""",
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
<div class="info-card">

<h3>🤖 AI Powered</h3>

<p>
Powered by Gemini,
LangChain and FAISS.
</p>

</div>
""",
        unsafe_allow_html=True
    )

st.write("")

# ======================================
# SESSION STATE
# ======================================

if "messages" not in st.session_state:

    st.session_state.messages = []

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# ======================================
# DISPLAY CHAT
# ======================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ======================================
# CHAT INPUT
# ======================================

query = st.chat_input(
    "Ask anything about BCET..."
)

# ======================================
# PROCESS QUERY
# ======================================

if query:

    # -----------------------------
    # USER MESSAGE
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):

        st.markdown(query)

    # -----------------------------
    # ASSISTANT RESPONSE
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching BCET Knowledge Base..."
        ):

            answer = ask_bot(
                query,
                st.session_state.chat_history
            )

            st.markdown(answer)

    # -----------------------------
    # SAVE RESPONSE
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # -----------------------------
    # MEMORY
    # -----------------------------

    st.session_state.chat_history.append(
        (
            "User",
            query
        )
    )

    st.session_state.chat_history.append(
        (
            "Assistant",
            answer
        )
    )
