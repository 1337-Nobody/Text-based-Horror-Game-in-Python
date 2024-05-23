


while True:
    answer = input("Would you lIke to pLay a Game?"
                   "---Failure to "
                   "answer questions "
                   "in one word answers will "
                   "terminate the game---."
                   "(yes/no)?")

    if answer.lower().strip() == "yes":

        answer = input("You are a soldier. Before you went to sleep you"
                       "were with your squad mates. You have Awakened at an outpost camp"
                       " to find them missing. "
                       "  .SOMETHING.   You have a bAsic service rifle, a ration "
                       "and a basic first aid kit. You have walked   .0FF.   "
                       "onward along a war torn path in a valley that now comes to a fork."
                       "There are two paths. One on the left and one on the right."
                       " Which side do you pick?").lower().strip()
        if answer == "left":
            answer = input("You go onward upon the left path. You march along and take in your surroundings. as you are gazing you notice "
                           "a dark foreboding chunk of sentient mass marching towards you. It has crimson glowing eyes and "
                           "dark black cold steel for a body and stands at about seven feet."
                           "Do you try to run past or fight it?").lower().strip()
            if answer == "fight":
                    answer = input("You shoot at the automaton. This does nothing. This does nothing."
                                   "This does nothing. The automaton runs at you. It rips your"
                                   "arms off slowly like monzarella sticks being ripped in half. Gorgeously thick sweet "
                                   "meaty crimson pours "
                                   "forth, bEauTiful. press ENTER KEY to c0ntinue")
                    import winsound
                    winsound.PlaySound("Death Glitch.wav", winsound.SND_ASYNC)
            elif answer == "run":
                    answer = input("You run past the automaton. You think about how foolish it would have been to try to fight"
                                   "it alone. You run past it but it is too slow. You travel onward until you reach a cabin and go inside."
                                   "The door creaks open and a smell of pHOsPorus and sulFur inVAdes your nostrils. The wallpaper on the walls"
                                   "looks as if it has rotted. Black mold is to be seen everywhere. You notice what appears to be a HatTch. You"
                                   "go to go towards it and as you do a mortar shell rips half of the wall off to the left of you. "
                                   "The force of it makes you dRop YouR SeRvice Rifle. You slam open the "
                                   "hatch and lock it behind you. You find TW0 d00rS. One orange and one PuRple. Both with gray sTaIns. WhiCh 0nE DO Y0u "
                                   "Ch00se?").lower().strip()
                    if answer == "purple":
                        answer = input("You step through the door. It slams BeHiNd you. A coLd Drip of BlUe lanDs on YoUr lEfT shoulder"
                                       "YoU looK Up. . . . A HeAd Is fUsed InTo the wall with Yellow DaRk Eyes that OsCillate wiTh a Violent Purple."
                                       "Similar to a blue RinG octopus. The eyes like that of a PrEdaTor. A sinkHoLe of Dry waLl opens froM the "
                                       "FlOor. GiAnt taPe worm like CrEatures Rip and InvaDe youR fleSh. A sLOW pAiNful DeAth coNsumes You."
                                       "Press ENTER KEY to continue.")
                    elif answer == "orange":
                        answer = input("You step through the orange door. Outside air hits you. The warmth of the sun makes you feel calm."
                                       "You waLk up a hill. You walk up a hIll. You walk up a hill. Sweat. Heat."
                                       "You walk up a hill. You wAlk up a hill. You walk Up a HiLl. "
                                       "A BuLlet furiously whizzed passed your head as you were waLkinG"
                                       "You RuN. You RuN until You FinD a DiTch that is "
                                       "conSiderably D3EP You Spot a A WaLl left OvEr from dEbris of an Old house about 20 feet"
                                       "away from the DiTch. Do you jump in the DiTch or Run to the Wall?").lower().strip()
                        if answer == "ditch":
                                input("A barrage of bullets sling towards you in your direction."
                                  "You Jump into the Ditch. The firing stops after a few minutes. You"
                                  "Look down to notice that you have been hit by a bullet in the leg."
                                  "You use your Basic FiRst Aid Kit. Do yOU continue to wait or do you leave the "
                                  "ditch?").lower().strip()
                                if answer == "leave":
                                    input("You leave the ditch and go up a nearby trail. You continue onward. "
                                      "You march for what feels like hours. Eventually you reach a camp. "
                                      "The camp looks to be of the allies. You push open the tent flap."
                                      "YoUr EyEs BuRsT OpEn. Dirt and sweat drips from "
                                      "your head. You look at the covers on your body. Around you are combat "
                                      "nurses and a surgeon also near. You go To Sit Up and NoTice a wound in your abdomen"
                                      "the color slowly returns to you. The surgeon comes near you, surprised you did not "
                                      "die from being shot during the outpost camp ambush..."
                                      "Thank you for playing!"
                                      "Press ENTER key to play again." )
                                elif answer == "wait":
                                    input("After waiting for a while"
                                        "You leave the ditch and go up a nearby trail. You continue onward. "
                                      "You march for what feels like hours. Eventually you reach a camp. "
                                      "The camp looks to be of the allies. You push open the tent flap."
                                      "YoUr EyEs BuRsT OpEn. Dirt and sweat drips from "
                                      "your head. You look at the covers on your body. Around you are combat "
                                      "nurses and a surgeon also near. You go To Sit Up and NoTice a wound in your abdomen"
                                      "the color slowly returns to you. The surgeon comes near you, surprised you did not "
                                      "die from being shot during the outpost camp ambush..."
                                      "Thank you for playing!"
                                      "Press ENTER key to play again.")
                                else:
                                    input(" After waiting for a while"
                                          "You leave the ditch and go up a nearby trail. You continue onward. "
                                      "You march for what feels like hours. Eventually you reach a camp. "
                                      "The camp looks to be of the allies. You push open the tent flap."
                                      "YoUr EyEs BuRsT OpEn. Dirt and sweat drips from "
                                      "your head. You look at the covers on your body. Around you are combat "
                                      "nurses and a surgeon also near. You go To Sit Up and NoTice a wound in your abdomen"
                                      "the color slowly returns to you. The surgeon comes near you, surprised you did not "
                                      "die from being shot during the outpost camp ambush..."
                                      "Thank you for playing!"
                                      "Press ENTER key to play again.")
                        elif answer == "wall":
                            input("Your RuNning made you An Easy TaRget and multiple"
                                  " projectiles are fired with extreme prejudice."
                                  "You Die. Press ENTER KEY to continue.")

                        else:
                            input("You fail to make a decision in time and a bullet rips through your stomach leaving a large hole."
                                  "You bleed out slowly and die. Press ENTER KEY to continue.yes")
                    else:
                        input("A hole grows in the floor it swallows you and you sink it a BeAuTiful pO0l of WaRm ThiCk CrImSon"
                              "...and maggots. DeAth takes you. Press ENTER KEY to continue.")
            else:
                input("A confused look grows upon your face. Relax. Press ENTER KEY to continue.")
        elif answer == "right":
            answer = input("You go oNward towards the right path. You march along and take in your surroundings. As your eyes descend"
                           "from the treeline to the path you notice a dog is coming towards you. ThE fuR is vEry normAl. Do you attack or try to run "
                           "past it?").lower().strip()
            if answer == "attack":
                answer = input("You charge forth and kill the dog with two shots from your service rifle. The DoG"
                                   "emitss a SaD croaking GrOan. the dark BroWn fades into a bLack CoLor puRple"
                                   "REd Green ViolEnt ViolEt Brown fur covered in crimson life blood draining out."
                                   "Cryy Death."
                                   "onward along the path until you reach a cabin and go inside.The door creaks open and a smell of phosporus and sulfur inades your nostrils. The wallpaper on the walls"
                                   "looks as if it has rotted. Black mold is to be seen everywhere. You notice what appears to be a hatch. You"
                                   "go to go towards it and as you do a mortar shell rips half of the wall off to the left of you. You slam open the "
                                   "hatch and lock it behind you. You find two doors. One green, the other yellow, Both with gray sTaIns."
                                   "WhIHWch Do YoU ChOose?").lower().strip()
                if answer == "yellow":
                    input("You Open the Door...you step through and go gliding into a spaceless void of flashing colors. Bright Red, vIOLEnt Orange,"
                          "Purple, Neon, an explosion of brilliant flashes of a rainbow from hell. You realize the colors radiate a warmth. It feels"
                          "pleasant...until it doesn't. Slowly sweat starts to drip from you. You realize now that you are floating "
                          "in a violently changing void with no door to be found. You feel as if a fever is overtaking you now. "
                          "Your body temperature steadily rises. Blood drips out of your nose. You look down at your hands as the bright "
                          "colors pulse violently. Your skin is pale and turning paper white. You feel as if you are going to faint."
                          "Then, an explosion from the dark psychedelic void. DeAtH. . . . . . . . "
                          ". . . . . . Press ENTER KEY to continue.")
                elif answer =="green":
                    input("You open the door. The smell of sewer and feces burns your nostrils. A look of disgust comes over you as your eyes burn."
                          "You walk a long a concrete path, looking down you see the colors of the sewage flashing into different colors"
                          "as if something akin to an oily rainbow from hell. You come to a ladder and climb up it."
                          "You poke your head out of a manhole. You are in a city which is war torn, but flags of the home country can be found."
                          "You march a long the path of rubble until you spot a tank. a white z marks this as that of the Russian forces. "
                          "There is a ditch nearby and also a wall. You think to yourself if the wall or hiding in the ditch would be the "
                          "smartest thing to do. Which do you pick?").lower().strip()
                    if answer == "wall":
                        input("You run towards the wall, the tank notices you but you run past the wall and hide. "
                              "You wait for a few moments. You hear a loud explosion. the wall you were hiding behind violently"
                              "breaks. The force of which and the resulting bricks making "
                              "contact with your body violently slams you to the ground. "
                              "Chunks of shrapnel and brick have ripped your skin"
                              "and shattered your bones. You look across the war torn "
                              "plain as the blood leaks out of you. You close "
                              "your eyes and drift away. Press ENTER KEY to continue.")
                    elif answer == "ditch":
                        input("You run and jump into the ditch. YOu wait. You wait. You wait." 
                                   "You wait until you hear the tank rumble away. the sound is similar" 
                                   "to that of an angry school bus. You wait a whole hour to be sure."
                              "afterwards you get up and walk some more. What seems like an hour passes "
                              "until you reach what seems to be a medical tent. It seems to be of the allies."
                              "you open the tent flap. . . . . . . . . . "
                              ". . . . . . . . . . . . Your eyes bust open. "
                              "sweat drips down your face along with a bit of dirt. panicked you sit up. you realisze"
                              "you are in a makeshift hospital bed in a military hospital made quickly near a combat zone."
                              "combat nurses and a surgeon are near you. You notice a wound in your abdomen that is covered "
                              "in bandages. The surgeon comes over you. He is surprised to see that you have finally woken up"
                              "after having had your outpost camp ambushed. "
                              ""
                              ""
                              ""
                              ""
                              ""
                              "thank you for playing!"
                              ""
                              ""
                              "Press ENTER KEY to play again.")
                    else:
                        print("You fail to react in time and the tank violently explodes your body and everything within "
                              "a five feet radius of it.")
                else:
                    print("A hole grows in the floor. it swallows you and you sink into a BeAuTiful pO0l of WaRm ThiCk CrImSon"
                              "...and maggots...you choke to death. DeAth takes you. Press ENTER KEY to continue.")
            elif answer == "run":
                answer = input("You go to run past the dog and it mauls you. The Dark Black eyes with a hint"
                                   "of BloOd Crimson gaze with lUSt of Gore. It DeVours yOUR FLES-h to get to your"
                                   "soul.It eats it. press ENTER to continue")
            else:
                print("A confused expression coMes acr0ss your face. press ENTER KEY to continue")
        else:
            print("A Confused eXpression comes across y-0ur face. Press ENTER KEY to continue")
    else:
        print("PItY.")
        break


