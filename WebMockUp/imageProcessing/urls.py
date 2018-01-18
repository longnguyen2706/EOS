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
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_image, name='upload'),
    url(r'^base64/$', views.show_base64, name='show_base64'),
    url(r'^library/$', views.library_page, name='library'),
    url(r'^modal-show-crystal/(?P<mask_id>[0-9]+)/$', views.modal_show_crystal, name='modal-show-crystal'),
    url(r'^download-crystal/(?P<mask_id>[0-9]+)/$', views.download_crystal, name='download-crystal'),

    url(r'^processing_page/(?P<image_id>[0-9]+)/$', views.processing_page, name='processing_page'),
    # url(r'^upload/$', ImageProcessingView.as_view()),
    url(r'^lower-thresholding/(?P<temp_idx>[0-9]+)/$', views.lower_thresholding, name='lower-thesholding'),
    url(r'^upper-thresholding/(?P<temp_idx>[0-9]+)/$', views.upper_thresholding, name='upper-thesholding'),
    url(r'^kmeans/(?P<temp_idx>[0-9]+)/$', views.kmeans, name='kmeans'),
    url(r'^laplacian/(?P<temp_idx>[0-9]+)/$', views.laplacian, name='laplacian'),
    url(r'^undo/(?P<temp_idx>[0-9]+)/$', views.undo_last_step, name="undo"),
    url(r'^fill-holes/(?P<temp_idx>[0-9]+)/$', views.fill_holes, name="fill-holes"),

    url(r'^extract-crystal-mask/(?P<temp_idx>[0-9]+)/$', views.extract_crystal_mask, name="extract-crystal-mask"),
    url(r'^all-crystal/(?P<temp_idx>[0-9]+)/$', views.show_all_crystal, name='show-all-crystal'),
    url(r'^top-crystal/(?P<temp_idx>[0-9]+)/$', views.show_top_area_crystal, name='show-max-area-crystal'),
    url(r'^reset/(?P<temp_idx>[0-9]+)/$', views.reset, name="reset"),
    url(r'^img-from-thumbnail/(?P<temp_idx>[0-9]+)/$', views.set_image_from_thumbnail, name="img-from-thumbnail"),
    url(r'^histogram/(?P<temp_idx>[0-9]+)/$', views.plot_histogram, name="plot-histogram"),
    url(r'^opening/(?P<temp_idx>[0-9]+)/$', views.do_opening, name='opening'),
    url(r'^closing/(?P<temp_idx>[0-9]+)/$', views.do_closing, name='closing'),
    url(r'^erosion/(?P<temp_idx>[0-9]+)/$', views.do_erosion, name='erosion'),
    url(r'^dilation/(?P<temp_idx>[0-9]+)/$', views.do_opening, name='dilation'),
    url(r'^update-mask/(?P<temp_idx>[0-9]+)/$', views.update_mask, name='update-mask'),
    url(r'^noise-removal/(?P<temp_idx>[0-9]+)/$', views.noise_removal, name='noise-removal'),
    url(r'^save-processed/(?P<temp_idx>[0-9]+)/$', views.save_processed, name='save-processed'),
    url(r'^delete-image/(?P<image_id>[0-9]+)/$', views.delete_image, name='delete-image'),



]
