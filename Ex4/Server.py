from flask import Flask, request, jsonify
from flask.json import dumps
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas
app.config['JSON_AS_ASCII'] = False


# Carregando os dados do CSV na inicialização do servidor
df_operadoras = pd.read_csv('./Relatorio_cadop.csv', delimiter=';', encoding='utf-8')

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    busca = request.args.get('busca', '').lower()  
    
    # Verificação de busca nula
    if not busca:
        return jsonify({"error": "É necessário fornecer um dado de busca"}), 400

    resultados = df_operadoras[df_operadoras.apply(lambda row: busca in row.astype(str).str.lower().to_string(), axis=1)]
    resultados.fillna(value=0, inplace=True)

    resultados_json = resultados.to_dict(orient='records')  
    
    return app.response_class(
        response=dumps(resultados_json, ensure_ascii=False),
        mimetype='application/json'
    )
if __name__ == '__main__':
    app.run(debug=True)
