from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, myPasswordchanageform, myPasswordResetform, mysetpasswordform
urlpatterns = [
    #path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:id>',
         views.ProdcutDetail.as_view(), name='product-detail'),

    #Cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.pluscart),
    path('minuscart/',views.minuscart),
    path('removecart/',views.removecart),


    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    #Login & Logout & Signup
    path('registration/', views.customerregistration.as_view(),
         name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                        authentication_form=LoginForm), name='login'),

    # Password Change
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                  form_class=myPasswordchanageform, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                 form_class=myPasswordResetform), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=mysetpasswordform), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),



    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.paymentdone,name='paymentdone'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>/', views.topwear, name='topwear'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('laptop/',views.laptop,name='laptop'),
    path('laptop<slug:data>/',views.laptop,name='laptop'),
    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomwear'),
    path('search/',views.Search.as_view(),name='search'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
