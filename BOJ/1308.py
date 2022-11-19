from datetime import datetime

def d_day(today, dday):
    if (dday[0] - today[0] > 1000 or (dday[0] - today[0] == 1000 and dday[1] - today[1] > 0) or \
            (dday[0] - today[0] == 1000 and dday[1] == today[1] and dday[2] - today[2] >= 0)):
        return "gg"
    else:
        today_date = datetime(year=today[0], month=today[1], day=today[2])
        dday_date = datetime(year=dday[0], month=dday[1], day=dday[2])
        # print(today_date, dday_date)

        dday_day = (dday_date - today_date).days # 와,,,, 대박
        # print(dday_date - today_date)

        return f"D-{dday_day}"


if __name__ == "__main__":
    today = list(map(int, input().split()))
    dday = list(map(int, input().split()))
    print(d_day(today, dday))