def salaire_mensuel(salaire_annuel):
    salaire_mensuel=salaire_annuel/12
    return salaire_mensuel
def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire=salaire_mensuel/4
    return salaire_hebdomadaire
def salaire_horaire(salaire_hebdomadaire,heures_travailles):
    salaire_horaire=salaire_hebdomadaire/heures_travailles
    return salaire_horaire
salaire_annuel=int(input("Tapez votre salaire annuel: "))
heures_travail=int(input("Tapez le nombre d'heures de travail par semaine: "))

salaire_mensuel=salaire_mensuel(salaire_annuel)
salaire_hebdomadaire=salaire_hebdomadaire(salaire_mensuel)
salaire_horaire=salaire_horaire(salaire_hebdomadaire,heures_travail)

print(f"Votre salaire horaire est de: {salaire_horaire} dollars")