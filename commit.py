import datetime as dt
import os

bg = 3 # number of commits for the background divided by 2
fg = 15

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



commit_and_push = """
echo Hello World >> README.md
git add .
git commit -m "Hello World!"
git push

echo \# Hello World > README.md
git add .
git commit -m "Hello again!"
git push
"""

# for _ in range(commits_for(row, col)):
#     os.system(commit_and_push)

os.system(commit_and_push)