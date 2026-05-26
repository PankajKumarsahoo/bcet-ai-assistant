# import json

# from langchain_core.documents import Document

# from langchain_text_splitters import (
#     RecursiveCharacterTextSplitter
# )

# from langchain_huggingface import (
#     HuggingFaceEmbeddings
# )

# from langchain_community.vectorstores import (
#     FAISS
# )

# documents = []

# # =====================================
# # Load Website Data
# # =====================================

# print("\nLoading Website Data...")

# with open(
#     "data/website_data.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     website_data = json.load(f)

# for page in website_data:

#     content = page.get(
#         "content",
#         ""
#     ).strip()

#     if len(content) > 50:

#         documents.append(

#             Document(

#                 page_content=content,

#                 metadata={
#                     "source": page.get(
#                         "url",
#                         "Unknown"
#                     ),
#                     "type": "website"
#                 }
#             )

#         )

# print(
#     f"Website Documents: {len(documents)}"
# )

# # =====================================
# # Load PDF Data
# # =====================================

# print("\nLoading PDF Data...")

# with open(
#     "data/pdf_data.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     pdf_data = json.load(f)

# pdf_count = 0

# for pdf in pdf_data:

#     content = pdf.get(
#         "content",
#         ""
#     ).strip()

#     if len(content) > 50:

#         documents.append(

#             Document(

#                 page_content=content,

#                 metadata={
#                     "source": pdf.get(
#                         "source",
#                         "Unknown PDF"
#                     ),
#                     "type": "pdf"
#                 }
#             )

#         )

#         pdf_count += 1

# print(
#     f"PDF Documents: {pdf_count}"
# )

# print(
#     f"\nTotal Documents Loaded: {len(documents)}"
# )

# # =====================================
# # Chunking
# # =====================================

# print(
#     "\nCreating Chunks..."
# )

# splitter = RecursiveCharacterTextSplitter(

#     chunk_size=500,

#     chunk_overlap=100,

#     separators=[
#         "\n\n",
#         "\n",
#         ".",
#         " ",
#         ""
#     ]
# )

# chunks = splitter.split_documents(
#     documents
# )

# print(
#     f"Total Chunks Created: {len(chunks)}"
# )

# # =====================================
# # Embeddings
# # =====================================

# print(
#     "\nLoading Embedding Model..."
# )

# embeddings = HuggingFaceEmbeddings(

#     model_name="all-MiniLM-L6-v2"
# )

# # =====================================
# # Create FAISS Vector Store
# # =====================================

# print(
#     "\nCreating FAISS Vector Store..."
# )

# vectorstore = FAISS.from_documents(

#     chunks,

#     embeddings
# )

# # =====================================
# # Save Vector Store
# # =====================================

# vectorstore.save_local(
#     "vectorstore"
# )

# print(
#     "\n✅ Vector Store Created Successfully"
# )

# print(
#     "📁 Saved inside: vectorstore/"
# )

###---------------------------------------

import json

from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

# =====================================
# Documents List
# =====================================

documents = []

# =====================================
# Load Website Data
# =====================================

print("\nLoading Website Data...")

with open(
    "data/website_data.json",
    "r",
    encoding="utf-8"
) as f:

    website_data = json.load(f)

website_count = 0

for page in website_data:

    content = page.get(
        "content",
        ""
    ).strip()

    if len(content) < 100:
        continue

    title = page.get(
        "title",
        ""
    )

    url = page.get(
        "url",
        "Unknown"
    )

    documents.append(

        Document(

            page_content=content,

            metadata={
                "source": url,
                "title": title,
                "type": "website",
                "filename": url.split("/")[-1]
            }
        )
    )

    website_count += 1

print(
    f"Website Documents Loaded: {website_count}"
)

# =====================================
# Load PDF Data
# =====================================

print("\nLoading PDF Data...")

with open(
    "data/pdf_data.json",
    "r",
    encoding="utf-8"
) as f:

    pdf_data = json.load(f)

pdf_count = 0

for pdf in pdf_data:

    content = pdf.get(
        "content",
        ""
    ).strip()

    if len(content) < 100:
        print(
            f"Skipped Empty PDF: {pdf.get('source')}"
        )
        continue

    filename = pdf.get(
        "source",
        "Unknown PDF"
    )

    # =====================================
    # Keyword Boosting
    # Helps retrieval for HOD, Director,
    # Principal, Committee, Faculty etc.
    # =====================================

    boosted_content = f"""
PDF DOCUMENT

Filename: {filename}

{content}
"""

    documents.append(

        Document(

            page_content=boosted_content,

            metadata={
                "source": filename,
                "filename": filename,
                "type": "pdf"
            }
        )
    )

    pdf_count += 1

print(
    f"PDF Documents Loaded: {pdf_count}"
)

print(
    f"\nTotal Documents Loaded: {len(documents)}"
)

# =====================================
# Chunking
# =====================================

print(
    "\nCreating Chunks..."
)

splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200,

    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

chunks = splitter.split_documents(
    documents
)

print(
    f"Total Chunks Created: {len(chunks)}"
)

# =====================================
# Remove Duplicate Chunks
# =====================================

print(
    "\nRemoving Duplicate Chunks..."
)

unique_chunks = []
seen = set()

for chunk in chunks:

    text = chunk.page_content.strip()

    if text not in seen:

        seen.add(text)

        unique_chunks.append(
            chunk
        )

print(
    f"Unique Chunks: {len(unique_chunks)}"
)

# =====================================
# Embedding Model
# =====================================

print(
    "\nLoading Embedding Model..."
)

embeddings = HuggingFaceEmbeddings(

    model_name="all-MiniLM-L6-v2"
)

# =====================================
# Create FAISS
# =====================================

print(
    "\nCreating FAISS Vector Store..."
)

vectorstore = FAISS.from_documents(

    unique_chunks,

    embeddings
)

# =====================================
# Save Vector Store
# =====================================

vectorstore.save_local(
    "vectorstore"
)

print(
    "\n✅ Vector Store Created Successfully"
)

print(
    "📁 Saved inside: vectorstore/"
)