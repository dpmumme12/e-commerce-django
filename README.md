## Web Scraper

### ==Description==</h3>
This is a e-commerce site where you can create account to post items for sale and also buy items. It functions on a bidding system that ends whenever the seller ends the auction. As a user you can comment on items, add items to your watchlist, bid on items and keep track of items you have won. There is also a filter where you can search for items by category to help the user find what they need. You can see a link to the demo at the bottom of this page, enjoy!

### ==Files and directories==
- `auctions` - Main application directory.
  - `static/auctions` - Contains all static files.
    - `styles.css` - Contains all the css for the app.
  - `template/auctions` - Contains all html files for the app.
    - `CategorySearch.html` - The results page for a filtered search.
    - `create_listing.html` - Creates a listing to put an item up for sale.
    - `layout.html` - The base template that all other templates extend.
    - `index.html` - Main template or "homepage".
    - `listing.html` - The info page for an item where you can bid, comment...etc on an item.
    - `login.html` - The login page where you sign into your account.
    - `register.html` - The page where you can make an account.
    - `watchlist.html` - The page where you see all of the items you have added to your watchlist.
    - `winnings.html` - The page where you can see all of the items you have won.
  - `admin.py` - File registering your models for the admin page.
  - `models.py` - File containing all of the models for the database.
  - `urls.py` - Contains all the urls for the app.
  - `views.py` - Contains all the views for the app.
- `commerce` - Project directory.

Demo link https://commerce-for-you.herokuapp.com/
