from django.contrib.admin import apps

class StoreAdminConfig(apps.AdminConfig):
    default_site = 'store.admin.StoreAdminSite'