
$(document).ready(function(){
    $(document).on('click','.settings-btn',function(){
        $('.settings-btn').not(this).next().removeClass('item');
        $(this).next().css()
    });
    $(document).on('click',function(e){
        if(!$(e.target).closest('.settings-btn').length)
			$('.settings-btn').next().removeClass('show2');
	});    
});
