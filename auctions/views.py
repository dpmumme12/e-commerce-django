from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, listing, bid, comment, watchlist, sale


def index(request):
    try:
        listings = listing.objects.all()
    except:
        listings = None
    
    return render(request, "auctions/index.html",{
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if (request.method == "POST"):
        listable = listing()

        listable.item_name = request.POST.get("title")
        listable.item_description = request.POST.get("description")
        listable.item_price = request.POST.get("price")
        listable.category = request.POST.get("category")
        listable.user_id = request.user.id

        if (request.FILES['image'] == ''):
            listable.item_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        else:
            listable.item_img = request.FILES['image']

        listable.save()

        return render(request, "auctions/create_listing.html", {
            "message": "Listing created!"
        })

    else:
        return render(request, "auctions/create_listing.html")

def listing_info(request, item_id):
        
        item_info = listing.objects.filter(id = item_id)
        item_info = item_info.get()

        try:
            watch_item = watchlist.objects.filter(item_id = item_id, user_id = request.user.id)
            watch_item = watch_item.get()
        except:
            watch_item = None

        try:
            all_bids = bid.objects.filter(item_id = item_id).order_by("-bid_amount")
            highest_bid = all_bids[0]
        except:
            highest_bid = 0
        
        try: 
            bid_info = bid.objects.filter(item_id = item_id, user_id = request.user.id)
            bid_info = bid_info.get()
        except:
            bid_info = None
        
        try:
            all_bids = bid.objects.filter(item_id = item_id).order_by("-bid_date")
        except:
            all_bids = None

        try:
            comments = comment.objects.filter(item_id = item_id).order_by("-date")
        except:
            comments = None

        try:
            winner = sale.objects.get(item_id = item_id)
        except:
            winner = None

        return render(request, "auctions/listing.html", {
            "listing": item_info,
            "watchlist": watch_item,
            "bid_info": bid_info,
            "highest_bid": highest_bid, 
            "all_bids": all_bids,
            "comments": comments,
            "winner": winner
        })

def watch_list(request):
    if (request.method == "POST"):
        watching = watchlist()

        item_id = request.POST.get("item_id")

        watching.item_id = request.POST.get("item_id")
        watching.user_id = request.user.id

        watching.save()

        return HttpResponseRedirect(reverse("listing_info", args = (item_id,)))

def remove_item(request):
    if(request.method == "POST"):
        watchlist.objects.filter(item_id = request.POST.get("item_id"), user_id = request.user.id).delete()

        item_id = request.POST.get("item_id")

        return HttpResponseRedirect(reverse("listing_info", args = (item_id,)))

def place_bid(request):
    if (request.method == "POST"):
        bid_item = bid()

        item_id = request.POST.get("item_id")

        try:
            all_bids = bid.objects.filter(item_id = item_id).order_by("-bid_amount")
            highest_bid = all_bids[0].bid_amount
        except:
            highest_bid = 0

        item_info = listing.objects.filter(id = item_id)
        item_info = item_info.get()


        try:
            watch_item = watchlist.objects.filter(item_id = item_id, user_id = request.user.id)
            watch_item = watch_item.get()
        except:
            watch_item = None

        try:
            comments = comment.objects.filter(item_id = item_id).order_by("-date")
        except:
            comments = None

        if (highest_bid >= float(request.POST.get("amount")) or item_info.item_price >= float(request.POST.get("amount"))):
            try: 
                bid_info = bid.objects.filter(item_id = item_id, user_id = request.user.id)
                bid_info = bid_info.get()
            except:
                bid_info = None

            try:
                all_bids = bid.objects.filter(item_id = item_id).order_by("-bid_amount")
                highest_bid = all_bids[0]
            except:
                highest_bid = 0
        
            return render(request, "auctions/listing.html", {
                "listing": item_info,
                "watchlist": watch_item,
                "message": "Bid must be greater than current highest bid.",
                "bid_info": bid_info,
                "highest_bid": highest_bid, 
                "comments": comments
                })
        else:
            pass
        
        if (len(bid.objects.filter(item_id = item_id, user_id = request.user.id)) != 0):

            bid_info = bid.objects.get(item_id = item_id, user_id = request.user.id)
            bid_info.bid_amount = request.POST.get("amount")
            bid_info.save()
        else:
            bid_item.bid_amount = request.POST.get("amount")
            bid_item.item_id = request.POST.get("item_id")
            bid_item.user_id = request.user.id
            bid_item.username = request.user.username 

            bid_item.save()

        return HttpResponseRedirect(reverse("listing_info", args = (item_id,)))

def create_comment(request):
    if (request.method == "POST"):
        new_comment = comment()

        new_comment.item_id = request.POST.get("item_id")
        new_comment.comment = request.POST.get("comment")
        new_comment.username = request.user.username

        new_comment.save()

        item_id = request.POST.get("item_id")

        return HttpResponseRedirect(reverse("listing_info", args = (item_id,)))

        

def close_listing(request):
    if (request.method == "POST"):
        winner_username = request.POST.get("winner_username")
        winner_id = request.POST.get("winner_id")
        item_id = request.POST.get("item_id")

        item_sale = sale()

        item_sale.item_id = item_id
        item_sale.buyer_id = winner_id
        item_sale.buyer_username = winner_username

        item_sale.save()

        listing.objects.filter(id = item_id).update(status = "Closed", winner_id = winner_id)

        return index(request)

def watchlist_page(request):
    try:
        watch_item = watchlist.objects.filter(user_id = request.user.id)
    except:
        watch_item = None

    listing_ids = []

    try:
        for item in watch_item:
            item_id = item.item_id
            listing_ids.append(item_id)
    except:
        pass

    listings = listing.objects.all()

    return render(request, "auctions/watchlist.html", {
        "listings": listings,
        "listing_ids": listing_ids
    })

def winnings(request):
    listings = listing.objects.all()
    
    return render(request, "auctions/winnings.html",{
        "listings": listings
    })

def cat_search(request):
    if (request.method == "POST"):
        listings = listing.objects.all()
    
        return render(request, "auctions/CategorySearch.html",{
        "listings": listings,
        "category": request.POST.get("category")
        })