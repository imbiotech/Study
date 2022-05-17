from flask import Flask, render_template, request, redirect
from JOB_Scrapper_F_NOMAD import get_indeed_jobs, exporter_csv

# template_folder는 경로를 지정해 주는 것이 좋음
app = Flask("SuperScrapper", template_folder="HTML Template")

# Fake_DB는 Dic형으로 저장, DB는 route 밖에 있어야 초기화되지 않음
Fake_DB = {}
Count_DB = {}

# Decorator는 바로 아래에 있는 Function을 실행시킴, 다른 구문을 넣으면 안 됨
@app.route("/")
def home():
    return render_template("Flask.html")

# Report 단 설정
@app.route("/report")
def report():
    text = request.args.get("text")
    if text:
        text = text.lower()
        # Fake_DB에 해당 Text가 존재할 경우 jobs에 결과값을 바로 출력하고, 없을 경우 스크래핑 후 Fake_DB에 저장
        if Fake_DB.get(text):
            jobs = Fake_DB[text]
            Count_DB[text] += 1
        else:
            jobs = get_indeed_jobs(text)
            Fake_DB[text] = jobs
            Count_DB[text] = 1
    else:
        return redirect("/")
    return render_template\
        ("Report.html", text = text,
         ResultsNumber = len(jobs), SerchingCount = Count_DB[text],
         jobs = jobs
         )

@app.route("/export")
def export():
    try:
        text = request.args.get("text")
        if not text:
            raise Exception()
        text = text.lower()
        jobs = Fake_DB.get(text)
        if not jobs:
            raise Exception()
        exporter_csv(jobs)
        return f"Generate CSV for {text}"
    except:
        return redirect("/")


app.run()



# Instanciation
class car():

    def __init__(self, *arg, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

# inherit or extend 부모의 성격을 상속
class convertible(car):

    def take_off(self):
        return "taking off"

    # 부모의 method를 덮어쓰기 할 수 있음
    def __str__(self):
        return f"Car with no roof"

    # super()를 통해서 덮어쓴 부모의 method를 다시 호출할 수 있음
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

# function
def start_function():
    print("I started.")

porche = convertible(color="green",price="$40",)
mini = car()

print(porche.color)