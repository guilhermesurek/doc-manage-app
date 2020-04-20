import xmltodict
from datetime import datetime

class xml_nfe:

    def __init__(self, xml_file):
        self.dict_nfe = {}
        self.sender = {}
        self.recipient = {}
        self.carrier = {}
        self.deliver_to = {}
        self.document = {}
        self.xml_parser_to_dict(xml_file)
        self.extract_fields_from_dict()

    def xml_parser_to_dict(self, xml_file):
        with open(xml_file, "rb") as xml:
            dict_nfe = xmltodict.parse(xml)
            self.dict_nfe = dict_nfe
    
    def extract_fields_from_dict(self):
        versao = self.dict_nfe["nfeProc"]["@versao"]
        if versao == '4.00':
            # Get Document Information
            self.document["document_number"] = self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["ide"]["nNF"]
            self.document["document_type"] = self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["ide"]["mod"]
            self.document["document_date"] = datetime.strptime(self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["ide"]["dhEmi"][:-6], '%Y-%m-%dT%H:%M:%S')
            self.document["document_key"] = self.dict_nfe["nfeProc"]["protNFe"]["infProt"]["chNFe"]
            self.document["document_status"] = self.dict_nfe["nfeProc"]["protNFe"]["infProt"]["cStat"]
            # Get Sender Information
            self.sender["cnpj"]  = self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["emit"]["CNPJ"]
            self.sender["company_name"]  = self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["emit"]["xNome"]
            self.sender["fantasy_name"]  = self.dict_nfe["nfeProc"]["NFe"]["infNFe"]["emit"]["xFant"]
        else:
            raise(f"xml version {versao} not suported yet.")