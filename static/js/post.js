
$(document).ready(function(){
    $(document).on('click','.post-opt-btn',function(){
        $('.post-opt-btn').not(this).next().removeClass('show2');
        $(this).next().toggleClass('show2');
    });
    $(document).on('click',function(e){
        if(!$(e.target).closest('.post-opt-btn').length)
			$('.post-opt-btn').next().removeClass('show2');
	});    
});
