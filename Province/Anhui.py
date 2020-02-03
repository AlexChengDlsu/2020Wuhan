### Project: 2020Wuhan@Github/Ginchung
## File: Template.py
## Run with 'python Template.py'

# object 'sdct'
# Function: stores the info from official message
# Key: YYYY-MM-DD-HH

province='beijing'

sdct={}
sdct['2020-01-22-16']='合肥市3例、六安市1例'
sdct['2020-01-23-10']='合肥市5例、六安市1例、滁州市1例、阜阳市1例、亳州市1例'
sdct['2020-01-24-00']='合肥市6例、六安市2例、阜阳市2例、滁州市1例、亳州市1例、安庆市1例、池州市1例、蚌埠市1例'
sdct['2020-01-25-00']='合肥市10例，铜陵市3例、六安市2例、阜阳市7例、滁州市2例、马鞍山市4例、亳州市4例、安庆市4例、池州市1例、芜湖市1例、蚌埠市1例'
sdct['2020-01-26-00']='合肥13例、阜阳10例、马鞍山7例、亳州6例、安庆5例、芜湖3例、六安3例、铜陵3例、宿州2例、滁州2例、宣城1例、淮北1例、淮南1例、池州1例、蚌埠1例、黄山1例'
sdct['2020-01-27-00']='合肥13例、阜阳10例、安庆8例、马鞍山7例、亳州6例、芜湖6例、六安3例、铜陵3例、宿州3例、蚌埠3例、滁州2例、淮南2例、宣城1例、淮北1例、池州1例、黄山1例'
sdct['2020-01-28-00']='阜阳21例、合肥16例、马鞍山10例、芜湖9例、铜陵9例、安庆8例、亳州8例、黄山4例、滁州4例、六安4例、宿州3例、蚌埠3例、淮南2例、宣城2例、淮北2例、池州1例'
sdct['2020-01-29-00']='合肥29例、淮北2例、亳州15例、宿州9例、蚌埠3例、阜阳23例、淮南2例、滁州4例、六安6例、马鞍山11例、芜湖11例、宣城2例、铜陵9例、池州1例、安庆18例、黄山7例'
sdct['2020-01-30-00']='合肥39例、淮北2例、亳州20例、宿州10例、蚌埠8例、阜阳28例、淮南6例、滁州4例、六安8例、马鞍山14例、芜湖14例、宣城4例、铜陵10例、池州2例、安庆24例、黄山7例'
sdct['2020-01-31-00']='合肥50例、淮北2例、亳州20例、宿州10例、蚌埠15例、阜阳38例、淮南6例、滁州4例、六安9例、马鞍山14例、芜湖14例、宣城4例、铜陵14例、池州4例、安庆24例、黄山9例'
sdct['2020-02-01-00']='合肥59例、淮北6例、亳州25例、宿州12例、蚌埠16例、阜阳47例、淮南6例、滁州6例、六安13例、马鞍山22例、芜湖15例、宣城4例、铜陵16例、池州4例、安庆37例、黄山9例'
sdct['2020-02-02-00']='合肥59例、淮北6例、亳州30例、宿州14例、蚌埠26例、阜阳59例、淮南6例、滁州6例、六安13例、马鞍山27例、芜湖16例、宣城4例、铜陵16例、池州6例、安庆43例、黄山9例'
sdct['2020-02-03-00']=''

city=[]
latest='2020-02-02-00'
for i in sdct[latest].replace('，','、').split('、'):
    city.append(i[:2])

print('city of %s: '%province,city,'\n')    
print('number of infected cities now: ',len(city))

Table={}
for k,v in zip(sdct.keys(),sdct.values()):
    if len(v)<5:
        continue
    s=['0']*len(city)
    v=v.replace('，','、').replace('武汉','外地')
    for i in v.split('、'):
        tmp=''
        for t in i:
            if t.isdigit():
                tmp+=t
            #tmp=int(tmp)
            s[city.index(i[:2])]=tmp
        Table[k]=s
    print(s)

### Output
print(province,',',','.join(city))
for date,out in zip(Table.keys(),Table.values()):
    print(date,',',','.join(out))
