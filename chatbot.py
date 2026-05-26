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
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# =====================================
# Load Environment Variables
# =====================================

load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")

print("\n" + "=" * 50)
print("API KEY FOUND:", api_key is not None)

if api_key:
    print("API KEY STARTS WITH:", api_key[:10] + "...")
else:
    print("GOOGLE_API_KEY NOT FOUND")

print("=" * 50 + "\n")

# =====================================
# Validate API Key
# =====================================

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found in .env file"
    )

# =====================================
# Load Embedding Model
# =====================================

print("Loading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# =====================================
# Load Vector Store
# =====================================

print("Loading Vector Store...")

vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Vector Store Loaded Successfully")

# =====================================
# Gemini Model
# =====================================

print("Loading Gemini Model...")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=api_key,
    temperature=0.2
)

print("Gemini Ready")

# =====================================
# Chat Function
# =====================================

def ask_bot(
    query,
    chat_history=None
):

    try:

        # =====================================
        # Greeting Handler
        # =====================================

        query_lower = query.lower().strip()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if query_lower in greetings:

            return """
👋 Hello!

I am the BCET AI Assistant.

You can ask me about:

• Admissions
• Departments
• Faculty Members
• Placements
• Hostel Facilities
• Fees
• Committees
• College Information
• Contact Details
"""

        # =====================================
        # Retrieve Documents
        # =====================================

        docs = vectorstore.max_marginal_relevance_search(
            query,
            k=10,
            fetch_k=50
        )

        if not docs:

            return (
                "I could not find relevant information "
                "in the BCET knowledge base."
            )

        # =====================================
        # Build Context
        # =====================================

        context = "\n\n".join(

            doc.page_content[:1000]

            for doc in docs
        )

        # =====================================
        # Conversation Memory
        # =====================================

        history_text = ""

        if chat_history:

            history_text = "\n".join(

                [
                    f"{role}: {message}"
                    for role, message
                    in chat_history[-6:]
                ]

            )

        # =====================================
        # Collect Sources
        # =====================================

        sources = sorted(

            list(

                set(

                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )

                    for doc in docs

                )

            )

        )

        # =====================================
        # Prompt
        # =====================================

        prompt = f"""
You are BCET Assistant.

You help students, parents,
faculty members and visitors.

Use ONLY the provided context.

RULES:

1. Answer only from the context.

2. Never invent information.

3. If the answer is not available,
reply exactly:

"I could not find that information in the BCET documents."

4. Use bullet points whenever possible.

5. Keep answers concise and professional.

6. If asked about:

- Admissions
- Departments
- Placements
- Hostel
- Committees
- Faculty
- Fees
- Facilities
- Principal
- Director
- Chairman
- Contact Information

answer only from the retrieved context.

CONVERSATION HISTORY:
{history_text}

CONTEXT:
{context}

CURRENT QUESTION:
{query}
"""

        # =====================================
        # Gemini Response
        # =====================================

        response = llm.invoke(
            prompt
        )

        # =====================================
        # Extract Text
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
        # Add Sources
        # =====================================

        if sources:

            answer += "\n\n### Sources\n"

            for source in sources[:5]:

                answer += f"• {source}\n"

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

• Incorrect .env Configuration
"""