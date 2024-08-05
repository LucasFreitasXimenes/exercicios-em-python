from math import radians,sin,cos,tan#importando somente as funcionalidades que vou usar da biblioteca math
an =  float (input('Digite um ângulo que deseja calcular: '))
seno = sin(radians(an))#aqui no caso voce ta pegando o angulo digitado convertendo para radiando para realizar a formula do seno
print ('O angulo de: {} tem o seno de: {:.2f}'.format(an,seno))
cosseno = cos(radians(an))
print ('O angulo de: {} tem o cosseno de: {:.2f}'.format(an,cosseno))
tangente = tan(radians(an))
print ('O angulo de: `{} tem a tangente de: {:.2f}'.format(an,tangente))