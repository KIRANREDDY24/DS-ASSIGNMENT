from matplotlib import pyplot as plt
import csv
with open("extreme.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    plt.style.use("fivethirtyeight")
    tra, top, gra, tim, att, sou = [], [], [], [], [], []

    nooftrainers, nooftopic, noofgrade, nooftimeslot, noofattendance, noofsource = [], [], [], [], [], []
    trainers = ['#N/A', 'FAC_5002', 'FAC_5003', 'FAC_5006', 'FAC_5008', 'FAC_5009', 'FAC_5011', 'FAC_5012', 'FAC_5013', 'FAC_5015', 'FAC_5016', 'FAC_5017', 'FAC_5019', 'FAC_5020', 'FAC_5022', 'FAC_5024', 'FAC_5025', 'FAC_5026', 'FAC_5027', 'FAC_5028', 'FAC_5029', 'FAC_5031', 'FAC_5036', 'FAC_5038', 'FAC_5039', 'FAC_5044', 'FAC_5046', 'FAC_5052']
    topic = ['Category Spin', 'In my head or real?', 'Structure of a story', 'Word Whiz', 'Spelling Star', 'Play with Punctuations', 'Sum it up', 'Rocking with Rhymes', 'Name it', 'Making Connections', "In my mind's eye"]
    grade = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4']
    timeslot = ['11:15 am', '11:45 am', '4:00 pm', '6:00 pm', '6:15 pm']
    attendance = ['Present', '', 'Absent', 'Cancelled']
    source = ['lastchance', 'TEB2ASMS', 'ntfpush', 'T1KRMSMS', 'rfmsms', 'TEB11SMS', 'TEB3SMS', 'ntfuiuser', 'TEB12SMS', 'TEB4SMS', 'TEB5SMS', 'b1rmsms', 'b2rmsms', 'adarsh', 'b3rmsms']

    for i in spamreader:
        tra.append(i[2])
        top.append(i[3])
        gra.append(i[4])
        tim.append(i[6])
        att.append(i[8])
        sou.append(i[9])
    for j in trainers:
        nooftrainers.append(tra.count(j))
    for k in topic:
        nooftopic.append(top.count(k))
    for l in grade:
        noofgrade.append(gra.count(l))
    for m in timeslot:
        nooftimeslot.append(tim.count(m))
    for n in attendance:
        noofattendance.append(att.count(n))
    for o in source:
        noofsource.append(sou.count(o))

    # plt.barh(trainers, nooftrainers, color="#008fd5")
    # plt.barh(source, noofsource, color="#008fd5")
    # plt.barh(topic, nooftopic, color="#008fd5")
    # plt.barh(grade, noofgrade, color="#008fd5")
    # plt.bar(timeslot, nooftimeslot, color="#008fd5")
    # plt.bar(attendance, noofattendance, color="#008fd5")
    print(nooftrainers, noofsource, nooftopic, noofgrade, nooftimeslot, noofattendance)

    #plt.tight_layout()
    #plt.show()
