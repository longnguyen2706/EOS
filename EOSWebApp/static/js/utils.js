/**************** UTIL FUNCTIONS ******************/
function do_ajax_post(e, domNameArr, inputNameArr, targetUrl, option){
    e.preventDefault();
    // var json_data ="{"+inputName+":"+ $("#"+domName+"").val()+"}";
    var json_data = {};
    for (i = 0; i < domNameArr.length; i++) {
        inputName = inputNameArr[i];
        domName = domNameArr[i];
        json_data[inputName] = $("#" + domName + "").val();
    }
    var URL = targetUrl + get_temp_index() + "/";
    $.ajax({
        url: URL,
        type: "POST",
        // data: {inputName: $("#"+domName+"").val()},
        data: json_data,

        beforeSend: function () {
            document.body.style.cursor = "wait";
        },
        complete: function () {
            document.body.style.cursor = "default";
        },

        success: function (data) {
            update_image(data);
            update_clickable(data);
            disp_hist_thumbnail(data);
            update_gray_levels(data);
        },

        error: function (data) {
            alert('error');
        }
    });
}

function do_ajax_post_val_only(valArr, inputNameArr, targetUrl, option) {
    // e.preventDefault();

    var json_data = {};
      for (i = 0; i < inputNameArr.length; i++) {
        inputName = inputNameArr[i];
        val = valArr[i];
        json_data[inputName] = val;
    }
    var URL = targetUrl + get_temp_index() + "/";

    $.ajax({
        url: URL,
        type: "POST",
        data: json_data,

        beforeSend: function () {
            document.body.style.cursor = "wait";
        },
        complete: function () {
            document.body.style.cursor = "default";
        },

        success: function (data) {
            update_image(data);
            update_clickable(data);
            disp_hist_thumbnail(data);
            update_gray_levels(data);
        },

        error: function (data) {
            alert('error');
        }
    });
}

function do_ajax_get(e, targetUrl, option) {
    e.preventDefault();

    var URL = targetUrl + get_temp_index() + "/";
    $.ajax({
        url: URL,
        type: "GET",

        beforeSend: function () {
            document.body.style.cursor = "wait";
        },
        complete: function () {
            document.body.style.cursor = "default";
        },
        success: function (data) {
            update_image(data);
            update_clickable(data);
            disp_hist_thumbnail(data);
            update_gray_levels(data);

        },

        error: function (data) {
            alert('error');
        }

    });
}

