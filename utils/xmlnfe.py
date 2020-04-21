from datetime import datetime
from benedict import benedict
import xmltodict

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
    
    def get_entity_info(self, cast_dict, ent_type):
        res_dict = {}
        # Get Entity Information
        res_dict["cnpj"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "CNPJ"])
        res_dict["company_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xNome"])
        if res_dict["company_name"] != None:
            res_dict["company_name"] = res_dict["company_name"].upper()
        else:
            del res_dict["company_name"]
        res_dict["fantasy_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xFant"])
        if res_dict["fantasy_name"] != None:
            res_dict["fantasy_name"] = res_dict["fantasy_name"].upper()
        else:
            del res_dict["fantasy_name"]
        if ent_type=="entrega":
            res_dict["address_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xLgr"])
        else:
            res_dict["address_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "xLgr"])
        if res_dict["address_name"] != None:
            res_dict["address_name"] = res_dict["address_name"].upper()
        else:
            del res_dict["address_name"]
        if ent_type=="entrega":
            res_dict["address_number"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "nro"])
        else:
            res_dict["address_number"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "nro"])
        if ent_type=="entrega":
            res_dict["neighborhood"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xBairro"])
        else:
            res_dict["neighborhood"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "xBairro"])
        if res_dict["neighborhood"] != None:
            res_dict["neighborhood"] = res_dict["neighborhood"].upper()
        else:
            del res_dict["neighborhood"]
        if ent_type=="entrega":
            res_dict["city_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "cMun"])
        else:
            res_dict["city_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "cMun"])
        if ent_type=="entrega":
            res_dict["city_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xMun"])
        else:
            res_dict["city_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "xMun"])
        if res_dict["city_name"] != None:
            res_dict["city_name"] = res_dict["city_name"].upper()
        else:
            del res_dict["city_name"]
        if ent_type=="entrega":
            res_dict["state_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "UF"])
        else:
            res_dict["state_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "UF"])
        if ent_type=="entrega":
            res_dict["zip_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "CEP"])
        else:
            res_dict["zip_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "CEP"])
        if ent_type=="entrega":
            res_dict["country_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "cPais"])
        else:
            res_dict["country_code"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "cPais"])
        if ent_type=="entrega":
            res_dict["country_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "xPais"])
        else:
            res_dict["country_name"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "xPais"])
        if res_dict["country_name"] != None:
            res_dict["country_name"] = res_dict["country_name"].upper()
        else:
            del res_dict["country_name"]
        if ent_type=="entrega":
            res_dict["phone_number"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "fone"])
        else:
            res_dict["phone_number"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "ender"+ent_type.capitalize(), "fone"])
        res_dict["state_registration"]  = cast_dict.get(["nfeProc", "NFe", "infNFe", ent_type, "IE"])
        return res_dict

    def extract_fields_from_dict(self):
        cast_dict = benedict(self.dict_nfe)
        versao = cast_dict['nfeProc', '@versao']
        if versao == '4.00':
            # Get Document Information
            self.document["document_number"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "ide", "nNF"])
            self.document["document_type"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "ide", "mod"])
            self.document["document_date"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "ide", "dhEmi"])
            if self.document["document_date"] != None:
                self.document["document_date"] = datetime.strptime(self.document["document_date"][:-6], '%Y-%m-%dT%H:%M:%S')
            self.document["document_key"] = cast_dict.get(["nfeProc", "protNFe", "infProt", "chNFe"])
            self.document["document_status"] = cast_dict.get(["nfeProc", "protNFe", "infProt", "cStat"])
            self.document["document_total_value"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "total", "ICMSTot", "vNF"])
            # Get Entity Information
            self.sender = self.get_entity_info(cast_dict, "emit")
            self.recipient = self.get_entity_info(cast_dict, "dest")
            self.deliver_to = self.get_entity_info(cast_dict, "entrega")
            # Get Carrier Information
            self.carrier["cnpj"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "CNPJ"])
            self.carrier["company_name"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "xNome"])
            if self.carrier["company_name"] != None:
                self.carrier["company_name"] = self.carrier["company_name"].upper()
            self.carrier["state_registration"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "IE"])
            self.carrier["address_name"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "xEnder"])
            if self.carrier["address_name"] != None:
                self.carrier["address_name"] = self.carrier["address_name"].upper()
            self.carrier["city_name"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "xMun"])
            if self.carrier["city_name"] != None:
                self.carrier["city_name"] = self.carrier["city_name"].upper()
            self.carrier["state_code"] = cast_dict.get(["nfeProc", "NFe", "infNFe", "transp", "transporta", "UF"])
        else:
            raise(f"xml version {versao} not suported yet.")