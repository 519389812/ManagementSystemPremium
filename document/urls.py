from django.urls import path, re_path
from . import views

app_name = 'document'

urlpatterns = [
    path('', views.document, name="document"),
    path('translate_words/', views.translate_words, name="translate_words"),
    path('delete_translate_words/', views.delete_translate_words, name="delete_translate_words"),
    path('error_docx_closed/', views.error_docx_closed, name="error_docx_closed"),
    path('error_docx_opened/', views.error_docx_opened, name="error_docx_opened"),
    path('error_docx_missing/', views.error_docx_missing, name="error_docx_missing"),
    path('preview_template/', views.preview_template, name="preview_template"),
    path('introduce_docx/', views.introduce_docx, name="introduce_docx"),
    path('select_template/', views.select_template, name="select_template"),
    path('view_docx_list/', views.view_docx_list, name="view_docx_list"),
    path('init_docx/', views.init_docx, name="init_docx"),
    path('upload_template/', views.upload_template, name="upload_template"),
    path('delete_template/', views.delete_template, name="delete_template"),
    path('fill_signature/', views.fill_signature, name="fill_signature"),
    path('supervisor_signature/', views.supervisor_signature, name="supervisor_signature"),
    path('supervise_docx/', views.supervise_docx, name="supervise_docx"),
    path('show_docx_html/', views.show_docx_html, name="show_docx_html"),
    path('set_signature/', views.set_signature, name="set_signature"),
    path('download_signature/', views.download_signature, name="download_signature"),
    re_path('translate_words/(.+)/$', views.translate_words, name="translate_words"),
    re_path('select_template/(.+)/$', views.select_template, name="select_template"),
    re_path('upload_template/(.+)/$', views.upload_template, name="upload_template"),
    re_path('write_init_docx/(.+)/$', views.write_init_docx, name="write_init_docx"),
    re_path('view_docx/(\d+)/$', views.view_docx, name="view_docx"),
    re_path('view_docx/(\d+)/(.+)/$', views.view_docx, name="view_docx"),
    re_path('fill_docx/(.+)/(.+)/$', views.fill_docx, name="fill_docx"),
    re_path('close_docx/(.+)/$', views.close_docx, name="close_docx"),
    re_path('download_docx/(.+)/$', views.download_docx, name="download_docx"),
]
