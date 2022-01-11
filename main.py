import requests
from flask import Flask, jsonify, request
app = Flask('app')


@app.route('/')
def hello_world():
    return jsonify({"error":"no api selected"})

# v1.0

@app.route('/<user>/favorite/')
def check(user):
    print(user)
    project = requests.get(f"https://api.scratch.mit.edu/users/{user}/favorites/").text
    partitioned_string = project.partition('[{"id":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',"title":')
    title = partitioned_string[0]
    print(title)
    
    return jsonify({"project id":int(title)})

@app.route('/<project>/thumbnail/')
def thumbnail(project):
    print(project)
    project = f"https://cdn2.scratch.mit.edu/get_image/project/{project}_480x360.png"
  
    return jsonify({"project thumbnail":project})

@app.route('/<user>/pfp/')
def pfp(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/").text

    partitioned_string = userdata.partition('{"id":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]
    print(title)
    logo = "https://uploads.scratch.mit.edu/get_image/user/"+title+"_60x60.png"

    return jsonify({"pfp":logo})

#v1.1

@app.route('/<user>/follower-count/')
def fcount(user):
    print(user)
    userdata = requests.get(f"https://scratchdb.lefty.one/v2/user/info/{user}").text
    partitioned_string = userdata.partition('","followers":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"followers count":int(title)})

# v1.2

@app.route('/<user>/project/')
def project(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/projects/").text
    partitioned_string = userdata.partition('[{"id":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"most recent project":int(title)})

# v1.3

@app.route('/<user>/scratchteam/')
def checkscratch(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/").text
    partitioned_string = userdata.partition('"scratchteam":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]
    if title == 'false':
        title = False
    else:
        title = True
    
    return jsonify({"scratchteam check":title})

@app.route('/<user>/id/')
def getid(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/").text
    partitioned_string = userdata.partition('"id":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"id":int(title)})

@app.route('/<user>/join-date/')
def getjoin(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/").text
    partitioned_string = userdata.partition('"joined":"')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition('"')
    title = partitioned_string[0]

    return jsonify({"join date":title})

@app.route('/<user>/country/')
def getcountry(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/").text
    partitioned_string = userdata.partition('"country":"')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition('"')
    title = partitioned_string[0]

    return jsonify({"country":title})

# v1.4

@app.route('/<project>/views/')
def getviews(project):
    print(project)
    userdata = requests.get(f"https://api.scratch.mit.edu/projects/{project}/").text
    print(userdata)
    partitioned_string = userdata.partition('{"views":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"views":int(title)})

@app.route('/<project>/loves/')
def getloves(project):
    print(project)
    userdata = requests.get(f"https://api.scratch.mit.edu/projects/{project}/").text
    print(userdata)
    partitioned_string = userdata.partition('"loves":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"loves":int(title)})

@app.route('/<project>/favorites/')
def getfavorites(project):
    print(project)
    userdata = requests.get(f"https://api.scratch.mit.edu/projects/{project}/").text
    print(userdata)
    partitioned_string = userdata.partition('"favorites":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"favorites":int(title)})

@app.route('/<project>/remixes/')
def getremixes(project):
    print(project)
    userdata = requests.get(f"https://api.scratch.mit.edu/projects/{project}/").text
    print(userdata)
    partitioned_string = userdata.partition('"remixes":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"remixes":int(title)})

# v1.5

@app.route('/<studio>/studio/followers/')
def getstudiofollowers(studio):
    print(studio)
    userdata = requests.get(f"https://api.scratch.mit.edu/studios/{studio}/").text
    print(userdata)
    partitioned_string = userdata.partition(',"followers":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"studio followers":int(title)})

@app.route('/<studio>/studio/host-id/')
def getstudiohost(studio):
    print(studio)
    userdata = requests.get(f"https://api.scratch.mit.edu/studios/{studio}/").text
    print(userdata)
    partitioned_string = userdata.partition('","host":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"studio host id":int(title)})

@app.route('/<studio>/studio/managers/')
def getstudiomanagers(studio):
    print(studio)
    userdata = requests.get(f"https://api.scratch.mit.edu/studios/{studio}/").text
    print(userdata)
    partitioned_string = userdata.partition('"managers":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"studio managers":int(title)})

@app.route('/<studio>/studio/comments/')
def getstudiocomments(studio):
    print(studio)
    userdata = requests.get(f"https://api.scratch.mit.edu/studios/{studio}/").text
    print(userdata)
    partitioned_string = userdata.partition('"},"stats":{"comments":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"studio comments":int(title)})



# The user message count code is having some trouble, and is still under construction. It does not work yet, and at the moment it will only return an error message that we have created.

@app.route('/<user>/messages/')
def mcount(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/messages/count").text
    print(userdata)
    partitioned_string = userdata.partition('{"count":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition('}')
    title = partitioned_string[0]
    print(title)

    return jsonify({"error":"This API is not yet ready."})



app.run(host='0.0.0.0', port=8000)
