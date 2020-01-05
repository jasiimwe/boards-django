from django.urls import path, include
from .views import   new_topic, reply_topic, \
    PostUpdateView, BoardListView, TopicListView, PostListView

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('board/<int:id>/', TopicListView.as_view(), name='board_topics'),
    path('board/<int:id>/new/', new_topic, name='new_topic'),
    path('board/<int:id>/topics/<int:topic_id>', PostListView.as_view(), name='topic_posts'),
    path('board/<int:id>/topics/<int:topic_id>/reply', reply_topic, name='reply_topic'),
    path('board/<int:id>/topics/<int:topic_id>/posts/<int:post_id>/edit', PostUpdateView.as_view(), name = 'edit_post'),
]