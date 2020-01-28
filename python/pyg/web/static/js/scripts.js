jQuery(document).ready(function( $ ) {
        $nav_news = $('.nav-news');
        $('.nav-search-icon').on('click', function(event){
                event.preventDefault();
                $('.nav-news').animate({width:'toggle'},1000);
                $('.nav-our_tail').animate({width:'toggle'},1000);
                $('.nav-search-form_container').animate({width:'toggle'},1000);
                $('.nav-search').toggleClass('active');
        });

        $('.nav-search-exit').on('click', function(event){
                event.preventDefault();
                $('.nav-news').show();
                $('.nav-our_tail').show();
                $('.nav-search-form_container').animate({width:'toggle'},350);
                $('.nav-search').toggleClass('active');
        });
});