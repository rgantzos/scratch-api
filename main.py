import requests
from flask import Flask, jsonify, request
app = Flask('app')


@app.route('/')
def hello_world():
    return jsonify({"error":"no api selected"})


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
    
    return jsonify({"project id":title})

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

@app.route('/<user>/follower-count/')
def fcount(user):
    print(user)
    userdata = requests.get(f"https://scratchdb.lefty.one/v2/user/info/{user}").text
    partitioned_string = userdata.partition('","followers":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition(',')
    title = partitioned_string[0]

    return jsonify({"followers count":title})

# The user message count code is having some trouble, and is still under construction. It does not work yet, and at the moment it will only return an error message that we have created.

@app.route('/<user>/messages/')
def mcount(user):
    print(user)
    userdata = requests.get(f"https://api.scratch.mit.edu/users/{user}/messages/count").text
    partitioned_string = userdata.partition('{"count":')
    before_first_period = partitioned_string[2]
    print(before_first_period)
    partitioned_string = before_first_period.partition('}')
    title = partitioned_string[0]
    print(title)

    return jsonify({"error":"this api is not yet ready for release"})



app.run(host='0.0.0.0', port=8000)
