points=0
def battingpoints(x):
    runs=x['runs']
    strike_rate=runs/x['balls']
    points=(runs//2)+(5 if runs>=50 else 0)+(10 if runs>=100 else 0)+(2 if strike_rate>=80/100 and strike_rate<=1 else 0)+(4 if strike_rate>100 else 0)+x['4']+x['6']*2
    return points
    return {'name':x['name'],'battingpoints':points}


points=0
def bowlingpoint(x):
    wkts=x['wkts']
    economy=x['runs']/x['overs']
    fields=x['field']
    points=(10*fields if fields>=1 else 0)+10*wkts+(5 if wkts>=3 else 0)+(10 if wkts>=5 else 0)+(4 if economy>3.5 and economy<4.5 else 0)+(7 if economy>2 and economy<=3.5 else 0)+(10 if economy<2 else 0)
    return points
    return {'name':x['name'],'bowlingpoints':points}
