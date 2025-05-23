document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formAdicionar');
    const tabela = document.getElementById('tabelaLivros');

    const API_URL = 'http://localhost:5000/api/consultas';

    // Listar livros
    async function listarLivros() {
        try {
            const resposta = await fetch(API_URL);
            const livros = await resposta.json();

            tabela.innerHTML = '';
            livros.forEach(livro => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${livro.id}</td>
                    <td>${livro.titulo}</td>
                    <td>${livro.autor}</td>
                    <td><button onclick="deletarLivro(${livro.id})">Excluir</button></td>
                `;
                tabela.appendChild(tr);
            });
        } catch (erro) {
            console.error('Erro ao listar livros:', erro);
        }
    }

    // Adicionar livro
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const titulo = document.getElementById('titulo').value;
        const autor = document.getElementById('autor').value;

        try {
            await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo, autor })
            });
            form.reset();
            listarLivros();
        } catch (erro) {
            console.error('Erro ao adicionar livro:', erro);
        }
    });

    // Deletar livro
    window.deletarLivro = async (id) => {
        try {
            await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            listarLivros();
        } catch (erro) {
            console.error('Erro ao deletar livro:', erro);
        }
    };

    listarLivros();
});
