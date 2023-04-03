def logged_in_user(request):
  return {"l_user":request.user}