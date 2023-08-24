package aula_01;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class PersistenciaPropriedades {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Properties propriedades = new Properties();
			propriedades.setProperty("usuario", "Joao");
			propriedades.setProperty("senha", "secreta");
			
			try {
				FileOutputStream arquivo = new FileOutputStream ("config.properties");
				propriedades.store(arquivo, "Configuração do Usuário");
				
				arquivo.close();
				
				System.out.println("Dados gravados com sucesso!");
			} catch (IOException e) {
					System.err.println("Erro ao gravar objeto: " + e.getMessage ());
			}
		}
}
