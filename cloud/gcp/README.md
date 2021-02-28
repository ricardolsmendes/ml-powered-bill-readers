# Automatic bill reading using Google Cloud AI and ML tools

The present use case consists of using Google Cloud AI and ML tools to extract as much structured
information as possible from an electricity bill issued by Cemig -- the Minas Gerais State (Brazil)
provider -- with minimum programming effort. The only input is a PDF file in the Portuguese
language.

---

## Document AI

- Official site: https://cloud.google.com/document-ai

- Script to test:
  ```shell script
  python read_with_document_ai.py <PROJECT-ID> <LOCATION-ID> <PROCESSOR-ID> <LOCAL-FILE-PATH>
  ```

### Document OCR Processor 

#### Results

- 02/27/2021

  **The good**: this processor accurately reads all information presented in the bill.

  **The bad**: results come in the format of unstructured text chunks, with almost no semantic
  grouping.

### Invoice Parser processor

#### Open questions

1. Should the **Invoice Parser** appropriately read utility bills, including line items? 
1. Or should it be under the responsibility of specialized processors since they are 
   schematized for domain-specific documents?
1. How to create and train custom/specialized processors? 

#### Results

- 02/27/2021

  **The good**: results come in the format of structured key-value pairs, with means useful
  semantic grouping.

  **The bad**: not all fields are returned, and I still didn't find a way to provide hints to the
  algorithms on the additional fields I expect. 
