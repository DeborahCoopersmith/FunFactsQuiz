#FACTS GAME
#I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department.
import random
import Draw

#global variables
#69 true nature facts
list_natureTrue=["Acacia trees can warn each other of danger","Owls don't have eyeballs","In space, metal can weld on its own","There are 28 kinds of 'corpse flowers'","Baby giraffes use their butts as pillows","Heat is the deadliest weather condition","Cows kill more people than sharks","An extinct species of penguins was nearly 7-feet tall","Goats have accents","There's a fungus that bleeds","African buffalo herds make decisions by voting","The Low's pitcher-plant is a toilet and food source all in one","Our brains are shrinking","The Milky Way is set to collide with the Andromeda galaxy in about 3.75 billion years","The average person will grow 590 miles of hair in their lifetime","The King's holly plant reproduces by cloning","Saturn could float on water","Armadillos are bulletproof","Caffeine is a natural pesticide","Women blink more often than men","Mars has the solar system's biggest volcano","Humans eat only 200 types of plants","Your femur is stronger than concrete","Your femur is the largest and strongest bone in your body","Sloths only poop once a week","Black holes aren't actually black","Liquids can boil and freeze at the same time","The Iberian ribbed newt uses its own bones as weapons","Hurricanes release the energy of 10,000 nuclear bombs","Bamboo is the world's fastest growing plant","Your tongue is made up of eight muscles","Camels' humps are made up of fat, not water","The resurrection plant can rise from the dead","The ocean produces up to 85 percent of the Earth's oxygen","One Venusian Day can take 243 Earth days","The rock hyrax is related to the elephants ","Diamonds and pencils are made of the same material","One inch of rain equals 10 to 15 inches of snow"," DNA is flame retardant","Greenland sharks don't reach puberty until they're 150 years old","Glass is neither a liquid nor a solid","The first carrots grown were purple","Slow lorises are the only venomous primate","Female dragonflies play dead to avoid sex","A tiger's skin also has stripes","The Great Barrier Reef in Australia is the world’s largest reef system","The waste hierarchy or 3 R’s are (in order of importance) reduce, reuse and recycle","Around 75% of volcanoes on Earth are found in the Pacific Ring of Fire","The Killer Whale (Orca) is actually a type of dolphin","There are seven species of marine turtles","Marine turtles were alive when dinosaurs roamed the earth","Six types of marine turtles are threatened with extinction","Turtles do not have teeth","Turtle shells are made of over 50 bones fused together","There are 36 species of marine dolphins","There are dolphins in the Amazon River","A Bottlenose dolphin swallows a fish head first so the fish's spines don't catch in their throat","Bottlenose dolphins have the ability to recognise themselves in a mirror","The word 'jaguar' comes from the indigenous word 'yaguar', which means 'he who kills with one leap'","The jaguar is the third biggest cat in the world","There are 5 species of rhino","Male rhinos are called 'bulls' and females are called 'cows'","Most of the panda - its face, neck, belly, rump - is white to help it hide in snowy habitats","At 5 months old, giant pandas learn how to climb","Giant pandas spend 10-16 hours a day feeding","In 1386, a pig was executed in France","The largest land based mammals on Earth are elephants","Female lions are better hunters than male lions","Cows and horses sleep while standing up"]

#30 false nature facts
list_natureFalse=["The femur is the weakest bone in your body","The Orca is a whale", "Sharks kill more people than cows","There are fourteen species of marine turtle","Marine turtles were first discovered in 1980", "Turtles have teeth","1 in 12,000 marine turtle hatchlings make it to adulthood","There are 29 species of marine dolphins","Bottlenose dolphins can reach speeds of over 80 mph for brief periods","Dolphins have the least elaborate acoustic abilities in the animal kingdom","Cows have the ability to recognise themselves in a mirror","Frogs have been documented to use tools","Jaguars can be found in Siberia","The jaguar is the biggest cat in the world","Jaguars have longer legs compared to leopards","Jaguars are terrible swimmers","There are 15 species of rhino","White rhinos are white","Male rhinos are called 'cows' and females are called 'bulls'","Male rhinos are more sociable than female rhinos","A white rhino's horn grows 12cm every year","Rhinos have great vision","Rhinos have a terrible sense of smell","Giant pandas have horizontal slits for pupils.","Mother pandas abandon their cubs after the first week","At 9 months old, giant pandas learn how to climb","Giant pandas spend 4 hours a day feeding","Pandas primarily eat small animals","The largest land based mammals on Earth are rhinos","Male lions are better hunters than female lions"]

