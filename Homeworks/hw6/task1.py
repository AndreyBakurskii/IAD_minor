import csv
# Focal depth - глубина
# Latitude - широта 0..90 север-юг
# Longitude - долгота 0..180 восток-запад
# Richter - баллы землетрясения

# northern_left = 0
# northern_right = 90
#
# southern_left = -90
# southern_right = 0
#
# western_left = -180
# western_right = 0
#
# eastern_left = 0
# eastern_right = 180

def a(data: list):
    print(len(list(filter(lambda x: float(x['Richter']) > 6, data))))

def b(data: list):

    rows = data

    northern_hemisphere = 0
    southern_hemisphere = 0
    western_hemisphere = 0
    eastern_hemisphere = 0

    print("FOCAL DEPTH")

    top10_focal_depth = sorted(rows, key=lambda x: float(x['Focal depth']), reverse=True)[:10]
    # print(*top10_focal_depth, sep="\n")
    for ind, obj in enumerate(top10_focal_depth):
        if float(obj['Latitude']) > 0:
            northern_hemisphere += 1
        else:
            southern_hemisphere += 1

        if float(obj['Longitude']) > 0:
            western_hemisphere += 1
        else:
            eastern_hemisphere += 1

        print(f"{ind + 1}. Latitude = {obj['Latitude']}, Longitude = {obj['Longitude']}")

    # print(f"northern_hemisphere = {northern_hemisphere}\n"
    #       f"southern_hemisphere = {southern_hemisphere}\n"
    #       f"western_hemisphere = {western_hemisphere}\n"
    #       f"eastern_hemisphere = {eastern_hemisphere}")

    print()
    print()

    northern_hemisphere = 0
    southern_hemisphere = 0
    western_hemisphere = 0
    eastern_hemisphere = 0

    print("RICHTER")

    top10_Richter = sorted(rows, key=lambda x: x['Richter'], reverse=True)[:10]
    # print(*top10_Richter, sep="\n")
    for ind, obj in enumerate(top10_Richter):
        if float(obj['Latitude']) > 0:
            northern_hemisphere += 1
        else:
            southern_hemisphere += 1

        if float(obj['Longitude']) > 0:
            western_hemisphere += 1
        else:
            eastern_hemisphere += 1

        print(f"{ind + 1}. Latitude = {obj['Latitude']}, Longitude = {obj['Longitude']}")

    print(f"northern_hemisphere = {northern_hemisphere}\n"
          f"southern_hemisphere = {southern_hemisphere}\n"
          f"western_hemisphere = {western_hemisphere}\n"
          f"eastern_hemisphere = {eastern_hemisphere}")


def c_task(data: list):
    northern_hemisphere = (list(filter(lambda x: float(x["Latitude"]) > 0, data)))
    southern_hemisphere = (list(filter(lambda x: float(x["Latitude"]) < 0, data)))
    western_hemisphere = (list(filter(lambda x: float(x["Longitude"]) > 0, data)))
    eastern_hemisphere = (list(filter(lambda x: float(x["Longitude"]) < 0, data)))

    print(f"northern_hemisphere = {len(northern_hemisphere)}\n"
          f"southern_hemisphere = {len(southern_hemisphere)}\n"
          f"western_hemisphere = {len(western_hemisphere)}\n"
          f"eastern_hemisphere = {len(eastern_hemisphere)}")

    top10_focal_depth_northern = top_10(northern_hemisphere, "northern", 'Focal depth')
    top10_focal_depth_southern = top_10(southern_hemisphere, "southern", 'Focal depth')
    top10_focal_depth_western = top_10(western_hemisphere, "western", 'Focal depth')
    top10_focal_depth_eastern = top_10(eastern_hemisphere, "eastern", 'Focal depth')

    top10_Richter_northern = top_10(northern_hemisphere, "northern", "Richter")
    top10_Richter_southern = top_10(southern_hemisphere, "southern", "Richter")
    top10_Richter_western = top_10(western_hemisphere, "western", "Richter")
    top10_Richter_eastern = top_10(eastern_hemisphere, "eastern", "Richter")


def top_10(data, hemisphere, key):
    print(f"Top 10 by {key} in {hemisphere} hemisphere:")
    top10_ = sorted(data, key=lambda x: float(x[key]), reverse=True)[:10]
    print(*top10_, sep="\n")
    print()
    return top10_

rows = []
with open("quake.csv", "r", newline='') as csv_file:
    for row in csv.DictReader(csv_file):
        rows.append(row)


# a(rows)
# b(rows)
# c_task(rows)