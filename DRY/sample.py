def nav_menu():
    print("<h1>Home</h1>")
    print("<h1>About</h1>")
    print("<h1>Contact</h1>")

def header():
    print('<div class="header">')
    nav_menu()
    print('</div>')

def footer():
    print('<div class="footer">')
    nav_menu()
    print('</div>')

def home_page():
    header()
    print('<p>This is home page</p>')
    footer()

def about_page():
    header()
    print('<p>This is about page</p>')
    footer()

def contact_page():
    header()
    print('<p>This is contact page</p>')
    footer()


about_page()

