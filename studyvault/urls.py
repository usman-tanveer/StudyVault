from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from resources.views import (
    home,
    subjects,
    data_science,
    quantitative_reasoning,
    ict,
    fundamental_mathematics,
    functional_english,
    global_challenges,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('subjects/', subjects, name='subjects'),

    path(
        'subjects/data-science/',
        data_science,
        name='data_science'
    ),

    path(
        'subjects/quantitative-reasoning/',
        quantitative_reasoning,
        name='quantitative_reasoning'
    ),

    path(
        'subjects/ict/',
        ict,
        name='ict'
    ),

    path(
        'subjects/fundamental-mathematics/',
        fundamental_mathematics,
        name='fundamental_mathematics'
    ),

    path(
        'subjects/functional-english/',
        functional_english,
        name='functional_english'
    ),

    path(
        'subjects/global-challenges/',
        global_challenges,
        name='global_challenges'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)