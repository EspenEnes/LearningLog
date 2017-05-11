from .models import Topic

def add_variables_to_context(request):
    topic = Topic.objects.all()
    return{"MenuTopics": topic}