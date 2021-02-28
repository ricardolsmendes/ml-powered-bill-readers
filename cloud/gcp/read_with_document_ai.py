import sys

from google.cloud import documentai


def _read_bill(project_id: str, location: str, processor_id: str, file_path: str):
    client = documentai.DocumentProcessorServiceClient()

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id.
    # Processors must be created in the Cloud Console first.
    name = f'projects/{project_id}/locations/{location}/processors/{processor_id}'

    # Read the file into memory
    with open(file_path, 'rb') as pdf:
        pdf_content = pdf.read()

    # Configure the process request
    request = {'name': name, 'document': {'content': pdf_content, 'mime_type': 'application/pdf'}}

    result = client.process_document(request=request)

    document = result.document
    document_pages = document.pages

    # Read the text recognition output from the processor
    print('The document contains the following entities:')
    for entity in document.entities:
        print(entity)

    print('The document contains the following paragraphs:')
    for page in document_pages:
        paragraphs = page.paragraphs
        for paragraph in paragraphs:
            print(paragraph)
            paragraph_text = _get_text(paragraph.layout, document)
            print(f'Paragraph text: {paragraph_text}')


def _get_text(doc_element: dict, document: dict):
    """
    Document AI identifies form fields by their offsets in document text. This function converts
    offsets to text snippets.
    """
    response = ''

    # If a text segment spans several lines, it will be stored in different text segments.
    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]

    return response


if __name__ == "__main__":
    argv = sys.argv
    _read_bill(argv[1], argv[2], argv[3], argv[4])
