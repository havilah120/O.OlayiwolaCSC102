girls = ["Samantha","Jada","Jane","Claire","Elizabeth","Mary","Susan","Waje","Taibat","Lilian"]
boys = ["Charles","Jude","James","Kelvin","Biodun","Wale","Kunle","Matthew","Tom","Kayode"]
age_1 = [17,16,17,18,16,18,17,20,19,17]
age_2 = [19,16,18,17,20,19,16,18,17,19]
height_1 = [5.5, 6.0, 5.4, 5.9,5.6,5.5,6.1,6.0,5.7,5.5]
height_2 = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
scores_1 = [80,85,70,60,76,66,87,95,50,49]
scores_2 = [74,87,75,68,66,78,87,98,54,60]
print("Names         |  age  |  height | scores")
for i in range(len(girls)):
    print(girls[i],  "|",age_1[i],"|",height_1[i],"|",scores_1[i])
    print(boys[i],   "|",age_2[i],"|",height_2[i],"|",scores_2[i])
