def dummy_config(conf_id):
    config_data=[
        {
            "id": 0,
            "tajuk": "Dokumen",
            "app_name": "dokumen",
            "model_name": "Dokumen",
            "header_display": "dokumen/partials/dokumen_header_listAll.html",
            "data_fields": "dokumen/partials/dokumen_data_listAll.html",
            "data_addNew": "dokumen/partials/dokumen_data_addNew.html",
            # "template_folder": "dokumen/partials/",
            "actions": True,
            "to_view": "dokumen/partials/details_view.html",
            "to_edit": "dokumen/partials/edit_details.html",
            "to_delete": True,
        },{
            "id": 1,
            "tajuk": "Tugasan",
            "app_name": "tugasan",
            "model_name": "Tugasan",
            "header_display": "tugasan/partials/tugasan_header_listAll.html",
            "data_fields": "tugasan/partials/tugasan_data_listAll.html",
            "data_addNew": "tugasan/partials/tugasan_data_addNew.html",
            # "template_folder": "dokumen/partials/dokumen/partials/",
            "actions": True,
            "to_view": "tugasan/partials/details_view.html",
            "to_edit": "tugasan/partials/edit_details.html",
            "to_delete": True,
        },

    ]

    return config_data[conf_id]
