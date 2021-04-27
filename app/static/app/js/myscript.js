function test(){
    var tabsNewAnim = $('#navbarSupportedContent');
    var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
    var activeItemNewAnim = tabsNewAnim.find('.active');
    var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
    var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
    var itemPosNewAnimTop = activeItemNewAnim.position();
    var itemPosNewAnimLeft = activeItemNewAnim.position();
    $(".hori-selector").css({
      "top":itemPosNewAnimTop.top + "px", 
      "left":itemPosNewAnimLeft.left + "px",
      "height": activeWidthNewAnimHeight + "px",
      "width": activeWidthNewAnimWidth + "px"
    });
    $("#navbarSupportedContent").on("click","li",function(e){
      $('#navbarSupportedContent ul li').removeClass("active");
      $(this).addClass('active');
      var activeWidthNewAnimHeight = $(this).innerHeight();
      var activeWidthNewAnimWidth = $(this).innerWidth();
      var itemPosNewAnimTop = $(this).position();
      var itemPosNewAnimLeft = $(this).position();
      $(".hori-selector").css({
        "top":itemPosNewAnimTop.top + "px", 
        "left":itemPosNewAnimLeft.left + "px",
        "height": activeWidthNewAnimHeight + "px",
        "width": activeWidthNewAnimWidth + "px"
      });
    });
  }
  $(document).ready(function(){
    setTimeout(function(){ test(); });
  });
  $(window).on('resize', function(){
    setTimeout(function(){ test(); }, 500);
  });
  $(".navbar-toggler").click(function(){
    setTimeout(function(){ test(); });
  });











$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];
    console.log(id)
    $.ajax({
        type:"GET",
        url:'/pluscart',
        data:{
            prod_id:id,
        },
        success:function(data)
        {
            console.log(data)
            eml.innerText=data.quantity
            amount=document.getElementById('amount').innerText=data.amount
            total=document.getElementById('total').innerText=data.total_amount
        }

    })
    
})


$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];
    console.log(id)
    $.ajax({
        type:"GET",
        url:'/minuscart',
        data:{
            prod_id:id,
        },
        success:function(data)
        {
            console.log(data)
            eml.innerText=data.quantity
            amount=document.getElementById('amount').innerText=data.amount
            total=document.getElementById('total').innerText=data.total_amount
        }

    })
    
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    console.log(id)
    $.ajax({
        type:"GET",
        url:'/removecart',
        data:{
            prod_id:id,
        },
        success:function(data)
        {
            console.log("Deleted")
            amount=document.getElementById('amount').innerText=data.amount
            total=document.getElementById('total').innerText=data.total_amount
            
            eml.parentNode.parentNode.parentNode.parentNode.remove()

            
        }

    })
    
})




