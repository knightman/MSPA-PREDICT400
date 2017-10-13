
# coding: utf-8

# ## Probability Example in Game of Spades
# Version/Date: Oct 9, 2017
# 
# ### Exercise
# > PREDICT_400-DL_SEC56
# > Week4 Discussion
# 
# ### File(s)
# Probability_Example_Spades.ipynb
# 
# ### Instructions
# Find a recent article or blog that discusses probabilities in a specific board game or card game.  Refrain from choosing common betting games, such as Blackjack, Poker (any variation), etc. Summarize the article, the analysis of the probabilities involved, and reproduce the probabilities using Python.  Are you able to reproduce the probabilities?  Why or why not?  Be sure to share a link to or a copy of your article and your Python code and output.
# 
# ### Reference
# I will be referencing concepts regarding probability in card games from two Scientific American articles:
# <a href='https://www.scientificamerican.com/article/bring-science-home-cards-odds-probability/'>Suited Science</a>
# <a href='https://www.scientificamerican.com/article/puzzling-adventures-unrav/'>Unraveling Probability Paradoxes</a>
# 
# ### Description
# Growing up, my family always loved playing cards games together. We've played many types of card games over the years, almost always of the non-betting, trick-taking, partnership games. Some of the favorites included Eucher, Rummy, Hearts, Spades and probably the all-time favorite... Pinochle. 
# 
# For this week's excercise, I thought it would be fitting to take a look at basic probability questions for our favorite family card games. While I orignially wanted to try this exercise for pinocle, the number of articles was somewhat limtied and the rules of the game require a more complex application of the example program I intended to create.
# 
# As a compromise I've instead chosen to use the game of Spades. It is a great team-playing game that involves some inital probabilstic estimation of outcome based on what you have in your hand. However, it affords the possbility of looking at another probability characteristic covered inthe second of my two Scientific American articles. This explores the idea of changing the orignial question based on new information. This concept has gained somewhat mainstream understanding based on movies like '21' or 'Rainman'. However I will be using a simplified example applied in the game of Spades as it relates to the intiial bidding. A basic explanation of the rules of the game is given below.
# 
# The idea is to consider differnt probabilities based on new information as it becomes availble to the bidder. This concept is commonly referred to the Monty Hall problem from the show Let's Make a Deal. It's also known as the Three Prisoners problem. My goal is to try to highlight this during the bidding process of Spades using the code below.

# ### A Breif Overview of Spades
# 
# Official instructions and more details can be found here:
# https://en.wikipedia.org/wiki/Spades
# 
# Spades are always trump and teams gain points basedon who can most accurately predict the number of tricks their team will take in each successive hand played. The team that obtains the most number of points first, wins.
# 
# As with many of the family card games we play, I'm sure the rules have deviated from the norm, however the bidding process is relatively standard in Spades. For the purposes of this example, I will be assuming it is played by four people, made up of two teams (called Partnership Spades) using a standard 52-card deck (jokers removed). 
# 
# I will be considering the three phases of the bidding process, before card play actually begins. I will look at different player perspectives in this process. The goal in most cases is to try to bid a 'Nil' due to the fact that the most number of points you can obtain in single hand requires the player to bid, and sucessfully play otu a 'Nil' hand. This basically means that the indiidual player does not expect to take any tricks, and will thus play his or her cards out that way. The three phases could be described as guessingt the number of tricks he or she expects to take at these points... 1. before the card are dealt, 2. after looking at their cards, 3. after hearing what others bid (assuming they are not the first to bid). We will also be ignoring concept of 'blind bids'.
# 
# 

# In[3]:


# Represent the players like this:
#
#          partner
#
# player2          player1
#
#            me
#
# All cards are dealt, which gives 13 cards per player
# Cards represented by integers like this...
# 1=A, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=10, 11=J, 12=Q, 13=K

import numpy as np

# Let's represent some probabilities now
carddeck = range(1,53,1)
spades = carddeck[0:13]
hearts = carddeck[13:26]
clubs = carddeck[26:39]
diamonds = carddeck[39:52]

