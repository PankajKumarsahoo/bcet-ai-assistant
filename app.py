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
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown(
    """
<style>

/* Main Background */

.stApp{
    background: linear-gradient(
        135deg,
        #f5f7fa,
        #c3cfe2
    );
}

/* Header */

.main-header{
    background: linear-gradient(
        90deg,
        #003366,
        #00509e
    );

    padding:20px;
    border-radius:15px;

    color:white;
    text-align:center;

    box-shadow:0px 4px 15px rgba(0,0,0,0.2);
}

/* Cards */

.info-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:15px;
}

/* Chat Messages */

[data-testid="stChatMessage"]{

    border-radius:15px;

    padding:10px;

    margin-bottom:10px;

    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background-color:#003366;
    color:white;
}

/* Footer */

.footer{
    text-align:center;
    padding:15px;
    color:#555;
    font-size:14px;
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

    st.divider()

    if st.button(
        "🗑 Clear Chat",
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

st.write("")

# ======================================
# INFO CARDS
# ======================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
<div class="info-card">

<h4>🏫 College Info</h4>

Ask about departments,
faculty and facilities.

</div>
""",
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
<div class="info-card">

<h4>📄 Documents</h4>

Search PDF notices,
prospectus and reports.

</div>
""",
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
<div class="info-card">

<h4>🤖 AI Powered</h4>

Powered by Gemini,
LangChain and FAISS.

</div>
""",
        unsafe_allow_html=True
    )

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
# INPUT
# ======================================

query = st.chat_input(
    "Ask anything about BCET..."
)

# ======================================
# PROCESS QUERY
# ======================================

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):

        st.markdown(query)

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching BCET Knowledge Base..."
        ):

            answer = ask_bot(
                query,
                st.session_state.chat_history
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

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

# ======================================
# FOOTER
# ======================================

st.markdown(
    """
<hr>

<div class="footer">

BCET AI Assistant |
Built using LangChain + Gemini + FAISS + Streamlit

</div>
""",
    unsafe_allow_html=True
)