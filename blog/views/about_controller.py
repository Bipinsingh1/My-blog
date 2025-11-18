from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Profile


def about(request):
    # Get the admin/first user to display on the about page
    try:
        admin_user = User.objects.filter(is_staff=True).first() or User.objects.first()
        
        # Try to get the profile, create it if it doesn't exist
        profile, created = Profile.objects.get_or_create(user=admin_user)
        
        # Since we removed the social media fields, create empty placeholders
        context = {
            'title': 'About',
            'user': admin_user,
            'profile': profile,
            'social_links': {
                'twitter': None,
                'linkedin': None,
                'github': None,
                'instagram': None
            }
        }
    except Exception as e:
        # Fallback if no users exist or there's another issue
        context = {
            'title': 'About',
            'error': str(e)
        }
        
    return render(request, 'blog/about.html', context)