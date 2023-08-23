import xml.etree.cElementTree as ET

tree = ET.parse('aula03/atividades/aula03/passageiros.xml')
root = tree.getroot()

passageiros = root.findall('passageiro')
qtd = len(passageiros)
origens = [passageiro.find('origem').text for passageiro in passageiros]
destinos = [passageiro.find('destino').text for passageiro in passageiros]

print('Quantidade de passageiros: ', qtd)
print('Origens dos passageiros: ', ', '.join(origens))
print('Destinos dos passageiros: ', ', '.join(destinos))
