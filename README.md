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
- Upload multiple files
- Create a handler to do something with the file
- Create a message to send to the user saing your file has been uploaded successfully
- Set a limit of 2.5 mb per upload - FileUploadHandler.chunk_size
- Create a progress bar upload
- MemoryFileUploadHandler and TemporaryFileUploadHandler in the django.core.files.uploadhandler
- For custom upload handlers: django.core.files.uploadhandler.FileUploadHandler

### Models
- Entity Model: Update Entity info every x days
- Document Model: Upload documents
- Document Model: Update documents

### Test environment
- Create a test environment to test interface
- Create a test environment to test database
- Create a test environment to test models

### References and Credits
- Vitor Freitas - https://github.com/sibtc/django-upload-example
- Vitor Freitas - https://simpleisbetterthancomplex.com/tutorial/2016/11/22/django-multiple-file-upload-using-ajax.html