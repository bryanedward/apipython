from mocks.data import posts


def find_post(id):
    for resp in posts:
        if resp['id'] == id:
            return resp