#81 true human facts
list_humanTrue=["Turkeys were once worshipped like gods","Paul Revere never shouted,'the British are coming!'","The Olympics used to award medals for Art","By the end of Prohibition in 1933, the federal poisoning program is estimated to have killed at least 10,000 people.","Napoleon was once attacked by a hoard of bunnies","Women were once banned from smoking in public","The US Government poisoned alcohol during the Prohibition","Forks were first introduced in Italy in the 11th Century","Forks were originally percieved to be sacrilegious","The Titanic's owners never said the Titanic was 'unsinkable'","The Cuban dictator was targeted to be killed 600 times","Cleopatra VII is a descendant of Alexander the Great's Macedonian general Ptolemy","Pope Gregory IV declared war on cats in the 13th Century","'Mary Had A Little Lamb' is based on true story.","Richard Nixon was an extremely talented musician","Lyndon B. Johnson gave interviews from the bathroom","In 1834, ketchup was sold as a cure for indigestion","Abraham Lincoln is in the Wrestling Hall of Fame","July 2 is the real American Independence Day.","Abraham Lincoln was a licensed bartender","George Washington never lived in the White House","The first $1 bill was issued during the Civil War in 1862","Thomas Edison did not invent the lightbulb","Benz patented the first automobile in 1886","George Washington owned a whiskey distillery","Ronald Reagan was deeply interested in astrology","George Washington never had wooden teeth","On July 4th, 1826, both U.S. presidents John Adams and Thomas Jefferson passed away","Norse explorer, Leif Erikson, was the first European to discover America","The witch trials in Salem, Massachusetts, lasted between February 1692 and May 1693","Benjamin Franklin complained about the bald eagle being chosen as the United States' national symbol","Walt Disney did not draw Mickey Mouse","The hat of choice for the 19th century cowboys was a bowler hat","The Protestant 'Separatists' left Holland because of too much religious freedom","John Appleseed is a real person","Walt Disney was cremated","On October 24th, 1929, the stockmarket crashed","U.S. president Zachary Taylor passed away after eating too many cherries and drinking milk at a Fourth of July party in 1850","Richard Nixon wanted to kill Washington columnist Jack Anderson","Andrew Jackson taught his parrot, Polly, to curse like a sailor","Calvin Coolidge owned a pair of lions","Calvin Coolidge had two lions he named Tax Reduction and Budget Bureau","A woman was elected to the U.S. Congress before women could even vote","The 19th Amendment which gave women the right to vote wasn't passed until August 18th, 1920","Augustus Caesar was the wealthiest man to ever live in history","Modern-day scientists believe Alexander the Great suffered from the neurological disorder Guillain-Barré Syndrome","In the Ancient Olympics, athletes performed naked","Julius Caesar was stabbed 23 times","The Colosseum was originally clad entirely in marble","The Colosseum was originally known as the Amphitheatrum Flavium","By the end of Prohibition in 1933, the federal poisoning program is estimated to have killed at least 10,000 people","Richard Nixon played 5 instruments","The world’s most successful pirate in history was a lady","Rasputin survived being poisoned and being shot","There were female Gladiators","The Vikings were the first people to discover America","The Luftwaffe had a master interrogator whose tactic was being as nice as possible","In Ancient Asia, death by elephant was a popular form of execution","When Marcus Crassus died, molten gold was poured down his throat","Marcus Licinius Crassus was known as the wealthiest man in Rome during his life","Germany uncovers 2,000 tons of unexploded bombs every year","In Ancient Greece, wearing skirts was manly","The UK government collected postcards as intelligence for the D-Day landings","A singing birthday card has more computer power in it than the entire Allied Army of WWII","Cleopatra’s reign was closer to the moon landings than the Great Pyramid being built","Shrapnel is named after its inventor","Since 1945, all British tanks are equipped with tea-making facilities","The Eastern Roman Empire’s weapon called Greek Fire was used in ship-mounted flamethrowers","An ancient text called the Voynich Manuscript still baffles scientists","A Japanese fighter pilot once dropped wreaths over the ocean to commemorate the dead from both sides","The saying “fly off the handle” originates from the 1800s","Fox Tossing” was once a popular sport","Captain Morgan was a real person","Genghis Khan was tolerant of all religions","Thomas Edison didn’t invent most of the stuff he patented","Albert Einstein turned down the presidency of Israel","Roman Emperor Caligula made one of his favorite horses a senator","The Leaning Tower of Pisa was never straight.","During the Great Depression, people made clothes out of food sacks","Lord Byron kept a bear in his college dorm","46 BC was 445 days long and is the longest year in human history"]

