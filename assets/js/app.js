{% if page.carousel %}
<!-- Google CDN Hosted jQuery  -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.2/jquery.min.js"></script>
<!-- Flexslider Library  -->
<script src="/js/flexslider.min.js"></script>
<!-- Initialisation Code  -->
<script src="/js/app.js"></script>

// Initialise FlexSlider for Carousels
$(window).load(function() {
    $('.flexslider').flexslider({
    animation: "fade",
    controlNav: false,
    directionNav: true,
    slideshowSpeed: 5000,
    animationSpeed: 600,
    touch: true
    });
});


{% endif %}