import streamlit as st

from api_handler import query
from utils import read_pdf

def streamlit_ui():
    st.title("All In One AI")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload PDF for context (Optional)", type="pdf")

    # Read PDF if uploaded
    pdf_context = ""
    if uploaded_file is not None:
        pdf_context = read_pdf(uploaded_file)
        print("PDF Context=========================================")
        print(pdf_context)

    # Text area for question input
    question_input = st.text_area("Question", "Enter your question here...")

    # Optional text area for additional context input
    additional_context_input = st.text_area("Additional Context (Optional)", "Enter any additional context here...")

    # Button to send the question (and optional context)
    if st.button("Submit"):
        if question_input.strip():
            # Combine PDF context, additional context, and question
            combined_context = f"{pdf_context} {additional_context_input}".strip()
            prompt = question_input
            if combined_context:
                prompt = f"{combined_context} Based on this, {question_input}"

            # Call your query function
            response = query(prompt)
            st.text_area("Response", response, height=300)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    streamlit_ui()