from fastapi import FastAPI

import pandas as pd

app = FastAPI()

one_hot_enc = pd.read_pickle('one_hot_encoder.pkl')
modelo = pd.read_pickle('modelo_treinado.pkl')
scaler = pd.read_pickle('scaler.pkl')

@app.get('/modelo/v1={idade}&v2={salario}&v3={situacao_moradia}&v4={tempo_trabalho}&v5={motivo_emprestimo}&v6={pontuacao_emprestimo}&v7={valor_emprestimo}&v8={taxa_juros}&v9={renda_percentual_emprestimo}&v10={devendo}&v11={tempo_de_credito}')
def previsao_modelo(idade, salario, situacao_moradia, tempo_trabalho, 
                    motivo_emprestimo, pontuacao_emprestimo, valor_emprestimo,
                    taxa_juros, renda_percentual_emprestimo, devendo, tempo_de_credito):
    
    dados = {
        'idade': [float(idade)],
        'salario': [float(salario)],
        'situacao_moradia': [situacao_moradia],
        'tempo_trabalho': [float(tempo_trabalho)],
        'motivo_emprestimo': [motivo_emprestimo],
        'pontuacao_emprestimo': [pontuacao_emprestimo],
        'valor_emprestimo': [float(valor_emprestimo)],
        'taxa_juros': [float(taxa_juros)],
        'renda_percentual_emprestimo': [float(renda_percentual_emprestimo)],
        'devendo': [float(devendo)],
        'tempo_de_credito': [float(tempo_de_credito)]
    }

    dados = pd.DataFrame(dados)

    dados = one_hot_enc.transform(dados)
    dados_transformados = pd.DataFrame(dados, columns=one_hot_enc.get_feature_names_out())

    dados_transformados = scaler.transform(dados_transformados)
    dados_transformados = pd.DataFrame(dados_transformados, columns = one_hot_enc.get_feature_names_out())
    return {'result': modelo.predict(dados_transformados)[0],
            'probability_0': modelo.predict_proba(dados_transformados).tolist()[0][0],
            'probability_1': modelo.predict_proba(dados_transformados).tolist()[0][1]}
