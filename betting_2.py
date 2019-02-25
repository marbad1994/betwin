def main(e_odds,x_odds, t_odds, x_bet):
    if e_odds < t_odds:
        bets = []
        #x_bet = 1000
        bonus = x_bet
        x_total = x_bet + bonus
        if bonus == 500:
            e_from = 1000
            e_to = 4000
            t_from = 200
            t_to = 1500
        if bonus == 1000:
            e_from = 2000
            e_to = 7000
            t_from = 500
            t_to = 3000
        if bonus == 2000:
            e_from = 5000
            e_to = 20000
            t_from = 800
            t_to = 6500
        if bonus == 2500:
            e_from = 6000
            e_to = 25000
            t_from = 1000
            t_to = 7500
    
        for i in range(e_from,e_to):#[::5]:    
            for n in range(t_from,t_to):#[::5]:
                t_total = n
                e_total = i

                vinst_e = (e_total * e_odds) - x_bet - t_total - e_total
                vinst_x = (x_total * x_odds) - e_total - t_total - x_bet
                vinst_t = (t_total * t_odds) - e_total - x_bet - t_total 
                if vinst_t >= 0 and vinst_e > 0 and  vinst_x == 0:
            
                    betting =  "Bet " + str(i) + " SEK on 1 and " +str(n) + " SEK on 2"
                    bets.append([vinst_e, vinst_x, vinst_t, betting])
    
        if bets != []:
            return sorted(bets, key=lambda x: x[0])[-1]
        else:
            return ["Inget resultat", "","",""]
    else:
        bets = []
        #x_bet = 1000
        bonus = x_bet
        x_total = x_bet + bonus
        #e_odds = 6.45 
        #x_odds = 4.2
        #t_odds = 1.63
        if bonus == 500:
            t_from = 1000
            t_to = 4000
            e_from = 200
            e_to = 1500
        if bonus == 1000:
            t_from = 2000
            t_to = 7000
            e_from = 500
            e_to = 3000
        if bonus == 2000:
            t_from = 5000
            t_to = 20000
            e_from = 800
            e_to = 6500
        if bonus == 2500:
            t_from = 6000
            t_to = 25000
            e_from = 1000
            e_to = 7500
    
        for i in range(t_from,t_to):#[::5]:    
            for n in range(e_from,e_to):#[::5]:
                e_total = n
                t_total = i

                vinst_e = (e_total * e_odds) - x_bet - t_total - e_total
                vinst_x = (x_total * x_odds) - e_total - t_total - x_bet
                vinst_t = (t_total * t_odds) - e_total - x_bet - t_total 
                if vinst_t > 0 and vinst_e >= 0 and  vinst_x == 0:
            
                    betting =  "Bet " + str(n) + " SEK on 1 and " +str(i) + " SEK on 2"
                    bets.append([vinst_e, vinst_x, vinst_t, betting])

        if bets != []:
            return sorted(bets, key=lambda x: x[2])[-1]
        else:
            return ["Inget resultat", "","",""]
if __name__ == '__main__':
    main()
