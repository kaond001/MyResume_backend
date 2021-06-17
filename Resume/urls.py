from django.urls import path
from Resume import views

urlpatterns = [
    path('contact',  views.Contact_list),
    path('skills',  views.Skills_list),
    path('education',  views.Education_list),
    path('home',  views.Home_list),
    path('testimonial',  views.Testimonial_list),
    path('socialMedia',  views.Media_list),
    # path('<int:pk>', views.visitor_detail),
    # path('<to>', views.visitor_list_by_position),
    # path('out',  views.Visitors_list),
]
# echo "# MyResume_backend" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/kaond001/MyResume_backend.git
# git push -u origin main