#31 false human facts
list_humanFalse=["By the end of Prohibition in 1933, the federal poisoning program is estimated to have killed at least 40,000 people.","Forks were first introduced in Italy in the 15th Century","The Titanic's owners said the Titanic was 'unsinkable'","The Cuban dictator was targeted to be killed 350 times","Cleopatra VII was fully Egyptian","Pope Gregory IV declared war on dogs in the 13th Century","Pope Gregory IV declared war on cats in the 18th Century","Richard Nixon played 8 instruments","In 1834, ketchup was sold as a cure for cancer","Abraham Lincoln was a doctor","George Washington lived in the White House","The first $1 bill was issued during the Revolutionary War","Thomas Edison invented the lightbulb","Benz patented the first automobile in 1790","Ronald Reagan did not believe in astrology","George Washington had wooden teeth","Christopher Columbus was the first European to discover America","Benjamin Franklin chose the United States' national symbol","Walt Disney drew Mickey Mouse","The Protestant 'Separatists' left Holland for religious freedom","John Appleseed is a made-up person","Walt Disney was cryogenically frozen","On December 24th, 1929, the stockmarket crashed","U.S. president Zachary Taylor passed away after eating too many apples and drinking milk at a Fourth of July party in 1850","The 19th Amendment which gave women the right to vote wasn't passed until August 18th, 1924","John Musk is the wealthiest man to ever live","Julius Caesar was stabbed 13 times","Lord Byron kept a tiger in his college dorm","Iceland has the world’s youngest parliament in history", "46 BC was 447 days long and is the longest year in human history","The shortest war in history lasted 68 minutes"]

