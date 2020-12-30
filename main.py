import json as j
from websocket_server import WebsocketServer
import datetime

def new_client(client, server):
    print("Request")
    message = "Joined new client"
    dtime = datetime.datetime.now()
    time = dtime.strftime('%Y年%m月%d日 %H:%M:%S')
    msg = j.dumps({"res" : "join", "time" : time, "text" : message})
    server.send_message_to_all(str(msg))

def rp(client, server, message):
    dtime = datetime.datetime.now()
    json = j.loads(message)
    time = dtime.strftime('%Y年%m月%d日 %H:%M:%S')
    msg = j.dumps({"res" : "msg", "time" : time, "text" :  json["msg"], "name" : json["name"]})
    server.send_message_to_all(str(msg))    

server = WebsocketServer(80)
server.set_fn_new_client(new_client)
server.set_fn_message_received(rp)
server.run_forever()
