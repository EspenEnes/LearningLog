from .models import Topic, Entry


def add_variables_to_context(request):


    if request.user.is_authenticated():
        topic = Topic.objects.filter(owner=request.user)
    else:
        topic = []


    publicEntries = Entry.objects.filter(public=True)
    b = []
    publicTopics = []
    for a in publicEntries:
        if a.topic.text not in b:
            b.append(a.topic.text)
            publicTopics.append(a)







    return{"MenuTopics": topic, "publicTopics":publicTopics,}