#73 true sports facts
list_sportsTrue=["The World Cup is held every four years","The name of the original World Cup trophy is the Jules Rimet Trophy","Uruguay were the hosts for the first ever World Cup in 1930 ","2018 is the first ever World Cup to be hosted in Russia","Almost half of the world’s population, that’s 3.2 billion people, tuned in to the 2014 World Cup","Brazil is currently the nation to boast the most World Cup wins","Egyptian Goalkeeper, Essam El Hadary, is the oldest player to ever play in the World Cup at the age of 45","The oldest person to ever score a goal at a World Cup was Cameroonian player Roger Milla","The fastest ever World Cup goal took place only 10.89 seconds after kick off","In 1966, the World Cup trophy was stolen prior to the tournament and was missing for 7 days","Retired German striker Miroslav Klose is the World Cup’s highest total goal scorer","The dimples on a golf ball are designed to make it more aerodynamic","The modern Olympic gold medals are predominantly made from sterling silver","In 1971, Alan Shephard and Edgar Mitchell became the first people to play sport on the moon","The Olympic rings were designed by Baron Pierre de Coubertein in 1912","Ski Ballet used to be a competitive sport","The 1956 Summer Olympics were held in two countries","Major League Baseball umpires are required to wear black underwear while on the job in case they split their pants"," Ken Griffey Jr. was allergic to chocolate"," Ken Griffey Jr. hit 630 home runs during his career","Michael Jordan makes more money from Nike annually than all of the Nike factory workers in Malaysia combined","The silhouette on the NBA logo is Hall of Fame Laker Jerry West","The referee tossed a jump ball after every basket in basketball until 1937","In July of 1934, Babe Ruth paid a fan $20 for the return of the baseball he hit for his 700th career home run","Kareem Abdul-Jabbar collects rugs","The average life span of an MLB baseball is five to seven pitches","There are more than 350 dimples on a golf ball","In 1910, an incomplete forward pass earned teams a 15-yard penalty","The household wrench was invented by boxing heavyweight champion Jack Johnson in 1922","Tug of war was an Olympic event between 1900 and 1920","A Formula One car generates so much downforce that it can drive upside down on the roof of a tunnel","Michael Jordan was once one of the best high school pitchers in North Carolina","A microwaved baseball will fly farther than a frozen baseball","When pitched, the average MLB baseball rotates 15 times before being hit","The state sport of Maryland is jousting","Three consecutive strikes in bowling is called a turkey","Table tennis balls can travel off the paddle at 105.6 miles per hour","The original Stanley Cup was only seven-and-a-half inches high","The first baseball caps were made of straw","Prior to 1900, prize fights lasted up to 100 rounds","In 1935 Jesse Owens broke four world records in 45 minutes","Manute Bol's grandfather had 40 wives","People in nudist colonies play volleyball more than any other sport","Most NASCAR teams use nitrogen in their tires instead of air","Each year, 30,000 people are seriously injured by exercise equipment","The Los Angeles Lakers are popular in the Bahamas","At horse race tracks, the favorite wins about 30 (or less) percent of the time","A faceoff in hockey was originally called a puck-off or a face of the puck","A forfeited game in baseball is recorded as 9-0","Fishing is the biggest participant sport in the world","Boxing became a legal sport in 1901","More than 100 million people hold hunting licenses","The record for the most career innings in Major League Baseball is held by Cy Young with 7,356","Kite flying is a professional sport in Thailand","The very first Olympic race, held in 776 BC, was won by Corubus, a chef","Major League Baseball teams use about 850,000 balls per season","Basketball and rugby balls are made from synthetic material","Golf is the only sport played on the moon","Former umpire Bill Klem has the record for most games served with 5,368","The 1912 Olympics was the last time that gold medals were solid gold","Basketball legend Wilt Chamberlain never fouled out of a game","The Dallas Cowboys hired the NFL's first professional cheerleading squad in 1972","Deion Sanders was the first athlete to rap at a Pro Bowl musical gala in 1995","Billiards great Henry Lewis once sank 46 balls in a row","Racehorses have been known to wear out new shoes in one race","Honey is used as a center for golf balls","Baseballs were originally made from the foreskins of horses","The state sport of Alabama is figure skating","Boxing legend Rocky Marciano invented the fax machine","The NCAA required college football players to study during halftime until 1925","It is customary for jockeys to be paid in coins, no matter how large their winnings","The Stanley Cup was originally two stories tall but was deemed too difficult to transport","Golf balls were originally made from dried cow eyeballs"]

#30 false sports facts
list_sportsFalse=["The World Cup is held every two years","Brazil were the hosts for the first ever World Cup in 1930 ","2018 is the second World Cup to be hosted in Russia","Uruguay is currently the nation to boast the most World Cup wins","The fastest ever World Cup goal took place only 20.89 seconds after kick off","In 1970, the World Cup trophy was stolen prior to the tournament and was missing for 7 days","The dimples on a golf ball are designed to make it pretty","The modern Olympic gold medals are predominantly made from gold","The Olympic rings were designed by Picasso","The 1956 Summer Olympics were held in one country","The referee tossed a jump ball after every basket in basketball until 1967","In July of 1934, Babe Ruth paid a fan $200 for the return of the baseball he hit for his 700th career home run.","Kareem Abdul-Jabbar collects pens","The average life span of an MLB baseball is 10 pitches","The household wrench was invented by Kareem Abdul-Jabbar","The state sport of Maryland is curling","Three consecutive strikes in bowling is called a spare","The original Stanley Cup was eight inches high","The first baseball caps were made of fabric","Prior to 1900, prize fights lasted up to 200 rounds","People in nudist colonies play tennis more than any other sport","At horse race tracks, the favorite wins about 60 percent of the time","Boxing became a legal sport in 1911","Less than 100 million people hold hunting licenses","Kite flying is a professional sport in Canada","Major League Baseball teams use over 2 million balls per season","Baseballs were originally made from the foreskins of cows"," Boxing legend Rocky Pincus invented the telegram","The NCAA required college football players to study during halftime until 1965","The Stanley Cup was originally 10 inches"]

