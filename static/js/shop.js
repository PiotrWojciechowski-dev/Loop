$(document).ready(function(){
    $(document).on('mouseover','.item',function(){
        $(this).css('border', '1px solid #e5e5e5', 'box-shadow', '0px 8px 16px #888')
        $(this).css('box-shadow', '0px 8px 20px rgba(0,0,0,0.2)')
        console.log('working')
    });
    $(document).on('mouseout','.item',function(){
        $(this).css('border', 'none')
        $(this).css('box-shadow', 'none')
        console.log('working')
    });
});