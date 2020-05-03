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

## Active Features
- Login/Logout
- Multi-file upload type xml/brazilian_NFe
- Show all uploaded files
- Single non-automatic download 

## Future Features
### Uploading Files
- Security risks from accepting uploaded content from untrusted users. See https://docs.djangoproject.com/en/3.0/topics/security/#user-uploaded-content-security
- Create a handler to do something with the file
- Create a message to send to the user saing your file has been uploaded successfully
- Set a limit of 2.5 mb per upload - FileUploadHandler.chunk_size
- Create a progress bar upload
- MemoryFileUploadHandler and TemporaryFileUploadHandler in the django.core.files.uploadhandler
- For custom upload handlers: django.core.files.uploadhandler.FileUploadHandler

### Downloading Files
- Search for files
- Select and multi-download files

### Models
- Entity Model: Update Entity info every x days
- Document Model: Update documents
- Document Model: Upload pdf files

### Test environment
- Create a test environment to test views
- Create a test environment to test database
- Create a test environment to test models

### References and Credits
- Vitor Freitas - https://github.com/sibtc/django-upload-example
- Vitor Freitas - https://simpleisbetterthancomplex.com/tutorial/2016/11/22/django-multiple-file-upload-using-ajax.html
- https://github.com/rg3915/django-datatables-experiment