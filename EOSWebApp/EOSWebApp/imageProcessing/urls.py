from django.conf.urls import url

from EOSWebApp.imageProcessing import views

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

    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_image, name='upload'),
    url(r'^base64/$', views.show_base64, name='show_base64'),
    url(r'^processing_page/(?P<image_id>[0-9]+)/$', views.processing_page, name='processing_page'),
    # url(r'^upload/$', ImageProcessingView.as_view()),
    url(r'^lower-thresholding-white/(?P<temp_idx>[0-9]+)/$', views.lower_thresholding_white, name='lower-thesholding-white'),
    url(r'^upper-thresholding-white/(?P<temp_idx>[0-9]+)/$', views.upper_thresholding_white, name='upper-thesholding-white'),
    url(r'^lower-thresholding-black/(?P<temp_idx>[0-9]+)/$', views.lower_thresholding_black, name='lower-thesholding-black'),
    url(r'^upper-thresholding-black/(?P<temp_idx>[0-9]+)/$', views.upper_thresholding_black, name='upper-thesholding-black'),
    url(r'^kmeans/(?P<temp_idx>[0-9]+)/$', views.kmeans, name='kmeans'),
    url(r'^laplacian/(?P<temp_idx>[0-9]+)/$', views.laplacian, name='laplacian'),
    url(r'^undo/(?P<temp_idx>[0-9]+)/$', views.undo_last_step, name="undo"),
    url(r'^fill-holes/(?P<temp_idx>[0-9]+)/$', views.fill_holes, name="fill-holes"),

    url(r'^extract-crystal-mask/(?P<temp_idx>[0-9]+)/$', views.extract_crystal_mask, name="extract-crystal-mask"),
    url(r'^all-crystal/(?P<temp_idx>[0-9]+)/$', views.show_all_crystal, name='show-all-crystal'),
    url(r'^top-crystal/(?P<temp_idx>[0-9]+)/$', views.show_top_area_crystal, name='show-max-area-crystal'),
    url(r'^reset/(?P<temp_idx>[0-9]+)/$', views.reset, name="reset"),
    url(r'^img-from-thumbnail/(?P<temp_idx>[0-9]+)/$', views.set_image_from_thumbnail, name="img-from-thumbnail"),

    url(r'^opening/(?P<temp_idx>[0-9]+)/$', views.do_opening, name='opening'),
    url(r'^closing/(?P<temp_idx>[0-9]+)/$', views.do_closing, name='closing'),
    url(r'^erosion/(?P<temp_idx>[0-9]+)/$', views.do_erosion, name='erosion'),
    url(r'^dilation/(?P<temp_idx>[0-9]+)/$', views.do_opening, name='dilation'),
    url(r'^morphgrad/(?P<temp_idx>[0-9]+)/$', views.do_morphgrad, name='morphgrad'),
    url(r'^tophat/(?P<temp_idx>[0-9]+)/$', views.do_tophat, name='tophat'),
    url(r'^blackhat/(?P<temp_idx>[0-9]+)/$', views.do_blackhat, name='blackhat'),

    url(r'^update-mask/(?P<temp_idx>[0-9]+)/$', views.update_mask, name='update-mask'),
    url(r'^noise-removal/(?P<temp_idx>[0-9]+)/$', views.noise_removal, name='noise-removal'),
    url(r'^save-processed/(?P<temp_idx>[0-9]+)/$', views.save_processed, name='save-processed'),
    url(r'^delete-image/(?P<image_id>[0-9]+)/$', views.delete_image, name='delete-image'),

    url(r'^fourier/(?P<temp_idx>[0-9]+)/$', views.do_fourier, name='fourier'),
    url(r'^backproj/(?P<temp_idx>[0-9]+)/$', views.do_backproj, name='backproj'),
    url(r'^large-thumbnail/(?P<thumbnail_id>[0-9]+)/$', views.large_thumbnail, name='large-thumbnail')
]
