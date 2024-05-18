from .cart import Cart
#create context processor so our cart can work on all pages 
def cart(request):
    # reutrn the defualt data from our cart 
    return {'cart':Cart(request)}