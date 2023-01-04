

city = ["Solboa", "Raris", "Lonpon", "Bodrid", "Serlin"]


temperatures = [
    {
        "city": "Solboa",
        "temperatures": [13, 14, 14, 12, 11, 15, 16, 15, 15, 14, 13, 12, 9]
    },
    {
        "city": "Raris",
        "temperatures": [10, 11, 12, 11, 23, 9, 7, 7, 8, 10, 11, 11, 8]
    },
    {
        "city": "Lonpon",
        "temperatures": [8, 8, 7, 8, 4, 5, 3, 3, 4, 7, 8, 9, 8]
    },
    {
        "city": "Bodrid",
        "temperatures": [12, 14, 114, 15, 14, 11, 10, 10, 1, 9, 9, 10, 8]
    },
    {
        "city": "Serlin",
        "temperatures": [283, 284, 285, 284, 286, 286, 283, 282, 281, 281, 280, 281, 282]
    },

]



def main_():
    my_list = ["David", "Ricky"]
    print(my_list)

    my_list.append("Stoyan")

    print(my_list)
    my_list.remove()
    del my_list[2]

    print(my_list)

def main():

    for city_temp in temperatures:
        print(city_temp['temperatures'])
        correct_temp = []
        skip_next = False
        for i, t in enumerate(city_temp['temperatures']):
            #analysis for temperature
            if i > 0:
                if not skip_next:

                    delta = t - city_temp['temperatures'][i-1]
                    print(t - city_temp['temperatures'][i-1])
                    if delta < abs(5):
                        correct_temp.append(t)
                    else:
                        skip_next = True
                else:
                    correct_temp.append(t)
                    skip_next = False
            else:
                correct_temp.append(t)
        print(correct_temp)

        city_temp["corrected_temperatures"] = correct_temp
        input("next?")


    print(temperatures)

if __name__ == '__main__':
    main()