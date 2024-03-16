$(document).ready(function () {
    $('#commentForm').submit(function (event) {
        // Prevent default form submission
        event.preventDefault();

        // Serialize form data
        var formData = $(this).serialize();

        var commentsSection = $('.comments-section');

        // Send AJAX request
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,

            success: function (data) {
                if (data.success) {
                    // Append the new comment content to the comments section
                    commentsSection.prepend(data.comment_html);
                    $('#commentForm textarea').val('');
                } else {
                    // Handle errors if necessary
                    console.error(data.errors);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle error
                console.error(xhr.responseText);
            }
        });
    });


    $('#likeForm').submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(data) {
                // 根据服务器返回的数据更新按钮的外观
                if (data.success) {
                    var likeButton = $('#likeForm button');
                    likeButton.toggleClass('btn-primary btn-secondary');

                    // 如果您有其他需要更新的 UI 元素，也可以在这里进行更新
                } else {
                    console.error('An error occurred:', data.errors);
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('An error occurred:', errorThrown);
            }
        });
    });
});

