
my_request = [
    {
        "title": "title of post 1", 
        "content": "content of post 1",
        "id": 1
    },

    {
        "title": "fav foods",
        "content": "Pizza",
        "id": 2
    }
]



def find_post(id):
    for post in my_request:
        if post['id'] == id:
            return post

def find_post_index(id):
    for index, post in enumerate(my_request):
        if post['id'] == id:
            return index