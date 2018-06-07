import argparse

parser = argparse.ArgumentParser(description = 'nãoimportanão')
parser.add_argument('--frase', action = 'store', default = 'Qualquer coisa...', required = False, help = 'A frase a ser impressa n vezes.')
parser.add_argument('-n', action = 'store', required = True, help = 'O no. de vezes que a frase será impressa.')
arguments = parser.parse_args()
for i in range(0, int(arguments.n)):
   print (arguments.frase)

#script no site https://pythonhelp.wordpress.com/2011/11/20/tratando-argumentos-com-argparse/