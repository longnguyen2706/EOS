from django.conf.urls import url
from imageProcessing import views

app_name = 'imageProcessing'
urlpatterns = [
    # show ,
    # url(r'^showImage/(?P<image_id>[0-9]+)/$', views.showImage, name='showImage'),
    # url(r'^masking/$', views.masking, name='masking'),
    # url(r'^dilating/$', views.dilating, name='dilating'),
    # url(r'^pengzhang/$', views.pengzhang, name='pengzhang'),
    # url(r'^windowing/$', views.windowing, name='windowing'),
    # url(r'^ostu/$', views.ostu, name='ostu'),
    # url(r'^your_name/$', views.get_name, name ='get_name'),
    # url(r'^post/new/$', views.post_new, name ='post_new'),
    # url(r'^success/$', views.success_message, name='success_message'),
    url(r'^base64/$', views.show_base64, name='show_base64'),
    url(r'^upload/$', views.model_form_upload, name='upload'),
    url(r'^upload/lower-thresholding/$', views.lower_thresholding, name='lower-thesholding'),
    url(r'^upload/upper-thresholding/$', views.upper_thresholding, name='upper-thesholding'),
    url(r'^upload/kmeans/$', views.kmeans, name='kmeans'),
    url(r'^laplacian/$', views.laplacian, name='laplacian'),
    url(r'^undo/$', views.undo_last_step, name="undo"),
    url(r'^upload/extract-crystal-mask/$', views.extract_crystal_mask, name="extract-crystal-mask"),
    url(r'^upload/all-crystal/$', views.show_all_crystal, name='show-all-crystal'),
    url(r'^upload/max-crystal/$', views.show_max_area_crystal, name='show-max-area-crystal'),
    url(r'^reset/$', views.reset, name="reset"),
    url(r'^upload/img-from-thumbnail/$', views.set_image_from_thumbnail, name="img-from-thumbnail"),
    url(r'^histogram/$', views.plot_histogram, name="plot-histogram"),
    url(r'^upload/opening/$', views.do_opening, name='opening'),
    url(r'^upload/closing/$', views.do_closing, name='closing'),
    url(r'^upload/erosion/$', views.do_erosion, name='erosion'),
    url(r'^upload/dilation/$', views.do_opening, name='dilation'),
]