# Create sets for probability calcs
allS = set(spades) # len(allS) = 13
allH = set(hearts) # len(allH) = 13
allC = set(clubs) # len(allC) = 13
allD = set(diamonds) # len(allD) = 13
U = set(carddeck)
print('Sets:\nS= ' + str(allS) + '\nH= ' + str(allH) + '\nC= ' + str(allC) + '\nD= ' + str(allD) + '\nU= '+ str(U))

# notN - represents set of J, Q, K, or A of Spades, or high Spades
highS = set([11,12,13,1])
print('highS is' + str(highS))
fourS = set([2,3,4,5])  # i think this can really be any four numbers between 2 and 10 that represent four spades
print('fourS is ' + str(fourS))

# GAME SETUP
player_table = ['partner', 'player1', 'me', 'player2']
dealer = player_table[0]
handsplayedcount = 1
print('\nBEGIN GAME')
print('Initial player order: ' + str(player_table))
print('Initial dealer: ' + str(player_table[0]))
print('Inital bid order: you bid second \nCARDS ARE SHUFFLED AND DEALT')

# FUNCTIONS
def card_from_setindex(index):
    # my lazy way of giving names to the set-indexed cards dealt from pseudo-random deck
    cardindex = ['', 'A of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', 
             '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', 
             'A of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', 
             '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 
             'A of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', 
             '8 of Clubs','9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 
             'A of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', 
             '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds']
    return str(cardindex[index])

def draw_card():
    return np.random.randint(1,52)
    #old code
    #suits = ['null', 'spades', 'hearts', 'clubs', 'diamonds']
    #cards = ['null', 'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    #the_card = [cards[np.random.randint(1,13)], suits[np.random.randint(1,4)]]
    #return the_card

def play_next_hand():
    player_table.append(player_table.pop(0))
    dealer = player_table[0] #player_table[0] is always current dealer
    print('The new player order is ' + str(player_table))
    print('The new dealer is ' + str(player_table[0]))
    if my_bid_turn() == 1:
        print('You bid first\nCARDS ARE SHUFFLED AND DEALT')
    elif my_bid_turn() == 2:
        print('You bid second\nCARDS ARE SHUFFLED AND DEALT')
    elif my_bid_turn() == 3:
        print('You bid third\nCARDS ARE SHUFFLED AND DEALT')
    else:
        print('You are the dealer and you bid last\nCARDS ARE SHUFFLED AND DEALT')

def my_bid_turn():
    return player_table.index('me')

def deal_my_hand():
    tmplist = []
    while len(tmplist) < 13:
        tmpcard = draw_card()
        try:
            tmplist.index(tmpcard)
            # do nothing because it already is in list, cant have same card twice
        except ValueError:
            # does not exist already in tmplist, so add it
            tmplist.append(tmpcard)
    mycardhand = tmplist
    return mycardhand

def you_should_go_nil():
    '''This function assumes a conservative bidding strategy :) '''
    go_nil = True  # decision var; start with True and switch to False if any of the face card conditions require it
    
    # A of Spades?
    if myhand.count([1]) > 0:
        go_nil = False
        print('you have the A of Spades... cannot go Nil')
    
    # K of Spades?
    if myhand.count([13]) > 0:
        go_nil = False
        print('you have the K of Spades')
    
    # Q of Spades?
    if myhand.count([12]) > 0:
        go_nil = False
        print('you have the Q of Spades')
    
    # J of Spades?
    if myhand.count([11]) > 0:
        go_nil = False
        print('you have the J of Spades')
    
    # Total spades in my hand?
    spadesinmyhand = 0
    for card in myhand:
        if card <= 13:
            spadesinmyhand += 1
    
    if spadesinmyhand <= 3 and go_nil:  # go_nil is still true and less than three spades
        print('you only have ' + str(spadesinmyhand) + " spades and no high spades, you should be able to go Nil")
        return go_nil
    else:  # do not go nil
        print('you have ' + str(spadesinmyhand) + " spades and/or at least one high Spade, you should NOT go Nil")
        return False


