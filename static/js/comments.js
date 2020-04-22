$('.comment-btn').click(function() {
    var id = $(this).attr('id');
    console.log(id);
    $('.comments' + id).toggle('slow', function() {
    });
  });

$(document).ready(function(){
    $(document).on('click','.comment-opt-btn',function(){
        $('.comment-opt-btn').not(this).next().removeClass('show2');
        $(this).next().toggleClass('show2');
    });
    $(document).on('click',function(e){
        if(!$(e.target).closest('.comment-opt-btn').length)
            $('.comment-opt-btn').next().removeClass('show2');
    });    
});