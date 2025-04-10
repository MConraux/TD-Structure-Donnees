# Créé par Administrateur, le 02/04/2025 en Python 3.7

###Exercice 1
class Polynomial:

    def __init__(self,coeff):
        self.coeff = coeff

    def __str__(self):


        terms = []
        for i, coef in enumerate(self.coeff):
            if coef != 0:
                if i == len(self.coeff) - 1:
                    if coef == 1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"{coef}")
                        elif i == 1:
                            terms.append(f"X")
                        else:
                            terms.append(f"X^{i}")

                    elif coef == -1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - X")
                        else:
                            terms.append(f"- X^{i}")

                    elif coef <0:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - {coef}*X")
                        else:
                            terms.append(f" - {coef}*X^{i}")
                    else:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"{coef}")
                        elif i == 1:
                            terms.append(f"{coef}*X")
                        else:
                            terms.append(f"{coef}*X^{i}")
                    return "".join(reversed(terms)) if terms else "0"
                else:
                    if coef == 1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"+ {coef}")
                        elif i == 1:
                            terms.append(f"+ X")
                        else:
                            terms.append(f"+ X^{i}")

                    elif coef == -1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - X")
                        else:
                            terms.append(f" - X^{i}")

                    elif coef <0:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - {coef}*X")
                        else:
                            terms.append(f" - {coef}*X^{i}")
                    else:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" + {coef}")
                        elif i == 1:
                            terms.append(f" + {coef}*X")
                        else:
                            terms.append(f" + {coef}*X^{i}")
    def scalar(self,c):
        new_coef = [coef *c for coef in self.coeff ]
        return Polynomial(new_coef)

    def __add__(self,other):

        z = max(len(self.coeff), len(other.coeff))
        new_coeff = [0] * z

        for i in range(len(self.coeff)):
            new_coeff[i] += self.coeff[i]

        for i in range(len(other.coeff)):
            new_coeff[i] += other.coeff[i]

        return Polynomial(new_coeff)


P1 = Polynomial([-1,0,1])
P2 = Polynomial([4,3,0,1])
P3 = Polynomial([2,4,4])

print(P1)
print(P2)
print(P3)
print(P1 + P2)
print(P1.scalar(2))





###Exercice 2

class Anneau:

    def __init__(self,coeff,q,n):
        if len(coeff)-1<=n and max(coeff)<q:
            self.coeff = coeff

    def __str__(self):


        terms = []
        for i, coef in enumerate(self.coeff):
            if coef != 0:
                if i == len(self.coeff) - 1:
                    if coef == 1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"{coef}")
                        elif i == 1:
                            terms.append(f"X")
                        else:
                            terms.append(f"X^{i}")

                    elif coef == -1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - X")
                        else:
                            terms.append(f"- X^{i}")

                    elif coef <0:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - {coef}*X")
                        else:
                            terms.append(f" - {coef}*X^{i}")
                    else:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"{coef}")
                        elif i == 1:
                            terms.append(f"{coef}*X")
                        else:
                            terms.append(f"{coef}*X^{i}")
                    return "".join(reversed(terms)) if terms else "0"
                else:
                    if coef == 1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f"+ {coef}")
                        elif i == 1:
                            terms.append(f"+ X")
                        else:
                            terms.append(f"+ X^{i}")

                    elif coef == -1:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - X")
                        else:
                            terms.append(f" - X^{i}")

                    elif coef <0:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" - {coef}")
                        elif i == 1:
                            terms.append(f" - {coef}*X")
                        else:
                            terms.append(f" - {coef}*X^{i}")
                    else:
                        coef = abs(coef)
                        if i == 0:
                            terms.append(f" + {coef}")
                        elif i == 1:
                            terms.append(f" + {coef}*X")
                        else:
                            terms.append(f" + {coef}*X^{i}")
    def scalar(self,c):
        new_coef = [coef *c for coef in self.coeff ]
        return Polynomial(new_coef)

    def __add__(self,other):

        z = max(len(self.coeff), len(other.coeff))
        new_coeff = [0] * z

        for i in range(len(self.coeff)):
            new_coeff[i] += self.coeff[i]

        for i in range(len(other.coeff)):
            new_coeff[i] += other.coeff[i]

        return Polynomial(new_coeff)

    def modul(self,q):
        new_coef = [coef % q for coef in self.coeff ]
        return Polynomial(new_coef)

    def __add__(self,other):



###Exercice 3"""