<template>
    <div class="busca-operadoras">
        <h1>Buscar Operadoras</h1>
    
        <!-- Campo de busca -->
        <input
            type="text"
            v-model="termoBusca"
            @keyup.enter="buscarOperadoras"
            placeholder="Digite o termo para busca"
        />
        <button @click="buscarOperadoras">Buscar</button>
    
        <!-- Exibição dos resultados -->
        <ul v-if="resultados.length">
            <li v-for="(resultado, index) in resultados" :key="resultado.CNPJ || index">
                <div><strong>Nome:</strong> {{ resultado.Nome_Fantasia || 'Nome não encontrado' }}</div>
                <div><strong>CNPJ:</strong> {{ resultado.CNPJ || 'CNPJ não encontrado' }}</div>
            <div><strong>Endereço:</strong> {{ resultado.Logradouro ? resultado.Logradouro + ', ' + resultado.Numero : 'Endereço não encontrado' }}</div>
            </li>
        </ul>

        <p v-else>Sem resultados para a busca atual.</p>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
data() {
    return {
    termoBusca: '', 
    resultados: [], 
    };
},
methods: {
    async buscarOperadoras() {
    if (!this.termoBusca) {
        alert('Por favor, insira um termo para busca.');
        return;
    }
    try {
        // Chamada para o servidor
        const resposta = await axios.get(`http://localhost:5000/buscar`, {
        params: { busca: this.termoBusca },
        });
        console.log("Resposta recebida do servidor:", resposta.data);
        this.resultados = resposta.data; // Atualizar resultados
        console.log("Resultados armazenados em resultados:", this.resultados);
    } catch (erro) {
        alert(`Erro ao buscar operadoras: ${erro.message}`);
        console.error(erro);
    }
    },
},
};
</script>

<style scoped>
.busca-operadoras {
text-align: center;
margin-top: 20px;
}
input {
padding: 10px;
width: 300px;
}
button {
padding: 10px 20px;
margin-left: 10px;
cursor: pointer;
}
ul {
list-style-type: none;
padding: 0;
}
li {
border: 1px solid #ccc;
margin: 10px 0;
padding: 10px;
text-align: left;
}
</style>
  