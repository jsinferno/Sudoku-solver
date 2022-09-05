from sudoku import *
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime


numbers = "123456789"

app = Flask(__name__)
inp = zip([""]*81,[""]*81)


def changelist(alist):
    green = ["yes" if x == "" or x =="0" else "useless" for x in alist]
    alist = [str(x) if x!="" else "0" for x in alist]
    newlist = []
    for x in range(0,81,27):
        newlist.append(alist[x:x+3] + alist[x+9:x+12] + alist[x+18:x+21])
        newlist.append(alist[x+3:x+6] + alist[x+12:x+15] + alist[x+21:x+24])
        newlist.append(alist[x+6:x+9] + alist[x+15:x+18] + alist[x+24:x+27])

    return [newlist,green]

def changeback(alist):
    newlist = []
    for line in range(0,9,3):
        for part in range(0,9,3):
            newlist.append(alist[line][part:part+3]+alist[line+1][part:part+3]+alist[line+2][part:part+3])
    
    return [x for n in newlist for x in n]



 
@app.route("/solver", methods = ["POST","GET"])  
def solver():
    if request.method == "GET": return render_template("input.html", top = "<p id = 'top' style = 'color: white'>dont look at thus</p>")
    return render_template("input.html", top = "<h1 id = 'top'>Impossible or Not allowed</h1>")
    

        
@app.route("/solver/solution", methods = ["POST","GET"])
def solution():
    if request.method == "GET":
        return redirect("/solver")

    newlist = request.form.getlist("minisquare[]")
    
    if newlist.count("") > 68: return render_template("input.html",top = "<h1 id = 'top'>Impossible or Not allowed</h1>")


    green,newlist = ["yes" if x == "" or x =="0" else "useless" for x in newlist],create_grid([x if x!="" else "0" for x in newlist])
    print(newlist)

    if valid_grid(newlist):
        newlist = make_grid(newlist)

        c = 0
        while c<5 and not newlist[1]:
            newlist = make_grid(newlist[0])
            c+=1

        if newlist[1]:

            newlist = [x for y in newlist[0] for x in y]
            multiple = create_grid(list(zip(newlist,green)))
            return render_template("output.html", square = multiple, top = "<h1 id = 'top'>Solution Found</h1>")
        else: newlist = newlist[0]

    print(newlist)
    for row,line in enumerate(newlist):
        for col,guess in enumerate(line):
            if guess=="0":
                newlist[row][col] = ["",False]
            else:
                newlist[row][col] = "0"
                if not is_valid(row, col, guess, newlist):
                    newlist[row][col] = [guess,"no"]
                else: newlist[row][col] = [guess,False]
    

    return render_template("output.html",square = newlist, top = "<h1 id = 'top'>Impossible or Not allowed</h1>")


@app.route("/")
def c():
    return redirect("/create")

@app.route("/create", methods = ["POST","GET"])
def create():
    square = [""]*81
    if request.method == "GET":
        square = create_grid(list(zip(square,square)))
        return render_template("output.html", top = "<form action = '/create' method = 'POST'><input id = 'top' type='submit' value = 'Create New'></form>", square = square)
    else:
        square = make_grid()[0]
        for cycle in range(10):
            square = take_away(square)

        square = [x if x!="0" else "" for n in square for x in n]
        square = create_grid(list(zip(square,square)))

        return render_template("output.html", square = square, top = "<h1 id = 'top'>Problem Made</h1>")





if __name__ == "__main__":
    app.run(debug = True)
    SQLALCHEMY_TRACK_MODIFICATIONS = False



