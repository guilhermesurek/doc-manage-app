$(document).ready( function () {
    $('#docTable').DataTable({
      //"processing": true,
      //"serverSide": true,
      "ajax": "/document/json/",
      "columns": [
        {"data": "name_sender"},
        {"data": "cnpj_sender"},
        {"data": "name_recipient"},
        {"data": "cnpj_recipient"},
        {"data": "document_number"},
        {"data": "document_key"},
        {"data": "document_date"},
        {"data": "document_total_value"},
        {"data": "document_file_url"}
      ]
    });
  });