#what to say after they choose: congrats or sorry
congrats=["Great job!", "You're doing so well", "Look at you go!", "Impressive", "Bravo", "I believe in you!", "Amazing", "Awesome"]

sorry=["Better luck next time!","You can still do this","I believe in you","Get your head in the game","Shake it off! You got this","If you believe you can achieve","Practice makes perfect","You're going to do so well on the next question"]

def firstPage(): #title page showcasing the three categories: nature, history,sports
    Draw.clear()
    Draw.setBackground(Draw.ORANGE)
    Draw.setColor(Draw.WHITE)       #This shows the game title
    Draw.filledRect(300,25,300,50)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(20)
    Draw.setFontBold(True)
    Draw.string("Fun Facts Quiz",380,40)
    Draw.string("Choose a Category of Questions",295,125) #instructions
    Draw.setFontSize(10)
    Draw.string("Created by Deborah Coopersmith",10,10)
    showBoxFirstPage(200,"Nature",len(list_natureTrue),len(list_natureFalse))   #nature category
    showBoxFirstPage(400,"History",len(list_humanTrue),len(list_humanFalse))    #history category
    showBoxFirstPage(600,"Sports",len(list_sportsTrue),len(list_sportsFalse))   #sports category
    Draw.show()
 
    
    #client clicks the category they want
   
    while not Draw.mousePressed():    #wait for user to click
        pass                          #get click

    y=Draw.mouseY()
#depending on which area they click open up the category they want
    if y >= 225 and y <= (225+50):
        secondPage(list_natureTrue, list_natureFalse) #open nature category
        
    elif y>= 425 and y<= (425+50):
        secondPage(list_humanTrue, list_humanFalse)  #open history category

    elif y >= 625 and y <= (625+50):
        secondPage(list_sportsTrue, list_sportsFalse)  #open sports category
   
def showBoxFirstPage(y,string, sizeTrue, sizeFalse):   #creates the boxes that are on the first page
    Draw.setColor(Draw.DARK_GRAY) 
    Draw.filledRect(0,y+25,900,50)
    Draw.setColor(Draw.WHITE)
    Draw.setFontSize(20)
    Draw.setFontBold(True)
    Draw.string(string+"              "+"("+str(sizeTrue+sizeFalse)+" "+'Questions'+")",410,y+40) #shows the category and how many questions there are in each topic

   
#opens the page with questions  
#parameters for this function are the category's list of facts and list of lies and the facts/lies already asked
def secondPage(listFacts, listLies, list_QuestionsAskedAlready=[]): 
    numQuestions=10 #amount of rounds in the game
    totalRight=0   #this is the total amount the person gets right
    for quizQuestions in range (numQuestions): #run game 10 times
        totalRight+=oneRoundOfQuestions(listFacts, listLies,list_QuestionsAskedAlready) #increment total right if the client chose correctly 
    endGame(totalRight,numQuestions) #Once all the rounds are complete move on to the endGame function

#this function orchestrates a round of questions
#parameters for this function are the category's list of facts and list of lies and the questions already asked
def oneRoundOfQuestions(listFacts, listLies,list_QuestionsAskedAlready):
    Draw.clear()                   
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(28)
    Draw.string("Choose the fact that you think is false",180,20) #instructions
    #No fact or lie should be repeated throughout one game
    fact1=choosingAQuestion(listFacts,list_QuestionsAskedAlready) #fact 1
    fact2=choosingAQuestion(listFacts,list_QuestionsAskedAlready) #fact 2
    lie=choosingAQuestion(listLies,list_QuestionsAskedAlready)    #lie
    combined=[fact1,fact2,lie]
    random.shuffle(combined)   #shuffles the options so the lie isn't in the same place each time
    showQuestionBox(combined[0],100)   #shows client first choice
    showQuestionBox(combined[1],300)   #shows client second choice
    showQuestionBox(combined[2],500)   #shows client third choice
    
    validClick = False
    while validClick == False:
        while not Draw.mousePressed(): #wait until client clicks
            pass
      
        y=Draw.mouseY()  #find the y location of the mouse click. depending on where it is choose that box or do nothing until they click on a box
       
        if y >= 100 and y <= 200: #this means the client chose the first choice
            result=choosingAnAnswer(combined[0],lie) #result equals the return of 0 or 1 depending if their choice was the right answer
            while not Draw.mousePressed(): #wait until they click
                pass
            validClick = True
            
        elif y >= 300 and y<= 400:   #this means the client chose the second choice
            result=choosingAnAnswer(combined[1],lie) #result equals the return of 0 or 1 depending if their choice was the right answer
            while not Draw.mousePressed(): #wait until they click
                pass
            validClick = True
            
        elif y >= 500 and y <= 600:  #this means the client chose the third choice
            result=choosingAnAnswer(combined[2],lie)   #result equals the return of 0 or 1 depending if their choice was the right answer
            while not Draw.mousePressed():  #wait until they click
                pass
            validClick = True   
    return result #if client got the answer right returns a 1 if not a 0. this then gets incremented to total right
