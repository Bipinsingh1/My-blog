My Blog — Django Full-Stack Blog Platform
A multi-user blog platform built with Django, PostgreSQL, and Bootstrap 4. Users can register, write rich-text posts with images, browse by category, and leave comments.

Features

User authentication — Register, log in, log out, and manage your profile with a custom avatar (auto-resized to 300×300px)
Rich text editor — Posts are written using TinyMCE with full formatting toolbar (bold, italic, links, images, code blocks, tables)
Post management — Create, edit, and delete your own posts; permission-protected so users can only modify their own content
Category filtering — Posts are tagged with categories; readers can browse all posts under a specific category
Comments — Readers can comment on posts; uses redirect-after-POST to prevent duplicate submissions
Pagination — Post lists paginate at 5 posts per page
User post pages — Each author has a dedicated page listing all their posts
About page — Displays the site admin's profile dynamically


Tech Stack
LayerTechnologyBackendPython 3, Django 3.1DatabasePostgreSQLFrontendBootstrap 4, crispy-formsRich TextTinyMCEImage handlingPillowEmailSMTP via GmailDeploymentReplit

Project Structure
My-blog/
├── blink/                  # Django project config (settings, urls, wsgi)
├── blog/
│   ├── models/
│   │   ├── post.py         # Post model with TinyMCE HTMLField, image, category, author
│   │   ├── comment.py      # Comment model linked to Post via ForeignKey
│   │   └── category.py     # Category model
│   ├── views/              # One controller per feature
│   │   ├── post_list_controller.py
│   │   ├── post_detail_controller.py
│   │   ├── post_create_controller.py
│   │   ├── post_update_controller.py
│   │   ├── post_delete_controller.py
│   │   ├── post_comment_controller.py
│   │   ├── user_post_list_controller.py
│   │   ├── category_controller.py
│   │   └── about_controller.py
│   └── forms/
│       ├── PostForm.py         # Create form with dynamic category dropdown
│       ├── PostUpdateForm.py   # Update form
│       └── CommentForm.py      # Comment form
├── users/
│   ├── models/profile.py       # Profile model with auto-resize via Django signals
│   ├── views.py                # Register, login, logout, profile update
│   └── forms/                  # UserRegisterForm, UserUpdateForm, ProfileUpdateForm
└── media/                      # Uploaded post images and profile pictures

Setup & Installation
Prerequisites

Python 3.8+
PostgreSQL
pip

1. Clone the repository
bashgit clone https://github.com/Bipinsingh1/My-blog.git
cd My-blog
2. Create and activate a virtual environment
bashpython -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
3. Install dependencies
bashpip install -r requirements.txt
4. Set environment variables
Create a .env file in the root directory (never commit this):
PGDATABASE=your_db_name
PGUSER=your_db_user
PGPASSWORD=your_db_password
PGHOST=localhost
PGPORT=5432
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_app_password

Note: For Gmail, use an App Password, not your regular password.

5. Apply migrations
bashpython manage.py migrate
6. Create a superuser (admin)
bashpython manage.py createsuperuser
7. Run the development server
bashpython manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Key Implementation Details
Django signals for profile images
When a user saves their profile, a post_save signal automatically opens the uploaded image with Pillow and resizes it to 300×300px if it exceeds that size — keeping storage usage low without any manual step.
python@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
Permission-protected views
Post editing and deletion use LoginRequiredMixin and UserPassesTestMixin to ensure only the post's author can modify it:
pythondef test_func(self):
    post = self.get_object()
    return self.request.user == post.author
Dynamic category dropdown
The post creation form queries the Category model at form initialisation time (not import time) to ensure the dropdown always reflects the current database state:
pythondef __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].widget.choices = get_categories()

Database Schema (simplified)
User (Django built-in)
 └── Profile          (OneToOne → User)

Post
 ├── author           (ForeignKey → User)
 ├── category         (CharField)
 ├── content          (TinyMCE HTMLField)
 └── image            (ImageField)

Comment
 └── post             (ForeignKey → Post)

Category
 └── name             (CharField)

Screenshots

Add screenshots here once the app is running.


License
MIT
