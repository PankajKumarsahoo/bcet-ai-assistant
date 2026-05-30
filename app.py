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
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# =====================================
# DISABLE TOKENIZER WARNING
# =====================================

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# =====================================
# LOAD ENV VARIABLES
# =====================================

load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")

print("\n" + "=" * 60)
print("GOOGLE API KEY FOUND:", api_key is not None)

if api_key:
    print("API KEY STARTS WITH:", api_key[:10] + "...")
else:
    print("GOOGLE_API_KEY NOT FOUND")

print("=" * 60 + "\n")

# =====================================
# VALIDATE API KEY
# =====================================

if not api_key:

    raise ValueError(
        "GOOGLE_API_KEY not found in .env file"
    )

# =====================================
# LOAD EMBEDDING MODEL
# =====================================

print("Loading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")

# =====================================
# LOAD VECTOR STORE
# =====================================

print("Loading FAISS Vector Store...")

vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Vector Store Loaded Successfully")

# =====================================
# LOAD GEMINI MODEL
# =====================================

print("Loading Gemini Model...")

llm = ChatGoogleGenerativeAI(

    model="gemini-3.1-flash-lite",

    google_api_key=api_key,

    temperature=0.2
)

print("Gemini Ready")

# =====================================
# GREETING FUNCTION
# =====================================

def greeting_response():

    return """
👋 Hello!

I am the BCET AI Assistant.

You can ask me about:

• Admissions  
• Departments  
• Faculty Members  
• Staff Members  
• HOD Details  
• Committees  
• IQAC  
• Hostel Facilities  
• Fees Structure  
• Placements  
• Contact Information  
• College Facilities  
• Principal / Director / Chairman  
• Department Faculty Lists  
"""

# =====================================
# MAIN CHAT FUNCTION
# =====================================

def ask_bot(
    query,
    chat_history=None
):

    try:

        # =====================================
        # CLEAN QUERY
        # =====================================

        query = query.strip()

        query_lower = query.lower()

        # =====================================
        # GREETING HANDLER
        # =====================================

        greetings = [

            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"

        ]

        if query_lower in greetings:

            return greeting_response()

        # =====================================
        # RETRIEVAL
        # =====================================

        docs = vectorstore.max_marginal_relevance_search(

            query,

            k=15,

            fetch_k=40

        )

        # =====================================
        # NO DOCUMENTS FOUND
        # =====================================

        if not docs:

            return """
I could not find relevant information
in the BCET knowledge base.
"""

        # =====================================
        # BUILD CONTEXT
        # =====================================

        context = "\n\n".join(

            [

                doc.page_content[:2000]

                for doc in docs

            ]

        )

        # =====================================
        # CHAT HISTORY
        # =====================================

        history_text = ""

        if chat_history:

            history_text = "\n".join(

                [

                    f"{role}: {message}"

                    for role, message
                    in chat_history[-8:]

                ]

            )

        # =====================================
        # SOURCES
        # =====================================

        sources = sorted(

            list(

                set(

                    [

                        doc.metadata.get(
                            "source",
                            "Unknown"
                        )

                        for doc in docs

                    ]

                )

            )

        )

        # =====================================
        # ADVANCED PROMPT
        # =====================================

        prompt = f"""
You are BCET AI Assistant.

You help students, parents,
faculty members and visitors.

You MUST answer ONLY from the
provided context.

=====================================

IMPORTANT RULES

=====================================

1. NEVER invent information.

2. If information is partially available:
- provide available information
- do NOT immediately say "not found"

3. If faculty/staff/member lists
are requested:
- combine ALL retrieved chunks
- include ALL names found
- do not stop after few names

4. If department faculty lists
are requested:
- search carefully through all context
- include faculty names,
designation and department if available

5. If exact answer unavailable:
say:
"Based on available BCET documents..."

6. If NO relevant answer exists:
reply exactly:

"I could not find that information in the BCET documents."

7. Keep answers:
- professional
- clean
- properly formatted

8. Use bullet points whenever possible.

9. For HOD / Faculty / Committee /
IQAC / Staff questions:
search very carefully in all context.

10. If multiple chunks contain
faculty names:
merge them into one final answer.

=====================================

CONVERSATION HISTORY

=====================================

{history_text}

=====================================

CONTEXT

=====================================

{context}

=====================================

CURRENT QUESTION

=====================================

{query}

=====================================

FINAL ANSWER

=====================================
"""

        # =====================================
        # GEMINI RESPONSE
        # =====================================

        response = llm.invoke(
            prompt
        )

        # =====================================
        # EXTRACT RESPONSE TEXT
        # =====================================

        if isinstance(
            response.content,
            str
        ):

            answer = response.content

        elif isinstance(
            response.content,
            list
        ):

            answer = ""

            for item in response.content:

                if isinstance(
                    item,
                    dict
                ):

                    answer += item.get(
                        "text",
                        ""
                    )

                else:

                    answer += str(item)

        else:

            answer = str(
                response.content
            )

        # =====================================
        # REMOVE DUPLICATE LINES
        # =====================================

        cleaned_lines = []

        seen = set()

        for line in answer.split("\n"):

            line_clean = line.strip()

            if (
                line_clean
                and line_clean not in seen
            ):

                seen.add(line_clean)

                cleaned_lines.append(line)

        answer = "\n".join(cleaned_lines)

        # =====================================
        # ADD SOURCES
        # =====================================
           # =====================================
        # RETURN ANSWER
        # =====================================

        return answer

    except Exception as e:

        return f"""
❌ Error

{str(e)}

Possible Reasons:

• Invalid Gemini API Key

• Internet Connection Issue

• Missing Vector Store

• Gemini Service Unavailable

• Corrupted Vector Database

• Incorrect .env Configuration
"""
