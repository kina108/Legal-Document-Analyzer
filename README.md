# Legal Document Analyzer

## Overview

The **Legal Document Analyzer** is a command-line tool designed to extract key legal clauses, summarize documents, and compare different versions of legal texts. This project demonstrates **Natural Language Processing (NLP)** techniques, **text similarity analysis**, and **document summarization**, making it useful for legal professionals and researchers.

## Features

- **Clause Extraction**: Identifies key legal obligations using regex-based pattern matching.
- **Document Summarization**: Ranks and extracts the most important sentences.
- **Text Similarity Analysis**: Compares two documents to determine their similarity score.
- **Command-Line Interface (CLI)**: Provides easy interaction through terminal commands.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed along with the required dependencies.

```sh
pip install -r requirements.txt
```

### Required Libraries

- `nltk`
- `scikit-learn`

## Usage

### Analyze a Legal Document

To analyze a legal document and extract key clauses and a summary:

```sh
python legal_doc_analyzer.py <path_to_document>
```

### Compare Two Documents

To compare two documents for similarities:

```sh
python legal_doc_analyzer.py <document1.txt> --compare <document2.txt>
```

### Save Analysis Output

To save the analysis results to a JSON file:

```sh
python legal_doc_analyzer.py <document.txt> --output output.json
```

## Example Output

```json
{
    "clauses": [
        "shall be responsible for...",
        "must ensure compliance with..."
    ],
    "summary": [
        "This agreement outlines the responsibilities...",
        "The party shall be liable for..."
    ],
    "similarity_score": 0.87
}
```

## Future Improvements

- Add Named Entity Recognition (NER) for identifying legal entities.
- Implement a web-based UI using Flask or FastAPI.
- Improve summarization using transformer-based NLP models.



## Author

Developed by Krishna.

