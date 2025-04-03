# This file and function was created so I can user "user" in base.html. Howver, it allows use of "user_object" anywhere.

def get_user_object(request):
    # If the user is authenticated, you can pass the user object
    if request.user.is_authenticated:
        return {'user_object': request.user}
    return {}
