# GEN-AI-BASED-VA-FOR-DENTAL-SCIENCES 🦷🤖

A virtual assistant powered by Google's Gemini Pro for dental sciences, providing intelligent responses to dental queries using PDF-based knowledge.

## Overview
This project implements an AI-powered virtual assistant specifically designed for dental sciences. It processes dental literature in PDF format and uses Google's Generative AI to provide accurate, context-aware responses to dental queries.

## Features
- PDF document processing and text extraction
- Advanced text chunking for optimal processing
- Vector-based semantic search using FAISS
- Integration with Google's Gemini Pro AI model
- Pre-loaded FAQ system for common dental queries
- Custom query handling for specific dental questions

## Tech Stack
- Streamlit: Web interface
- LangChain: For AI chain operations
- Google Generative AI (Gemini Pro): Core AI model
- FAISS: Vector store for efficient text search
- PyPDF2: PDF processing

## Installation

```bash
# Clone the repository
git clone https://github.com/niranjan-ellur/GEN-AI-BASED-VA-FOR-DENTAL-SCIENCES.git

# Navigate to project directory
cd GEN-AI-BASED-VA-FOR-DENTAL-SCIENCES

# Install required packages
pip install -r requirements.txt
```

## Configuration
1. Create a `.env` file in the root directory
2. Add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage
1. Place your dental knowledge base PDF file as 'pdfs.pdf' in the project directory
2. Run the application:
```bash
streamlit run app.py
```

## Features in Detail
- **PDF Processing**: Extracts text from dental literature
- **Text Chunking**: Splits content into manageable segments
- **Vector Store**: Creates and manages FAISS embeddings
- **Conversational Chain**: Implements context-aware Q&A system
- **Pre-loaded FAQs**: Common dental queries ready to use

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


##Result
![image](https://github.com/user-attachments/assets/ad3a89ad-b0c7-4a8a-927e-e25a46a9dfde)




## Contact
Niranjan Ellur - [GitHub Profile](https://github.com/niranjan-ellur)

Project Link: [https://github.com/niranjan-ellur/GEN-AI-BASED-VA-FOR-DENTAL-SCIENCES](https://github.com/niranjan-ellur/GEN-AI-BASED-VA-FOR-DENTAL-SCIENCES)

## Acknowledgments
- Google Generative AI team for Gemini Pro
- LangChain community
- FAISS developers

---
⭐ Star this repository if you find it helpful!
