jQuery(document).ready(function( $ ) {
        $nav_news = $('.nav-news');
        $('.nav-search-icon').on('click', function(event){
                event.preventDefault();
                $('.nav-search-form_container').slideToggle();
                $('.nav-search').toggleClass('active');
        });

        $('.nav-search-exit').on('click', function(event){
                event.preventDefault();
                $('.nav-search-form_container').slideToggle();
                $('.nav-search').toggleClass('active');
        });

        autosize($('textarea'));
});