from flask import Flask, render_template, jsonify, request
import requests

app=Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/api/stats-scoreboard/")
def api_stats_scoreboard():
    game_date = request.args.get("game_date")
    r = requests.get("https://stats.nba.com/stats/scoreboard/?GameDate=" + game_date + "&LeagueID=00&DayOffset=0")
    return jsonify(r.json())

@app.route("/api/game-detail/")
def api_game_detail():
    gid = request.args.get("gid")
    r = requests.get("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/scores/gamedetail/" + gid + "_gamedetail.json")
    return jsonify(r.json())

@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html", title="Page Not Found"), 404

