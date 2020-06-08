import datetime as dt
import os

bg = 10 # number of commits for the background divided by 2
fg = 30

start = dt.date(2020, 6, 8)

today = dt.date.today()
row = today.weekday()
col = (today - start).days // 7



def commits_for(row, col):
    with open("pattern.csv", "r") as f:
        value = f.readlines()[row].split(";")
        value = value[col%len(value)]
    value = fg if value == "X" or value == "\ufeffX" else bg
    return value



commit_twice = """
echo Hello World >> README.md
git add README.md
git commit -m "Hello World!"

echo \# Hello World > README.md
git add README.md
git commit -m "Hello again!"
"""

with open("counts", "r") as f:
    line = f.readline()
contributions = int(line.split("data-count=\"")[1].split("\"")[0])
todo = commits_for(row, col) - contributions

for _ in range(commits_for(row, col) - contributions):
    os.system(commit_twice)
os.system("git push")
