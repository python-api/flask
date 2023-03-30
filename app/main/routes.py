from app.main import blue_print


@blue_print.route('/')
def index():
    return 'This is The Main Blueprint'
