from app.models import Entry

def api_lookup(request):

    entry_value = Entry.objects.create(value=request['api_key'])
    entry_value.save()