# In[20]:


# Note: If you have the A of Spades, it is impossible, you must bid at least one
# The following probability rules should be applied to other Spades in your hand.
#
# For the purposes of this simplified example, let's assume you can/should
# go Nil only if the following two conditions exist:
# 1. You do NOT have the Ace, King, Queen or Jack of Spades
# 2. You do not have more than two spades total
#
# These two conditions will generally ensure a safe Nil bid. In this first scenario we will 
# only consider what is in your hand, later we will consider other bids to see if that changes
# the probability of achieving your Nil bid, or ensuring your partner's Nil bid.

# According to our rules above, blind knowldge prob is given by
noNil = set(highS | fourS) #union of the two conditions that result in a bid other than Nil
oddsNoNil = round(len(noNil)/float(len(U-noNil)),3)
print('P(that you will have a Nil-capable hand) on any given hand according to our rules above is approx: '+ str(oddsNoNil))

# Time to deal the cards
myhand = deal_my_hand()   # myhand is the set of ints representing my cards from the deck
#print('My hand in numbers' + str(myhand) + '\n')
prettyhand = [] # show the hand in pretty print, rather than index numbers
for item in myhand:
    prettyhand.append(card_from_setindex(item))

# Now you look at your cards and see if you can go 'Nil', meaning take zero tricks
print('\nNow, looking at the cards in my hand...\nMy playing hand is ' + str(prettyhand) + '\n')
should_go_nil = you_should_go_nil() # function to determine if you should bid Nil or not
print('\nWait! Before you make your bid, lets consider the first bid from player1...')

# player1 bids before you, simulated first bid is...
def other_player_bid():
    return np.random.randint(0,4)

player1bid = other_player_bid()
print('player1 bids ' + str(player1bid) + '\nNow, your turn to bid...')


# In[29]:


# To assess the current situation for my bid, I should be asking three questions:
# Part 1. If I DO bid zero, what is the probability that my partner will be able to cover me?
# Part 2. If I do NOT bid zero, what is the probability that my partner can bid zero given only what I know about my hand?
# 3. Based on player1's bid (and the assumption that their bid is based on same rules above), do the probabilities change?

if you_should_go_nil():  #Part 1
    # Find the the following probability scenarios about my partner's hand
    # 1. that he/she has AT LEAST ONE high spades
    cardsNotInMyHand = U - set(myhand)  # this is the compliment of myhand set
    oddsOfFirst = round(len(cardsNotInMyHand & highS)/float(3*len(U-(cardsNotInMyHand & highS))),3)
    print('Odds of first test: ' + str(oddsOfFirst))
    # 2. that he/she has MORE THAN THREE total spades
    oddsOfSecond = round(len(cardsNotInMyHand & fourS)/float(3*len(U-(cardsNotInMyHand & fourS))),3)
    print('Odds of second test: ' + str(oddsOfSecond))
    # 2. that he/she meets both conditions
    oddsOfThird = round(len(cardsNotInMyHand & (fourS & highS))/float(3*len(U-(cardsNotInMyHand & (fourS & highS)))),3)
    print('Odds of third test: ' + str(oddsOfThird))
    # Now test taking into account the bid from player1, to do this let test to see if they bid 1 or more
    # This would indicate they likely have highS
    if player1bid > 0:
        oddsWithPlayer1Bid = round(len(cardsNotInMyHand & highS)/float(2*len(U-(cardsNotInMyHand & highS))),3)
        print('Odds conditional on player1 bid of at least one: ' + str(oddsWithPlayer1Bid))
else:                 #Part 2
    # Probability that he/she has a hand that can be safely played as Nil given the rules above
    oddsOfPartnerNil = round(len(cardsNotInMyHand & (fourS | highS))/float(len(U-(cardsNotInMyHand & (fourS | highS)))),3)
    print('\nOdds of your partner being able to go Nil given what is in your hand: ' + str(oddsOfPartnerNil))


# In[131]:


# Play second hand
# now we move to the next hand and repeat the scenarios
play_next_hand()

