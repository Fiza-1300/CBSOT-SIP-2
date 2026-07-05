#  AI Research Paper Recommendation System

An AI-powered Research Paper Recommendation System that helps researchers and students quickly discover relevant research papers using semantic search instead of traditional keyword search.

The system retrieves the most relevant papers, generates concise summaries, extracts important keywords, and creates an AI-generated research profile for every recommended paper.

---

##  Features

✅ Semantic Search using Sentence Transformers

✅ Fast similarity search using FAISS

✅ Automatic paper summarization using BART

✅ Keyword extraction using KeyBERT

✅ AI-generated Research Paper Profile using Groq LLaMA 3.3

✅ Displays

- Match Score
- Paper Title
- Abstract Preview
- Summary
- Keywords
- Research Area
- Method Used
- Dataset
- Task
- Contribution
- Difficulty Level
- Best For
- Estimated Reading Time

---

##  Project Pipeline

User Query
↓

Sentence Transformer Embedding

↓

FAISS Similarity Search

↓

Top-K Relevant Research Papers

↓

BART Summarization

↓

KeyBERT Keyword Extraction

↓

Groq LLaMA Paper Profiling

↓

Final AI Recommendation Report

---

##  Tech Stack

### Programming Language

- Python

### NLP Models

- Sentence Transformers (all-MiniLM-L6-v2)
- Facebook BART Large CNN
- KeyBERT
- Groq LLaMA 3.3 70B

### Libraries

- FAISS
- Transformers
- Sentence Transformers
- KeyBERT
- Pandas
- NumPy
- Scikit-learn
- Datasets

---

##  Dataset

Dataset used:

**ML-ArXiv Papers Dataset**

- Source: HuggingFace
- Contains thousands of Machine Learning research papers.

---

##  Installation

```bash
git clone https://github.com/yourusername/AI-Research-Paper-Recommendation-System.git

cd AI-Research-Paper-Recommendation-System

pip install -r requirements.txt
```

---

##  Run

```python
search_and_summarize(
    "Deep learning in medical imaging",
    k=2
)
```

---

##  Sample Output

The system returns:

- Research paper title
- Match score
- Abstract preview
- AI summary
- Extracted keywords
- Research paper profile
- Reading difficulty
- Estimated reading time

---

##  Example

**Query**

```
Deep learning in medical imaging
```

The system recommends the most relevant papers along with their AI-generated summaries and detailed research profiles.

---

##  Project Structure

```
AI-Research-Paper-Recommendation-System/

│── notebooks/
│── paper_embeddings.npy
│── paper_faiss.index
│── requirements.txt
│── README.md
│── main.py
```

---

##  Future Improvements

- Streamlit Web Application
- PDF Upload Support
- Research Paper Chatbot
- Citation Generation
- Download Summary as PDF
- Multi-language Support

---

##  Author

Fiza Khatoon

Machine Learning & NLP Enthusiast
