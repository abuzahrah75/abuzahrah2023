def dummy_config(conf_id):
    config_data=[
        {
            "id": 0,
            "app_name": "dokumen",
            "model_name": "Dokumen",
            "header_display": "dokumen/partials/dokumen_header_listAll.html",
            "data_fields": "dokumen/partials/dokumen_data_listAll.html",
            "data_addNew": "dokumen/partials/dokumen_data_addNew.html",
            "actions": True,
            "to_view": True,
            "to_edit": True,
            "to_delete": True,
        },{
            "id": 1,
            "app_name": "tugasan",
            "model_name": "Tugasan",
            "header_display": "tugasan/partials/tugasan_header_listAll.html",
            "data_fields": "tugasan/partials/tugasan_data_listAll.html",
            "data_addNew": "tugasan/partials/tugasan_data_addNew.html",
            "actions": True,
            "to_view": True,
            "to_edit": True,
            "to_delete": True,
        },

    ]

    return config_data[conf_id]