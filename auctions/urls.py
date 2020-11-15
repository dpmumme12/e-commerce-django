from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing_info/<int:item_id>", views.listing_info, name="listing_info"),
    path("watch_list", views.watch_list, name="watch_list"),
    path("remove_item", views.remove_item, name="remove_item"),
    path("place_bid", views.place_bid, name="place_bid"),
    path("create_comment", views.create_comment, name="create_comment"),
    path("close_listing", views.close_listing, name="close_listing"),
    path("watchlist_page", views.watchlist_page, name="watchlist_page"),
    path("winnings", views.winnings, name="winnings"),
    path("cat_search", views.cat_search, name="cat_search")
]
