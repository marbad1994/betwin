def odds_calc(e_odds,x_odds, t_odds, x_bet):
        bets = []
        #x_bet = 1000
        x_bet = x_bet/2
        bonus = x_bet
        x_total = x_bet + bonus
        #e_odds = 6.45 
        #x_odds = 4.2
        #t_odds = 1.63
        for i in range(15000)[::2]:    
            for n in range(15000)[::2]:
                e_total = n
                t_total = i

                vinst_e = (e_total * e_odds) - x_bet - t_total - e_total
                vinst_x = (x_total * x_odds) - e_total - t_total - x_bet
                vinst_t = (t_total * t_odds) - e_total - x_bet - t_total 
                if vinst_t > x_bet and vinst_e > x_bet and  vinst_x == 0:
            
                    betting =  "Bet " + str(n) + " SEK on 1 and " +str(i) + " SEK on 2"
                    bets.append([vinst_e, vinst_x, vinst_t, betting, n, i])

        if bets != []:
            return [sorted(bets, key=lambda x: x[0])[-1], sorted(bets, key=lambda x: x[2])[-1]]
        else:
            return [["Inget resultat", "","",""], ["Inget resultat","","",""]]
def main(e_odds,x_odds,t_odds,bonus):
    bet_list = list(odds_calc(e_odds, x_odds, t_odds, bonus))
    one_win = bet_list[0]
    two_win = bet_list[1]
    if one_win[0] == "Inget resultat":
        print "Inget resultat"
    else:
        print "bet " + str(one_win[4] + two_win[4]) + " on 1"
        print "bet " + str(one_win[5] + two_win[5]) + " on 2"
        print "win " + str(one_win[0] + two_win[0]) + " if one wins and " + str(two_win[2] + one_win[2]) + " if two wins"
if __name__ == '__main__':
    main(5.25,4.05,1.75,1000)
