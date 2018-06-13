from flask import Flask, render_template, jsonify, request
import requests
import json
import sys

if sys.platform in ["darwin", "win32"]:
    run_mode = "local"
else:
    run_mode = "production"

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html", run_mode=run_mode)


@app.route("/api/stats-scoreboard/")
def api_stats_scoreboard():
    game_date = request.args.get("game_date")
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    r = requests.get("https://stats.nba.com/stats/scoreboard/?GameDate=" + game_date + "&LeagueID=00&DayOffset=0", headers=headers)
    return jsonify(r.json())


@app.route("/api/game-detail/")
def api_game_detail():
    gid = request.args.get("gid")
    r = requests.get("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/scores/gamedetail/" + gid + "_gamedetail.json")
    return jsonify(r.json())


@app.route("/test-api/stats-scoreboard/")
def test_api_stats_scoreboard():
    game_date = request.args.get("game_date")
    with open("static/data/stats-scoreboard/game_date=" + game_date.replace("/", "") + ".json", "r") as file:
        loaded = json.load(file)
    return jsonify(loaded)


@app.route("/test-api/game-detail/")
def test_api_game_detail():
    gid = request.args.get("gid")
    with open("static/data/game-detail/gid=" + gid + ".json", "r") as file:
        loaded = json.load(file)
    return jsonify(loaded)


@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html", title="Page Not Found"), 404
