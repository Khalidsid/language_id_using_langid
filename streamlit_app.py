# Import necessary libraries
import langid
import streamlit as st

# Function to detect language
def detect_language(text):
    lang, _ = langid.classify(text)
    return lang

# Streamlit app
def main():
    # Set page title
    st.title("Language Detection App")

    # Get input text from user
    input_text = st.text_area("Enter text:", "Type or paste your text here...")

    # Detect language on button click
    if st.button("Detect Language"):
        # Check if input text is not empty
        if input_text.strip():
            # Perform language detection
            language = detect_language(input_text)
            st.success(f"The language detected is: {language}")
        else:
            st.warning("Please enter some text for language detection.")

# Run the app
if __name__ == "__main__":
    main()
