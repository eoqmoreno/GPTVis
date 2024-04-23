from openai import OpenAI
client = OpenAI()
import json


completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "Você como um assistente para gerar cenários, deverá construir personagens e cenários de uso para uma visualização de dados e retornar em uma lista no formato JSON"},
    {"role": "user", "content": "Você deve substituir a persona e o contexto no template a seguir: 'Eu como um [persona] preciso [cenário], qual seria o melhor tipo de visualização para fazer isso?' e gerar uma possível resposta para a visualização do contexto."},
    {"role": "user", "content": "Siga esse modelo para criar as respostas: {prompt: 'Eu como um lojista preciso produzir uma visualização para apresentar o número de vendas de um Iphone 13 em relação aos meses do ano e aos demais Iphones a partir do 11, qual seria o melhor tipo de visualização para fazer isso?', completion: 'Gráfico de linhas múltiplas pois ela poderá dar uma visão temporal da evolução ou queda nas vendas ao longo do tempo, adicionando uma linha para cada aparelho e um ponto no eixo X para cada mês do ano.'}]"},
    {"role": "user", "content": "As respostas devem substituir os valores entre coxetes na pergunta de uma maneira criativa e com cenários reais e responder no completion a possível resposta para a visualização requisitada com pelo menos 500 caracteres e que ajude à persona a escolher esse tipo de visulização. Gere uma lista de 50 exemplos de cenários e completion para mim no formato JSON."}
  ],
)

responseJson = completion.choices[0].message.content

print(responseJson)

if responseJson is not None:
  jsonConverted = json.loads(responseJson)
  with open("response1.json", "w") as outfile:
    json.dump(jsonConverted, outfile)
  print("Dados salvos em response.json")