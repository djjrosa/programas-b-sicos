meuPrimo = 961
maiorAnterior = 0

def e_primo(k):
  fator = 2
  if k == 2:
    return True
  
  while k % fator and fator <= k/2:
    fator = fator + 1
  if k % fator == 0:
    return False
  else:
    return True

def maior_primo(k):
    i = 1
    while e_primo(k - i) == False:
      i = i + 1
    
    return k - i

maiorAnterior = maior_primo(meuPrimo)