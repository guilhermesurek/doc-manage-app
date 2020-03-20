import os
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = os.environ['AZURESTORAGEACCOUNT']
    account_key = os.environ['AZURESTORAGEKEY']
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.environ['AZURESTORAGEACCOUNT']
    account_key = os.environ['AZURESTORAGEKEY']
    azure_container = 'static'
    expiration_secs = None