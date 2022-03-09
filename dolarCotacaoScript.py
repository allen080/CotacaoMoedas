import requests,json,time

def cotacao_dolar():
	dolar=requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL')
	if dolar.status_code!=200:
		print('erro na requisição da api!'); exit()
	cotacao_dolar=json.loads(dolar.text)
	dolar_cotacao='Dolar Valor atual: %.2fR$'%float(cotacao_dolar[0]['high'])
	return dolar_cotacao

if __name__=='__main__':
	print(cotacao_dolar())
	time.sleep(10)