#the paremeters ensure that the random fact is being chosen from the right list and that there are no repeats of facts/lies asked
def choosingAQuestion(list_ofQuestions,list_QuestionsAskedAlready): 
    question=random.choice(list_ofQuestions) #question is the random choice from the list
    while question in list_QuestionsAskedAlready: #if it was already asked choose a different one
        question=random.choice(list_ofQuestions)
    list_QuestionsAskedAlready.append(question) 
    return question #the question gets returned to oneRoundOfQuestions function to be displayed

def choosingAnAnswer(combinedOrder, falseFact):  #this returns whether you got it right or wrong to totalRight 
    if combinedOrder==falseFact: #if client chose the lie return a 1 to result
        questionResults("Congrats",congrats)
        return 1
            
    else:   #if client chose the fact return a 0 to result
        questionResults("Sorry, wrong answer",sorry) 
        return 0
          
        
def showQuestionBox(question, y):    #this function shows the lie/fact in the right location to the client
    Draw.setColor(Draw.WHITE)  
    Draw.filledRect(0,y,6000,100)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(15)
    Draw.setFontBold(True)
    Draw.string(question,10,y+45) 
    
def questionResults(remark,saying):   #whether the client got it right or wrong
    Draw.clear()
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(35)
    Draw.setFontBold(True)
    Draw.string(remark,50,160) #says whether they succeeded or got it wrong
    Draw.setFontSize(20)
    Draw.string(random.choice(saying),50,210)  #give a saying from the global variable sorry if they were wrong or congrats if they were right
    Draw.setFontSize(15)
    Draw.string("Click anywhere to move on to the next question",50,310) #notify the client to move on to the next question or if this was their last question code moves on to endGame function
    Draw.show()     
      

#this function takes two parameters the number the client got right and the number of questions they were asked
def endGame(totalRight,numQuestions):   #after all the sets say game over and report score 
    if totalRight/numQuestions>.5: #if they were successful
        endGameScore("Great Job! You scored %d out of %d" %(totalRight,numQuestions),1)
        
    else: #if they were not successful
        endGameScore("Better luck next time! You scored %d out of %d" %(totalRight,numQuestions),0)
        
#this function takes two parameters the string that congratulates or encourages the client and the integer determines what the color the screen should be       
def endGameScore(string, integer):   
    Draw.clear()
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(20)
    Draw.setFontBold(True)
    Draw.string(string,60,180) #shows how many they go tight
    Draw.string("Click to move on to the next page",60,210) 
    
    if integer==0: #if integer is 0 shows red screen
        Draw.setBackground(Draw.RED) 
    else: #if integer 1 show green screen
        Draw.setBackground(Draw.GREEN)
    Draw.show() 
    while not Draw.mousePressed():     #wait until client clicks 
        pass
    Draw.clear()
    Draw.setFontSize(30)    #allow the client to play again
    Draw.string("Want to play again? If so, click on the screen",60,180) #client needs to click to restart game
    Draw.show()
    while not Draw.mousePressed(): #wait until the client clicks
        pass      
    

#this is the main function
def main():
    Draw.setCanvasSize(900,900)    #makes the canvas size 900 by 900
    while True: firstPage()    #client can play as many times as they like
main()