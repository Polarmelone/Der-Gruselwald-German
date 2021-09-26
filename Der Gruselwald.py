import time
import random as rnd

damage = rnd.randint(1,5)

print ("Das Spiel Startet in kürze ...")
time.sleep(1)
print ("...loading...")
time.sleep(1)
print ("... Willkommen im Gruselwald ...")
time.sleep(1)
print ("Bitte achte beim Schreiben auf deine Rechtschreibung...")
time.sleep(1)

answer = input("Du stehst vor einer Abzweigung, wohin gehst du? (rechts/links) ")

if answer.lower().strip() == "rechts":

    answer = input("Vor dir steht in Oga, was tust du? (rennen/kämpfen)")
    time.sleep(1)
    if answer == "rennen":
        answer = input ("Puh Glück gehabt, du konntest entkommen. Ein Magier ist erschienen und fordet dich auf ihm deine Socken zu geben. (geben/nicht geben)")
        
        if answer == "geben":
            answer = input ("Als dank für die Socken gibt er dir einen alten Zauberstab. Möchtest du zurück zum Oga oder dem Pfad folgen? (zurück/folgen)")
                
            if answer == "folgen":
                    answer = input ("Du hast Hunger und musst etwas essen, vor dir ist ein Busch mit Beeren und ein Vogel. Was ist du? (beeren/vogel)")
                    
                    if answer == "vogel":
                        answer = input ("Du benutzt deinen Zauberstab und brätst den Vogel, du kannst ihn direkt essen. Ein kleiner Zwerg erscheint neben dir und möchte essen. Gibst du ihm etwas? (geben/behalten)")

                        if answer == "geben":
                            answer = input ("Er bedankt sich freundlich und fragt dich ob du zu ihm nachhause gehen willst (nein sagen/ja sagen)")

                            if answer == "nein sagen":
                                answer = input ("Er zieht einen Dolch... du rennst los und er versucht dir zu folgen. Aufgrund seiner Größe kommt er jedoch nicht hinterher. Du siehst ein Schild auf dem Ausgang steht möchtest du ihm folgen (folgen/nicht folgen)")

                                if answer == "nicht folgen":
                                    answer = input ("Du folgst dem Weg... am Ende des Weges zeigt sich der Ausgang des Waldes...")
                                    time.sleep(1)
                                    print ("... du hast gewonnen!!!")

                                else:
                                    print ("Du versinkst bis zum Bauch im Treibsand und dein Körper wirdvon Vögeln zerrupft... das Schild muss wohl falsch herum gehangen")
                                    time.sleep(1)
                                    print("Ende")

                            else:
                                if answer == "ja sagen" :
                                    answer = input ("Er läuft los und ihr begegnet einem verbitertem Kobold. Dieser sitzt in seinem Kessel voll Gold und lacht verrückt. Der Zwerg sagt zu dir, dass er das Gold stehlen will und das er deine Hilfe braucht (helfen/nicht helfen)")
                                
                                else:
                                    answer = input ("Er geht nach einer Weile los... du siehst eine Fee. Sie sagt dir, dass du ihr helfen musst verrät dir jedoch nicht wobei. (helfen/nicht helfen)")
                                    
                                    if answer == "nicht helfen":
                                        print ("Du läufst und stolperst über einen Stein und fällst eine Klippe hinunter. Du schlägst unten auf und stirbst")
                                        time.sleep(1)
                                        print ("Ende")

                                    else:
                                        print ("Sie geht mit dir weiter und stößt dich eine Klippe runter. Du schlägst unten auf und stirbst")
                                        time.sleep(1)
                                        print ("Ende")

                        else:
                            print ("Er ruft seine kleinen Zwergen Freunde und sie atackieren dich. Gegen so viele hast du keine Chance sie vernichten dich")
                            time.sleep(1)
                            print ("Ende")


                    else:
                        print ("Du pflückst dir die Beeren und ist sie. Es waren giftige Vogelbeeren, welche dich langsam und qualvoll sterben lassen")
                        time.sleep(1)
                        print ("Ende")
            else:
                answer = input ("Du kommst zurück zum Oga und er versucht dich anzu greifen (mit der Faust kämpfen/mit dem Zauberstab kämpfen)")
                
                if answer == "mit dem Zauberstab kämpfen" :
                    print ("WOW!!! Du konntest ihn besiegen. *Du erhältst seine Keule und Fleisch*")
                
                    answer = input ("Du siehst einen Zwerg, er sagt er hätte Hunger. Er fragt dich unhöflich nach Essen (geben/nicht geben)")
                    
                    if answer == "geben" :
                        answer = input ("Er bedankt sich freundlich und fragt dich ob du zu ihm nachhause gehen willst (nein sagen/ja sagen)")
                        
                        if answer == "ja sagen":
                            answer = input ("Er versucht dich einzusperren und zu töten. Du entkommst jedoch und stehst hinter ihm. Was tust du? (ihn töten/rennen)")

                            if answer == "ihn töten":
                                answer = input ("In seiner Leiche findest du eine Karte (der Karte folgen/der Karte nicht folgen)")

                                if answer == "der Karte folgen":
                                    print ("Die Karte führt dich zum Ende des Waldes... ")
                                    time.sleep(1)
                                    print ("... du hast gewonnen!!!")
                                
                                else:
                                    print ("Du bist verärgert über das geschehen und versuchst zum Anfang des Waldes zu laufen... jedoch stolperst du in eine Fütze und ertrinkst")
                                    time.sleep(1)
                                    print ("Ende")
                            
                            else:
                                print ("Du verirrst dich und verdurstest jämmerlich")
                                time.sleep(1)
                                print ("Ende")
                        
                        else:
                            print ("Du verirrst dich und verdurstest jämmerlich")
                            time.sleep(1)
                            print ("Ende")
                    else:
                        print ("Er zieht einen Dolch und ersticht dich")
                        time.sleep(1)
                        print ("Ende")
                
                else:
                    print (damage)
                    print ("damage")

                    if damage > 5 :
                        print ("gewonnen")
                    else:
                        print ("Du bist noch zu schwach")
                        time.sleep(1)
                        print ("Er greift nach seiner Keule und erschlägt dich...")
                        time.sleep(1)
                        print ("Ende")
                        
                

        else:
            print ("Er zieht seinen Zauberstab und verflucht dich mit einem Lähmungszauber")
            time.sleep(3)
            print("Ende?")
            time.sleep(1)
            
            answer = input ("Nach mehreren Stunden kannst du dich langsam wieder bewegen. Der Zauberer hat dir alles weggenommen... du hörst ein Geräusch rennst du weg? (wegrennen/hingehen)")
            if answer == "hingehen":
                
                answer = input ("Es ist eine schlafender Troll mit einer Magischen Kugel neben sich. Klaust du die? (klauen/wegrennen)")
                if answer == "klauen":
                    print ("Du schüttelst die Kugel und wirst aus dem Wald teleportiert... ")
                    time.sleep(1)
                    print ("... du hast gewonnen!!!")

                else:
                    print ("Das Gift ist noch nicht vollständig aus deinem Körper gewichen... kippst um und schlägst dir den Kopf auf")
                    time.sleep(1)
                    print ("Ende")

            else:
                print ("Das Gift ist noch nicht vollständig aus deinem Körper gewichen... kippst um und schlägst dir den Kopf auf")
                time.sleep(1)
                print ("Ende")
    else:
        print (damage)
        print ("damage")

        if damage > 5 :
            print ("gewonnen")
        else:
            print ("Du bist noch zu schwach")
            time.sleep(1)
            print ("Er greift nach seiner Keule und erschlägt dich...")
            time.sleep(1)
            print ("Ende")

else:
    print("Du wirst von einem einem herabfallendem Ast erschlagen...")
    time.sleep(1)
    print ("Ende")
