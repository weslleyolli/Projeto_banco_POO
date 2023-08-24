package aula_01;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class PersistenciaBinaria {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Pessoa pessoa = new Pessoa("Felipe", 23);
			
			try {
				FileOutputStream arquivo = new FileOutputStream ("dados.bin");
				ObjectOutputStream escritor = new ObjectOutputStream(arquivo);
				
				escritor.writeObject(pessoa);
				escritor.close();
				arquivo.close();
				
				System.out.println("Dados gravados com sucesso!");
			} catch (IOException e) {
					System.err.println("Erro ao gravar objeto: " + e.getMessage ());
			}
		}
}


@SuppressWarnings("serial")
class Pessoa implements Serializable{
	String nome;
	int idade;
	
	public Pessoa(String nome, int idade) {
		this.nome = nome;
		this.idade = idade;
	}
}
