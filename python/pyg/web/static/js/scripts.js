jQuery(document).ready(function( $ ) { 

        autosize($('textarea'));

        // Check if gamer profile is in edit mode, if not, add class 'editing'
        $('#member_profile input').on('click', function(event){
                console.log('editing');
                if( $('#member_profile').hasClass('editing') ){
                } else{
                        $('#member_profile').addClass('editing');
                        $('.member_profile-alert-editing').slideToggle();
                }
        });
        $('#member_profile textarea').on('click', function(event){
                if( $('#member_profile').hasClass('editing') ){
                } else{
                        $('#member_profile').addClass('editing');
                        $('.member_profile-alert-editing').slideToggle();
                }
        });
        $('.member_profile-alert-editing').on('click', function(event){
                $('.member_profile-alert-editing').slideToggle();
                 $('#member_profile').removeClass('editing');
        });

        $("#member_profile").on("input", function() {
               
            alert("Change to " + this.value);
        });
});