# Document Management Application
Python web application - Django based - to manage document files.

## Django
Documentation: https://docs.djangoproject.com/en/3.0/

## Website structure

    .
    ├── Login
    |   ├── Menu
    |   ├── Upload
    |   ├── Download
    └── Logout


## Future Features
### Uploading Files
- Security risks from accepting uploaded content from untrusted users. See https://docs.djangoproject.com/en/3.0/topics/security/#user-uploaded-content-security
- Create a form with a FileField()
- Create a view get the files from the user
- Create a handler to do something with the file
- Create a message to send to the user saing your file has been uploaded successfully
- Keep user in upload_view
- Set a limit of 2.5 mb per upload - FileUploadHandler.chunk_size
- Create a progress bar upload
- Information of the document
    - Data do Documento
    - CNPJ emissor
    - CNPJ remetente
    - Numero do documento
    - Chave do documento
- MemoryFileUploadHandler and TemporaryFileUploadHandler in the django.core.files.uploadhandler
- For custom upload handlers: django.core.files.uploadhandler.FileUploadHandler
- Use cloud services to storage uploaded files https://docs.djangoproject.com/en/3.0/ref/files/storage/

### Test environment
- Create a test environment to test interface
- Create a test environment to test database