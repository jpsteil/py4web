from py4web import action, request

# pls, run websockets server - look at utils/wsservers.py.txt
# test example for websockets


@action("ws/index")
@action.uses("ws/examples/index.html")
def index():
    ws_url = "ws://127.0.0.1:8000/"
    return dict(ws_url=ws_url)
