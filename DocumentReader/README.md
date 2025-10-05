# Word Search & Summarizer MCP Server

## Overview

**Word Search & Summarizer** is a Python-based MCP server that allows you to:  

- Read the full text of Word (`.docx`) documents.  
- Search for keywords across multiple Word documents and get relevant snippets.  
- Generate summaries of entire documents or keyword search results in multiple styles (concise, detailed, bullet).  
- Provide user-friendly prompts for greetings and text summarization.  

The server is built using **FastMCP** and integrates **python-docx** for Word file processing.  

---

## Features

1. **Read Document**
   - Input: Document ID  
   - Output: Full text of the document  
   - Example: “Read the document with ID DOC001”

2. **Search Keyword**
   - Input: Keyword  
   - Output: All occurrences of the keyword across documents with context snippets  
   - Example: “Search for the word ‘project’ in all documents”

3. **Summarize Document**
   - Input: Document ID  
   - Output: Summary of the document  
   - Styles supported: `concise`, `detailed`, `bullet`  
   - Example: “Summarize the Project Proposal document in bullet points”

4. **Summarize Keyword Results**
   - Input: Keyword  
   - Output: Summary of all snippets containing the keyword  
   - Example: “Summarize all mentions of ‘proposal’ in documents”

5. **Prompts**
   - Greeting users in different styles (`friendly`, `formal`, `casual`)  
   - Summarize arbitrary text in different styles  

---

## Installation

1. Clone the repository or copy the project files.  
2. Install dependencies:  

```bash
pip install python-docx mcp
```

3. Make sure your Word documents are placed in a folder, e.g., `C:\Users\User\OneDrive\Documents\`, and the paths are updated in `mock_doc_db` in `main.py`.

---

## Usage

1. Run the MCP server:

```bash
python main.py
```

2. Example interactions via Claude Desktop or any MCP client:

- **Read document:**  
  ```
  Read the document with ID DOC001
  ```

- **Search keyword:**  
  ```
  Search for the word 'project' in all documents
  ```

- **Summarize document:**  
  ```
  Summarize the Project Proposal document in bullet points
  ```

- **Summarize keyword results:**  
  ```
  Summarize all mentions of 'proposal' in documents concisely
  ```

- **Greeting user:**  
  ```
  Greet A person in a friendly way
  ```

---

## Project Structure

```
docxReder/
│
├── main.py               # MCP server code
├── README.md             # Project documentation
├── docs/                 # Folder to store Word documents
│   ├── DOC001.docx
│   ├── DOC002.docx
│   └── ...
└── requirements.txt      # Optional: dependencies list
```

---

## Notes

- Only `.docx` files are supported.  
- Optional parameters like `style` for summaries are handled internally; you can specify style in natural language or via query if using an MCP client.  
- The server uses **mock database (`mock_doc_db`)** — update it to include real document paths.  

---

## Dependencies

- Python 3.11+  
- `mcp` (FastMCP server framework)  
- `python-docx` (for reading Word documents)  

Install dependencies via:

```bash
pip install mcp python-docx
```

---
